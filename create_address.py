import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

try:
    address = client.address.create(
        street1="Garbage",
        street2="",
        city="Garbage",
        state="Garbage",
        zip="V2Y 3J1",
        country="Canada",
        company="",
        name=None,
        phone="",
        # verify=True
    ) 

    print(address)

except Exception as error:
  print("...uh oh: ", error) 