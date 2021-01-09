import wikipedia
import datetime
import webbrowser
from googlesearch import search
import os
import sys
import pyfiglet

#installation
command="pip install -r requirement.txt && exit"
os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")
command="gsettings set org.gnome.desktop.background picture-uri file:///home/aritra/jarvis/jarvis.jpg && exit"
os.system("gnome-terminal -e 'bash -c \""+command+";bash\"'")


os.system("clear")
#one time print
print("Hi, I am JARVIS. Your own AI bot. I can perform many things.")
name = input("By the way what's your name: ")
print("So your name is "+name)
print("I will remember that. \nHave a look in your wallpaper.")
#one time quistion
o = input("By the way did you heard about my little brother(y/n): ")
if o == 'y':
    print("OH really 😊 !!.\nHe is my cute little brother.\nFrom the famous WINDOWS OS.\nOur dad(DEVLOPER) want to make him a great person(PROGRAME).\nSo He is there with his friend to get success like me and you.\nForget that")
if o == 'n':
    print("OH.😞\nThanks for telling that.\nForget that") 

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
        ascii_banner = pyfiglet.figlet_format("||||| JARVIS |||||")
        print(ascii_banner)
        print("")
        print("Type 'help' for all the commands")
        print("")
        choice = input("What can I do for you: ")
        
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
            os.system("clear")
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
            print("open app")
            print("exit")
            print("")
            print("**Note**")
            print(" Type anything to search in your existing browser.")
            print(" You can also search through wikipedia.")
            print(" JARVIS is made by Aritra Malik.")
            print("")
                    
        elif 'calculate' in choice:
            os.system("clear")
            
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
                    print("Sorry "+name+" you typed some/a invalid Input")
        
        elif 'open app' in choice:
            os.system("clear")
            print("All app commands are:")
            print("")
            print("File manager names : nautilus[fedora,ubuntu], dolphine[kde], thunar[xfce], pacman[arch], nemo[mint]")
            print("Text editor: gedit[all]")
            print("pdf veiwer: acroread[all]")
            print("Libreoffice apps: libreoffice --'NAME OF THE APP'[example:libreoffice --writer]")
            print("Browsers: firefox[all], google-chrome[all]")
            print("Mailing apps: thunderbird[only those who have installed]")
            print("Terminal: gnome-terminal[all]")
            print("There are more apps but these are the default ones.") 
            print("")
            print("")
            app = input("which app I should open[example: libreoffice --writer ]: ")
            os.system(app)
                     
        elif 'exit' in choice:
            hour = int(datetime.datetime.now().hour)
            print("")
            if  hour>18:
                print("Thanks for using me " +name + "." + " Good night! 😴 .")
            
            else:
                print("Thanks for using me "+name+"."+" Have a good day! 😃")
            exit()
       
        else:
            print("")
            print("Didn't match any, trying to search the web.")
            for url in search(choice, tld="co.in", num=1, stop = 1, pause = 2):
                os.system("clear")
                webbrowser.open("https://google.com/search?q=%s" % choice)




    





































































