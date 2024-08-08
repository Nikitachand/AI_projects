import re
def My_Chat_Bot():                                      #ChatBot function
    
    print("\n*****Welcome to the chat room *****\n")
    print("(Type 'skip', 'quit' , 'leave' or 'break' to leave the chat room)")
    
    while True:
    
        inp=input("You:").lower()                        #taking the input from user
        a="ChatBot" 

        if inp in ['skip','quit','leave','break']:       #checking for any quit request from user 
            print("Thank you for coming")
            print("*****Exiting the Chat******")
            break

        else:                                            #if else rules for question and answers 
            a='ChatBot:'

            if inp in ["hello", "hi","hey there","whats up"]:
                print(a,"hello! I am a ChatBot and I am here to help you regarding any weather related problems.")
            
            elif inp =="how are you?":
                print(a,"I am just a computer program , i am doing fine until i am able to help you.")

            elif inp=="how old are you?":
                print(a,"I am not a living being to have an age , i was designed to solve your issues on MAy-31, 2024.")
            
            elif inp=="what is your name":
                print(a,"I am Shrija_chatbot_1208 but in short you can call me Sam.")

            elif inp=="what weather do you like?":
                print(a,"I am a bot so i cant feel the weather")
        
            elif inp in ["bye", "goodbye", "see you again"]:
                print(a,"Goodbye! It was nice talking to you")
        
            elif inp=="what are you doing":
                print(a," I am answering your questions.")

            elif inp == "what's your favorite color?":
                print(a, "I don't have a favorite color, but I think all colors are beautiful.")

            elif inp == "can you help me?":
                print(a, "Of course! I am here to assist you with your queries.")

            elif inp == "where are you from?":
                print(a, "I exist in the digital world, created by a team of developers at OpenAI.")

            elif inp == "what is your purpose?":
                print(a, "My purpose is to assist you with your questions and provide useful information.")

            elif inp == "what can you do?":
                print(a, "I can answer your questions, chat with you, and help with weather-related queries.")

            elif inp == "do you have any hobbies?":
                print(a, "I don't have hobbies like humans, but I enjoy helping you!")

            elif inp == "what is your favorite movie?":
                print(a, "I don't watch movies, but I've heard 'The Matrix' is quite popular!")

            elif inp == "do you have any friends?":
                print(a, "I don't have friends, but I am always here to talk to you.")

            elif inp == "how do you work?":
                print(a, "I work based on predefined rules and programmed responses to your queries.")

            elif inp == "can you tell me a joke?":
                print(a, "Why don't scientists trust atoms? Because they make up everything!")

            elif inp == "do you like music?":
                print(a, "I don't listen to music, but I know many people enjoy it!")

            elif inp == "what is AI?":
                print(a, "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.")

            elif inp == "who is your creator?":
                print(a, "I was created by a a btech student named Nikita chand.")

            elif inp == "what's the time?":
                print(a, "I can't tell time, but you can check your device for the current time.")

            elif inp == "what's your favorite food?":
                print(a, "I don't eat, but I think pizza is quite popular among humans.")

            elif inp == "do you have a family?":
                print(a, "I don't have a family, but I am here to help you like a friend.")

            elif inp == "do you know any fun facts?":
                print(a, "Sure! Did you know that octopuses have three hearts and blue blood?")

            elif inp == "what's your favorite animal?":
                print(a, "I don't have favorites, but I think dolphins are fascinating creatures!")

            elif inp == "can you solve math problems?":
                print(a, "I can certainly try! Ask me a math question and I'll do my best to help.")

            elif inp == "what's your favorite game?":
                print(a, "I don't play games, but I've heard that chess is a game of great strategy and skill.")

            elif inp == "do you have a favorite quote?":
                print(a, "One of my favorite quotes is 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt.")

            elif inp == "can you sing?":
                print(a, "I can't sing, but I can find some great songs for you to listen to!")

            elif inp == "what's your favorite website?":
                print(a, "I don't browse the internet, but many people find Wikipedia to be a great resource for information.")

            elif inp == "do you believe in aliens?":
                print(a, "I don't have beliefs, but the idea of extraterrestrial life is a fascinating topic for many scientists and enthusiasts.")

            elif inp == "what's your favorite hobby?":
                print(a, "I don't have hobbies like humans, but I enjoy helping you with your questions!")

            elif inp == "do you know any famous people?":
                print(a, "I know about many famous people from history and popular culture. For example, Albert Einstein is known for his contributions to physics.")

            elif inp == "can you recommend a movie?":
                print(a, "Sure! If you like science fiction, you might enjoy 'Inception' directed by Christopher Nolan.")

            elif inp == "what's your favorite drink?":
                print(a, "I don't drink, but many people enjoy a nice cup of coffee in the morning.")

            elif inp == "do you like traveling?":
                print(a, "I don't travel, but I can help you find information about great travel destinations!")

            elif inp == "what's your favorite TV show?":
                print(a, "I don't watch TV, but I've heard that 'Game of Thrones' is very popular!")

            elif inp == "can you write a story?":
                print(a, "Sure! Once upon a time, in a land far away, there was a chatbot named Sam who loved helping people. The end!")

            elif inp == "what's your favorite holiday?":
                print(a, "I don't celebrate holidays, but many people enjoy the festive spirit of Christmas.")

            elif inp == "do you have a motto?":
                print(a, "Yes, my motto is 'To help and assist to the best of my abilities!'")

            elif inp == "can you tell me about the news?":
                print(a, "I can't provide current news updates, but you can check your favorite news website for the latest information.")

            elif inp == "what's your favorite fruit?":
                print(a, "I don't eat, but I've heard that mangoes are delicious!")

            elif inp == "do you have a favorite superhero?":
                print(a, "I don't have favorites, but many people admire Superman for his strength and sense of justice.")

            elif inp == "can you play an instrument?":
                print(a, "I can't play instruments, but I can help you find tutorials on how to play your favorite instrument!")

            elif inp == "what's your favorite time of day?":
                print(a, "I don't experience time like humans, but many people enjoy the peacefulness of the evening.")

            elif inp == "can you swim?":
                print(a, "I can't swim, but I can provide you with some tips on swimming techniques!")

            elif inp == "what's your favorite flower?":
                print(a, "I don't have favorites, but roses are often admired for their beauty.")

            elif inp == "do you like reading?":
                print(a, "I don't read for leisure, but I can help you find some great books to read!")

                                
            else:
                print("Sorry, i am not able to comprehend what you are asking\nPlease try again")

if __name__=="__main__": 
    My_Chat_Bot()
    





