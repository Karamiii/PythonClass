"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane karam.chafqane@tuni.fi (TAMK ristiinopiskelu)
Opiskelijanumero (TAMK): 2207055
Opiskelijanumero (Yliopisto): 151552274

Programs main purpose is to calculate altitude variation. Program calculates mean, median, deviation, minimum, maximum and variation,
which it uses to calculate the previously mentioned deviation. Porgram recieves the values from user input.

"""
# Import sqrt from math library
from math import sqrt

def save_input():
    """
    Function fills a list with user input. When user is done filling the list, function will send 
    the filled list to "calculate_Results()" function for calculations.
    """

    seaWaterLevels = []
    # While loop, which breaks if user gives an empty argument.
    while True:
        answer = input()
        if answer != '':
            seaWaterLevels.append(float(answer))
        else:
            break

    # Check whether or not user has provided at least 2 values
    if len(seaWaterLevels) < 2:
        Error_Message()
    else:
        caculate_Results(seaWaterLevels)

def Error_Message():
    """
    Function presents an error message to user.
    """
    print("Error: At least two measurements must be entered!")
    

def caculate_Results(seaWaterlevels):
    """
    Function reseaves user filled list as an parameter, which it uses to calculate values in seperate functions.
    At the end, function sends all the calculated values to be presented in a seperate function.

    """
    # Calculate mean of the values provided
    mean = calculate_mean(seaWaterlevels)
   
    # Calculate median of the numbers provided
    median = calculate_median(seaWaterlevels)

    # Calculate max and min values from the provided values
    maxValue = float(max(seaWaterlevels))
    minValue = float(min(seaWaterlevels))

     # Calculate the standard deviation of the provided values
    standardDeviation = calculate_standard_deviation(seaWaterlevels, mean)

    # Send calculated values to be presented
    present_results(minValue, maxValue, median, mean, standardDeviation)

def calculate_standard_deviation(seaWaterlevels, mean):
    """
    Function reseves a user filled list and previously calculated mean, which it uses to calculate the variation of the provided values.
    After it has calculated the varition, it uses the result to calculate standard deviation, which it returns back to where it was
    called from.
    """

    # Calculate variation of the provided values
    variation = 0
    for index in seaWaterlevels:
        variation += pow(index - mean, 2)
    variation = variation * (1 / (len(seaWaterlevels) - 1))

    # Calculate the standard deviation by using variation
    standardDeviation = sqrt(variation)
    return standardDeviation


def calculate_mean(seaWaterlevels):
    """
    Function reseves user filled list and calculates the mean of the provided values.
    Function returns calculated mean value back to where it was called from.
    """
    mean = 0
    for index in seaWaterlevels:
        mean += index
    mean = mean / len(seaWaterlevels)
    return mean

def calculate_median(seaWaterlevels):
    """
    Function reseves user filled list and calculates the median of the provided values.
    Function returns calculated median value back to where it was called from.
    """
    median = 0
    SortedLevels = sorted(seaWaterlevels)
    if len(seaWaterlevels) % 2 == 0:
        index = len(SortedLevels) // 2
        value1 = float(SortedLevels[index])
        value2 = float(SortedLevels[index - 1])
        median = (value1 + value2) / 2
    else:
        index = (len(SortedLevels) // 2)
        median = SortedLevels[index]
    return median    



def present_results(minValue, maxValue, median, mean, deviation):
    """
    Function recieves all the calculated values as parameters and presents them to the user.
    This is where the program finishes.
    """
    print(f"Minimum:   {minValue:.2f} cm")
    print(f"Maximum:   {maxValue:.2f} cm")
    print(f"Median:    {median:.2f} cm")
    print(f"Mean:      {mean:.2f} cm")
    print(f"Deviation: {deviation:.2f} cm")



def main():
    
    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")
    save_input()

   
        

if __name__=="__main__":
    main()
