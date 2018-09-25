import pandas as pd



t1 = pd.read_csv("Temprature.csv")
l1 = pd.read_csv("Light.csv")
h1 = pd.read_csv("Humidity1.csv")
t2 = pd.read_csv("Temprature2.csv")
l2 = pd.read_csv("Light2.csv")
h2 = pd.read_csv("Humidity12.csv")

t=int(t2.values[-1])-int(t1.values[-1])
h=int(h2.values[-1])-int(h1.values[-1])
l=int(l2.values[-1])-int(l1.values[-1])


if(int(t2.values[-1]) < 10):
    print ("Its Too Cold Outside!!\nTrips are not Recomanded!!\n")
    
elif(int(t2.values[-1]) > 40):
    print ("Its Too Hot Outside!!\nTrips are not Recomanded!!\n")
    
elif ( t < 0 ):
    print ( "Its compratively Colder Outside: \n" )
    if(t < -15):
        print ("Temprature change could affect your health\n")
    else:
        print ("But Temprature change could not affect your health\n")
else :
    print ( "Its compratively Hotter Outside: \n" )
    if(t > 15):
        print ("Temprature change could affect your health\n")
    else:
        print ("But Temprature change could not affect your health\n")

