import dad_tool
import easypost
import settings

if settings.ENVIRONMENT == "test":
    client = easypost.EasyPostClient(settings.EASYPOST_TEST_KEY)
if settings.ENVIRONMENT == "production":
    client = easypost.EasyPostClient(settings.EASYPOST_PRODUCTION_KEY)

# SHIPMENT PARAMETERS ////////////////////////////////////////////////////////////////////////////////////////////////////
# ADDRESSES:

custom_recepient_address = {
      "name": "Amanda Miller",
      "street1": "525 S Winchester Blvd",
      "street2": "",
      "city": "San Jose",
      "state": "CA",
      "zip": "95128",
      "country": "US",
      "phone": "9999999999"
}
custom_sender_address = {
      "name": "Walmart",
      "street1": "5597 S WALTON BLVD",
      "street2": "",
      "city": "BENTONVILL",
      "state": "AR",
      "zip": "72712",
      "country": "US",
      "phone": "9999999999"
}

# DOMESTIC: 
california_address = dad_tool.random_address('US_CA')
texas_address = dad_tool.random_address('US_TX')
utah_address = dad_tool.random_address('US_UT')

# INTERNATIONAL: 
australia_address_1 = dad_tool.random_address('AU_VT')
australia_address_2 = dad_tool.random_address('AU_VT')
canada_address = dad_tool.random_address('CA_BC')
france_address = dad_tool.random_address('EU_FR')

destination = california_address
buyer = california_address
origin = utah_address
return_destination = utah_address


to_address = {
    "name": "McKay Archibald",
    "street1": destination['street1'],
    "street2": destination['street2'],
    "city": destination['city'],
    "state": destination['state'],
    "zip": destination['zip'],
    "country": destination['country'],
    "phone": "415-456-7890",
    "email": "mckay@example.com"
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
    "name": "Grainger",
    "company": "C/O Vendor Company Name",
    "street1": origin['street1'],
    "street2": origin['street2'],
    "city": origin['city'],
    "state": origin['state'],
    "zip": origin['zip'],
    "country": origin['country'],
    "phone": "1111111111",
    "email": ""
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
    "contents_type": "dangerous_goods",
    "contents_explanation": "this is the general notes section",
    "restriction_type": "none",
    "restriction_comments": '',
    "non_delivery_option": "return",
    "customs_items": [
        {
            "description": "Sweat shirts",
            "quantity": 1,
            "weight": 5,
            "value": 23,
            "hs_tariff_number": "654321",
            "origin_country": "US",
            "code": "1234",
        },
    ],
}

# CREATE SHIPMENT ////////////////////////////////////////////////////////////////////////////////////////////////////////
try:
    shipment = client.shipment.create(
        from_address = from_address,
        to_address = to_address,
        # return_address = return_address,
        # buyer_address = buyer_address,
        parcel = {
            # "length": 12,
            # "width": 5,
            # "height": 5,
            "weight": 3,
            "predefined_package": "Letter",
        },
        # customs_info = customs_info,
        options = {
           "print_custom_1": "1234567890",
           "print_custom_2": "print custom 2",
        #    "print_custom_2_code": "PO",
           "print_custom_3": "print custom 3",
        #    "print_custom_3_code": "DP",
           "invoice_number": "invoice number"
            # "currency": "EUR"
        },
        carrier_accounts = [settings.carriers['FEDEX']],
        # service = "Priority",
    )   

    print(shipment.id)
except Exception as error:
  print("...uh oh: ", error)  

# SHIPMENT BUY ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# LOWEST RATE:
try:
    bought_shipment = client.shipment.buy(
        shipment.id,
        rate=shipment.lowest_rate()
    )
    print(bought_shipment.id)
except Exception as error:
  print("...uh oh: ", error)

# SPECIFIC CARRIER AND SERVICE:
# try:
#     bought_shipment = client.shipment.buy(
#         shipment.id,
#         rate=shipment.lowest_rate(["USPS"], ["First"])
#     )
#     print(bought_shipment)
# except: 
#     print("It did not work")