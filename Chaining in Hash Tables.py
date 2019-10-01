# This algorithm is a continuation of the previous code on Hash Tables. It uses the concept of chaining to avoid collisions in hash tables. 
# It also builds a table to compare the collisions between different hash functions. A better hash function is the one with less collisions. 

my_table = empty_hash_table(100000)
import types

i =1
while i <= 100000: 
    word = randomword(10)
    add_to_hash_table(my_table,word,hash_str1)
    i +=1

#chaining 
def chain_hash_table(N, hashing_function): 
    table = empty_hash_table(N)
    
    i =1
    while i <= 5000: 
        word = randomword(10)
        if isinstance(my_table[hashing_function(word)],list):
            my_table[hashing_function(word)].append(word)
        if contains(my_table,word,hashing_function):
            add_to_hash_table(my_table,{my_table[hashing_function(word)],word},hashing_function)
        else:
            add_to_hash_table(my_table,word,hashing_function)
        i +=1

table1 = chain_hash_table(5000,hash_str1)
table2 = chain_hash_table(5000,hash_str2)
table3 = chain_hash_table(5000,hash_str3)
table4 = chain_hash_table(5000,hash_str4)

def collisions(table):
    collision_count = 0
    for i in range(0,len(table)):
        if table[i] == None:
            collision_count += 1
    return collision_count
print collisions(table1)
print collisions(table2)
print collisions(table3)
print collisions(table4)
