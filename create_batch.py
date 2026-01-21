import easypost
import settings
import time

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# BATCH PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////

shipments = [
    {"id": "shp_90d14037458f43fca65fc8e66f1d95bd"},
]

# CREATE BATCH ////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    batch = client.batch.create(
        shipments=shipments,
    )

    print("Batch: ", batch.id)
    while batch.state != "purchased":
        print(f"The current batch status is '{batch.state}'")
        print("Checking batch status...")
        time.sleep(3)
        batch = client.batch.retrieve(batch.id)

    if batch.state == "purchased":
        print(f"The current batch status is '{batch.state}'")

except Exception as error:
    print("...uh oh: ", error)
