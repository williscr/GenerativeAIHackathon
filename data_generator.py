import csv
import random
import string


# function to generate random strings of length n
def generate_random_string(n):
    return ''.join(random.choices(string.ascii_letters, k=n))


# function to generate random integer between a and b
def generate_random_integer(a, b):
    return random.randint(a, b)


# function to generate random decimal between a and b
def generate_random_decimal(a, b):
    return round(random.uniform(a, b), 2)


# list of industries
industries = ['Technology', 'Healthcare', 'Finance', 'Manufacturing', 'Retail', 'Construction', 'Transportation']

# list of business rationales
business_rationales = ['Expansion', 'Inventory', 'Equipment', 'Marketing', 'Working Capital']

# number of loan applications to generate
k = 100

# generate loan application data and write to CSV file
with open('loan_applications.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Applicant Name', 'Applicant Age', 'Company Name', 'Revenue', 'Profit', 'Industry',
                     'Employee Count', 'Year Founded', 'Assets', 'Liability', 'Liquid Cash',
                     'Number of Key Suppliers', 'Customer Count', 'Business Rationale', 'Loan Amount',
                     'Loan Period in Years'])
    for i in range(k):
        applicant_name = generate_random_string(10)
        applicant_age = generate_random_integer(18, 75)
        company_name = generate_random_string(10) + ' ' + generate_random_string(5) + ' ' + 'Ltd.'
        revenue = generate_random_decimal(100000, 10000000)
        profit = generate_random_decimal(10000, 5000000)
        industry = random.choice(industries)
        employee_count = generate_random_integer(20, 100)
        year_founded = generate_random_integer(1900, 2023)
        assets = generate_random_decimal(100000, 10000000)
        liability = generate_random_decimal(10000, 1000000)
        liquid_cash = generate_random_decimal(10000, 1000000)
        num_key_suppliers = generate_random_integer(1, 20)
        customer_count = generate_random_integer(100, 10000)
        business_rationale = random.choice(business_rationales)
        loan_amount = generate_random_integer(10000, 500000)
        loan_period = generate_random_integer(1, 25)
        writer.writerow([applicant_name, applicant_age, company_name, revenue, profit, industry,
                         employee_count, year_founded, assets, liability, liquid_cash,
                         num_key_suppliers, customer_count, business_rationale, loan_amount,
                         loan_period])
