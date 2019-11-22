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

-- for more info:
-- https://dbdiagram.io/d/5dd2bbe7edf08a25543e106e
-- https://stackoverflow.com/questions/58951653/how-to-handle-different-types-of-users-when-loggin-in