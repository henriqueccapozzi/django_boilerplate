# Bussiness rules / combined constraints

- All reservations are of a fixed time length
- Any user can only have 1 active or scheduled reservation at any time
- The maximum time a reservation can take to be ready is 10 minutes
- All reservations will be fullfilled with our own cloud account

# Infrastructure requirements

A user can only create a reservation if the server/cloud/cluster have enough
resources at the scheduled time. For that to happen the whole reservation
capacity is going to be considered

# 1

As a user, when I choose the option to create a reservation now
I want to able to reserve a 'design' deployment as soon as there is
available infrastructure for it

# 2

As a user, when I choose the option to schedule a reservation
I must only see dates/times when I can reserve the choosen design

# 3

When loged in as a user, I can check the status of all his reservation

# 4

As a special user I can have more than 1 scheduled reservation plus
1 active reservation
