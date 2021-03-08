# class Movie is just a simple data class
class Movie():
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, priceCode):
        self.__title = title
        self.__priceCode = priceCode

    def getTitle(self):
        return self.__title

    def getPriceCode(self):
        return self.__priceCode

    def setPriceCode(self, priceCode):
        self.__priceCode = priceCode


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
        result = 0
        if (self.getMovie().getPriceCode() == Movie.REGULAR):
            result += 2
            if (self.getDaysRented() > 2):
                result += (self.getDaysRented() - 2) * 1.5
        elif (self.getMovie().getPriceCode() == Movie.NEW_RELEASE):
            result += self.getDaysRented() * 3
        elif (self.getMovie().getPriceCode() == Movie.CHILDRENS):
            result += 1.5
            if (self.getDaysRented() > 3):
                result += (self.getDaysRented() - 3) * 1.5
        return result


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
        totalAmount = 0
        frequentRenterPoints = 0
        result = ""

        for rental in self.__rentals:
            frequentRenterPoints += 1
            if (rental.getMovie().getPriceCode() == Movie.NEW_RELEASE and rental.getDaysRented() > 1):
                frequentRenterPoints += 1

            result += "{title}\t{cost}\n".format(
                title=rental.getMovie().getTitle(),
                cost=rental.getCharge())
            totalAmount += rental.getCharge()
        result += 'Amount owed is ' + str(totalAmount) + '\n'
        result += 'You earned ' + str(frequentRenterPoints) + ' frequent renter points'
        return result


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
