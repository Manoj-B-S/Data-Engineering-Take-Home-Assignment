CREATE TABLE IF NOT EXISTS staging_exchange_rates (
    rate_date DATE PRIMARY KEY,
    gbp_to_inr NUMERIC(10,4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raw_products (
    title TEXT,
    price_gbp NUMERIC(10,2),
    category TEXT,
    availability TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    title TEXT,
    category TEXT,
    availability_count INT,
    price_gbp NUMERIC(10,2),
    price_inr NUMERIC(10,2),
    price_tier TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);