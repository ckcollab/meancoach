import os
import plivo


plivo_incoming_number = os.environ.get("PLIVO_INCOMING_NUMBER", None)
auth_id = os.environ.get("PLIVO_AUTH_ID", None)
auth_token = os.environ.get("PLIVO_AUTH_TOKEN", None)

assert plivo_incoming_number, "PLIVO_INCOMING_NUMBER env var missing"
assert auth_id, "PLIVO_AUTH_ID env var missing"
assert auth_token, "PLIVO_AUTH_TOKEN env var missing"

p = plivo.RestAPI(auth_id, auth_token)

params = {
    'src': plivo_incoming_number,
    'dst' : '12087711010',
    'text' : "Hi, message from Plivo",
    'type' : "sms",
}

response = p.send_message(params)
print response


