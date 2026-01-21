/// AUSTRALIA POST
curl -X POST https://api.easypost.com/v2/carrier_accounts \
 -u EASYPOST_PRODUCTION_API_KEY: \
 -d 'carrier_account[type]=AustraliaPostAccount' \
 -d 'carrier_account[description]=AustraliaPostAccount' \
 -d 'carrier_account[credentials][account_number]=ACCOUNT_NUMBER \
 -d 'carrier_account[credentials][api_key]=API_KEY' \
 -d 'carrier_account[credentials][api_secret]=API_SECRET' \
 -d 'carrier_account[credentials][print_as_you_go]=PRINT_AS_YOU_GO' \
 -d 'carrier_account[test_credentials][account_number]=ACCOUNT_NUMBER \
 -d 'carrier_account[test_credentials][api_key]=API_KEY' \
 -d 'carrier_account[test_credentials][api_secret]=API_SECRET' \
 -d 'carrier_account[test_credentials][print_as_you_go]=PRINT_AS_YOU_GO' \

curl -X POST https://api.easypost.com/v2/carrier_accounts \
 -u EASYPOST_PRODUCTION_API_KEY: \
 -d 'carrier_account[type]=AustraliaPostAccount' \
 -d 'carrier_account[description]=AustraliaPostAccount' \
 -d 'carrier_account[credentials][account_number]=1012945123' \
 -d 'carrier_account[credentials][api_key]=99b763f0-ccf8-4331-9623-5ea773f7b992' \
 -d 'carrier_account[credentials][api_secret]=x4500e60044a72852330' \
 -d 'carrier_account[credentials][print_as_you_go]=true' \
 -d 'carrier_account[test_credentials][account_number]=1012945123' \
 -d 'carrier_account[test_credentials][api_key]=99b763f0-ccf8-4331-9623-5ea773f7b992' \
 -d 'carrier_account[test_credentials][api_secret]=x4500e60044a72852330' \
 -d 'carrier_account[test_credentials][print_as_you_go]=true' \

/// FEDEX FULFILLMENT
curl -X POST https://api.easypost.com/v2/carrier_accounts \
-u EASYPOST_PRODUCTION_API_KEY: \
 -d 'carrier_account[type]=FedexFulfillmentAccount' \
 -d 'carrier_account[description]=FedexFulfillmentAccount' \
 -d 'carrier_account[reference]=FedexFulfillment' \
 -d 'carrier_account[credentials][retailer_account]=2559234' \
 -d 'carrier_account[test_credentials][retailer_account]=2559234' \

/// OSM v1
curl -X POST https://api.easypost.com/v2/carrier_accounts \
 -u EASYPOST_PRODUCTION_API_KEY: \
 -d 'carrier_account[type]=OsmWorldwideAccount' \
 -d 'carrier_account[description]=OsmWorldwideAccount \
 -d 'carrier_account[credentials][account_number]=ACCOUNT_NUMBER' \
 -d 'carrier_account[credentials][mailer_id]=MAILER_ID' \
 -d 'carrier_account[credentials][facility_code]=FACILITY_CODE' \
 -d 'carrier_account[credentials][company_name]=COMPANY_NAME' \
 -d 'carrier_account[credentials][aws_sftp_username]=SFTP_USERNAME'

/// UPS DAP
curl -X POST https://api.easypost.com/v2/carrier_accounts/open \
 -u EASYPOST_PRODUCTION_API_KEY: \
 -d 'carrier_account[type]=UpsDapAccount' \
 -d 'carrier_account[description]=UPS DAP Account' \
 -d 'carrier_account[name]=Lux Perfume' \
 -d 'carrier_account[title]=Shipping' \
 -d 'carrier_account[company]=Lux Perfume' \
 -d 'carrier_account[street1]=12503 Exchange Dr' \
 -d 'carrier_account[street2]=Suite 524' \
 -d 'carrier_account[city]=Stafford' \
 -d 'carrier_account[state]=TX' \
 -d 'carrier_account[postal_code]=77477' \
 -d 'carrier_account[country]=US' \
 -d 'carrier_account[website]=luxperfume.com' \
 -d 'carrier_account[email]=info@luxperfume.com' \
 -d 'carrier_account[phone]=5128291972' \
