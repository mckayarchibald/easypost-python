import easypost
import settings
import time

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# SCANFORM PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////

batch_id = "batch_039a8069fca64f809e82b756a2e4553b"

# CREATE SCANFORM FROM BATCH ////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    batch = client.batch.create_scan_form(batch_id)
    scanform = batch.scan_form

    print("Scanform: ", scanform.id)
    while scanform.status != "created":
        print(f"The current scanform status is '{scanform.status}'")
        print("Checking scanform status...")
        time.sleep(3)
        batch = client.batch.retrieve(batch_id)
        scanform = batch.scan_form
        if scanform.status == "failed":
            print("There was an error in creating the scanform:\n", scanform.message)
            break

    if scanform.status == "created":
        print(f"The current scanform status is '{scanform.status}'")

except Exception as error:
    print("...uh oh: ", error)
