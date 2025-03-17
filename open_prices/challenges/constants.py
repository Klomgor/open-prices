CHALLENGE_STATUS_DRAFT = "DRAFT"
CHALLENGE_STATUS_UPCOMING = "UPCOMING"
CHALLENGE_STATUS_ONGOING = "ONGOING"
CHALLENGE_STATUS_COMPLETED = "COMPLETED"
CHALLENGE_STATUS_LIST = [
    CHALLENGE_STATUS_DRAFT,
    CHALLENGE_STATUS_UPCOMING,
    CHALLENGE_STATUS_ONGOING,
    CHALLENGE_STATUS_COMPLETED,
]

CHALLENGE_STATUS_CHOICES = [(key, key) for key in CHALLENGE_STATUS_LIST]
