import os
from dotenv import load_dotenv
load_dotenv()

EASYPOST_PRODUCTION_KEY = os.getenv('EASYPOST_PRODUCTION_KEY')
EASYPOST_TEST_KEY = os.getenv('EASYPOST_TEST_KEY')
ENVIRONMENT = "test"

carriers = {
    "USPS": os.getenv("USPS"),
    "FEDEX": os.getenv("FEDEX"),
    "DPD": os.getenv("DPD")
}
