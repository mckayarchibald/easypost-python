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
customs_info = {
    "eel_pfc": shipment_data['customs_info']['eel_pfc'],
    "customs_certify": shipment_data['customs_info']['customs_certify'],
    "customs_signer": shipment_data['customs_info']['customs_signer'],
    "contents_type": shipment_data['customs_info']['contents_type'],
    "contents_explanation": shipment_data['customs_info']['contents_explanation'],
    "restriction_type": shipment_data['customs_info']['restriction_type'],
    "restriction_comments": shipment_data['customs_info']['restriction_comments'],
    "non_delivery_option": shipment_data['customs_info']['non_delivery_option'],
    # The customs items need to be dynamically imported
    "customs_items": [
        {
            "description": shipment_data['customs_info']['customs_items'][0]['description'],
            "quantity": shipment_data['customs_info']['customs_items'][0]['quantity'],
            "weight": shipment_data['customs_info']['customs_items'][0]['weight'],
            "value": shipment_data['customs_info']['customs_items'][0]['value'],
            "hs_tariff_number": shipment_data['customs_info']['customs_items'][0]['hs_tariff_number'],
            "origin_country": shipment_data['customs_info']['customs_items'][0]['origin_country'],
            "code": shipment_data['customs_info']['customs_items'][0]['code'],
            "currency": shipment_data['customs_info']['customs_items'][0]['currency'],
        },
    ],
}


# CREATE SHIPMENT ////////////////////////////////////////////////////////////////////////////////////////////////////////
shipment = client.shipment.create(
    is_return=shipment_data.get('is_return', False),
    to_address=to_address,
    # buyer_address=buyer_address,
    from_address=from_address,
    return_address=return_address,
    parcel= {
        "length": shipment_data['parcel']['length'],
        "width": shipment_data['parcel']['width'],
        "height": shipment_data['parcel']['height'],
        "weight": shipment_data['parcel']['weight'],
        "predefined_package": shipment_data['parcel']['predefined_package'],
    },
    customs_info=customs_info,
    options=shipment_data['options'],
    carrier_accounts=[settings.carriers['USPS']],
)

print(shipment.id)

# SHIPMENT BUY ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# LOWEST RATE:
# try:
#     bought_shipment = client.shipment.buy(
#         shipment.id,
#         rate=shipment.lowest_rate()
#     )
#     print(bought_shipment.id)
# except Exception as error:
#   print("...uh oh: ", error) 

# SPECIFIC CARRIER AND SERVICE:
try:
    bought_shipment = client.shipment.buy(
        shipment.id,
        rate=shipment.lowest_rate(["USPS"], ["PriorityMailInternational"])
    )
    print(bought_shipment.id)
except Exception as error:
     print("...uh oh: ", error) 