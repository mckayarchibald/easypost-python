import easypost
import settings
import time

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# BATCH PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////

shipments = [
    {"id": "shp_ca63a893fc3542ab99e1b0e273f34c5e"},
    {"id": "shp_c67146f2c27940ab906435ab1fa95e52"},
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
