from oops_proj import chatbook

# user1 = chatbook()

# function vs method

lst = [1,2,3]
# function
a1 = len(lst)
# print(a1)

# method
user1 = chatbook()
print(user1.id)

# using static method directly from class rather than object
print(chatbook.get_id())

chatbook.set_id(10)


user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)

# user1.my_post()

# print(user1._chatbook__name)






# getter and setter
# print(user1.get_name())
# user1.set_name("ritik mer")
# print(user1.get_name())