import wikipedia
import datetime
import webbrowser
from googlesearch import search
import os
import sys

command="pip install -r requirement.txt"
os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")
os.system("clear")
#one time print
print("Hi, I am JARVIS. Your own AI bot. I can perform many things.")
name = input("By the way what's your name: ")
print("So your name is "+name)
print("I will remember that.")

#wishing
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning " + name + "!")
    if hour>=12 and hour<=18:
        print("Good afternoon " + name + "!")
    if  hour>18:
        print("Good evening " + name + "!")

#commands    
if __name__ == "__main__":
    wishMe()
    while True:
        print("")
        print("Type 'help' for all the commands")
        print("")
        choice = input("What can I do for you " + name + ": ")
        
        if 'wikipedia' in choice:
            print("")
            print("Searching wikipedia...")
            choice = choice.replace("wikipedia", "")
            results = wikipedia.summary(choice, sentences=2)
            print("According to wikipedia ")
            print(results)

        elif 'youtube' in choice:
            webbrowser.open("https:\\www.youtube.com")
                
        elif 'time' in choice:
            print("")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"It's {strTime}")

        elif 'open google' in choice:
            webbrowser.open("https:\\www.google.com")
        
        elif 'search in google' in choice:
            query = input("What should I search: ")
            print("Just a moment...")
            for i in search(query, tld="co.in", num=10, stop=10, pause=2):
                webbrowser.open(i)
                print("if you want to go back to pages you have visited ,here 👇 are the links for that.") 
                print(i)


        elif 'facebook' in choice:
            webbrowser.open("https:\\www.facebook.com")
        
        elif 'amazon' in choice:
            os.system("clear")
            webbrowser.open("https:\\www.amazon.in")
          
        elif 'flipkart' in choice:
            os.system("clear")
            webbrowser.open("https:\\www.flipkart.com")
        
        elif 'help' in choice:
            print("")
            print("Useful commands:")
            print("")
            print("youtube")
            print("open google")
            print("search in google")
            print("time")
            print("facebook")
            print("amazon")
            print("flipkart")
            print("calculate")
            print("exit")
            print("")
            print("**Note**")
            print(" Type anything to search in your existing browser.")
            print(" You can also search through wikipedia.")
            print(" JARVIS is made by Aritra Malik.")
            print("")
                    
        elif 'calculate' in choice:
            def add(x, y):
                return x + y

            def subtract(x, y):
                return x - y

            def multiply(x, y):
                return x * y

            def divide(x, y):
                return x / y
            
            print("")
            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            while True:
                C = input("Enter choice(1/2/3/4): ")

                if C in ('1', '2', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if C == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif C == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif C == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif C == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))
                    break
                else:
                    print("Invalid Input")
        
        elif 'exit' in choice:
            hour = int(datetime.datetime.now().hour)
            print("")
            if  hour>18:
                print("Thanks for using me " +name + "." + "Good night! 😴 .")
            
            else:
                print("Thanks for using me "+name+"."+"Have a good day! 😃")
            exit()
       
        else:
            print("")
            print("Didn't match any, trying to search the web.")
            for url in search(choice, tld="co.in", num=1, stop = 1, pause = 2):
                os.system("clear")
                webbrowser.open("https://google.com/search?q=%s" % choice)




    
