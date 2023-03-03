class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

# Create a new object
test = ClassTest()

# Both of this two exactly the same
test.instance_method()
ClassTest.instance_method(test)
