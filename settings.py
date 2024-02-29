import os
from dotenv import load_dotenv
load_dotenv()

EASYPOST_TEST_KEY = os.getenv('EASYPOST_TEST_KEY')
EASYPOST_PRODUCTION_KEY = os.getenv('EASYPOST_PRODUCTION_KEY')