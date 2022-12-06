class developer:

    def __init__(self):
        self.__seniority = 'Junior'
        self.skills = ''

    def display(self) :
        print('Bienvenido a turing with {seniority} developer with skill {skills}'.format(seniority=self.__seniority, skills=self.skills))


class NodeJS(developer):
    def __init__(self):
        super().__init__()    
        self.__seniority = "Senior"
        self.skills = 'NodeJS' 

c = NodeJS()
c.display()  

print(type(c))