import tkinter as tk
import numpy as np
import string
import re

prob={}    
ngrams={}
model={}


file = open("C:/Users/dell/Desktop/Newfolder/data.txt", "r", encoding="utf8")
data = file.read()
file.close()

# split data in single words
data=data.split()
wordsTokens = [w.strip(" ") for w in data]
#print(wordsTokens)

for i in range(len(wordsTokens)-2):
    seq=' '.join(wordsTokens[i:i+3])
    if seq not in ngrams.keys():
        ngrams[seq]=1
    else:
        ngrams[seq]+=1
        
  
for i in range(len(wordsTokens)-1):
    seq=' '.join(wordsTokens[i:i+2])
    if seq not in model.keys():
        model[seq]=1
    else:
        model[seq]+=1


for trigram in ngrams:
    bigram= trigram.split()
    seq=' '.join(bigram[0:2])

    prob[trigram]=ngrams[trigram]/model[seq]

#print(ngrams.keys())
#print(ngrams.values())
#print(" ")
#print(model.keys())
#print(model.values())
#print(" ")
#print(prob.keys())
#print(prob.values())

window = tk.Tk()
window.title("Auto Filler")
window.geometry("600x400")
text=tk.StringVar()

def predict():
    input=text.get()
    input_word=input.split(" ")
    output_list=[]
    for i in prob.keys():
        if input in  i :
            if i.split(" ")[0] != input_word[0] or i.split(" ")[1] != input_word[1]:
                continue
            output_list.append((i,prob[i]))

    output_list.sort(key=lambda x: x[1],reverse=True)

    numOfSuggestions = 5
    if numOfSuggestions > len(output_list):
        numOfSuggestions = len(output_list)

    print("    ",input)
    var='options are:\n '
    for i in range( 0 , numOfSuggestions ):
        print(output_list[i][0].split(" ")[2])
        var += output_list[i][0].split(" ")[2]
        var+='\n'

        
    answer_label = tk.Label(window, text=var)
    answer_label.place(rely=0.5, relwidth=1)  

name_label = tk.Label(window, text = 'Input', font=('calibre',10, 'bold'))
name_entry = tk.Entry(window,textvariable = text, font=('calibre',10,'normal'))
sub_btn=tk.Button(window,text = 'Submit', command = predict)
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)


window.mainloop()






