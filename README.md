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

1. Create a function and name it "`get_dob`" (`dob` is short for date of birth):
    - Takes no parameters.
    - Ask the user for their birth year.
    - Ask the user for their birth month.
    - Ask the user for their birth day.
    - Combines the 3 values retrieved from the user and returns a `date` object.
2. Create another function and name it "`get_age`":
    - Takes `dob` as the only parameter, which is a date object.
    - Calculates the age of the user from today.
    - Returns the user's age in years as an integer.
3. In the main function, get the user's date of birth using `get_dob`.
4. Check if the user's `dob` is in the future.
    - If it is in the future, print a message to the user that their date of birth is invalid
    - If it is not in the future, get the user's age using `get_age`, and then print it to the terminal.
5. Push your code.

Note: You will need the [`datetime` library](https://www.programiz.com/python-programming/datetime)
