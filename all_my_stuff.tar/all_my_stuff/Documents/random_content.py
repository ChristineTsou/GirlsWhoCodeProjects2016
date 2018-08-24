import random
adjective_list=["Rocky","Beautiful","Strong","Musical","Cheap","Corrupt"]
ing_verb_list=["Dancing","Singing","Partying","Laughing","Flying","Cheering"]
noun_list=["Cats","Angels","Beauties","Rockstars","Pirates","Canaries","Sparrows"]
num_adj=len(adjective_list)
num_ing=len(ing_verb_list)
num_noun=len(noun_list)
random_index1=random.randint(0,num_adj-1)
random_index2=random.randint(0,num_ing-1)
random_index3=random.randint(0,num_noun-1)
print("The "+adjective_list[random_index1]+" "+ing_verb_list[random_index2]+" "+noun_list[random_index3])

#biography
places=["Seattle","Miami","Austin","Oklahoma City","Detroit","Los Angeles","Boston","New York City"]
family=["brother","sister","step-father","mother","kids","step-mother","father"]
animals=["dogs","cats","ants","turkeys","mice","head-lice","hamsters","termites","wasps","bees"]
hobby1=["crafting","drawing","climbing","laughing","face-palming","swimming","crying"]
hobby2=["lying","jumping","writing","typing","coding","driving"]
name=["Alice","Mary","Jessica","Lily","Dove","Juniper","Summer"]
num_places=len(places)
num_family=len(family)
num_animals=len(animals)
num_hobby1=len(hobby1)
num_hobby2=len(hobby2)
num_name=len(name)
random_index4=random.randint(0,num_places-1)
random_index5=random.randint(0,num_family-1)
random_index6=random.randint(0,num_animals-1)
random_index7=random.randint(0,num_hobby1-1)
random_index8=random.randint(0,num_hobby2-1)
random_index9=random.randint(0,num_name-1)
print(name[random_index9]+" was born in "+places[random_index4]+" and lived with her "+family[random_index5]+ " and her two "+animals[random_index6]+". She enjoys "+hobby1[random_index7]+" and "+hobby2[random_index8]+".")




