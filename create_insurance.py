import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

try:
    insurance = client.insurance.create(
        to_address={"id": "adr_b1448adde8ab11ef9a2a3cecef1b359e"},
        from_address={"id": "adr_101def73e8ac11efa51fac1f6bc539ae"},
        tracking_code="9400110898825022579493",
        carrier="Aramex",
        amount="5000.00",
        reference="insuranceRef1",
    )

    print(insurance)

except Exception as error:
  print("...uh oh: ", error) 