import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# SCANFORM PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////

batch_id = "batch_250e9353c696411bab8780e3366cc1ae"

# CREATE SCANFORM ////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    scanform = client.batch.create_scan_form(batch_id)

    print(scanform.id)

except Exception as error:
  print("...uh oh: ", error) 
