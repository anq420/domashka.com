create database lesson_16_hw_food owner anq420 encoding='utf8';
create table users(
    user_id serial primary key, -- unique user id
    user_full_name varchar(50) not null, -- name cannot be longer than 50 letters and cannot be null
    user_ward integer not null unique -- it cannot be null, and moreover must be unique - 1 person can live in a ward
);

create table food(
    food_id serial primary key, -- unique food id
    food_name varchar(50) not null, -- food name cannot be longer than 50 letters and cannot be null
    grams_per_serving integer check (grams_per_serving > 0) not null -- grams in portion must be INT and cannot be 0
);

create table food_intake(
    intake_id serial primary key, -- unique intake id
    user_id integer references users(user_id) on delete cascade, -- this table reference on the column user_id ->
-- -> from table users; if a used is deleted from USERS, than all info which is relevant for a certain user gets deleted
    food_id integer references food(food_id) on delete cascade,-- this table reference on the column food_id ->
-- -> from table food; if a position is deleted from FOOD, than all info which is relevant for a certain pos gets deleted
    quantity integer check (quantity > 0) not null, -- quantity must be integer (amount of portions), it cannot be NULL
    food_intake_date date not null, -- date of intake; cannot be NULL
    food_intake_time time not null -- time of intake; cannot be NULL
)
