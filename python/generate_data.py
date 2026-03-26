import csv
import random
import os
from datetime import datetime, timedelta

random.seed(42)

suppliers = ["SUP_A", "SUP_B", "SUP_C"]
operators = ["OP_01", "OP_02", "OP_03", "OP_04"]

start_date = datetime(2025, 1, 1)
num_rows = 1000

base_path = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_path, "data", "raw", "compressor_data.csv")

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "supplier_id",
        "batch_id",
        "test_date",
        "pressure_value",
        "pressure_threshold",
        "result",
        "operator_id",
        "temperature",
        "humidity"
    ])

    for i in range(num_rows):
        supplier = random.choice(suppliers)
        operator = random.choice(operators)

        batch_id = f"BATCH_{random.randint(1001, 1100)}"
        test_date = start_date + timedelta(
            days=random.randint(0, 90),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )

        temperature = round(random.uniform(18, 32), 1)
        humidity = round(random.uniform(30, 70), 1)
        pressure_threshold = 50.0

        if supplier == "SUP_A":
            pressure_value = round(random.normalvariate(52, 2.5), 2)
        elif supplier == "SUP_B":
            pressure_value = round(random.normalvariate(49, 3.0), 2)
        else:
            pressure_value = round(random.normalvariate(46.5, 3.5), 2)

        result = "pass" if pressure_value >= 50 else "fail"

        writer.writerow([
            supplier,
            batch_id,
            test_date.strftime("%Y-%m-%d %H:%M:%S"),
            pressure_value,
            pressure_threshold,
            result,
            operator,
            temperature,
            humidity
        ])

print("✅ Data generated at:", file_path)
