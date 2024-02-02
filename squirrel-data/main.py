import pandas

data = pandas.read_csv("data.csv")

attribute = "Primary Fur Color"
colors = ["Gray", "Cinnamon", "Black"]

squirrel_count_dict = {}

count_list = []

for color in colors:
    count = data[data[attribute] == color][attribute].count()
    count_list.append(count)


squirrel_count_dict["Fur Color"] = ["gray", "red", "black"]
squirrel_count_dict["Count"] = count_list

print(squirrel_count_dict)

data_csv = pandas.DataFrame(squirrel_count_dict)

print(data_csv)

data_csv.to_csv("squirrel_count.csv")

