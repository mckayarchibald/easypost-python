import easypost
import settings
import time

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)


try:
    parcel = client.parcel.create(length=150, width=100, height=100, weight=0.1)

    print(parcel)

except Exception as error:
    print("...uh oh: ", error)
