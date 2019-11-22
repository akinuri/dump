-- selects all columns from all tables (joined or not)
SELECT * FROM users
    LEFT JOIN admins    ON (users.type = "admin"     AND users.user_id = admins.user_id) 
    LEFT JOIN staff     ON (users.type = "staff"     AND users.user_id = staff.user_id) 
    LEFT JOIN customers ON (users.type = "customers" AND users.user_id = customers.user_id)
WHERE users.email = "someone@example.com"

-- if I'm querying for just one user, I'd like to get only the related fields
-- so if "someone@example.com" is a staff, I want to get users.*, staff.*
-- currently, I end up with all the fields (30) from all tables (admins, staff, customers)

-- this query will be run when I don't know the user's type (e.g. when the user logs in)
-- otherwise (if I know the user's type), I can just do

SELECT * FROM staff
JOIN users USING (user_id)

-- I thought I could use CASE, but I don't think it'll help in this case
-- I'd have to add like 30+ CASEs

-- select users.*, (+ columns from the joined table)
SELECT users.*,
    (CASE
        WHEN users.type = "admin" THEN admins.name
    END) as name,
    (CASE
        WHEN users.type = "admin" THEN admins.surname
    END) as surname,
    -- on and on
FROM users
    LEFT JOIN admins    ON (users.type = "admin"     AND users.user_id = admins.user_id) 
    LEFT JOIN staff     ON (users.type = "staff"     AND users.user_id = staff.user_id) 
    LEFT JOIN customers ON (users.type = "customers" AND users.user_id = customers.user_id)
WHERE users.email = "someone@example.com"

-- something like this would be much better
SELECT users.*,
    (CASE
        WHEN users.type = "admin"    THEN [select admins.*]
        WHEN users.type = "staff"    THEN [select staff.*]
        WHEN users.type = "customer" THEN [select customers.*]
    END)
FROM users
    LEFT JOIN admins    ON (users.type = "admin"     AND users.user_id = admins.user_id) 
    LEFT JOIN staff     ON (users.type = "staff"     AND users.user_id = staff.user_id) 
    LEFT JOIN customers ON (users.type = "customers" AND users.user_id = customers.user_id)
WHERE users.email = "someone@example.com"


-- for more info:
-- https://dbdiagram.io/d/5dd2bbe7edf08a25543e106e
-- https://stackoverflow.com/questions/58951653/how-to-handle-different-types-of-users-when-loggin-in
