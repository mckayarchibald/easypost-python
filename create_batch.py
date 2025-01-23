import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# BATCH PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////

shipments=[
    {"id": ""},
    {"id": ""},
]

# CREATE BATCH ////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    batch = client.batch.create(
        shipments=shipments,
    )

    print(batch.id)

except Exception as error:
  print("...uh oh: ", error) 
