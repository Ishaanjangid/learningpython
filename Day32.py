#! python 3
import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sound fine to me.""",
        'busy': """"Sorry, can we do this later this week or next week?""",
        'upsell': """Would you  consider this a monthly donation?"""}


arguments = sys.argv

if len(arguments) < 2:
    print("Usage: python Day32.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = arguments[1]  #First command line arg is the keyphrase

if keyphrase.lower() in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipiboard.")
    
else:
    print(f"There is no text for {keyphrase}")
