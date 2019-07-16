-- creates new user and gives them privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIES BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
