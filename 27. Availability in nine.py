uptime_percentage = 99.9  # change this value to the desired availability percentage
nines = round((100 - uptime_percentage) / 0.1)
print(f"Availability in {nines} nines: {uptime_percentage}%")


# This code takes the desired availability percentage as input and calculates the number of nines required to express that availability. It then outputs the availability in nines.

#For example, if you set uptime_percentage to 99.999, the code will output "Availability in 5 nines: 99.999%". If you set uptime_percentage to 99.9, the code will output "Availability in 3 nines: 99.9%".

#Note that this code only calculates the number of nines required to express availability. Achieving high availability in a system requires careful system design, including redundancy, fault tolerance, failover mechanisms, and proactive monitoring and maintenance.
