class Terrain:
    def __init__(self, contents):
        numbers = [int(i) for i in contents[0].split() if i.isdigit()]
        self._width = numbers[0]
        self._height = numbers[1]
        self._cust_offices = numbers[2]
        self._reply_offices = numbers[3]
        self.terrain = []
        print("Width: {}\
        \nHeight: {}\
        \nCustomer Offices: {}\
        \nReply Offices: {}".format(self._width, self._height, self._cust_offices,
        self._reply_offices))
        # Create the flat map
        for terrain_line in contents[self._cust_offices+1:]:
            for c in terrain_line.replace("\n", ""):
                self.terrain.append(c)

    def map_2d_to_flat(row, col):
        return row * self._width + col

    def insert(self, item):
        idx = map_2d_to_flat(item.row, item.column)
        self.terrain[idx] = item.points

class Customer:
    def __init__(self, column, row, points):
        self.column = column
        self.row = row
        self.points = points

    def get_customers():
        inputFile = open("input.txt","r")
        lines = inputFile.read().splitlines()
        firstLine = list(lines[0].split(" "))
        c = firstLine[2]
        count=1
        customers=[]
        for client in lines[1:]:
            fields = client.split(" ")
            customers.append(Customer(fields[0],fields[1],fields[2]))
            count+=1
            if(count>int(c)):
                break

if __name__ == '__main__':
    path = '/Users/michaliskaseris/Documents/dev/reply-challenge/reply-2019/input1.txt'
    f = open(path, "r")
    lines = f.readlines()
    terrain = Terrain(lines)
