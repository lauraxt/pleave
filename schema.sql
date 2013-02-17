drop table if exists company_and_policy;
create table company_and_policy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING NOT NULL,
    parent STRING NOT NULL,
    leave_policy STRING NOT NULL,
    number_of_women_employees INTEGER DEFAULT 0,
    number_of_employees INTEGER DEFAULT 0,
    full_pay_days_off INTEGER,
    applies_equally BOOLEAN
);
