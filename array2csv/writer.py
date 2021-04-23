

class Writer(object):

    def __init__(self, data):
        self.data = data

    def set_length(self):
        return len(self.data)

    def save(self):
        n = self.set_length()
        print("residueA,residueB,distance")
        for i in range(n):
            for j in range(n):
                if self.data[i][j] < 20:
                    print("%i,%i,%.2f" % (i + 1, j + 1, self.data[i][j]))