import easypost
import settings
import json

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

with open('recreate_data.json') as recreate_data:
    shipment_data = json.load(recreate_data)

# CREATE SHIPMENT ////////////////////////////////////////////////////////////////////////////////////////////////////////
shipment = client.shipment.create(
    is_return=shipment_data.get('is_return', False),
    to_address=shipment_data['to_address'],
    from_address=shipment_data['from_address'],
    parcel=shipment_data['parcel'],
    customs_info=shipment_data.get('customs_info', None),
    options=shipment_data['options'],
    carrier_accounts=[settings.carriers['FEDEX']],
    tax_identifiers=shipment_data.get('tax_identifiers', None)
)

print(shipment)

# SHIPMENT BUY ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# LOWEST RATE:
try:
    bought_shipment = client.shipment.buy(
        shipment.id,
        rate=shipment.lowest_rate()
    )
    print(bought_shipment)
except: 
    print("...uh oh")

# SPECIFIC CARRIER AND SERVICE:
# try:
#     bought_shipment = client.shipment.buy(
#         shipment.id,
#         rate=shipment.lowest_rate(["USPS"], ["First"])
#     )
#     print(bought_shipment)
# except: 
#     print("...uh oh")