# def activity_select(start, end, ac_no, n):
#     ac_no = 1  # Start with the first activity
#     print(ac_no)
#     for i in range (n):
#         if(end[i]<=start[i+1]):
#             return ac_no
        
#         else:
#             ac_no += ac_no
        
#     return ac_no

# ac_no = [1,2,3,4,5]
# start = [5,6,0,4,10]
# end = [8,10,5,7,12]
# sort = sorted(zip(ac_no ,end),  reverse = True)
# n = len(sort)
# start = [sort[0] for i in range(n)]
# end = [sort[1] for i in range(n)]
# result = activity_select(start, end, ac_no, n)
# print("Maximum number of activities that can be performed:", result)

def activity_select(start, end, n):
    # Sort activities by end time
    activities = sorted(zip(start, end), key=lambda x: x[1])
    count = 1  #  select the first activity
    last_end = activities[0][1]
    for i in range(1, n):
        if activities[i][0] >= last_end:
            count += 1
            last_end = activities[i][1]
    return count

start = [5, 6, 0, 4, 10]
end = [8, 10, 5, 7, 12]
n = len(start)
result = activity_select(start, end, n)
print("Maximum number of activities that can be performed:", result)