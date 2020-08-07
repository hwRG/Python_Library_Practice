import clipboard
import webbrowser
while True:
    select = input("Press 1 is connectively, 2 is broken sentence(0 is break) : ")
    if select == '1':
        text = input()
    elif select == '2':
        text = input()
        text = text.replace(". ", ".\n\n")
    elif select == '0':
        break
    else:
        print("다시 입력해 주세요.")
        continue
    clipboard.copy(text)
    webbrowser.open("https://translate.google.com/")
    