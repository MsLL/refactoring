class Movie():
    def __init__(self, title):
        self.title = title

    def getFrequentRenterPoints(self, daysRented):
        pass

    def getCost(self, daysRented):
        pass


class CHILDRENSMovie(Movie):
    def __init__(self, title):
        Movie.__init__(self, title)

    def getCost(self, daysRented):
        amount = 2
        if (daysRented > 2):
            amount += (daysRented - 2) * 1.5
        return amount

    def getFrequentRenterPoints(self, daysRented):
        return 0


class REGULARMovie(Movie):
    def __init__(self, title):
        Movie.__init__(self, title)

    def getCost(self, daysRented):
        return daysRented * 3

    def getFrequentRenterPoints(self, daysRented):
        return 0


class NEWRELEASEMovie(Movie):
    def __init__(self, title):
        Movie.__init__(self, title)

    def getCost(self, daysRented):
        amount = 1.5
        if (daysRented > 3):
            amount += (daysRented - 3) * 1.5
        return amount

    def getFrequentRenterPoints(self, daysRented):
        if (daysRented > 1):
            return 1
        return 0


class Rental():
    def __init__(self, movie, daysRented):
        self.movie = movie
        self.daysRented = daysRented


class Customer():
    def __init__(self, name):
        self.name = name
        self.rental = []

    def addRental(self, rental):
        self.rental.append(rental);

    def statement(self):
        cost = 0
        frequentRenterPoints = 0
        result = ""
        for rental in self.rental:
            costThis = rental.movie.getCost(rental.daysRented)
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
customer.addRental(Rental(NEWRELEASEMovie('李欢迎'), 5))
customer.addRental(Rental(REGULARMovie('三国演艺'), 10))
customer.addRental(Rental(CHILDRENSMovie('娜扎'), 12))
customer.statement()
# output:
# 李欢迎  4.5
# 三国演艺        30
# 娜扎    17.0
# Amount owed is 51.5
# You earned 1 frequent renter points

