from collections import Counter

def most_populous_year(people):
    year_counter = Counter()
    first_year = 2000
    last_year = 1900
    for person in people:
        if person["birth"] < first_year: first_year = person["birth"]
        if person["death"] > last_year: last_year = person["death"]
        year_counter[person["birth"]] += 1
        year_counter[person["death"] + 1] -= 1

    print(year_counter)

    people_alive = 0
    most_people_alive = 0
    pop_year = first_year
    for year in range(first_year, last_year + 1):
        if year_counter.get(year):
            people_alive += year_counter[year]
            if people_alive > most_people_alive:
                most_people_alive = people_alive
                pop_year = year

    return pop_year

def test_case(people, solution, test_func):

    output = test_func(people)
    if output == solution:
        print("Passed")
    else:
        print(f"Failed, expected {solution}, got {output}")


people = [{"birth": 1908, "death": 1909},
          {"birth": 1900, "death": 1917},
          {"birth": 1910, "death": 1976},
          {"birth": 1919, "death": 1954},
          {"birth": 1924, "death": 1986},
          {"birth": 1924, "death": 1944},
          {"birth": 1925, "death": 2001},
          {"birth": 1931, "death": 1979},
          {"birth": 1933, "death": 2020},
          {"birth": 1937, "death": 1994},
          {"birth": 1937, "death": 1942},
          {"birth": 1948, "death": 2010},
          {"birth": 1950, "death": 2018}]

test_case(people, 1953, most_populous_year)
