#pip install keyboard
import time
import random
#import keyboard

# Initial list of restaurant and their corresponding probabilities
available_restaurants = ['Nago Sushi', 'Nago Pineapple', 'Nagopork', 'Wagyu', 'Kokosai St',
               'Morning Bowls', 'Shushirakyo', 'Nepal House', 'Touch n Go', 'McDonalds', 'Taco Bell']
restaurant_ranking = available_restaurants[:]
# 7 is most likely, 6 and 8 next most likely, 
roll_for_print = [7, 6, 8, 5, 9, 4, 10, 3, 11, 2, 12]


        #          7     6      8     5    9     4     10    3    11     2    12
probabilities = [6/36, 5/36, 5/36, 4/36, 4/36, 3/36, 3/36, 2/36, 2/36, 1/36, 1/36]
# dice roll: index of orderd probability list (7 is most likely, 12 is least likely)
my_dict = {7: 0, 6: 1, 8: 2, 5: 3, 9: 4, 4: 5, 10: 6, 3: 7, 11: 8, 2: 9, 12: 10}

# Ensure they sum up to 1
total_prob = sum(probabilities)
probabilities = [p / total_prob for p in probabilities]


# have users input restuarants instead of hard coded
# def input_rest()
#     for y in range(11): # 11 restaurants
#        new_rest = input("Input your top 10 fav restaurants in order of most likely") # ask user for new 
#        available_restaurants.append(new_rest)


# probabilites won't change
def select_restaurant(restaurant_ranking, probabilities):
        # Select an restaurant based on the current probabilities
    a = 0
    b = 0
    for rest in restaurant_ranking:
        if b == 0:
            print(f" Most likely: {rest} (roll a {roll_for_print[a]})")
            b = b+1
        elif b == 10:
            print(f" Least likely: {rest} (roll a {roll_for_print[a]})")
            b = b+1
        else:
            print(f" {rest} (roll a {roll_for_print[a]}):")
            b = b+1
        a = a+1
    print("Roll your dice!")
    selected_index_str = input("Input your dice roll\n... ") # inputs as a string
    selected_index = int(selected_index_str)
#    selected_restaurant = random.choices(restaurant_ranking, probabilities)[0] # prints string of restaurant
    nthmostlikely = my_dict[selected_index]  # converts rolling 2 into 10th most likely - TBell
    selected_restaurant = restaurant_ranking[nthmostlikely]
#    selected_index = restaurant_ranking.index(selected_restaurant) # gives the index (needed for pop)

        # rolls the restaurants
#    if selected_index < len(restaurant_ranking) - 1: # < (less than) so everything but last place (ie least likely)
    restaurant_ranking.pop(my_dict[selected_index]) # pop removes nth teir (@ specific index)
    restaurant_ranking.append(selected_restaurant)
    
    return restaurant_ranking, selected_restaurant




def printed(restaurant_ranking, selected_restaurant): 
    # probabilities don't change
    # restaurant_ranking, selected_restaurant = select_restaurant(restaurant_ranking, probabilities)
    print(f"CONGRATS SHOGUN NERDS YOU ARE EATING AT\n...\n...\n...")
    time.sleep(2)
    # print 'herding cats', 'waiting for the lights to turn on', 'waiting for the world to end'
    time.sleep(2)
    print(f" {selected_restaurant}\n\n")
    time.sleep(2)

    # Prints in likely hood of being picked. 7, 6, 8, 5, 9... etc
    x = 0
    i = 0
#    for rest in restaurant_ranking:
#        if i == 0:
#            print(f" Roll {roll_for_print[x]}): {rest} (most likely)")
#            i = i+1
#        elif i == 10:
#            print(f" Roll {roll_for_print[x]}): {rest} (least likely)\n---")
#            i = i+1
#        else:
#            print(f" Roll {roll_for_print[x]}): {rest}")
#            i = i+1
#        x = x+1



n = 1
while n < 1000:
    restaurant_ranking, selected_restaurant = select_restaurant(restaurant_ranking, probabilities)
    printed(restaurant_ranking, selected_restaurant)




