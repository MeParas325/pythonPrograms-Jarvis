import pickle

cars = ["MclarenGT", "Audi", "BMW", "Lamborgini"]
file = "mycar.pkl"
fileobj = open(file, "wb")
pickle.dump(cars, fileobj)
fileobj.close()

file = "mycar.pkl"
fileobj = open(file, "rb")
car = pickle.load(fileobj)
print(car)
print(type(car))
