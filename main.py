from datetime import datetime

# Expense and ExpenseDatabase

# Expense Class -> Represents an individual financial expense

from uuid import uuid4
from datetime import datetime

class Expense:
    def __init__(self, title, amount) -> None:
        # Initialize expense attributes
        self.id = str(uuid4())
        self.title = str(title)
        self.amount = float(amount)
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update_expense(self, title, amount):
        # This method updates expense details
        self.title = title
        self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        # This method returns a dictionary representation of the expense
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
    

# ExpenseDataBase Class -> Manages a collection of Expense objects.
    

class ExpenseDataBase:
    def __init__(self):
        # Initialize an empty list to store expenses
        self.expenses = []
    
    def add_expense(self, expense):
        # This method adds an expense
        self.expenses.append(expense)
        print(f"Expense with ID {expense.id} added successfully")
        return expense

    def remove_expense(self, expense_id):
        # This method removes an expense
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
        print(f"Expense with ID {expense_id} has been removed")


    def get_expense_by_id(self, expense_id):
        # This method retrieves an expense by ID
        expense = [expense for expense in self.expenses if expense.id == expense_id]
        if len(expense) == 0:
            return None
        return expense[0]
    
    def get_expense_by_title(self, expense_title):
        # This method retrieves expenses by title
        similar_expenses = [expense for expense in self.expenses if expense.title == expense_title]
        return similar_expenses.copy() # This will return a copy to avoid modifying the state
    
    def to_dict(self):
        # This method returns a list of dictionaries representing expenses
        return [expense.to_dict() for expense in self.expenses]

def main():
    # Create an instance of ExpenseDataBase
    expense_db = ExpenseDataBase()

    # Create some expenses
    expense1 = Expense("Beans", 100.00)
    expense2 = Expense("Bread", 50.00)

    # Add expenses to the database
    expense_db.add_expense(expense1)
    expense_db.add_expense(expense2)

    # Display the current expenses
    print("Current Expenses:")
    for expense in expense_db.to_dict():
        print(expense)

    # Remove an expense by ID
    expense_db.remove_expense(expense1.id)

    # Display the updated expenses
    print("\nUpdated Expenses:")
    for expense in expense_db.to_dict():
        print(expense)

if __name__ == "__main__":
    main()
