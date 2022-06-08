#!/usr/bin/env python
# coding: utf-8

# Python Screening Assignment
# 1. Create a function in python to read the text file and replace specific content
# of the file.
# File name example.txt
# Origin file content This is a placement assignment
# Replace string Placement should be replaced by
# screening.
# Replaced file content This is a screening assignment
# 

# In[ ]:


def replacement():##Defined a function replacement which would replace placement with screening
    f= open("example.txt","r+")## Opening the file in read mode
    lines=f.read() #Reading the contents of the file
    rstring=lines.replace("placement","screening") #Replacing placemnt with screening and storing the replaced string      
    s=open("example.txt","w")#Opening the file in write mode
    s.write(rstring)#writing the replaced string in the file
    f.close()
    s.close
    print("Text changed sucessfully")
    


# In[ ]:


replacement()

2. Demonstrate use of abstract class, multiple inheritance and decorator in
python using examples.
# In[ ]:


#First we will import the necessary files
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, no_of_seats):
        self.no_of_seats = no_of_seats
    @abstractmethod
    def get_cost(self):
        pass


# In[ ]:


class Car(Vehicle):
    def __init__(self,no_of_seats,hp,cost):
        super().__init__(no_of_seats)
        self.hp=hp
        self.cost=cost
    def get_cost(self):
        return self.cost


# In[ ]:


class Bus(Vehicle):
    def __init__(self,no_of_seats,hp,cost,passengers):
        super().__init__(no_of_seats)
        self.hp=hp
        self.cost=cost
        self.passengers=passengers
    def get_cost(self):
        super().get_cost()


# In[ ]:


class Truck(Car,Bus):
    def __init__(self,no_of_seats,hp,cost,passengers):
        super().__init__(no_of_seats,hp,cost)
        self.passengers=passengers
    def get_cost(self):
        super().get_cost()


# In[ ]:


v=Truck(1000,90000,3,1)


# In[ ]:




