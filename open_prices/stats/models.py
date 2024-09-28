from django.db import models
from django.utils import timezone
from solo.models import SingletonModel


class TotalStats(SingletonModel):
    PRICE_COUNT_FIELDS = ["price_count", "price_barcode_count", "price_category_count"]
    PRODUCT_COUNT_FIELDS = ["product_count", "product_with_price_count"]
    LOCATION_COUNT_FIELDS = ["location_count", "location_with_price_count"]
    PROOF_COUNT_FIELDS = ["proof_count", "proof_with_price_count"]
    USER_COUNT_FIELDS = ["user_count", "user_with_price_count"]

    price_count = models.PositiveIntegerField(default=0)
    price_barcode_count = models.PositiveIntegerField(default=0)
    price_category_count = models.PositiveIntegerField(default=0)
    product_count = models.PositiveIntegerField(default=0)
    product_with_price_count = models.PositiveIntegerField(default=0)
    location_count = models.PositiveIntegerField(default=0)
    location_with_price_count = models.PositiveIntegerField(default=0)
    proof_count = models.PositiveIntegerField(default=0)
    proof_with_price_count = models.PositiveIntegerField(default=0)
    user_count = models.PositiveIntegerField(default=0)
    user_with_price_count = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Total Stats"
        verbose_name_plural = "Total Stats"

    def update_price_stats(self):
        from open_prices.prices.models import Price

        self.price_count = Price.objects.count()
        self.price_barcode_count = Price.objects.filter(
            product_code__isnull=False
        ).count()
        self.price_category_count = Price.objects.filter(
            category_tag__isnull=False
        ).count()
        self.save(
            update_fields=self.PRICE_COUNT_FIELDS
            + [
                "updated",
            ]
        )

    def update_product_stats(self):
        from open_prices.products.models import Product

        self.product_count = Product.objects.count()
        self.product_with_price_count = Product.objects.has_prices().count()
        # self.product_with_price_count = User.objects.values_list("product_id", flat=True).distinct().count()  # noqa
        self.save(update_fields=self.PRODUCT_COUNT_FIELDS + ["updated"])

    def update_location_stats(self):
        from open_prices.locations.models import Location

        self.location_count = Location.objects.count()
        self.location_with_price_count = Location.objects.has_prices().count()
        # self.location_with_price_count = User.objects.values_list("location_id", flat=True).distinct().count()  # noqa
        self.save(update_fields=self.LOCATION_COUNT_FIELDS + ["updated"])

    def update_proof_stats(self):
        from open_prices.proofs.models import Proof

        self.proof_count = Proof.objects.count()
        self.proof_with_price_count = Proof.objects.has_prices().count()
        # self.proof_with_price_count = User.objects.values_list("proof_id", flat=True).distinct().count()  # noqa
        self.save(update_fields=self.PROOF_COUNT_FIELDS + ["updated"])

    def update_user_stats(self):
        from open_prices.users.models import User

        self.user_count = User.objects.count()
        self.user_with_price_count = User.objects.has_prices().count()
        # self.user_with_price_count = User.objects.values_list("owner", flat=True).distinct().count()  # noqa
        self.save(update_fields=self.USER_COUNT_FIELDS + ["updated"])