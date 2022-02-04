#Mini Project Week 3Mini Project Week 3
#So far we've been using one-dimensional lists of data, 
#however, this won't work for orders. We need to store more 
# information such as the customer's name, address
#and phone number, as well as the status of the order, the courier etc.
# To solve this we'll use a two-dimensional data structure, a  
# dictionary . We won't be able to

#read/write this structure to text file anymore, but we'll fix this later. 
#For now we'll also skip adding products to the order.
#STRETCH We'll also write a unit test that covers the update order status functionality.
'''GoalsGoals
As a user I want to:
create a product, courier, or order and add it to a list
view all products, couriers, or orders
update the status of an order
persist my data (products and couriers)
STRETCH persist my data (orders in a  .csv  file)
STRETCH update or delete a product, order, or courier
STRETCH add a unit test for the update order status functionality
SpecSpec
A  product  should just be a  string  containing its name, i.e:  "Coke Zero"
A list of  products  should be a list of  strings , i.e:  ["Coke Zero"]
A  courier  should just be a  string  containing its name, i.e:  "John"
A list of  couriers  should be a list of  strings , i.e:  ["John"]
An  order  should be a  dict , i.e:
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "preparing"
}
A list of  orders  should be a list of  dicts , i.e:  [{...},{...}]
Data should be persisted to a  .txt  file on a new line for each courier
or product'''