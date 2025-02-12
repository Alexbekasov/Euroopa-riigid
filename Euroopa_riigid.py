from random import *
def failist_to_dict(f:str):
    riik_pealinn={} #sõnastik {"Riik": "Pealinn"}
    pealinn_riik={} #sõnastik {"Riik": "Pealinn"}
    riigid=[] #järjend, kus talletakse riigide nimetused
    file=open(f,'r', encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split('-') #k-võti, v-väärtus
        riik_pealinn[k]=v
        pealinn_riik[v]=riigid.append(k)
    file.close()
    return riik_pealinn,pealinn_riik,riigid
#käivitame loodud funktsion
riik_pealinn,pealinn_riik,riigid=failist_to_dict("riigid_pealinnad.txt")
riigid=list(riik_pealinn.values())
print(riik_pealinn)
print(riik_pealinn.values())

while True:
    riik=input("Riik: ")
    if riik=="A": break
    print("Pealinn: ", riik_pealinn[riik])

for key,value in riik_pealinn.items():
    print(key+"-"+value+"\n")