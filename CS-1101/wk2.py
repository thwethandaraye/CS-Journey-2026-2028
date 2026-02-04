# Exercise 2.2

# 1. The volume of a sphere with radius r is 4/3πr3. What is the volume of a sphere with radius 5?

r = 5
V = (4 / 3) * 3.14159 * (r ** 3)
print(V)

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
#    Shipping costs $3 for the first copy and 75 cents for each additional copy. 
#    What is the total wholesale cost for 60 copies?

cover_price = 24.95
discount = 0.40
num_copies = 60
shipping_cost_1st = 3.00
shipping_cost_remaining = 0.75
print(((num_copies * cover_price) * (1 - discount)) + shipping_cost_1st + ((num_copies - 1) * shipping_cost_remaining))

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
# tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

start_time = (6 * 60) + 52       # 412 in minutes
easy_pace = (8 * 60) + 15        # 495 in seconds
tempo = (7 * 60) + 12            # 435 in seconds
time_taken = (1 * easy_pace) + (3 * tempo) + (1 * easy_pace)   # 2295 in seconds
end_time = start_time + (time_taken / 60)    # 450.25 in minutes
get_home_hour = end_time // 60
get_home_minute = end_time % 60
print(f"{int(get_home_hour)}:{get_home_minute:02.0f} am")