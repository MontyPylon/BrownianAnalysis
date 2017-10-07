class R2:

    INFILES = []
    ALL_X = []
    ALL_Y = []
    R = []
    Ri = []
    R2 = []
    PARTICLES = 157
    FILE_LENGTH = 500
    PIXEL_CONVERSION = 1.0079*(10**(-7))
    FPS = 30

    def setupFiles(self):
        start = 'data/particles/particle'
        end = '.csv'
        for a in range(1,self.PARTICLES+1):
            filename = start + str(a) + end
            f = open(filename, 'r')
            self.INFILES.append(f)

    def getLineNum(self, file):
        return sum(1 for line in file)

    def findMinSet(self):
        min = 10000000000
        for i in range(len(self.INFILES)):
            num_lines = sum(1 for line in self.INFILES[i])
            #print(str(num_lines))
            if num_lines < min:
                min = num_lines
        return min

    def main(self):
        self.setupFiles()
        print("Starting to create R^2 data...")

        # Find the minimum data set length
        #min = self.findMinSet()
        #print("Minimum data set is " + str(min) + " long.")

        #for b in range(len(self.INFILES)):
        #    self.INFILES[b].seek(0)
        """        
        for i in range(len(self.INFILES)):
            for j in range(0, min):
                dataRaw = self.INFILES[i].readline()
                if not dataRaw: break
                data = dataRaw.split(',')
                x = float(data[0])
                y = float(data[1].rstrip())
                self.Ri.append(x*x + y*y)
            self.R.append(self.Ri)
            self.Ri = []
        """

        for i in range(len(self.INFILES)):
            fileLength = self.getLineNum(self.INFILES[i])
            if(fileLength < self.FILE_LENGTH):
                self.PARTICLES -= 1
                continue
            self.INFILES[i].seek(0)
            for j in range(self.FILE_LENGTH):
                dataRaw = self.INFILES[i].readline()
                if not dataRaw: break
                data = dataRaw.split(',')
                x = float(data[0]) * self.PIXEL_CONVERSION
                y = float(data[1].rstrip()) * self.PIXEL_CONVERSION
                self.Ri.append(x * x + y * y)
            self.R.append(self.Ri)
            self.Ri = []
        
        # Check to see if we have bad data
        ran = len(self.R)
        i = 0
        while(i < ran):
            total = 0
            counter = 0
            for j in range(len(self.R[i])):
                total += self.R[i][j]
                counter += 1
            total = total / counter
            if(total < 10*self.PIXEL_CONVERSION*self.PIXEL_CONVERSION):
                print("----------------------")
                print("Total: " + str(total))
                print("Filename = particle" + str(i+1) + ".csv")
                print("----------------------")
                self.R.pop(i)
                i -= 1
                ran -= 1
                self.PARTICLES -= 1
            i += 1

        n = len(self.R)
        for a in range(len(self.R[0])):
            final = 0
            for b in range(n):
                final += self.R[b][a]
            final = final / n
            self.R2.append(final)

        counter = 0
        f = open("data/results/result.csv", 'w')
        for a in range(len(self.R2)):
            put = str(counter/self.FPS) + "," + str(self.R2[a]) + "\n"
            f.write(put)
            counter += 1
        f.close()
        print("Finished writing data. Total good particles: " + str(self.PARTICLES))

if __name__ == "__main__":
    caller = R2()
    caller.main()