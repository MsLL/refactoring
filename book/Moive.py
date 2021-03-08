#
class PriceState():
    def getPriceCode(self):
        pass


class ChildrenPrice(PriceState):
    def getPriceCode(self):
        return Movie.CHILDRENS


class NewReleasePrice(PriceState):
    def getPriceCode(self):
        return Movie.NEW_RELEASE


class RegularPrice(PriceState):
    def getPriceCode(self):
        return Movie.REGULAR


# class Movie is just a simple data class
class Movie():
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, priceCode):
        self.__title = title
        self.__price = None
        self.setPriceCode(priceCode)

    def getTitle(self):
        return self.__title

    def getPriceCode(self):
        return self.__price.getPriceCode()

    def setPriceCode(self, priceCode):
        if (priceCode == self.REGULAR):
            self.__price = RegularPrice()
        elif (priceCode == self.CHILDRENS):
            self.__price = ChildrenPrice()
        elif (priceCode == self.NEW_RELEASE):
            self.__price = NewReleasePrice()

    def getCharge(self, daysRented):
        result = 0
        if (self.getPriceCode() == Movie.REGULAR):
            result += 2
            if (daysRented > 2):
                result += (daysRented - 2) * 1.5
        elif (self.getPriceCode() == Movie.NEW_RELEASE):
            result += daysRented * 3
        elif (self.getPriceCode() == Movie.CHILDRENS):
            result += 1.5
            if (daysRented > 3):
                result += (daysRented - 3) * 1.5
        return result

    def getFrequentRenterPoints(self, daysRented):
        frequentRenterPoints = 1
        if (self.getPriceCode() == Movie.NEW_RELEASE and daysRented > 1):
            frequentRenterPoints += 1
        return frequentRenterPoints


# class Rental represents a customer renting a movie
class Rental():
    def __init__(self, movie, daysRented):
        self.__movie = movie
        self.__daysRented = daysRented

    def getMovie(self):
        return self.__movie

    def getDaysRented(self):
        return self.__daysRented

    def getCharge(self):
        return self.__movie.getCharge(self.getDaysRented())

    def getFrequentRenterPoints(self):
        return self.__movie.getFrequentRenterPoints(self.getDaysRented())


#
class Customer():
    def __init__(self, name):
        self.__name = name
        self.__rentals = []

    def addRental(self, Rental):
        self.__rentals.append(Rental)

    def getName(self):
        return self.__name

    def statement(self):
        result = ""

        for rental in self.__rentals:
            result += "{title}\t{cost}\n".format(
                title=rental.getMovie().getTitle(),
                cost=rental.getCharge())
        result += 'Amount owed is ' + str(self.getTotalCost()) + '\n'
        result += 'You earned ' + str(self.getTotalFrequentRenterPoints()) + ' frequent renter points'
        return result

    def getTotalCost(self):
        cost = 0
        for rental in self.__rentals:
            costThis = rental.getCharge()
            cost += costThis
        return cost

    def getTotalFrequentRenterPoints(self):
        frequentRenterPoints = 0
        for rental in self.__rentals:
            frequentRenterPoints += rental.getFrequentRenterPoints()
        return frequentRenterPoints


customer = Customer('tli2')
customer.addRental(Rental(Movie('李欢迎', Movie.NEW_RELEASE), 5))
customer.addRental(Rental(Movie('三国演艺', Movie.REGULAR), 10))
customer.addRental(Rental(Movie('娜扎', Movie.CHILDRENS), 12))
print(customer.statement())
# output：
# 李欢迎	15
# 三国演艺	14.0
# 娜扎	15.0
# Amount owed is 44.0
# You earned 4 frequent renter points
