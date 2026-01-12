import discord
import random

# This example requires the 'message_content' intent.
#ew
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('d'):
        sim()
        last = need[-1]
        if len(need) == 1:
            await message.channel.send("Plot " + need + "needs to be watered.")

        else:
            await message.channel.send("Plots " + ', '.join(need[:-1]) + " and " + ''.join(last) + " need to be watered.")

def threshold(x):
    for k, v in x.items():
        if round(v, -1) == 30 or round(v, -1) < 30:
            need.append(k)
    return need

def final(x):
    for k, v in x.items():
        if round(v, -1) == 30 or round(v, -1) < 30:
            
            need.append(k)
            #print(k + str(round(v, -1)) + "[!]")
        else:
            #print( k + str(round(v, -1)))
            pass
    
    

def sim():
    global need
    need = []
    class Plant:
        def __init__(self, num):
            self.temperature = 0
            self.moisture = 0
            self.num = num

        def mock(self):
            self.temperature = random.randint(0, 100)
            self.moisture = random.randint(0, 100)
    
    # Create instances of the class
    plant1 = Plant(1)
    plant2 = Plant(2)
    plant3 = Plant(3)
    plant4 = Plant(4)
    plant5 = Plant(5)
    plant6 = Plant(6)
    plant7 = Plant(7)
    plant8 = Plant(8)
    plant9 = Plant(9)
    plant10 = Plant(10)

    plant1.mock()
    plant2.mock()
    plant3.mock()
    plant4.mock()
    plant5.mock()
    plant6.mock()
    plant7.mock()
    plant8.mock()
    plant9.mock()
    plant10.mock()


    #plots are paired to form a plot
    batch1 = {"1": plant1.moisture, "2": plant2.moisture}
    batch2 = {"3": plant3.moisture, "4": plant4.moisture}
    batch3 = {"5": plant5.moisture, "6": plant6.moisture}
    batch4 = {"7": plant7.moisture, "8": plant8.moisture}
    batch5 = {"9": plant9.moisture, "10": plant10.moisture}


    #plots = [plot1.temperature, plot2.temperature, plot3.temperature, plot4.temperature]


    threshold(batch1)
    threshold(batch2)
    threshold(batch3)
    threshold(batch4)
    final(batch5)


client.run('MTIzMDEzNjg5NTk4ODgzMDI4OQ.GQ_vKM.Lyq4KhyRhed86RUcaKCvcx46i5rHghXZxHsGrE')
