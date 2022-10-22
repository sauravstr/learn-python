# Sal's Shipping
# Sonny Li

weight = 80

# Ground Shipping 🚚

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)
      
# Ground Shipping Premimum 🚚💨

cost_ground_premium = 125.00

print("Ground Shipping Premimium $", cost_ground_premium)

# Drone Shipping 🛸

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Drone Shipping: $", cost_drone)

# Printing the cheapest method of shipping
print ("")
if cost_ground < cost_ground_Premium and cost_ground < cost_drone:
  print("The cheapest method of shipping is 'Ground Shipping'")
elif cost_drone < cost_ground and cost_drone < cost_ground_Premium:
  print("The cheapest method of shipping is 'Drone Shipping'")
elif cost_ground_Premium < cost_ground and cost_ground_Premium < cost_drone:
  print("The cheapest method of shipping is 'Ground Shipping Premium'")
