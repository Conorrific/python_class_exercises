students = {
    "best": "Mittens",
    "worst": "Jason",
}

students = dict(best = "Mittens", Worst = "Jason")
students['best']
students['Worst']

students.keys()

students["best"] = "lassie"
students["fastest"] = "Rusty"
students["favorite_foods"][0]
students["favorite foods"] = {
  "best": "pizza", "protein": "chicken"
}
students["favorite_foods"]["best"]
students.get("favorite_foods", "bread")
students.get("Pet", "fluffy")