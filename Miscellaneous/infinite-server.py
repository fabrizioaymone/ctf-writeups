import requests
import re

ok=True
s=requests.Session()
r = s.get("http://infinite.challs.olicyber.it")
page = r.text
i=0
while(ok and i <550):    
    print(page)
    i+=1
    print("COUNT = ", i)
    if("ART TEST" in page):
        question = re.search(r"<p>.*</p>", page).group()    
        print("this is the question: ", question)
        if "Verde" in question:
            print("the color is green")
            nextpage = s.post("http://infinite.challs.olicyber.it", data={"Verde":""})
        elif "Rosso" in question: 
            print("the color is red")
            nextpage = s.post("http://infinite.challs.olicyber.it", data={"Rosso":""})
        elif "Blu" in question:
            print("the color is blue")
            nextpage = s.post("http://infinite.challs.olicyber.it", data={"Blu":""})
        else:
            print("ERROR")
    elif("MATH TEST" in page):
        question = re.search(r"<p>.*</p>", page).group()
        print("this is question", question)
        a = re.search(r"\d+\s", question).group()
        print("this is a: ", a)
        a = int(a[:-1])
        b = re.search(r"\d+\?", question).group()
        b = int(b[:-1])
        if "+" in question:
            ris = a+b
        elif "-" in question:
            ris = a-b
        elif ":" in question:
            ris = a/b
        elif "*" in question:
            ris = a*b
        nextpage = s.post("http://infinite.challs.olicyber.it", data = {"sum": ris})
    elif("GRAMMAR TEST" in page):
        question = re.search(r"<p>.*</p>", page).group()
        print("this is question", question)
        letter = re.search(r'\s".*"\s', question).group()
        letter = letter[2]
        print("this is letter", letter)
        word = re.search(r'a\s".*"\?', question).group()
        word = word[1:-2]
        print("this is word", word)
        ris = word.count(letter)
        print("this is word count", ris)
        nextpage = s.post("http://infinite.challs.olicyber.it", data = {"letter": ris, "submit": "Submit"})
    else:
        ok = False
    page = nextpage.text


print(page)
