import dad_tool
import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# SHIPMENT PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////
# ADDRESS:
utah_address = dad_tool.random_address('US_UT')
california_address = dad_tool.random_address('US_CA')
canada_address = dad_tool.random_address('CA_BC')

destination = california_address
buyer = california_address
origin = utah_address
return_destination = utah_address

to_address = {
    "name": "EasyPost",
    "street1": destination['street1'],
    "street2": destination['street2'],
    "city": destination['city'],
    "state": destination['state'],
    "zip": destination['zip'],
    "country": destination['country'],
    "phone": "415-456-7890",
}

buyer_address = {
    "name": "EasyPost",
    "street1": buyer['street1'],
    "street2": buyer['street2'],
    "city": buyer['city'],
    "state": buyer['state'],
    "zip": buyer['zip'],
    "country": buyer['country'],
    "phone": "415-456-7890",
}

from_address = {
    "name": "EasyPost",
    "street1": origin['street1'],
    "street2": origin['street2'],
    "city": origin['city'],
    "state": origin['state'],
    "zip": origin['zip'],
    "country": origin['country'],
    "phone": "415-456-7890",
}

return_address = {
    "name": "EasyPost",
    "street1": return_destination['street1'],
    "street2": return_destination['street2'],
    "city": return_destination['city'],
    "state": return_destination['state'],
    "zip": return_destination['zip'],
    "country": return_destination['country'],
    "phone": "415-456-7890",
}

# CUSTOMS INFORMATION:
customs_info = {
    "eel_pfc": "NOEEI 30.37(a)",
    "customs_certify": True,
    "customs_signer": "Steve Brule",
    "contents_type": "merchandise",
    "contents_explanation": "this is the general notes section",
    "restriction_type": "none",
    "restriction_comments": '',
    "non_delivery_option": "return",
    "customs_items": [
        {
            "description": "Sweet shirts",
            "quantity": 2,
            "weight": 5,
            "value": 23,
            "hs_tariff_number": "654321",
            "origin_country": "US",
            "code": "1234",
        },
    ],
}

# SHIPMENT CREATE ////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    shipment = client.shipment.create(
        from_address = from_address,
        to_address = to_address,
        # return_address = return_address,
        # buyer_address = buyer_address,
        parcel = {
            "length": 10.2,
            "width": 7.8,
            "height": 4.3,
            "weight": 21.2,
            # "predefined_package": "LargeFlatRateBox",
        },
        # customs_info = customs_info,
        options = {
            # "label_size": "4x6",
            # "label_format": "PDF",
            # "print_custom_1": "Print Custom 1",
            # "print_custom_2": "Print Custom 2",
            # "print_custom_3": "Print Custom 3",
        },
        carrier_accounts = [settings.carriers['DPD']],
        # service = "GroundAdvantage",
    )   
except:
    print("...uh oh")    

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
#     print("It did not work")