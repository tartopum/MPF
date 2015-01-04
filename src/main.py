from analysis.factory import Factory
from models.db import DBSelector
from models.cow import Cow


    
def main():
    factory = Factory()
    
    for num in DBSelector().cows():
        cow = Cow(num)

        factory.prod_by_day(cow)
        factory.prod_diff(cow)
        factory.prod_by_cons(cow)
        # factory.linear_reg(cow)


if __name__ == "__main__":
    main()
