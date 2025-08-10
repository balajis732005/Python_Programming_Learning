# To print the vowels and consonants in a word
word=input("Enter a word : ")
vowels=['a','e','i','o','u','A','E','I','O','U']
vow_word=con_word=""
v=c=0
for i in word:
    if i in vowels:
        vow_word+=i
        v+=1
    else:
        con_word+=i
        c+=1
print("VOWELS IN GIVEN WORD IN LIST FORM : ",list(vow_word))
print("VOWELS IN GIVEN WORD : ",vow_word)
print("THERE ARE ",v,"VOWELS IN A STRING")
print("CONSONANTS IN GIVEN WORD IN LIST FORM : ",list(con_word))
print("CONSONANTS IN GIVEN WORD : ",con_word)
print("THERE ARE ",c,"CONSONANTS IN A STRING")
