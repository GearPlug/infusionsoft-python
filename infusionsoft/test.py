from infusionsoft.client import Client

"""
MAIN INSTANCE
here you instance the main class, obligatory send the token
"""
#client_id = "kbj7nhv3b7yezsrxck2cc749"
#client_secret = "UMtN6PGPud"
#petition = Client("ddrctdj9kqen9z797449xwnk")

"""
OAUTH URL
here you will get the url to do the oauth petition, you have to send the client id and the callback url
"""
# oauth = petition.oauth_access("client_id", "callback")
# print(oauth)

"""
REFRESH TOKEN
here you can refresh the token, are obligatory the client id, client secret and the refresh token
"""
#refresh_token = petition.refresh_token("client ID","client secret","refresh token")
#print(refresh_token)

"""
CONTACT TEST
here you can list all the custom fields of the contacts
"""
# custom_fields = petition.get_contact_custom_fields()
# print(custom_fields)

""" ***here you create a contact, you must to give a valid email or a phone number"""
# create_contact = petition.create_contact('pepito_lo123lo@gmail.com', '123456789', given_name="Luisa", family_name="Hernandez")
# print(create_contact)

""" ***here you delete a contact, is obligatory the id of the contact"""
# delete_contact = petition.delete_contact('70')
# print(delete_contact)

""" ***here you can update a contact, is obligatory the id of the contact to update"""
# update_contact = petition.update_contact('68', given_name="Hernan", family_name="Herrera", email_addresses=[{"email":"hernan_herre@gmail.com","field":"EMAIL1"}])
# print(update_contact)

""" ***here you list the contacts, can receive limit, order, and offset"""
# list_contacts = petition.get_contacts()
# print(list_contacts)

"""
CAMPAIGN TEST
here you list the campaigns, can receive limit and offset
"""
# list_campaigns = petition.get_campaigns(limit=2)
# print(list_campaigns)

""" ***here you can retrieve a specific campaign, obligatory the id of the campaign"""
# retrieve_campaign = petition.retrieve_campaign('')
# print(retrieve_campaign)

"""
EMAIL TEST
here you can get all, or some emails, receive limit or offset
"""
# list_emails = petition.get_emails()
# print(list_emails)

"""
OPPORTUNITIES TEST
here you can list the opportunities, can receive limit, order, and offset
"""
# list_opportunities = petition.get_opportunities()
# print(list_opportunities)

""" ***here you can list all the opportunities in pipeline, not receive anyshit"""
# list_all_opportunities = petition.get_opportunities_pipeline()
# print(list_all_opportunities)

""" ***here you can create an opportunity, obligatory opportunity_title, contact, and stage as json array"""
# create_opportunity = petition.create_opportunity()
# print(create_opportunity)

""" ***here you can retrieve a specific opportunity, obligatory send the id"""
# retrieve_opportunity = petition.retrieve_opportunity("")
# print(retrieve_opportunity)

"""
HOOKS METHODS TEST
here you can list the hooks events, just call the method
"""
# get_hook_events = petition.get_hook_events()
# print(get_hook_events)

""" ***here you can get all the hook subscriptions, just call the method"""
# get_hook_subscriptions = petition.get_hook_subscriptions()
# print(get_hook_subscriptions)

""" ***here you can verify a hook subscription"""
# verify_hook = petition.verify_hook_subscription("34")
# print(verify_hook)

""" ***here you can create a hook subscription, send the hook event and the url callback"""
# create_hook = petition.create_hook_subscription("contact.delete", "http://4b6be146.ngrok.io/api/callback")
# print(create_hook)

""" ***here you can update a hook, send the hook id, event and url"""
# update_hook = petition.update_hook_subscription()
# print(update_hook)

""" ***here you can delete a hook subscription, is obligatory to send the hook id"""
# delete_hook = petition.delete_hook_subscription("30")
# print(delete_hook)