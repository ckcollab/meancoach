import os
import plivo


PLIVO_INCOMING_NUMBER = os.environ.get("PLIVO_INCOMING_NUMBER", None)
PLIVO_AUTH_ID = os.environ.get("PLIVO_AUTH_ID", None)
PLIVO_AUTH_TOKEN = os.environ.get("PLIVO_AUTH_TOKEN", None)

assert PLIVO_INCOMING_NUMBER, "PLIVO_INCOMING_NUMBER env var missing"
assert PLIVO_AUTH_ID, "PLIVO_AUTH_ID env var missing"
assert PLIVO_AUTH_TOKEN, "PLIVO_AUTH_TOKEN env var missing"


def send_message(to_number, message):
    p = plivo.RestAPI(PLIVO_AUTH_ID, PLIVO_AUTH_TOKEN)
    params = {
        'src': PLIVO_INCOMING_NUMBER,
        'dst': to_number,
        'text': "Hi, message from Plivo",
        'type': "sms",
    }
    return p.send_message(params)


class SmsManager(object):

    '''

    UserSmsProfile
        state = ("has not responded", "available")
        message_queue = Many to many with SmsMessage
        data = hstore, just in case it's useful

    SmsMessage
        message_type = Name of message class (CheckIn, FoodInput, UserResponse)
        goal = fk to goal we're dealing with??
        when =
        text =


    CheckIn
        time_of_day =
        days_of_week =





    ---------------------
    User's can have 1 message state at a time. ???????



    Sms Message "Stack" needed?

    Each user has message_stack which is a json/hstore stack with expected message responses




    Sms model:
        message_type = Name of the Message class (CheckIn, FoodInput, UserResponse)
        message_fk = Maybe we can have a DB entry for each message that way we can have multiple CheckIns and shit???
        data = json/hstore shit, the Message Class should have an init that takes this data and from that only
               it will figure out what to do next!!
        when = datetime
        positive = true/false/Null (they did good or N/A)
        negative = true/false/Null (they done bad or N/A)
        text =


        Each to/from will be an Sms model??

    Message prefixes can put a user in a state, i.e. sending




    Types of messages:
    - UserResponse
    - UserMessage
    - CheckIn (triggered at certain times, static recording, 1 response requested)
        Coach: Did you do this <checklist item> by <check time>? (y/n)
        User: yes|y|no|n
        On yes
            Coach: <coach.get_positive_message()>
        On no
            Coach: <coach.get_negative_message()>
    - FoodInput (ongoing, responses any time)
        User: food hamburger fries
        Coach: I got 2 foods "hamburger" and "fries", if that's not correct please say "no" and I'll delete this record
        assuming success, calculate macros
    - Encouragement (random, limit to once a day between 8am and 3pm)
        Coach: <coach.get_positive_message()>

    '''

    def receive_message(self):
        # parse sender
        # each sender has a "message state" which we'll store in the database?
        #



        pass
