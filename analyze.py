class RemoveColumns:

    OUTFILE = open("data/data-253.csv", 'r')
    STARTSTRING = "data/particles/particle"
    ENDSTRING = ".csv"
    ID = 61

    def main(self):
        currentLine = self.OUTFILE.readline()
        currentList = currentLine.split(',')
        currentID = currentList[3]
        startX = float(currentList[5])
        startY = float(currentList[6].rstrip())
        f = open(self.STARTSTRING + str(self.ID) + self.ENDSTRING, 'w')
        f.write("0, 0\n")
        f.close()
        while True:
            currentLine = self.OUTFILE.readline()
            if not currentLine: break
            currentList = currentLine.split(',')
            if(currentList[3] == currentID):
                f = open(self.STARTSTRING + str(self.ID) + self.ENDSTRING, 'a')
                x = float(currentList[5]) - startX
                y = float(currentList[6].rstrip()) - startY
                f.write(str(x) + "," + str(y) + "\n")
                f.close()
            else:
                currentID = currentList[3]
                self.ID += 1
                startX = float(currentList[5])
                startY = float(currentList[6].rstrip())
                g = open(self.STARTSTRING + str(self.ID) + self.ENDSTRING, 'w')
                g.write("0, 0\n")
                g.close()

        print("Done.")

if __name__ == "__main__":
    col = RemoveColumns()
    col.main()
