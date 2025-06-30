import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

try:
    address = client.address.create(
        street1="47 West 13th Street Unit 2",
        street2="",
        city="New York",
        state="NY",
        zip="10011",
        country="US",
        company="",
        name="Sofja Akimova",
        phone="",
        email="",
        verify=True,
    )

    print(address)

except Exception as error:
    print("...uh oh: ", error)
