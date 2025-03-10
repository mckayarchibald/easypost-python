import easypost
import settings
import json

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

with open('recreate_data.json') as recreate_data:
    shipment_data = json.load(recreate_data)


# SHIPMENT PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////
# ADDRESSES:
to_address = {
    "name": shipment_data['to_address']['name'],
    "company": shipment_data['to_address']['company'],
    "street1": shipment_data['to_address']['street1'],
    "street2": shipment_data['to_address']['street2'],
    "city": shipment_data['to_address']['city'],
    "state": shipment_data['to_address']['state'],
    "zip": shipment_data['to_address']['zip'],
    "country": shipment_data['to_address']['country'],
    "phone": shipment_data['to_address']['phone'],
}

buyer_address = {
    "name": shipment_data['buyer_address']['name'],
    "company": shipment_data['buyer_address']['company'],
    "street1": shipment_data['buyer_address']['street1'],
    "street2": shipment_data['buyer_address']['street2'],
    "city": shipment_data['buyer_address']['city'],
    "state": shipment_data['buyer_address']['state'],
    "zip": shipment_data['buyer_address']['zip'],
    "country": shipment_data['buyer_address']['country'],
    "phone": shipment_data['buyer_address']['phone'],
}

from_address = {
    "name": shipment_data['from_address']['name'],
    "company": shipment_data['from_address']['company'],
    "street1": shipment_data['from_address']['street1'],
    "street2": shipment_data['from_address']['street2'],
    "city": shipment_data['from_address']['city'],
    "state": shipment_data['from_address']['state'],
    "zip": shipment_data['from_address']['zip'],
    "country": shipment_data['from_address']['country'],
    "phone": shipment_data['from_address']['phone'],
}

return_address = {
    "name": shipment_data['return_address']['name'],
    "company": shipment_data['return_address']['company'],
    "street1": shipment_data['return_address']['street1'],
    "street2": shipment_data['return_address']['street2'],
    "city": shipment_data['return_address']['city'],
    "state": shipment_data['return_address']['state'],
    "zip": shipment_data['return_address']['zip'],
    "country": shipment_data['return_address']['country'],
    "phone": shipment_data['return_address']['phone'],
}

# CUSTOMS INFORMATION:

if shipment_data['customs_info'] is not None:

    customs_items = shipment_data['customs_info']['customs_items']

    for customs_item in customs_items:
        del customs_item['id']
        del customs_item['object']
        del customs_item['created_at']
        del customs_item['updated_at']
        del customs_item['mode']

    customs_info = {
        "eel_pfc": shipment_data['customs_info']['eel_pfc'],
        "customs_certify": shipment_data['customs_info']['customs_certify'],
        "customs_signer": shipment_data['customs_info']['customs_signer'],
        "contents_type": shipment_data['customs_info']['contents_type'],
        "contents_explanation": shipment_data['customs_info']['contents_explanation'],
        "restriction_type": shipment_data['customs_info']['restriction_type'],
        "restriction_comments": shipment_data['customs_info']['restriction_comments'],
        "non_delivery_option": shipment_data['customs_info']['non_delivery_option'],
        "customs_items": customs_items
    }


# CREATE SHIPMENT ////////////////////////////////////////////////////////////////////////////////////////////////////////
shipment = client.shipment.create(
    is_return=shipment_data.get('is_return', False),
    to_address=to_address,
    buyer_address=buyer_address,
    from_address=from_address,
    return_address=return_address,
    parcel= {
        "length": shipment_data['parcel']['length'],
        "width": shipment_data['parcel']['width'],
        "height": shipment_data['parcel']['height'],
        "weight": shipment_data['parcel']['weight'],
        "predefined_package": shipment_data['parcel']['predefined_package'],
    },
    # customs_info=customs_info,
    options={
        **shipment_data['options'],
        # "import_control": "PRINT",
        # "import_control_description": "DESCRIPTION_HERE",
    },
    carrier_accounts=[settings.carriers['CANADA_POST']],
    # service="FEDEX_2_DAY",
)

print("The shipment was successfully created: ", shipment.id)

# SHIPMENT BUY ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# LOWEST RATE:
try:
    bought_shipment = client.shipment.buy(
        shipment.id,
        rate=shipment.lowest_rate()
    )
    print("The shipment was successfully purchased: ", bought_shipment.id)
except Exception as error:
  print("...uh oh. The purchase request failed: ", error) 

# SPECIFIC CARRIER AND SERVICE:
# try:
#     bought_shipment = client.shipment.buy(
#         shipment.id,
#         rate=shipment.lowest_rate(["UPS"], ["UPSStandard"])
#     )
#     print(bought_shipment.id)
# except Exception as error:
#      print("...uh oh: ", error) 