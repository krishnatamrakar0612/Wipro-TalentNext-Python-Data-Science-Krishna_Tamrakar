hourly_rate = 0.51
hours_per_day = 24
days_per_week = 7
days_per_month = 30

cost_per_day = hourly_rate * hours_per_day
cost_per_week = cost_per_day * days_per_week
cost_per_month = cost_per_day * days_per_month
days_with_budget = 918 / cost_per_day

print(f"How much does it cost to operate one server per day? ${cost_per_day:.2f}")
print(f"How much does it cost to operate one server per week? ${cost_per_week:.2f}")
print(f"How much does it cost to operate one server per month? ${cost_per_month:.2f}")
print(f"How many days can I operate one server with $918? {days_with_budget:.2f} days")