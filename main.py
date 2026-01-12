import random
need = []
global add
add = []

def threshold(x):
    for k, v in x.items():
        if round(v, -1) == 30 or round(v, -1) < 30:
            
            need.append(k)
            #print("k = " + k)
            #print(k + str(v) + "[!]")
            
        else:
            #print( k + str(round(v, -1)))
            pass
    #print(add)
    return need 

def final(x):
    for k, v in x.items():
        if round(v, -1) == 30 or round(v, -1) < 30:
            
            need.append(k)
            #print(k + str(round(v, -1)) + "[!]")
        else:
            #print( k + str(round(v, -1)))
            pass
    
    

    if len(need) == 1:
        print("Plot " + ', '.join(need[:-1]) + " needs to be watered.")

    else:
        last = need[-1]

        print("Plot " + ', '.join(need[:-1]) + " & " + ''.join(last) + " needs to be watered.")
        
# TODO create function that returns plots in an ASCII grid
def gridify(x):
    length = len(need)




def sim():


    class Plot:
        #Plot sensor data
        def __init__(self, num):
            self.temperature = 0
            self.moisture = 0
            self.num = 0
            
            #method to mock plot data
        def mock(self):

            self.temperature = random.randint(0, 100)
            self.moisture = random.randint(0, 100)
            





        #create instances of the class
    plot1 = Plot(1)
    plot2 = Plot(2)
    plot3 = Plot(3)
    plot4 = Plot(4)
    plot5 = Plot(5)
    plot6 = Plot(6)
    plot7 = Plot(7)
    plot8 = Plot(8)
    plot9 = Plot(9)
    plot10 = Plot(10)

        #mock plot data
    plot1.mock()
    plot2.mock()
    plot3.mock()
    plot4.mock()
    plot5.mock()
    plot6.mock()
    plot7.mock()
    plot8.mock()
    plot9.mock()
    plot10.mock()


    #plots are paired to form a plot
    batch1 = {"1": plot1.moisture, "2": plot2.moisture}
    batch2 = {"3": plot3.moisture, "4": plot4.moisture}
    batch3 = {"5": plot5.moisture, "6": plot6.moisture}
    batch4 = {"7": plot7.moisture, "8": plot8.moisture}
    batch5 = {"9": plot9.moisture, "10": plot10.moisture}


    #plots = [plot1.temperature, plot2.temperature, plot3.temperature, plot4.temperature]


    threshold(batch1)
    threshold(batch2)
    threshold(batch3)
    threshold(batch4)
    final(batch5)


sim()

