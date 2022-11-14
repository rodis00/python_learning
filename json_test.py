import json

class Human:
    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight
    
    def saveToJson(self, filename):
        dict = {
            "people": [{

                "name": self.name,
                "age": self.age,
                "weight": self.weight
            }]
        }
        jsonString = json.dumps(dict, indent=2)
        with open(filename, 'w') as file:
            file.write(jsonString)
    
    def readFromJson(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file.read())
        return data
    

MY_FILE2 = 'peoples.json'
person = Human("Jan", 25, 77)
# person = Human("Ania", 33, 68)
person.saveToJson(MY_FILE2)






        