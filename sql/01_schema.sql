-- Compressor Pressure Validation Project
-- Schema Definition

CREATE TABLE compressor_tests (
    id SERIAL PRIMARY KEY,
    supplier_id VARCHAR(50),
    batch_id VARCHAR(50),
    test_date TIMESTAMP,
    pressure_value FLOAT,
    pressure_threshold FLOAT,
    result VARCHAR(10), -- 'pass' or 'fail'
    operator_id VARCHAR(50),
    temperature FLOAT,
    humidity FLOAT
);

-- Optional: supplier table
CREATE TABLE suppliers (
    supplier_id VARCHAR(50) PRIMARY KEY,
    supplier_name VARCHAR(100)
);

-- Optional: operators table
CREATE TABLE operators (
    operator_id VARCHAR(50) PRIMARY KEY,
    operator_name VARCHAR(100)
);
