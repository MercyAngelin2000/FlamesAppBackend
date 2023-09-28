from fastapi import APIRouter
router = APIRouter()

@router.post("/check")
def findFlames(data: dict):
    flames=['F','L','A','M','E','S']
    boy=list(data['boyName'].lower().replace(" ",""))
    girl=list(data['girlName'].lower().replace(" ",""))
    boyIndex=[]
    girlIndex=[]
    for i in range(len(boy)):
        for j in range(len(girl)):
            if boy[i]==girl[j]:
                boyIndex.append(i)
                girlIndex.append(j)
                boy[i]=0
                girl[j]=0
                break
    overallLength=(len(boy)-len(boyIndex))+(len(girl)-len(girlIndex))
    for letter in range(5):
        temp=[]
        x= overallLength
        if(overallLength>len(flames)):
            x%=len(flames)
            temp= flames[:x-1] if x==0 else flames[x:]+flames[:x-1]
        else:
            temp= flames[x:]+flames[:x-1]
        flames.clear()
        flames.extend(temp)
    flames= ''.join(flames)
    out= "Friend" if flames=='F' else "Love" if flames=='L' else "Affection" if flames=='A' else "Marriage" if flames=='M' else "Enemy" if flames=='E' else "Sister"  
    return {"res":"The relationship between {} and {} is {}".format(data['boyName'],data['girlName'],out)}
