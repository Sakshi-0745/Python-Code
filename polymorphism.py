class bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot.")
class sparrow(bird):
    def flight(self):
        print("Sparrows can fly.")
class ostrich(bird):
    def flight(self):
        print("Ostriches cannot fly.")
b=bird()
b_sp = sparrow()
b_ost = ostrich()
b.intro()
b.flight()

b_sp.intro()
b_sp.flight()

b_ost.intro()
b_ost.flight()