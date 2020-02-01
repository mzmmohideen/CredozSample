# class a:
#     def reverse(self, c):

#         return c[::-1]


# class b(a, object):
#     def reverse(self):
#         c = raw_input("enter the word")
#         c = super(b, self).reverse(c[::-1])
#         return c


# if __name__ == "__main__":
#     s = b()
#     print s.reverse()


class IPL_2019:
    def CSK_List(self):
    	print(players)
    	self.players = players
        # self.watson = a
        # self.duPlessis = b
        # self.raina = c
        # self.dhoni = d
        # self.raydu = e
        # self.jadhav = f
        # self.jadeja = g
        # self.chahar = h
        # self.harbhajan = i
        # self.tahir = j
        # self.kuggeleijn = k

class IPL_summary(IPL_2019, object):
    def CSK_List(self, players):
        super(IPL_summary,self).CSK_List()
        self.total = sum(self.players.values())
        print("CSK Total score = ", self.total)
        self.run_rate = self.total/20
        print("Run rate = ", self.run_rate)

# import csv

# def csvReader():
# 	f = open('showData.csv', 'r')
# 	cs = list(csv.reader(f))
# 	header = cs[0]
# 	print dict(zip(header, cs[1]))


if __name__ == "__main__":
	# csvReader()
	# Z=IPL_summary()
	players = {
		"watson": 0,
		"duPlessis": 0,
		"raina": 0,
		"dhoni": 0,
		"raydu": 0,
		"jadhav": 0,
		"jadeja": 0,
		"chahar": 0,
		"harbhajan": 0,
		"tahir": 0,
		"kuggeleijn": 0
	}
	for i in players:
		players[i] = input("Enter the score of %s : "%i)

	Z=IPL_summary()
	Z.CSK_List(players)

# aa = eval(input("Enter the score of watson : "))
# bb = eval(input("Enter the score of duPlessis : "))
# cc = eval(input("Enter the score of raina : "))
# dd = eval(input("Enter the score of dhoni : "))
# ee = eval(input("Enter the score of raydu : "))
# ff = eval(input("Enter the score of jadhav : "))
# gg = eval(input("Enter the score of jadeja : "))
# hh = eval(input("Enter the score of chahar : "))
# ii = eval(input("Enter the score of harbhajan : "))
# jj = eval(input("Enter the score of tahir : "))
# kk = eval(input("Enter the score of kuggeleijn : "))

