import pytest


class Checkout:
    class Discount:
        def __init__(self, number_of_items, price):
            self.number_of_items = number_of_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_item(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def add_item_price(self, item, price):
        self.prices[item] = price

    def calculate_total(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculate_item_total(item, cnt)
        return total

    def calculate_item_total(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.number_of_items:
                total += self.calculate_item_discounted_total(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt

        return total

    def calculate_item_discounted_total(self, item, cnt, discount):
        total = 0
        number_of_items = cnt / discount.number_of_items
        total += number_of_items * discount.price
        remaining = cnt % discount.number_of_items
        total += remaining * self.prices[item]

        return total

    def add_discount(self, item, number_of_items, price):
        discount = self.Discount(number_of_items, price)
        self.discounts[item] = discount


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_price("a", 1)
    checkout.add_item_price("b", 2)
    return checkout


def test_can_calculate_total(checkout):
    checkout.add_item("a")

    assert checkout.calculate_total() == 1


def test_get_correct_total_with_multiple_items(checkout):
    checkout.add_item("a")
    checkout.add_item("b")

    assert checkout.calculate_total() == 3


def test_can_add_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)


def test_can_apply_discount_rule(checkout):
    checkout.add_discount("a", 3, 2)
    checkout.add_item("a")
    checkout.add_item("a")
    checkout.add_item("a")

    assert checkout.calculate_total() == 2


def test_exception_with_bad_item(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
