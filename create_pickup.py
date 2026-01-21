import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)


pickup = client.pickup.create(
    address={"id": "adr_d8c507277f7d11f08c963cecef1b359e"},
    shipment={"id": "shp_fe72789a64304757ab97a17be6fbe6c0"},
    reference="my-first-pickup",
    min_datetime="2025-08-26 9:30:00",
    max_datetime="2025-08-26 17:30:00",
    is_account_address=False,
    instructions="Please knock",
)

print(pickup.id)
