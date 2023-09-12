import os
import json

def make(name):
    dic = {str(name):[]}
    f = open(str(name)+".txt", encoding="utf8")

    line = f.readline()

    while line != "\n":
        #print("hej")
        dic[str(name)].append(line[0:-1])
        line = f.readline()

    js = json.dumps(dic)
    with open("data.json", "w") as outfile:
        json.dump(dic, outfile)

#make("facts")

def make_01(name):
    #a = 0
    l = []
    f = open(str(name)+".txt", encoding="utf8")

    line = f.readline()

    while line != "":
        #print(a)
        #a += 1
        l.append(line[0:-1])
        line = f.readline()

    return l

dic = {"quotes":{}, "facts":[], "rhyme":{}}


f = open("rest/facts.txt", encoding="utf8")
line = f.readline()
while line != "\n":
    dic["facts"].append(line[0:-1])
    line = f.readline()
f.close()

f = open("rest/quotes.txt", encoding="utf8")
line = f.readline()[0:-1]

while line != "":
    author = line.split(" ")[0]
    author = author.split("\t")[0]

    
    quote = line[len(author):len(line)]
    while quote.startswith(" " or "\t" or " "):
        quote = quote[1:len(quote)]
    if quote.startswith("\t"):
        quote = quote[1:len(quote)]
    if author in dic["quotes"].keys():
        dic["quotes"][author].append(quote)
    else:
        dic["quotes"][author] = [quote]
    line = f.readline()[0:-1]



l = ["elf", "cze", "eng", "lat"]

for i in l:
    print("hej")
    dic["rhyme"][i] = make_01(i)





js = json.dumps(dic)
with open("data.json", "w") as outfile:
    json.dump(dic, outfile)


