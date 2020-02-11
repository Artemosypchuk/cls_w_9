# git push -u origin master


class Person:
    def __init__(self, name: str, surname:str, age:int):

        self.__name: str = name
        self.__surname: str = surname
        self.__age: int = age

    @property
    def name(self):
        print("Getter prop")
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
        return self.__name
    @property
    def surname(self):
        print("Getter prop")
        return self.__surname

    @surname.setter
    def surname(self, new_surname: str):
        self.__surname = new_surname
        return self.__surname
    
    @property
    def age(self):
        print("Getter prop")
        return self.__name

    @age.setter
    def age(self, age: int):
        self.__age = age
        return self.__age

    def show_info(self):
        print("name: ", self.__name.title(), "\nsurname: ",
              self.__surname, "\nage: ", self.__age)


new_person = Person("Jon", "TRAVOLTA", 55)


new_person.name = "BILL"
new_person.age = 40

new_person.show_info()

class Junior(Person):
    def __init__(self,skill):
        self.__skill = skill
    @property
    def worked_place(self):
        print("-"*55)
        print(self.name,self.surname,"FaceBook")
        
mark = Junior("Mark","Tsukerberg",42)
mark.worked_place
mark.show_info()
