# Caesar's cipher (ROT 13)

# Let's make a program that transfers the given input into Caesar's cipher

# The point of this task is to learn strings and python along the way

# Have had some consiredable problems with going through the string

# Then found out on the internet that I should be transferring it to a list and then back

# Had considerable problems with getting the loop to go through the entire thing

# At first it only printed 1 letter in the correct form

# for example used these sources:
#            https://fi.wikipedia.org/wiki/Suomen_kielen_aakkoset
#            https://en.wikipedia.org/wiki/ROT13
#            https://en.wikipedia.org/wiki/Caesar_cipher
#            https://stackoverflow.com/questions/61175095/cannot-iterate-through-list-with-for-loop-in-python
#            https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
#            https://www.reddit.com/r/learnpython/comments/tc32uw/why_is_my_loop_only_iterating_once/


aakkoset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def Caesar():


   merkkijono = input().lower()
   merkkijono = list(merkkijono)

    
   for i in range(len(merkkijono)):

      if(merkkijono[i] == ' '):  # if the character is a space, then just go to the next index
          continue


      if merkkijono[i].isalpha():   # if the character is indeed an letter in the alphabet, let's go through. if not, then print an error and exit the program    
         kirjain = merkkijono[i]
         indeksi = aakkoset.index(kirjain)
         if indeksi <= 12:
               merkkijono[i] = aakkoset[indeksi+13]
         else:
               merkkijono[i] = aakkoset[indeksi-13]
      else:
          print("käytä kirjaimia")
          exit()
     

   if len(merkkijono) < 1:
      print("Täytyy olla vähintään yksi merkki")
      exit()
   return "".join(merkkijono)
   



print('Tervetuloa! Tämän ohjelman tarkoitus on kääntää antamasi viesti salaviestiksi.')
print(Caesar())



