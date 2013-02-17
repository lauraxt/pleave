drop table if exists policy;
create table policy (
    id INTEGER PRIMARY KEY,
    company INTEGER,
    leave_policy STRING NOT NULL,
    full_pay_days_off INTEGER,
    applies_to STRING,
    FOREIGN KEY(company) REFERENCES company(id)
);

create table company (
    id INTEGER PRIMARY KEY,
    name STRING NOT NULL,
    parent STRING NOT NULL,
    number_of_women_employees INTEGER,
    number_of_employees INTEGER
);
