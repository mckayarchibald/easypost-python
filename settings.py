import os
from dotenv import load_dotenv
load_dotenv()

EASYPOST_PRODUCTION_KEY = os.getenv('EASYPOST_PRODUCTION_KEY')
EASYPOST_TEST_KEY = os.getenv('EASYPOST_TEST_KEY')
ENVIRONMENT = "test"

carriers = {
    "AUSTRALIA_POST": os.getenv("AUSTRALIA_POST")
    "DPD": os.getenv("DPD"),
    "FEDEX": os.getenv("FEDEX"),
    "FEDEX_MAILVIEW": os.getenv("FEDEX_MAILVIEW"),
    "USPS": os.getenv("USPS"),
}
