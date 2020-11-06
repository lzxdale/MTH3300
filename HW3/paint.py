 #******************************************************************************
# paint.py
#******************************************************************************
# Name: Zexiang Lin
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#My brother: on the challange problem, idea on methods
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# The challenge is a little bit tricky
#
#
red_start = float(input("Enter Robbie Red’s starting point: "))
red_end = float(input("Enter Robbie Red’s ending point: "))
if red_start > red_end: # to eliminate possible errors. it will produce the correct results even the order is wrong.
    a = red_start       # A question: Do I to write this? Or I can just skip thinking about possible error for HW?
    red_start = red_end
    red_end = a
blue_start = float(input("Enter Bert Blue’s starting point: "))
blue_end = float(input("Enter Bert Blue’s ending point: "))
if blue_start > blue_end:
    a = blue_start
    blue_start = blue_end
    blue_end = a
#case 1, they do overlap
if  red_start <= blue_start and red_end >= blue_start: # red is before or equal blue, red may or may not include blue in it.
    end = max(red_end, blue_end)
    total_dis = abs(end - red_start) # incas the user enter negative number
elif blue_start <= red_start and blue_end >= red_start: # blue is before or equal red, blue may or may not include red in it.
    end = max(red_end, blue_end)
    total_dis = abs(end - blue_start)
#case 2, they don't overlap
else:
    dis1 = red_end - red_start
    dis2 = blue_end - blue_start
    total_dis = dis1 + dis2
print("The total distance painted is", total_dis)
print("")
####challenge####
print("Below is the challenge Problem!!!")
green_start = float(input("Enter Greta Green’s starting point: "))
green_end = float(input("Enter Greta Green’s ending point: "))
if green_start > green_end:
    a = green_start
    green_start = green_end
    green_end = a
start = min(red_start, blue_start, green_start)
end = max(red_end, blue_end, green_end)
#using the below method, the distance, we can find whatever they are overlap or not. if they are >=0, they are overlap
#to be overlap, one color's end must be greater then the other color's start. This idea was provided by my brother
#before I was thinking about listing all the possible line combination, which can be very tedious.
re_bs = red_end - blue_start
re_gs = red_end - green_start
be_rs = blue_end - red_start
be_gs = blue_end - green_start
ge_rs = green_end - red_start
ge_bs = green_end - blue_start
the_list = [re_bs, re_gs, be_rs, be_gs, ge_bs, ge_rs]
count = 0
for i in the_list:
    if i >= 0:
        count += 1
#case 1 if count = 5 or 6, they all overlap with one and other r--b--g--b--g--r = 6 or r--b--r--g--b--g = 5
if count >= 5:
    print("all together")
    total_dis = end - start
#case 2 if count = 4, two of the lines overlap, and one is by itself g--g b--r--b--r =4
elif count == 4:
    print("one by itself")
    #the one by itself is in the front r--r b--g--b--g
    if re_bs < 0 and re_gs < 0 and start == red_start: # if red is the line by itself
        red = red_end - red_start
        total_dis = red + (max(green_end, blue_end) - min(green_start, blue_start))
    elif be_rs < 0 and be_gs < 0 and start == blue_start:  # if blue is the line by itself
        blue = blue_end - blue_start
        total_dis = blue + (max(green_end, red_end) - min(green_start, red_start))
    elif ge_bs < 0 and ge_rs < 0 and start == green_start:  # if green is the line by itself
        green = green_end - green_start
        total_dis = green + (max(red_end, blue_end) - min(red_start, blue_start))
    #the one by itself is in the end, as it is impossible to be in the middle while the other overlap
    #b--g--b--g a--a
    elif re_bs > 0 and re_gs > 0: # if red is the line by itself
        red = red_end - red_start
        total_dis = red + (max(green_end, blue_end) - min(green_start, blue_start))
    elif be_rs > 0 and be_gs > 0:  # if blue is the line by itself
        blue = blue_end - blue_start
        total_dis = blue + (max(green_end, red_end) - min(green_start, red_start))
    elif ge_bs > 0 and ge_rs > 0:  # if green is the line by itself
        green = green_end - green_start
        total_dis = green + (max(red_end, blue_end) - min(red_start, blue_start))
#case 3 if count = 3, all of them are separate, g--g r--r b--b = 3 all separate
elif count == 3:
    print("all by itself")
    red = red_end - red_start
    blue = blue_end - blue_start
    green = green_end - green_start
    total_dis = red + blue + green
print("The total distance painted is", total_dis)

