x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name']= 'Bryant'
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)

students = [
         {'first_name' : 'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for dictionary in students:
        output_string = ""
        for key, value in dictionary.items():
            output_string += f"{key} - {value}, "
        print(output_string[:-2])
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students) 


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key, value in dojo.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
printInfo(dojo)
