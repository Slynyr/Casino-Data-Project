import random
import statistics
from tqdm import tqdm
from colorama import Fore

#use pip install -r requirements.txt to install dependencies

def getSimulatedTrials(numberList, numberWeights, cardList, cardWeights, trials):
    print(Fore.RED)
    results = []
    for i in tqdm(range(0, trials)):
        point = random.choices(numberList, weights=numberWeights)[0]
        card = random.choices(cardList, weights=cardWeights)[0]

        result = point*card
        results.append(result)
    return results

def displayDataMean(data):
    print("Calculating mean of total points. This may take some time depending on the number of trials")
    mean = statistics.mean(data)
    print(mean)

trials = 100000000

#Spinner
numberList = [1, 2, 3, 10, 0]
numberWeights = [3/12, 3/12, 3/12, 1/12, 2/12]

#Cards
cardList = [1, 2, 3]
cardWeights = [6/10, 3/10, 1/10]

if __name__ == "__main__":
    data = getSimulatedTrials(numberList, numberWeights, cardList, cardWeights, trials)
    displayDataMean(data)

