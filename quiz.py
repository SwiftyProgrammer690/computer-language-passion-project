# Imports be like...
from colorama import Fore

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

score_counter = 0

# Introductory be like...
print(Fore.GREEN, "\nWelcome to this awesome\n")
print(Fore.GREEN, logo)
print("(c) Swarit Choudhari and Leilah Dinh, Made for a passion project!\n")

# Functions be like...
def ask_questions(counter):
    def show_score(counter):
        print("Your score is " + counter + "/10")
    show_score(counter)
    