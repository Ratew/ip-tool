import os,sys
os.system("clear")
print("\033[32m [+] Paketler İndiriliyor...\033[0m")
print()

os.system("pip install --upgrade pip")
os.system("pkg upgrade && pkg update")
os.system("pkg install python -y ")
os.system("pkg install python2 -y")
os.system("pip install requests")
os.system("pip install socket")
os.system("pip install json")
print()
print()
