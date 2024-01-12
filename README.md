# Object-Oriented programming (OOP) Project

![Object-Oriented Programming!](https://images.pexels.com/photos/577585/pexels-photo-577585.jpeg)

## The goal of this project is to assess my understanding of object-oriented programming (OOP) concepts in Python. I am tasked with implementing two classes, Expense and ExpenseDatabase to model and manage financial expenses. This project tested my proficiency in defining classes, utilizing class attributes and methods as well as handling time-related functionalities.


## Table of Contents

- [Getting Started](#Getting-Started)
  - [Tools Used](#Tools-Used)
  - [Clone Repo](#Clone-Repo)
  - [Usage](#Usage)
- [Project Structure](#Project-Structure)
- [Contributing](#Contributing)



## Getting Started

The Expense Tracker is a Python program that manages individual financial expenses. It consists of two classes: `Expense` and `ExpenseDataBase`.

- `Expense` represents an individual financial expense with attributes such as ID, title, amount, creation time, and update time. It provides methods that allows for updating expense attributes. It also provides a `to_dict` method that returns a dictionary representation of the expense.
- `ExpenseDataBase` manages a collection of `Expense` objects. It provides methods to add expense, remove expense, and retrieve expenses such as getting expense by ID and Titles. It provides a `to_dict` method that returns a list of dictionaries representing expenses.
  


## Classes

### Expense

#### Attributes
`id`: Unique identifier generated as a UUID string.

`title`: String representing the title of the expense.

`amount`: Float representing the amount of the expense.

`created_at`: Timestamp indicating when the expense was created (UTC).

`updated_at`: Timestamp indicating the last time the expense was updated (UTC).



#### Methods
`update_expense(title, amount)`: Updates the expense details.

`to_dict()`: Returns a dictionary representation of the expense.



### ExpenseDataBase

#### Attributes
`expenses`: List storing Expense instances.



#### Methods
`add_expense(expense)`: Adds an expense to the collection.

`remove_expense(expense_id)`: Removes an expense from the collection.

`get_expense_by_id(expense_id)`: Retrieves an expense by ID.

`get_expense_by_title(expense_title)`: Retrieves expenses by title.

`to_dict()`: Returns a list of dictionaries representing expenses.



## Tools Used

- [Python](https://www.python.org/) (version 3)
- [Git](https://git-scm.com/)



## Clone Repo

Copy link below and paste on yout Git to clone the repository.

   ```bash
   git clone https://github.com/victorcezeh/Object_Oriented_Programming_Project.git
   cd Object_Oriented_Programming_Project
   ```


## Usage

Run the Expense Tracker with the code below.

```bash
python main.py
```


## Project Structure

`Object_Oriented_Programming.py`: This code containes the Expense and ExpenseDataBase Class Implementations.

`README.md`: Project documentation.

`main.py`: The main script to test run the Expense Tracker.



## Contributing

If you'd like to contribute to the project, kindly contact ezeh_victor@yahoo.com
