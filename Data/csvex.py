import matplotlib.pyplot as plt
import csv

year_intervals = []
Seoul_pop = []
Capital_region_pop = []

with open('data/Seoul_pop2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 0 or row[0][0] == '#':
            continue
        else:
            year_intervals.append(row[0])
            Seoul_pop.append(float(row[1]))
            Capital_region_pop.append(float(row[2]))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

plt.plot(range(12), Seoul_pop, color='purple', marker='o', linestyle='solid', label='Seoul')
plt.plot(range(12), Capital_region_pop, color='blue', marker='o', linestyle='solid', label='Capital Region')

plt.xticks(range(12), year_intervals, rotation=45)

plt.title('Population Change')
plt.ylabel('Percentage')

plt.legend()
plt.show()
