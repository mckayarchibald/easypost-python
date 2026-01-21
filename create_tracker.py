import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)


tracker = client.tracker.create(
    carrier="FedEx",
    tracking_code="396829094087",
)

print(tracker.id)
