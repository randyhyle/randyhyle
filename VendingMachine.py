# File: VendingMachine.py
#
# Description: CS303e programming assignment 13.
# Create a class that models a vending machine.
#
# Assignment Number: 13
#
# Name: Randy Hy Le
# EID:  hhl385
# Email: le.hy.randy@gmail.com
# Grader: Emma
#
# On my honor, Randy Hy Le, this programming assignment is my own work
# and I have not provided this code to any other student.

import random


class VendingMachine:
    """Models a Vending Machine.

    All transactions are in cents.
    """

    def __init__(self, initial_drinks=0, cost=0, capacity=0):
        """Setting the parameters of the machine. The amount of drinks
        the machine initially contains, the cost of each drink, and
        the max capacity of the vending machine.
        """
        self.__initial_drinks = initial_drinks
        self.__cost = cost
        self.__capacity = capacity
        self.__transaction_amount = 0

    def insert_money(self, amount_inserted):
        """For amount of money inserted, add to the current
        transaction amount.
        """
        self.__transaction_amount += amount_inserted

    def can_dispense(self):
        """Check if the vending machine can dispense a drink by
        checking if the current amount of drinks contained in the
        machine is greater than 0 and if the current amount inserted
        is greater than or equal to the cost for each drink.
        """
        if self.__initial_drinks > 0 and self.__transaction_amount >= \
                self.__cost:
            return True
        else:
            return False

    def dispense(self):
        """If the vending machine is empty return that it is empty,
        otherwise check if the current amount inserted is less than the
        cost of the drink. If the current amount inserted is greater
        than the cost, output a drink and subtract one from the initial
        amount of drinks while also updating the transaction amount.
        """
        if self.__initial_drinks == 0:
            return 'EMPTY'
        elif self.__transaction_amount < self.__cost:
            return 'INSUFFICIENT FUNDS'
        else:
            self.__initial_drinks -= 1
            self.__transaction_amount -= self.__cost
            return 'ENJOY'

    def get_change(self):
        """If the amount that is inserted is more than the cost of a
        drink, give the amount leftover back and set the amount
        inserted back to zero.
        """
        change = self.__transaction_amount
        self.__transaction_amount = 0
        return change

    def refill(self):
        """When it is deemed necessary, refill the vending machine
        back to its max capacity.
        """
        self.__initial_drinks = self.__capacity


def main():
    """# Run a simulation using the Vending Machine objects."""
    if input('Run simple tests? ') == 'y':
        simple_tests()
    stress_tests()


def simple_tests():
    """Simple operations with a single Vending Machine.

     The VendingMachine has a capacity of 5 drinks, currently
     has 2 drinks, and it costs 50 cents per drink.
     """
    print('***** SIMPLE TESTS *****')
    vend1 = VendingMachine(2, 50, 5)
    vend1.insert_money(25)
    vend1.insert_money(10)
    vend1.insert_money(10)
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    vend1.insert_money(10)
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    print('can dispense:', vend1.can_dispense())
    print('get change:', vend1.get_change())
    print('get change:', vend1.get_change())
    vend1.insert_money(100)
    vend1.insert_money(25)
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    vend1.refill()
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    print('can dispense:', vend1.can_dispense())
    print('dispense:', vend1.dispense())
    print('get change:', vend1.get_change())
    print()


def stress_tests():
    """Run stress tests.

    Given the same number of machines, the same number of operations,
    and the same initial seed, output will be the same.
    """
    # Get the seed, number of operations,
    # and number of machines from the user.
    random.seed(int(input('Enter random seed: ')))
    num_operations = int(input('Enter the number of operations: '))
    num_machines = int(input('Enter the number of machines: '))
    print('\n***** STRESS TESTS *****')

    # Create the required number of machines and run the tests.
    machines = create_machines(num_machines, 10)
    perform_stress_tests_ops(machines, num_operations)


def perform_stress_tests_ops(machines, num_operations):
    """# Run the actual operations for the stress tests."""
    # Only allow US coins, excluding pennies!
    # (We should get rid of pennies and probably nickels too!)
    coins = [5, 10, 25, 50, 100]
    last_coin_index = len(coins) - 1
    last_machine_index = len(machines) - 1

    # Pick a random operation.
    # 55% chance of insert_money.
    # 20% chance of can dispense.
    # 21% chance of dispense. (If we dispense, there is a 80%
    #       chance dispense is called directly after.)
    #  3% chance of get_change.
    #  1% chance of refill.
    for i in range(1, num_operations + 1):
        print('Operation =', i)
        machine_number = random.randint(0, last_machine_index)
        print('Machine =', machine_number)
        machine = machines[machine_number]

        random_op = random.randint(1, 100)
        if random_op <= 55:
            coin = coins[random.randint(0, last_coin_index)]
            print('Insert money, amount =', coin)
            machine.insert_money(coin)
        elif random_op <= 75:
            print('Can dispense:', machine.can_dispense())
        elif random_op <= 96:
            result = machine.dispense()
            print('Dispense:', result)
            if result == 'ENJOY':
                # Do they remember their change? 80% chance of yes.
                if random.randint(1, 5) <= 4:
                    print('Get change, amount =', machine.get_change())
                else:
                    print('Forgot change after dispense.')
        elif random_op <= 99:
            print('Get change, amount =', machine.get_change())
        else:
            print('Refill.')
            machine.refill()
        print()


def create_machines(num_machines, max_capacity):
    """Create a list with the required number of machines.

    I expect num_machines > 0.
    The first machine always has a price of 25, 1 drink,
    and a capacity of 3.
    All machines will have a price between
    25 and 200 in multiples of 25.
    All machines will have a capacity between 2 and max_capacity.
    """
    price_multiplier = 25
    machines = [VendingMachine(1, price_multiplier, 3)]
    print('Machine 0: price = 25, capacity = 3, initial drinks = 1')
    for i in range(1, num_machines):
        price = random.randint(1, 8) * price_multiplier
        capacity = random.randint(2, max_capacity)
        drinks = random.randint(0, capacity)
        print('Machine ', i, ': price = ', price, ', capacity = ', capacity,
              ', initial drinks = ', drinks, sep='')
        machines.append(VendingMachine(drinks, price, capacity))
    print()
    return machines


main()
