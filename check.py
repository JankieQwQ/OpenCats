def openTest(filename:bool) -> bool:
    try:
        file = open(filename)
        file.close()
        return True
    except:
        return False

def canOpen(filename:str,isOK:bool) -> None:
    print('[{}] OpenCats File Check:{}'.format(str(isOK).replace('True','OK').replace('False','ERROR'),filename))
    return

filelist = ['./src/init.py','./src/server.py','./src/web/index.html','./check.py','./run.bat','./other/ChatGPT_DAN.tex','./other/latexboom.tex','./other/markdownoom.md','./other/usbot.py']

for name in filelist:
    canOpen(name,openTest(name))