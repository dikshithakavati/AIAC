class emp:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def inc(self,p):
        self.s=self.s+(self.s*p/100)
e=emp("dikshitha",20000)
e.inc(10)
print(f"employee name:{e.n}\nemployee salary:{e.s}")