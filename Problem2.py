# Application that takes individual words form Luceafarul and compares them to a dictionary to see with are anagrams
def anagramchk(word,chkword):
    if word != chkword:  #excluding identical words
        for letter in word:  
            if letter in chkword:  
                chkword=chkword.replace(letter, '', 1)  
            else:  
                return 0  
        return 1  
  
count=0 #anagrams counter
g=open('Luceafarul.txt', 'r')
for line in g:
    words = line.split() #splitting lines into words
    for wordin in words:
        f=open('english.txt', 'r')  
        for line in f:  
            line=line.strip()  
            if len(line)>=len(wordin): #considering only words with the same length
                if anagramchk(line,wordin):  #testing if the word is a anagram
                    print (line)
                    count += 1  #counting the number of anagrams found for a word
        if count != 0: print(count,'anagrams')
        count=0  #reseting counter
        f.close()  
g.close()