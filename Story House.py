class Scene:
  def __init__(self,index,no,text,question,branch1,branch2 ):
    self.index= index
    self.no = no
    self.text = text
    self.question= question
    self.branch1= branch1
    self.branch2= branch2
    


scenes = []


file = open("StoryLine.txt", "r")
for line in file:
    line = file.readline()
    attributes = line.split("#")
    s = Scene(attributes[0], attributes[1],attributes[2],attributes[3],attributes[4],attributes[5])

    scenes.append(s)
    print(len(scenes))

i = 0
print (scenes[i].text)
userChoice=input(scenes[i].question)
while scenes[i].branch1 != "":
    if userChoice == "1":
        i = int(scenes[i].branch1)
    else:
        i = int(scenes[i].branch2)
    print (scenes[i].text)
    userChoice=input(scenes[i].question)

    
