numWorker = int(input("how many people work at the company: "))
salaries = [float(input(f"how much does employee {i+1} earn: ")) for i in range(numWorker)]
new_salaries = [500.00 for i in range(numWorker)]
print(salaries)
print(new_salaries)