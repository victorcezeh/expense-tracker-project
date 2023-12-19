#Expense and ExpenseDatabase

from uuid import uuid4
from datetime import datetime

class Expense:
    def __init__(self, title, amount) -> None:
        self.id = str(uuid4())
        self.title = str(title)
        self.amount = float(amount)
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update_expense(self, title, amount):
        self.title = title
        self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }