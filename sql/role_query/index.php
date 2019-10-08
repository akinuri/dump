<?php

$db = [
    "users" => [
        // id , name, surname, age, sex
        [ 1, "Oliver", "Alston",   14, "male"   ],
        [ 2, "Ava",    "Phillips", 21, "female" ],
        [ 2, "Jack",   "Morton",   25, "male"   ],
        [ 3, "Harry",  "Nye",      20, "male"   ],
        [ 2, "Kayla",  "Brown",    19, "female" ],
    ],
    
    "roles" => [
        // id , name, display_name
        [ 1, "admin",   "Admin"],
        [ 2, "editor",  "Editor"],
        [ 3, "manager", "Manager"],
    ],
    
    "user_role" => [
        // id , user_id, role_id
        [ 1, 1, 3],
        [ 1, 2, 1],
        [ 1, 3, 2],
    ],
];

echo "<pre>";



// SELECT * FROM users WHERE id = 1
$result = [];
// FROM users
foreach ($db["users"] as $user) {
    // WHERE id = 1
    if ($user[0] == 1) {
        // SELECT *
        $result[] = $user;
    }
}
print_r($result);
// logically -> FROM users WHERE id = 1 SELECT *



// SELECT name, surname FROM users WHERE sex = male
$result = [];
// FROM users
foreach ($db["users"] as $user) {
    // WHERE sex = male
    if ($user[4] == "male") {
        // SELECT name, surname
        $result[] = [
            "name"    => $user[1],
            "surname" => $user[2],
        ];
    }
}
print_r($result);
// logically -> FROM users WHERE sex = male SELECT name, surname



// SELECT * FROM roles WHERE id IN (SELECT role_id FROM user_role WHERE user_id = 1)
$IN_result = [];
// FROM user_role
foreach ($db["user_role"] as $user_role) {
    // WHERE user_id = 1
    if ($user_role[1] == 1) {
        // SELECT role_id
        $IN_result[] = $user_role[2];
    }
}
$result = [];
// FROM roles
foreach ($db["roles"] as $role) {
    // WHERE id IN ()
    if (in_array($role[0], $IN_result)) {
        // SELECT *
        $result[] = $role;
    }
}
print_r($result);
// logically (parenthesis first) -> FROM roles WHERE id IN (FROM user_role WHERE user_id = 1 SELECT role_id) SELECT *



// SELECT r.* FROM user_role AS ur INNER JOIN roles AS r ON r.id = ur.role_id WHERE ur.user_id = 1
// WTH?

