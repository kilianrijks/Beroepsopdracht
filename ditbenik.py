while True:
  print("Hello You!, ik ben Kilian")
  print("de datum en tijd is")
  import datetime
  x = datetime.datetime.now()
  print(x)
  name = input("Wie ben jij?: ")
  print("Hello " + name)

  print("Hier zijn een aantal vragen over mezelf, je kunt antwoorden met a b en c")
  print("Waar woon ik?")

  print("a Hoorn")
  print("b Utrecht")
  print("c Amsterdam")

  answerq1 = input()

  if ( answerq1 == 'a' ):
    print("Dat is het goeie antwoord!")

  if ( answerq1 == 'b' ):
    print("Dit antwoord is fout! Ik woon in Hoorn")

  if ( answerq1 == 'c' ):
    print("Dit antwoord is fout! Ik woon in Hoorn")

  print("volgende vraag")
  print("op welke school in Hoorn zat ik voor het media college?")

  print("a het d'ampte")
  print("b het osg")
  print("c het Clusius")

  answerq2 = input()

  if ( answerq2 == 'a' ):
    print("Dit antwoord is fout! Ik zat op het clusius")

  if ( answerq2 == 'b' ):
    print("Dit antwoord is fout! Ik zat op het clusius")

  if (answerq2 == 'c' ):
    print("Dit is het goeie antwoord!")

  print("Laatste vraag")
  print("Hoe oud ben ik?")

  print("a 16")
  print("b 17")
  print("c 18")

  answerq3 = input()

  if ( answerq3 == 'a' ):
    print("Dit antwoord is goed!")

  if ( answerq3 == 'b'):
    print("Dit antwoord is fout! Ik ben 16")

  if ( answerq3 == 'c' ):
    print("Dit antwoord is fout! Ik ben 16")
        
  print("Wil je dit programma nog een keer doen? Type y/n")
  answer = input()

  if ( answer == 'n' ):
    print("Dankjewel")
    break

  elif( answer == 'y' ):
    print("Restarting...")

  
    
  



  

 


  





