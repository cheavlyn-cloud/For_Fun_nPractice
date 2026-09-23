##Try 1
# print("Mini Copilot: Hello, Type 'exit' to quit.")
# while True:
#     user_input = input("You: ")

#     if user_input.lower() == 'exit':
#         print("Mini Copilot: Bye!")
#         break
        
#     print("Mini Copilot: I heard you say:", user_input)

##Try 2
# while True:
#     user_input = input('You: ').lower()

#     if 'hello' in user_input.lower():
#         print("Mini Copilot: Hey there :)")

#     elif 'how are you' in user_input:
#         print("Mini Copilot: I'm just code, but I'm doing great!")

#     elif "bye" in user_input.lower():
#         print("Mini Copilot: See you soon!")

#     else:
#         print('Mini Copilot: Interesting... tell me more.')

##Try 3
# chat_history = []

# while True:
#     user_input = input('You: ')

#     if user_input.lower() == 'exit':
#         break

#     chat_history.append(user_input)

#     print('Mini Copilot: ', "You've said ", len(chat_history), "thing(s) so far.")

##Try 4
import random
while True:
    user_input = input('You: ')
    responses = [
        "That's actually interesting...",
        "Tell me more.",
        "I'm not sure about that...",
        "Okay, you got me thinking now."
    ]
    print('Mini Copilot:', random.choice(responses))