emoticon = "v.v"
emoticon2 = "<0> <0>"

#execute main/change global variable to modifiable instead of accesbile
def main():
    global emoticon
    say("is anyone there? ")
    emoticon = ":D"#python doesnt want to change a global variable
    say("oh, hi")

def say(phrase):
    print(phrase+ " " + emoticon)



main()
