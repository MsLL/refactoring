class Movie():
    def __init__(self, title, type):
        self.title = title
        self.type = type

    def getFrequentRenterPoints(self, daysRented):
        if (self.type == 'NEWRELEASE' and daysRented > 1):
            return 1
        return 0


class CalCostRule():
    def getCost(self, daysRented):
        pass


class CHILDRENSCalCostRule(CalCostRule):
    def getCost(self, daysRented):
        amount = 2
        if (daysRented > 2):
            amount += (daysRented - 2) * 1.5
        return amount


class REGULARCalCostRule(CalCostRule):
    def getCost(self, daysRented):
        return daysRented * 3


class NEWRELEASECalCostRule(CalCostRule):
    def getCost(self, daysRented):
        amount = 1.5
        if (daysRented > 3):
            amount += (daysRented - 3) * 1.5
        return amount


class CalCostRuleFactory():
    @staticmethod
    def getCalCostRule(movieType):
        if (movieType == 'CHILDRENS'):
            return CHILDRENSCalCostRule();
        if (movieType == 'REGULAR'):
            return REGULARCalCostRule();
        if (movieType == 'NEWRELEASE'):
            return NEWRELEASECalCostRule();


class Rental():
    def __init__(self, movie, daysRented):
        self.movie = movie
        self.daysRented = daysRented


class Customer():
    def __init__(self, name):
        self.name = name
        self.rental = []

    def addRental(self, rental):
        self.rental.append(rental)

    def statement(self):
        cost = 0
        frequentRenterPoints = 0
        result = ""
        for rental in self.rental:
            costThis = CalCostRuleFactory.getCalCostRule(rental.movie.type).getCost(rental.daysRented)
            cost += costThis
            frequentRenterPoints += rental.movie.getFrequentRenterPoints(rental.daysRented)

            result += "{title}\t{cost}\n".format(
                title=rental.movie.title,
                cost=str(costThis)
            )
        result += "Amount owed is {totalCost}\n".format(totalCost=str(cost))
        result += "You earned {frequentRenterPoints} frequent renter points".format(
            frequentRenterPoints=str(frequentRenterPoints))
        print(result)


customer = Customer('tli2')
customer.addRental(Rental(Movie('李欢迎', 'NEWRELEASE'), 5))
customer.addRental(Rental(Movie('三国演艺', 'REGULAR'), 10))
customer.addRental(Rental(Movie('娜扎', 'CHILDRENS'), 12))
customer.statement()
# output:
# 李欢迎  4.5
# 三国演艺        30
# 娜扎    17.0
# Amount owed is 51.5
# You earned 1 frequent renter points

