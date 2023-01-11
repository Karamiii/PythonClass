"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""


def calculate_dose(weight, timeSinceLast, totalDoce):
  """
  Funktion tarkoitus on laskea paracetamolin sallittu määrä, jonka voi antaa.
  Funktio ottaa 3 parametriä, joilla lasketaan sallittu määrä ja määrä sitten
  palautetaan takaisin pääohjelmaan.
  """


  totalAmountTaken = totalDoce
  totalByWeight = weight * 15
  if (timeSinceLast <= 24 and totalDoce >= 4000) or timeSinceLast < 6:
    return 0
  else:
    totalAmountTaken = totalAmountTaken + totalByWeight
    if timeSinceLast >= 6 and totalAmountTaken <= 4000:
      return totalByWeight
    else:
      answer = 4000 - totalDoce
      if answer <= 0:
        return 0
      elif answer > totalByWeight:
        return totalByWeight     
      else:
        return answer


def main():

    weight = int(input("Patient's weight (kg): "))
    timeSinceLast = int(input("How much time has passed from the previous dose (full hours): "))
    totalDoce = int(input("The total dose for the last 24 hours (mg): "))
    

    answer = calculate_dose(weight, timeSinceLast, totalDoce)

    print("The amount of Parasetamol to give to the patient:", answer)

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
