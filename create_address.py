import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

try:
    address = client.address.create(
        street1="655 South Monaco Street Parkway",
        street2="",
        city="Denver",
        state="Colorado",
        zip="80224",
        country="US",
        company="",
        name="Mike Hammond",
        phone="",
        verify=True
    ) 

    print(address)

except Exception as error:
  print("...uh oh: ", error) 