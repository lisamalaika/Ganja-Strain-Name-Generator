import random
    
with open('C:\\Users\\Lisa\\Desktop\\strain_name_generator\\cannabis_strains\\weedstrains.txt', 'r', encoding='utf8') as file:
    lines = [line.strip().split() for line in file]
#    print(lines)

flat_list = []
for sublist in lines:
    for item in sublist:
        flat_list.append(item)

def main():
    while True:
        print("Ganja Name Generator")
        print("Your super random Ganja Strain is: " , random.choice(flat_list))
        x = input("Press enter for a new name or n if you have enough strain names \n")
        if x == "n":
             break
    
    input("\nPress enter to exit.")

if __name__ == "__main__":
    main()


