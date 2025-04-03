import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

try:
    address = client.address.create(
        street1="865 Pomeroy Avenue",
        street2="APT 320 B",
        city="Santa Clara",
        state="CA",
        zip="95051",
        country="US",
        company="",
        name="Rachel Sales",
        phone="6509063463",
        email="pizza_buddy@yahoo.com",
        verify=True
    ) 

    print(address)

except Exception as error:
  print("...uh oh: ", error) 