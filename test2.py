def calculate_simple_interest(principal, rate, time):
    return principal * rate * time
 
def calculate_compound_interest(principal, rate, time, n):
    return principal * (1 + rate / n) ** (n * time) - principal
 

principal = 1000 
rate = 0.05  
time = 5  
n = 12 
print(calculate_simple_interest(principal, rate, time))
print(calculate_compound_interest(principal, rate, time, n))
