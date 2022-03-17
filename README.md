# Fork & Clone

Fork and clone [this repository](https://github.com/JoinCODED/age-calculator) in your `python` directory.

---

# Task 

In this task you'll be creating an age calculator where the user will input their birth date and the program will give them back their age.

In this task, you'll create a python script that calculates the user's age. The user enters their birth year, month, and day, and the script prints their age.

Assuming today's date is September 4th, 2019:

```
Enter year of birth: 2000
Enter month of birth: 6
Enter day of birth: 6
You are 18 years old.
```

## Steps:
1. Create a function and name it "`check_birthdate`":
    - Takes the `year`, `month`, and `day` as parameters.
    - Returns `False` if the given birthdate is in the future and `True` if it was in the past.
2. Create another function and name it "`calculate_age`":
    - Takes the `year`, `month`, and `day` as parameters.
    - Calculates the age of the user.
    - Prints a message to the user with their age in years.
    - This function does not return anything.
3. Ask the user for their birthdate (year, month, and day)
4. Using the `check_birthdate` function:
    - If `True` was returned, call the `calculate_age` function.
    - If `False` was returned, print a message to the user that the birthdate is invalid.
5. Push your code.

Note: You will need the [`datetime` library](https://www.programiz.com/python-programming/datetime)
