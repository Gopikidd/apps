class operaoroverload:

    def add(self, a, b):
        self.a = a
        self.b = b

        print(self.a - self.b )





obj = operaoroverload()
obj.add(10, 5 )
obj.add(b=5, a=50)

