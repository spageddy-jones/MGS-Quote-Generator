import tweepy
import time
from mgsFunc import *

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)


while True:

    if len(quote_history) > 9:
        quote_history.pop(0)
    quote = random.randint(1, 13)
    while quote_history.count(quote) != 0:  # quote_history stores previous quotes to ensure variety
        quote = random.randint(1, 13)
    quote_history.append(quote)

    if quote == 1:
        newObj = get_new_obj()
        newVerb = get_new_verb()
        api.update_status("Now go! Let the " + newObj + " " + newVerb + " back to life!")
    elif quote == 2:
        newObj = get_new_obj()
        api.update_status("I'm no " + newObj + ". Never was, never will be.")
    elif quote == 3:
        newCharacter = get_new_character()
        newCharacter2 = get_new_character()
        newVerb = get_new_verb()
        api.update_status(newCharacter + "? I've got " + newCharacter2 + " here. We've managed to avoid " +
                          convert_present_tense(newVerb) + ".")
    elif quote == 4:
        newObj = get_new_obj()
        newObj2 = get_new_obj()
        newAdj = get_new_adj()
        api.update_status("A cornered " + newObj + " is more " + newAdj + " than a "
                          + newObj2 + "!")
    elif quote == 5:
        newObj = get_new_obj()
        newVerb = get_new_verb()
        api.update_status("I'm just a " + newObj + " who's good at what he does: " +
                          convert_present_tense(newVerb) + ".")
    elif quote == 6:
        newCharacter = get_new_character()
        newObj = get_new_obj()
        newObj2 = get_new_obj()
        api.update_status("What about you, " + newCharacter + "? What's it going to be? Loyalty to your " +
                          newObj + " or loyalty to " + convert_plural(newObj2) + "?")
    elif quote == 7:
        newVerb = get_new_verb()
        newObj = get_new_obj()
        api.update_status("THEY " + (convert_past_tense(newVerb)).upper() + " US LIKE A DAMN " + newObj.upper() + "!")
    elif quote == 8:
        newObj = get_new_obj()
        newObj2 = get_new_obj()
        newObj3 = get_new_obj()
        api.update_status((convert_plural(newObj)).capitalize() + " are a myth. " +
              (convert_plural(newObj2)).capitalize() + " are a joke. We are all pawns, " +
              "controlled by something greater: " + convert_plural(newObj3) + ".")
    elif quote == 9:
        newCharacter = get_new_character()
        newObj = get_new_obj()
        newVerb = get_new_verb()
        api.update_status(newCharacter + "? Do you think " + convert_plural(newObj) +
                          " can " + newVerb + ", even on a battlefield?")
    elif quote == 10:

        newAdj = get_new_adj()
        newAdj2 = get_new_adj()
        newAdj3 = get_new_adj()
        newObj = get_new_obj()
        newAdj4 = get_new_adj()
        newObj2 = get_new_obj()
        newAdj5 = get_new_adj()
        newVerb = get_new_verb()
        newObj3 = get_new_obj()

        api.update_status("I hear it's amazing when the " + newAdj + " " + newAdj2 + " " + newAdj3 + " " + newObj +
                          " in " + newAdj4 + " space with the " + newObj2 + " does a " + newAdj5 + " " + newVerb +
                          " on Hara-Kiri Rock. I need " + convert_plural(newObj3) + "! 61!")

    elif quote == 11:
        newAdj = get_new_adj()
        newVerb = get_new_verb()
        newAdj2 = get_new_adj()
        api.update_status("But that was some " + newAdj + " " + convert_present_tense(newVerb) +
                          ". You're pretty " + newAdj2 + ".")
    elif quote == 12:

        newObj = get_new_obj()
        newObj2 = get_new_obj()
        newObj3 = get_new_obj()
        newObj4 = get_new_obj()
        newCharacter = get_new_character()

        api.update_status("You're not a " + newObj + " and I'm not an " + newObj2 + ". We're " + convert_plural(newObj3)
                          + ", with " + convert_plural(newObj4) + ". My name is " + newCharacter + ". What's yours?")

    elif quote == 13:
        newObj = get_new_obj()
        api.update_status("Hrrrngg... " + convert_plural(newObj) + "...")

    time.sleep(3600)  # wait 1 hour before posting again
