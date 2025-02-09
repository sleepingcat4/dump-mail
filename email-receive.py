import mailslurp_client
import re

configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = "API KEY"

with mailslurp_client.ApiClient(configuration) as api_client:
    inbox_controller = mailslurp_client.InboxControllerApi(api_client)
    inbox = inbox_controller.create_inbox()
    
    print(f"Inbox created: {inbox.email_address}")
    print("Listening for emails...")

    wait_for_controller = mailslurp_client.WaitForControllerApi(api_client)
    email = wait_for_controller.wait_for_latest_email(
        inbox_id=inbox.id, timeout=60_000, unread_only=True
    )

    match = re.search(r"https://elevenlabs\.io/app/action\?\S+", email.body)
    
    if match:
        print(f"Found link: {match.group(0)}")
    else:
        print("No matching link found.")
