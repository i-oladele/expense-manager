
import uuid
from datetime import datetime

class Expense:

    def __init__(self, title, amount ):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title:
            self.title = title
        if amount:
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

class ExpenseDB:

    def __init__(self, expenses=None):
        self.expenses = expenses if expenses else []

    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def remove_expense(self, expense):
        self.expenses.remove(expense)

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  
    
    def get_expense_by_title(self, title):
        for expense in self.expenses:
            if expense.title == title:
                return expense
        return None
    
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
    


if __name__ == "__main__":
    my_expenses = ExpenseDB()

    expense1 = Expense("Groceries", 50.75)
    my_expenses.add_expense(expense1)

    expense2 = Expense("Utilities", 120.00)
    my_expenses.add_expense(expense2)

    print("All expenses:", my_expenses.to_dict())

    expense1.update(amount=60.00)
    print("Updated expense:", expense1.to_dict())

    my_expenses.remove_expense(expense1)
    print("After removal:", my_expenses.to_dict())
