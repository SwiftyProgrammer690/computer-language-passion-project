# Imports be like...
from colorama import Fore
import time
import os

# Actual god logo and variables be like...
logo = '''
                                                                                                                          
     QQQQQQQQQ                         iiii                   
   QQ:::::::::QQ                      i::::i                  
 QQ:::::::::::::QQ                     iiii                   
Q:::::::QQQ:::::::Q                                           
Q::::::O   Q::::::Quuuuuu    uuuuuu  iiiiiii zzzzzzzzzzzzzzzzz
Q:::::O     Q:::::Qu::::u    u::::u  i:::::i z:::::::::::::::z
Q:::::O     Q:::::Qu::::u    u::::u   i::::i z::::::::::::::z 
Q:::::O     Q:::::Qu::::u    u::::u   i::::i zzzzzzzz::::::z  
Q:::::O     Q:::::Qu::::u    u::::u   i::::i       z::::::z   
Q:::::O     Q:::::Qu::::u    u::::u   i::::i      z::::::z    
Q:::::O  QQQQ:::::Qu::::u    u::::u   i::::i     z::::::z     
Q::::::O Q::::::::Qu:::::uuuu:::::u   i::::i    z::::::z      
Q:::::::QQ::::::::Qu:::::::::::::::uui::::::i  z::::::zzzzzzzz
 QQ::::::::::::::Q  u:::::::::::::::ui::::::i z::::::::::::::z
   QQ:::::::::::Q    uu::::::::uu:::ui::::::iz:::::::::::::::z
     QQQQQQQQ::::QQ    uuuuuuuu  uuuuiiiiiiiizzzzzzzzzzzzzzzzz
             Q:::::Q                                          
              QQQQQQ                                          
                                                              
'''

# Stuff I don't know be like
os.system('clear')

# Introductory be like...
print(Fore.GREEN, "\nWelcome to this awesome\n")
print(Fore.GREEN, logo)
print("(c) Swarit Choudhari and Leilah Dinh, Made for a passion project!\n")

# Functions be like...
def ask_questions():

    def exit_quiz():
      print("Wrong! Now you will be redirected back to the terminal... Try again!")
      time.sleep(3)
      exit()

    def correct():
      print("\nCorrect!\n")
      time.sleep(2)

    question_1 = int(input("What are the strenghts of a compiled language? 1. It's Faster, 2. It's Slower, 3. It can handle complex tasks? "))
    if question_1 != 1:
      exit_quiz()
    else:
      correct()
      question_2 = int(input("What is an interpreted language good for handling? 1. It cannot handle complex tasks, 2. It can handle complex tasks, 3. It's faster? "))
      if question_2 != 2:
        exit_quiz()
      else:
        correct()
        question_3 = int(input("What is a compiled language? 1. C, 2. Python, 3. Java? "))
        if question_3 != 1:
          exit_quiz()
        else:
          correct()
          question_4 = int(input("What is a interpreted language? 1. C++, 2. Rust, 3. Perl? "))
          if question_4 != 3:
            exit_quiz()
          else:
            correct()
            print("This is your last question and then you get your next clue and instructions on it! You are doing great! Keep up the hard work!\n")
            question_5 = int(input("Who invented the world's first computer language? 1. Ada, 2. Lovelace, 3. Ada Lovelace? "))
            if question_5 != 3:
              exit_quiz()
            else:
              correct()
              print("Yay! You did it! Your next clue awaits you in the file labeled, '1.txt'. TIP: To access files, all you need to do in the terminal is 'cat [name_of_file]'\n")
              quit()

ask_questions()
