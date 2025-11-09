class IntList():
    def __init__(self):
        self.ints = self.insert()

    def insert(self):
        ent = []
        while len(ent) < 10:
            try:
                ent.append(int(input("Enter a integer")))
            except:
                print("Invalid entry")
        return ent

list_1 = IntList()
        
            
            
    
