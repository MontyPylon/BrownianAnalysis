class RemoveColumns:

    OUTFILE = open("data/data-245.csv", 'r')
    STARTSTRING = "data/particles/particle"
    ENDSTRING = ".csv"
    ID = 1

    def main(self):
        currentLine = self.OUTFILE.readline()
        currentList = currentLine.split(',')
        currentID = currentList[0]
        startX = float(currentList[1])
        startY = float(currentList[2][:-1])
        f = open(self.STARTSTRING + str(self.ID) + self.ENDSTRING, 'w')
        f.write("0, 0\n")
        f.close()
        while True:
            currentLine = self.OUTFILE.readline()
            if not currentLine: break
            currentList = currentLine.split(',')
            if(currentList[0] == currentID):
                f = open(self.STARTSTRING + str(self.ID) + self.ENDSTRING, 'a')
                x = float(currentList[1]) - startX
                y = float(currentList[2][:-1]) - startY
                f.write(str(x) + "," + str(y) + "\n")
                f.close()
            else:
                currentID = currentList[0]
                self.ID += 1
                startX = float(currentList[1])
                startY = float(currentList[2][:-1])
                g = open(self.STARTSTRING + str(self.ID) + self.ENDSTRING, 'a')
                g.write("0, 0\n")






if __name__ == "__main__":
    col = RemoveColumns()
    col.main()
