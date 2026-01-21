import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

carrier_account = client.carrier_account.create(
    type="UpsAccount",
    description="",
    credentials={
        "account_number": "C0W838",
    },
)

print(carrier_account)
