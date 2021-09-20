# CS5001
# Fall 2021
# HW01
# Yingshu Wang 

# Function: make tables 
def make_tables(tops, legs, screws):
    # one table requires 1 table top, 4 legs, 8 screws
    # Determine how many tables can be made
    num_tables = min(tops, legs//4, screws//8)

    # Determine leftovers 
    tops_left = tops - num_tables
    legs_left = legs - num_tables*4
    screws_left = screws - num_tables*8

    # Output 
    if num_tables > 0:
        message = "{0} tables assembled.\n" + "Leftover parts: {1} tops, {2} legs and {3} screws." 
        message = message.format(num_tables, tops_left, legs_left, screws_left)
    else: 
        message = "You have {0}/1 tops, {1}/4 legs and {2}/8 screws."
        message = message.format(tops_left, legs_left, screws_left)

    return message 

# End make tabels 

def get_input():

    tops = int(float(input("Number of tops: ")))
    legs = int(float(input("Number of legs: ")))
    screws = int(float(input("Number of screws: ")))

    return (tops, legs, screws)

# End get_input 

tops, legs, screws = get_input()
print()
print(make_tables(tops, legs, screws))

# Test Case 1:
# In: Number of tops: 4
# Number of legs: 20
# Number of screws: 32

# 4 tables assembled.
# Leftover parts: 0 tops, 4 legs and 0 screws.

# Test Case 2:
# In: Number of tops: 40
# Number of legs: 10
# Number of screws: 300

# 2 tables assembled.
# Leftover parts: 38 tops, 2 legs and 284 screws.

# Test Case 3:
# In: Number of tops: 30
# Number of legs: 30
# Number of screws: 40

# 5 tables assembled.
# Leftover parts: 25 tops, 10 legs and 0 screws.

