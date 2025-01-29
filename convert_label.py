import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

shipment = client.shipment.label("shp_e12384c1edbf4741906fd44c3e964a7c", file_format="PDF")

print(shipment.id)