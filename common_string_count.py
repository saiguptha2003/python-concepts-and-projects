def word(words):
    count=0
    for w in words:
      if len(w)>1 and w[0]==w[-1]:
         count=count+1
    return count
print(word(['aba','cb','cfc','191']))
