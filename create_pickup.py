import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)


pickup = client.pickup.create(
    address={"id": "adr_..."},
    shipment={"id": "shp_416745b846bc479b87e325d0872c74ec"},
    reference="my-first-pickup",
    min_datetime="2022-10-01 10:30:00",
    max_datetime="2022-10-02 10:30:00",
    is_account_address=False,
    instructions="Please knock",
)

print(pickup.id)
