import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# BATCH PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////

shipments=[
    {"id": "shp_cabc353321084f80982d5a6e7ed8b334"},
    {"id": "shp_e10f799638c14fc98c3827b1f9dcc206"},
]

# CREATE BATCH ////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    batch = client.batch.create(
        shipments=shipments,
    )

    print(batch.id)

except Exception as error:
  print("...uh oh: ", error) 
