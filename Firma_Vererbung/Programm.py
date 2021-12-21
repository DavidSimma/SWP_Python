if __name__ == "__main__":
    class Person:
        def __init__(self, firstname, lastname, age, isMale):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            self.isMale = isMale


    class Employee(Person):
        def __init__(self, firstname, lastname, age, gender, salary):
            super().__init__(firstname, lastname, age, gender)
            self.salray = salary


    class Leader(Employee):
        def __init__(self, firstname, lastname, age, gender, salary):
            super().__init__(firstname, lastname, age, gender, salary)


    class Department:
        def __init__(self, name):
            self.name = name

        leader = Leader("", "", 0, True, 0)
        employees = []


    class Company:
        departments = []


    e1 = Employee("Sebi", "Rimml", 19, False, 1800)
    e2 = Employee("Daniel", "Niederhauser", 18, True, 2400)
    l1 = Leader("David", "Simma", 18, True, 3200)
    d1 = Department("IT")
    d1.leader = l1
    d1.employees.append([e1, e2])
    c1 = Company()
    c1.departments.append(d1)


    def countDeps(com=Company()):
        return com.departments.count()


    def returnAllEmp(com=Company()):
        dep=[x for x in com.departments]
        emp=[]
        for a in dep:
            emp=[b for b in a.employees]
        return emp

    def countEmp(com=Company()):
        count = 0
        for d in com.departments:
            for a in d.employees:
                count += len(a)
        return count


    def countLead(com=Company()):
        count = 0
        for d in com.departments:
            if d.leader is not None:
                count += 1
        return count


    def biggestDep(com=Company()):
        count = 0
        bigCount = 0
        dep = None
        for d in com.departments:

            if d.leader is not None:
                count += 1
            for a in d.employees:
                count += len(a)
            if bigCount < count:
                bigCount = count
                dep = d
            count = 0
        return dep.name


    def howManyMen(com=Company()):
        ges = 0
        count = 0
        for d in com.departments:
            if d.leader is not None:
                if d.leader.isMale:
                    count += 1
                ges += 1
            for a in d.employees:
                for b in a:
                    if b.isMale:
                        count += 1
                    ges += 1

        return count / ges * 100


    print(countEmp(c1))
    print(countLead(c1))
    print(biggestDep(c1))
    print(howManyMen(c1), "%")
    for x in returnAllEmp(c1):
        for a in x:
            print(a.firstname)

