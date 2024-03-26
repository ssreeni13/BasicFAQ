# can you find which movie collects more profit without using any in-built functions?
movie_names = ["spiderman", "batman", "superman"]
production_cost = [100, 200, 300]
total_collection = [100, 250, 250]

profit_index = 0
max_profit = total_collection[0] - production_cost[0]
for i in range(1, len(movie_names)):
        profit = total_collection[i] - production_cost[i]
        if max_profit < profit:
            profit = max_profit
            profit_index = i

movie_profit = movie_names[profit_index]
print("Movie with the highest profit:", movie_profit)

#
# movie_names = ["spiderman", "batman", "superman"]
# production_cost = [100, 200, 300]
# total_collection = [100, 250, 250]
#
# # Initialize variables to keep track of the movie with the highest profit
# max_profit_movie_index = 0
# max_profit = total_collection[0] - production_cost[0]
#
# # Loop through the lists to find the movie with the highest profit
# for i in range(1, len(movie_names)):
#     profit = total_collection[i] - production_cost[i]
#     if profit > max_profit:
#         max_profit = profit
#         max_profit_movie_index = i
#
# # Get the name of the movie with the highest profit
# max_profit_movie = movie_names[max_profit_movie_index]
#
# print("Movie with the highest profit:", max_profit_movie)
#
#
