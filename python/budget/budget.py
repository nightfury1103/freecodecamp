from builtins import range


class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description,
        })
        self.balance += amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.balance -= amount
        self.ledger.append({
            'amount': -amount,
            'description': description,
        })

        return True

    def transfer(self, amount, other_cat):
        if not self.withdraw(amount, f"Transfer to {other_cat.name}"):
            return False

        other_cat.deposit(amount, f"Transfer from {self.name}")
        return True

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return self.balance >= amount

    def spent(self):
        b = 0
        for t in self.ledger:
            amount = t["amount"]
            if amount < 0:
                b += amount

        return -b

    def __str__(self):
        ss = [self.name.center(30, "*")]
        ss.extend(
            "{:<23}{:>7.2f}".format(t["description"][:23], t["amount"])
            for t in self.ledger
        )

        ss.append(f"Total: {self.balance}")
        return "\n".join(ss)


def create_spend_chart(categories):
    spending = [c.spent() for c in categories]
    total = sum(spending)
    percentages = [s * 100 / total for s in spending]
    ss = ["Percentage spent by category"]
    for i in range(11):
        level = 10 * (10 - i)
        s = '{:>3}| '.format(level)
        for p in percentages:
            s += "o  " if p >= level else "   "
        ss.append(s)
    padding = " " * 4
    ss.append(padding + "-" * 3 * len(spending) + "-")

    names = [c.name for c in categories]
    n = max(map(len, names))
    for i in range(n):
        s = padding
        for name in names:
            s += " "
            s += name[i] if len(name) > i else " "
            s += " "

        # damn the additional white space, I hate that
        ss.append(f"{s} ")

    return "\n".join(ss)
