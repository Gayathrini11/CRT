def linear_search(elements,target):
    for i in range(len(elements)):
        if target == elements[i]:
            return i
    return -1
print(linear_search([12,45,78,69,32],12))
print(linear_search([12,45,78,69,32],78))
print(linear_search([12,45,78,69,32],32))