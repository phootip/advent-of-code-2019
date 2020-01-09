def make_fuel(amount, recipes):
    supply = defaultdict(int)
    orders = Queue()
    orders.put({"ingredient": "FUEL", "amount": amount})
    ore_needed = 0

    while not orders.empty():
        order = orders.get()
        if order["ingredient"] == "ORE":
            ore_needed += order["amount"]
        elif order["amount"] <= supply[order["ingredient"]]:
            supply[order["ingredient"]] -= order["amount"]
        else:
            amount_needed = order["amount"] - supply[order["ingredient"]]
            recipe = recipes[order["ingredient"]]
            batches = ceil(amount_needed / recipe["servings"])
            for ingredient in recipe["ingredients"]:
                orders.put(
                    {"ingredient": ingredient["ingredient"], "amount": ingredient["amount"] * batches})
            leftover_amount = batches * recipe["servings"] - amount_needed
            supply[order["ingredient"]] = leftover_amount
    return ore_needed


f = open('example5.txt')
