import easypost
import settings
import time

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

form_type = "rma_qr_code"
form_options = {"rma": {"label_image_data": None, "retailer_account": "2559234"}}

shipment = client.shipment.generate_form(
    "shp_4fe6d64ba2264002ac7086668a94d072", form_type, form_options
)

print(shipment)
