import random as r
import time
import os as o


class com():
    place=None
    __places = ['tirupati','kasi','shirdhi','kolhapur','kanyakumari','ooty']
    __tir = ['kapilteertham', 'thuda',
             'SV University', 'Tirumala', 'Jalashakam']
    __kasi = ['Shri kashi Vishwanath Temple',
              'Dashashwamedh Ghat', 'Assi Ghat', 'Manikarnika Ghat']
    __shir = ['Shri Sai Baba Temple', 'Dwarakamai', 'Sanstahn Trust',
              'Shri baba Devotional Park', 'sanisingnapur']
    __kol = ['Mahalaxmi Temple', 'Siddhagiri Museum',
             'Kaneri math', 'Narsinhwadi Datta Mandir']
    __kanya = ['Vivekananda Rock Memorial', 'Thiruvallur Statue',
               'Our Lady of Ransom Shrine', 'Kanyakumari Beach']
    __ooty = ['Government Rose Garden', 'Boat House',
              'St.Stephens Church', 'Botanical Garden', 'Doddabetta Peak']
    __cost = [1000, 10000, 5000, 4000, 6500, 9000]
    __guides = {'John': 'english', 'siva': 'telugu', 'manikumar': 'tamil',
                'ram': 'telugu', 'datta': 'hindi', 'akhil': 'tamil', 'guru': 'hindi'}
    __languages=['hindi','telugu','tamil','english']
    __previousPlan = None

    def costid(self, place):
     for i in range(0, len(self.__places)):
          if self.__places[i] == place:
               return i

    def printcity(self, place):
        match place:
            case 'tirupati':
                j = 1
                for i in self.__tir:
                    print(j, '.', i)
                    j = j+1
            case 'kasi':
                j = 1
                for i in self.__kasi:
                    print(j, '.', i)
                    j = j+1
            case 'shirdhi':
                j = 1
                for i in self.__shir:
                    print(j, '.', i)
                    j = j+1
            case 'kolhapur':
                j = 1
                for i in self.__kol:
                    print(j, '.', i)
                    j = j+1
            case 'kanyakumari':
                j = 1
                for i in self.__kanya:
                    print(j, '.', i)
                    j = j+1
            case 'ooty':
                j = 1
                for i in self.__ooty:
                    print(j, '.', i)
                    j = j+1

    def journey(self):
        print("Travel Place:",end='')
        flag=0
        place = input()
        for i in self.__places:
            if (i == place):
               print("\nLoding", end='')
               for i in range(0, 5):
                    print('.', end='')
                    time.sleep(1)
               print("\nwe guide and provide to this place....")
               flag=1
               break
        if flag==0: 
            print("we dont serve to this place")
            return
        print("We cover These places :")
        self.printcity(place)
        print("would You Continue With Pakage(y/n):")
        con = input()
        if (con == 'y'):
            print("Bill with name:")
            self.__name = input()
            print("Number of Travellers :")
            num = int(input())
            
            time.sleep(3)
            o.system('cls')
            print("Loding",end='')
            for i in range(0, 5):
                    print('.', end='')
                    time.sleep(0.5)

            self.selectguide()

    def selectguide(self):
        print("Guide Selection:")
        print("enter Guide's Language Preference:",end='')
        f=input()
        flag=0
        for i in self.__languages:
            if(i==f):
                flag=1
                break
        if flag==0:
            print("sorry! enter another preference")
            return
        else :
            print("we got u the preffered guide")
        print("list of guides filtered:")
        j=1
        for key, value in self.__guides.items():
            if(value==f):
                print(j,'.',key)
                j=j+1
        print("Choice one guide name:",end='')
        guide_name=input()
        print("Guide conformation(y/n):")
        con=input()
        if(con=='y'):
            cos=r.sample(range(2000,2500),1)
            print("______BILL______")
            print("name:{}".format(self.__name))
            print("number of Travellers :", self.num)
            print("Destination place:", self.place)
            print("conformed Places to Visit:")
            print(self.printcity(self.place))
            c = self.costid(self.place)
            print("Total Cost :{} ".format(self.num*self.__cost[c]))
            print("Conformed Guide :",guide_name)
            print("Guide Fee:{}/-".format(cos))
            print("\n\nThanks visit again")
            return
        else:
            print("no problem Thanks! visit again")
            return


