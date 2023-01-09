"""
COMP.CS.100 Ohjelmointi 1.
Tekijä: Karam Chafqane (TAMK ristiinopiskelu)

"""

def main():
  
  counter = 0
  
   
  for month in range(1,13):
    
    for day in range(1,32):
        counter += 1
        if (month == 4 or month == 6 or month == 9 or month == 11) and day == 30:
            break 
        if month == 1 and day == 3:
            print(f"{day}.{month}.")
            counter = 0
        if counter == 7:
            print(f"{day}.{month}.")    
            if month == 2 and day == 28:
                counter = 0
                break
            if (month == 4 or month == 6 or month == 9 or month == 11) and day == 30:
                break
            else:
                counter = 0
            
                    
if __name__=="__main__":
    main()