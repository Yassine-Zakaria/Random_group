import random 
ma_list =["anne","aline","gros","eve","armand","yves","elv","allo","sonia","luc","marc","jules","kevin","Yassine","Hamza","issa"]
#this will contain an occurence of our list
maListOc = ma_list
#this list will contain our random list
random_list = None
groupe = 1
#for each element in ma_list, we randome and put into our variable
for i in ma_list:
#This condition will avoid errors when n is greater than 4
    if(len(ma_list)<=5):
        break
    random_list = random.sample(ma_list, 5)
    #then we remove data already randomize in our list, but the complexity is high for this little program
    for element in random_list:
        ma_list.remove(element)
    print("Goupe N°:",groupe, random_list)
    #and we finally print our randomized list
    print()
    print("______________________________")
    groupe += 1
print("Goupe N°:",groupe,maListOc)# j'ais juste ajouter ça et à la ligne 10 j'ais juste modifier le 6 par 5
