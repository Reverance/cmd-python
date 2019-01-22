import os, datetime, sys

def echo(inp):
        text = ""
        for a in range(len(inp)-1):
                text = text + inp[a+1] + " "
        print(text)

def history(inp):
        with open("history.csv","r") as file:
                oldFile = file.read()
        history = oldFile.split("\n")
        if len(inp) > 1:
                if inp[1] != "all":
                        length = int(inp[1])
                else:
                        length = len(history) + 1
        else:
                length = 10
        if len(history) > length:
                for a in range(length):
                        print(history[len(history)-11 + a])
        else:
                for a in range(len(history)):
                        print(history[a])

def clear():
        os.system("cls")

def command(inp,comm):
        if comm == "echo":
                echo(inp)
        elif comm == "history":
                history(inp)
        elif comm == "clear":
                clear()

def time():
        time = datetime.datetime.now()
        time = str(time)
        return time

def save(inp):
        with open("history.csv","r") as file:
                oldFile = file.read() + "\n"
        newFile =  oldFile + time() + " - " + inp
        with open("history.csv",'w') as file:
                file.write(newFile)

def run():
        while 1:
                rawInp = input("> ")
                save(rawInp)
                inp = rawInp.split()
                command(inp,inp[0])



print("#################")
print("#   OMANOMANOM   #")
print("#           CMD              #")
print("#################")
print("")
run()
