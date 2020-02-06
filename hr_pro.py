import datetime
class Employee:
   #Employee class here
	def __init__(self, name, age, salary, employment_year):
		self.name=name
		self.age=age
		self.salary=salary
		self.employment_year=employment_year
	def get_working_years(self):
		now = datetime.datetime.now()
		return now.year-self.employment_year
	
   

class Manager(Employee):
	def __init__(self, name, age, salary, employment_year, bonus_percentage):
		self.bonus_percentage=bonus_percentage
		Employee.__init__(self, name, age, salary,employment_year )
		
	def get_bonus(self):
		return self.bonus_percentage*self.salary
    #Manager class here
        
def main():
	# main code here
	EList =[]
	MList =[]
	con=True
	print("Welcome to HR Pro 2019")
	while con:
		print("""
Options:
    1. Show Employees
    2. Show Managers
    3. Add An Employee
    4. Add A Manager
    5. Exit""")
		inp=int(input("What would you like to do? "))
		print("------------")
		
		if (inp==1):
			if(len(EList)==0):
				print("No Employees yet!")
			else:
			
				print("Employees  ")
				for i in range(0, len(EList)):
					print("Name: "+ EList[i].name+", Age: "+str(EList[i].age)+", Salary: "+ str(EList[i].salary)+", working Years: "+str(EList[i].get_working_years()))
			print("------------")
			
		elif (inp==2):
			if (len(MList)==0):
				print("No Managers yet!")
			else:
				print("Managers  ")
				for i in range(0, len(MList)):
					print("Name: "+ MList[i].name+", Age: "+str(MList[i].age)+", Salary: "+ str(MList[i].salary)+", working Years: "+str(MList[i].get_working_years())+", Bonus: "+str(MList[i].get_bonus()))
			print("------------")	
		elif(inp==3):
			name=input("Name: ")
			age=int(input("Age: "))
			salary=int(input("Salary: "))
			empyear=int(input("Employement year: "))
			e=Employee(name, age, salary, empyear)
			EList.append(e)
			print("Employee added succesfully")
			print("------------")
			
		elif(inp==4):
			name=input("Name: ")
			age=int(input("Age: "))
			salary=int(input("Salary: "))
			empyear=int(input("Employement year: "))
			bon=float(input("Bonus Percentage: "))
			m=Manager(name, age, salary, empyear, bon)
			MList.append(m)
			print("Manager added succesfully")
			print("------------")
			
		else:
			con=False
			
		
			
		
			
				
		

if __name__ == '__main__':
	main()
