#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name = "John Doe",job = "unemployed"):
         self.set_name(name)
         self.set_job(job)


    def get_name(self):
        return self._name
    
    def set_name(self,value):
        if isinstance(value,str) and 1 <= len(value) <= 25:
            title_value = value.title()
            self._name= title_value
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        return self._job
    
    def set_job(self,value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name,set_name)
    job = property(get_job,set_job)

cindy = Person(name = "Cindy" , job = "Admin")
print(cindy.name,cindy.job)
