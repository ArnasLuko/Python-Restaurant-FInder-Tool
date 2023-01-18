#For this project, I created a series of classes that would process information regarding restaurants, 
#including their name, location, opening hours, distance from the user and rating, all of which would culminate in the 
#creating of a tool which finds the nearest and best restaurant. Below is the first class, which deals with locations. 
#It has a methods for finding and setting the co-ordinates of a location object as well as a method for finding the 
#Manhattan distance between two location objects.

import random #Importing of the random module.

class Location(): #Location class for creating location objects.
        
        def __init__(self, x, y):
            self.__x = x
            self.__y = y

        def get_loc(self): #Finds the co-ordinates of a location object.
            return (self.__x, self.__y)
        
        def set_loc(self, a, b): #Sets the co-ordinates of a location object.
            self.__x = a
            self.__y = b
            
        def __str__(self):
            X = str(self.__x)
            Y = str(self.__y)
            return str('Coordinates are: X=' + X + ' Y='+ Y)
        
        def manhat_meth(self, a): #Finds the manhattan distance between the co-ordinates of two location objects.
            loc1 = self.get_loc()
            x__loc1 = loc1[0]
            y__loc1 = loc1[1]
            loc2 = a.get_loc()
            x__loc2 = loc2[0]
            y__loc2 = loc2[1]
            res = abs(x__loc1-x__loc2) + abs(y__loc1-y__loc2)
            return res

        
locations = []

while len(locations) <= 10: #Loop to generate random locations.
    i = random.randint(0, 100)
    i2 = random.randint(0, 100)
    i3 = (i, i2)
    locations.append(i3)
            
loc = Location(10,15)
print(loc)
loc.set_loc(13, 16)
print(loc)
loc.get_loc()
loc1 = Location(0,0)

for x in range(0, 10):
    locx = locations[x]
    a = locx[0]
    b = locx[1]
    locy = Location(a,b)
    res = loc1.manhat_meth(locy)
    res = str(res)
    ch = 'A'
    x = chr(ord(ch) + x)
    print("Distance of Ref from " + x + " : " + res)

#Below is the second class created for the project, the Restaurant class. This class creates Restaurant objects which 
#contain restaurant information such as name, location and operating hours. The class has methods which can be used to 
#retrieve information on restaurant objects, such as name, location and operating hours, as well as a method for changing 
#the operating hours of a restaurant object. There is also a method which can check whether a restaurant is open or not.

class Restaurant(): #Restaurant class for creating restaurant objects.
    def __init__(self, a, b, c, d):
        self.name = a
        self.loc = b
        self.open = c
        self.close = d
    
    def __str__(self):
        locx = self.loc
        a = locx[0]
        b = locx[1]
        res = "Restaurant: " + self.name + ", in X: " + str(a) + " Y: " + str(b) + ", Operating hours: "+ str(self.open) + "-" + str(self.close)
        return res  #formatted to display restaurant information.
        
    def get_name(self): #returns the restaurant’s name.
        return self.name
    
    def get_operating_hours(self): #returns the opening and closing times in a tuple.
        return self.open, self.close
    
    def change_operating_hours(self,o,c): #updates the opening and closing times with new values.
        self.open = o
        self.close = c
    
    def getLocation(self): #returns the location object of the restaurant.
        return self.loc
    
    def is_open(self,curr): #tells whether the restaurant is open.
        if curr in range(self.open, self.close):
            return True
        else:
            return False
        
    
rat = Restaurant('MACCAS', (0, 10), 6, 23)
rat2 = Restaurant('BORGOR', (9, 24), 6, 21)
rat3 = Restaurant('BEPIS', (15, 31), 11, 21)
rat4 = Restaurant('JUSTINS', (30, 5), 12, 24)
rat5 = Restaurant('JUSTINS2', (30, 5), 15, 24)

print(rat.get_name())
print(rat.getLocation())
print(rat.get_operating_hours())
rat.change_operating_hours(10,22)
print(rat.get_operating_hours())

print(rat.is_open(7))
print(rat)

restaurants = [rat, rat2, rat3, rat4]

curtime = 7

for i in restaurants:
    opens = i.is_open(curtime)
    if opens == True:
        print(i)

#Below is the third class created for the project, the Where2Eat_tool class. This class processes information on multiple 
# restaurants, giving them ratings and checking to see which is the closest and best restaurant to a user location. 
# The information is contained in data structures inside the class. The class includes methods for updating the users 
# location, adding one or more restaurant and a rating to data structures, and a final tool for comparing information 
# on the restaurants to present a user with the closest and best rated option.

class Where2Eat_tool():

    
    def __init__(self, x, y):
        self.restaurant = []
        self.user_loc = Location(x, y)
        self.rating = {}
        self.openrest = []
   
    def reload_location(self, a, b): #Updates the self.user_loc (location of the user).
        locx = a
        locy = b
        self.user_loc = Location(locx, locy)
        
    def add_restaurant(self, new_rest, rating): #Adds a new restaurant and it's rating to the stored data structures.
        self.restaurant.append(new_rest)
        self.rating[new_rest.name] = rating
    
    def add_many_restaurants(self, rest_list, rating_list): #Adds many restaurants and their ratings to the stored data structures.
        for i in range(len(rest_list)):
            self.restaurant.append(rest_list[i])
            self.rating[rest_list[i].name] = rating_list[i]
            
    def info(self): #Prints information on the stored restaurants (including their rating)
        l = len(self.restaurant)
        c = 0
        for i in range(0, l):
            rating = list(self.rating.values())[c]
            print(self.restaurant[i], "Rating:", rating)
            c += 1
            
    def where_to_eat(self, curr_time): #Tool for finding the nearest and best restaurant.
        for a in self.restaurant: #First loop checks restaurant list for availiable restaurants, appending open ones to a list.
             if a.is_open(curr_time) == True:
                self.openrest.append(a)
                
        distances = {} 
        for i in self.openrest: ##Second loop checks restaurant distance away from self.user_loc, adding them to a dictionary in order of ascending distance.
            loc = i.getLocation()
            a, b = loc[0], loc[1]
            loc2 = Location(a, b)
            distances[i] = loc2.manhat_meth(self.user_loc)
        org_dist = sorted(distances.items(), key=lambda item:item[1])
        closest_dist = org_dist[0]
        close_restaurants = []
        for rest in org_dist: #Returns only the restaurants with the smallest Manhattan distance value.
            if rest[1] <= closest_dist[1]:
                close_restaurants.append(rest)
        
        final_cut = {}
        if len(closest_dist) > 0: #Checks the quantity of nearby restaurants (to see if the closest shares the same distance with another).
            for i in close_restaurants: #Orders the close restaurants by their rating.
                restname = close_restaurants[0][0].get_name()
                rating = self.rating[restname]
                final_cut[i] = rating
        org_cut = sorted(final_cut.items(), key=lambda item:item[1])
        res = org_cut[0][0][0]
        final_loc = res.getLocation()
        hours = res.get_operating_hours()
        print("Best option is the Restaurant: ", res.get_name(), " in X: ", final_loc[0], ", Y: ", final_loc[1]," Operating hours:", hours[0], "-", hours[1])
        print("Rating:", str(org_cut[0][1]), "/10 Distance:", str(org_cut[0][0][1]))
        

App = Where2Eat_tool(5,5)
print(App.user_loc)
App.reload_location(10, 10)
print(App.user_loc)
  
Res = Where2Eat_tool(0,0)
ResList = [rat, rat2, rat3, rat4, rat5]
RateList = [5, 4, 7, 10, 2]

Res.add_many_restaurants(ResList, RateList)
Res.info()

Res.where_to_eat(22)