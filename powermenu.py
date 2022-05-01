import os

  
shutdown = input("Do you wish to powe comandlog your computer ? shutdown / restart / log : ")
  
if shutdown == 'no':
    exit()
elif shutdown=='shutdown':
    os.system("shutdown /s /t 1")
elif shutdown=='restart':
    os.system("shutdown /r /t 1")
elif shutdown=='log':
    os.system("shutdown -l")

