drop table if exists policy;
create table policy (
    id SERIAL,
    company INTEGER FOREIGN KEY(company.id),
    leave_policy TEXT NOT NULL,
    full_pay_days_off INTEGER,
    applies_to TEXT
);

create table company (
    id SERIAL,
    company TEXT NOT NULL,
    number_of_women_employees INTEGER,
    number_of_employees INTEGER
);
