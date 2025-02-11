import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

try:
    address = client.address.create(
        street1="10 Persiaran KLCC Level 33",
        street2="",
        city="Kuala Lumpur",
        state="",
        zip="50088",
        country="MY",
        company="",
        name="SM Nasarudin",
        phone="60192887878",
        verify=True
    ) 

    print(address)

except Exception as error:
  print("...uh oh: ", error) 