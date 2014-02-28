__author__ = 'Akshay'
#todo Add the organisation class, student class, mentor class.

from numpy import loadtxt
class Gsoc:
    """
    Main class.
    """
    years = [2013, 2012, 2011, 2010, 2009]
    def __init__(self):
        return

    def load_array(self, year):
        if year in years:
            return loadtxt('gsoc_' + str(year) + 'txt', dtype = 'string')

    def get_organisation(self, year):
            a = self.load_array(year)
            return a

    def get_student(self, organisation, year):
        a = self.load_array(year)
        return [i[1] for i in a if i[3] == organisation]

    def get_mentor(self, organisation, year):
        a = self.load_array(year)
        return [i[1] for i in a if i[5] == organisation]

    def get_number_organisations(self, year):
        a = self.load_array(year)
        return len(a)

    def get_number_students(self, year, organisation):
        if organisation:
            a = self.load_array(year)
            return [len(i[1]) for i in a if i[3] == organisation]
        else:
            return self.get_number_organisations

    def get_number_mentors(self, year, organisation):
        if organisation:
            a = self.load_array(year)
            return [len(i[5]) for i in a if i[3] == organisation]
        else:
            return self.get_number_organisations



