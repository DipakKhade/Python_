# Shoutouts to Everyone | Python Tutorial - Day #83

# module pywin32  for converting text in speech 



from text_to_speech import save

# save("Hello World", "en", file="Hello-World.mp3")

list=['Dipak','Gaurav','Aniket']


for list in list:
    save(f'shoutout to {list}','en',file=f'shoutout_to_everyone_{list}.mp3')
    list=list+1






