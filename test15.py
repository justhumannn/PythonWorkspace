# def search_list(a,x):
#     n = len(a)
#     result = []
#     for i in range(0,n):
#         if x == a[i]:
#             result.append(i)
#     return result
# v = [17,92,18,33,58,7,33,42]
# print(search_list(v,18))
# print(search_list(v,33))
# print(search_list(v,900))
# def get_name(s_no,s_name,find_no):
#     n = len(s_no)
#     for i in range(0,n):
#         if find_no == s_no[i]:
#             return s_name[i]
#     return '?'
# sample_no = [39,14,67,105]
# sample_name = ['Justin','John','Mike','Summer']
# print(get_name(sample_no,sample_name,105))
# print(get_name(sample_no,sample_name,777))
def sel_sort(a):
    result = []
    while a:
        result.append(a.pop(a.index(min(a))))
    return result
d = [2,4,5,1,3]
print(sel_sort(d))