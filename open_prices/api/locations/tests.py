from django.db.models import signals
from django.test import TestCase
from django.urls import reverse

from open_prices.locations.factories import LocationFactory
from open_prices.locations.models import (
    Location,
    location_post_create_fetch_data_from_openstreetmap,
)

LOCATION_NODE_652825274 = {
    "osm_id": 652825274,
    "osm_type": "NODE",
    "osm_name": "Monoprix",
    "osm_lat": "45.1805534",
    "osm_lon": "5.7153387",
    "price_count": 15,
}
LOCATION_NODE_6509705997 = {
    "osm_id": 6509705997,
    "osm_type": "NODE",
    "osm_name": "Carrefour",
    "price_count": 0,
}
LOCATION_WAY_872934393 = {
    "osm_id": 872934393,
    "osm_type": "WAY",
    "osm_name": "Auchan",
    "price_count": 50,
}


class LocationListApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("api:locations-list")
        LocationFactory(price_count=15)
        LocationFactory(price_count=0)
        LocationFactory(price_count=50)

    def test_location_list(self):
        # anonymous
        response = self.client.get(self.url)
        self.assertEqual(response.data["total"], 3)
        self.assertEqual(len(response.data["items"]), 3)
        self.assertTrue("id" in response.data["items"][0])
        self.assertEqual(response.data["items"][0]["price_count"], 15)  # default order


class LocationListOrderApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("api:locations-list")
        LocationFactory(price_count=15)
        LocationFactory(price_count=0)
        LocationFactory(price_count=50)

    def test_location_list_order_by(self):
        url = self.url + "?order_by=-price_count"
        response = self.client.get(url)
        self.assertEqual(response.data["total"], 3)
        self.assertEqual(response.data["items"][0]["price_count"], 50)


class LocationListFilterApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse("api:locations-list")
        LocationFactory(**LOCATION_NODE_652825274)
        LocationFactory(**LOCATION_NODE_6509705997)
        LocationFactory(**LOCATION_WAY_872934393)

    def test_location_list_filter_by_osm_name(self):
        url = self.url + "?osm_name__like=monop"
        response = self.client.get(url)
        self.assertEqual(response.data["total"], 1)
        self.assertEqual(response.data["items"][0]["osm_name"], "Monoprix")

    def test_location_list_filter_by_price_count(self):
        # exact price_count
        url = self.url + "?price_count=15"
        response = self.client.get(url)
        self.assertEqual(response.data["total"], 1)
        self.assertEqual(response.data["items"][0]["price_count"], 15)
        # lte / gte
        url = self.url + "?price_count__gte=20"
        response = self.client.get(url)
        self.assertEqual(response.data["total"], 1)
        self.assertEqual(response.data["items"][0]["price_count"], 50)
        url = self.url + "?price_count__lte=20"
        response = self.client.get(url)
        self.assertEqual(response.data["total"], 2)
        self.assertEqual(response.data["items"][0]["price_count"], 15)


class LocationDetailApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.location = LocationFactory(**LOCATION_NODE_652825274)
        cls.url = reverse("api:locations-detail", args=[cls.location.id])

    def test_location_detail(self):
        # 404
        url = reverse("api:locations-detail", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        # existing location
        response = self.client.get(self.url)
        self.assertEqual(response.data["id"], self.location.id)
        # self.assertEqual(response.data["osm_lat"], 45.1805534)

    def test_location_detail_by_osm(self):
        # 404
        url = reverse("api:locations-get-by-osm", args=["NODE", 999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        # existing location
        url = reverse(
            "api:locations-get-by-osm",
            args=[self.location.osm_type, self.location.osm_id],
        )
        response = self.client.get(url)
        self.assertEqual(response.data["id"], self.location.id)


class LocationCreateApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        signals.post_save.disconnect(
            location_post_create_fetch_data_from_openstreetmap, sender=Location
        )
        cls.url = reverse("api:locations-list")

    def test_location_create(self):
        response = self.client.post(
            self.url, LOCATION_NODE_652825274, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["osm_id"], 652825274)
        self.assertEqual(response.data["osm_type"], "NODE")
        self.assertEqual(
            response.data["osm_name"], None
        )  # ignored (and post_save signal disabled)
        self.assertEqual(response.data["price_count"], 0)  # ignored


class LocationUpdateApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.location = LocationFactory(**LOCATION_NODE_652825274)
        cls.url = reverse("api:locations-detail", args=[cls.location.id])

    def test_location_update_not_allowed(self):
        data = {"osm_name": "Carrefour"}
        response = self.client.patch(self.url, data, content_type="application/json")
        self.assertEqual(response.status_code, 405)


class LocationDeleteApiTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.location = LocationFactory(**LOCATION_NODE_652825274)
        cls.url = reverse("api:locations-detail", args=[cls.location.id])

    def test_location_delete_not_allowed(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 405)