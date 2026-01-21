import easypost
import settings
import json

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)
if settings.ENVIRONMENT == "personal":
    client = easypost.EasyPostClient(settings.PERSONAL_PRODUCTION_KEY)

trackers = client.tracker.all(
    tracking_codes=["408045663991"],
    start_datetime="2025-07-10T00:00:00Z",
    end_datetime="2025-07-20T00:00:00Z",
    page_size=5,
)

print(trackers)
