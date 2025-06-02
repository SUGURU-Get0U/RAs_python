# CODE ETIQUETE

''' 
            Naming variables
-> Never use a single letter to name a variable
ex: int y;

-> Never abbreviate when naming a variable

            HUNGARIAN NOTATION
-> Its when, in the older versions of windows, you'd put the type of the variable on its name
ex: boolean bIsValid;

- NO LONGER NECESSARY

            TESTING FUNCTIONS
Let's say you have a module called conect, and you want to test it before appyling to your code
ex: def connect() -> None:
        print('connecting to the internet')
        time.sleep(3)

to make sure the code will run the right script
if __name__ == '__main__'
''' 
number: int = 10

if __name__ == "__main__":
    print(number)