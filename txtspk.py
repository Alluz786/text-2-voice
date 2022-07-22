from gtts import gTTS
import os
print("TEXT TO VOICE"+'\U0001f600')
print('''
  ========================================================
       DEVELOPPER :  AL AMEEN HUSAIN
       SUPPORT : @_alameen_husain(instagram)
       PROJECT : Text converts to voice
  ========================================================


''')
 
txt = input("ENTER YOUR WORDS==>")
lg = 'en'
speech = gTTS(text=txt, lang=lg, slow=False)
save = input("save file name==>")
speech.save(save)
os.system(save)


