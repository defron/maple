INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (2, 'Auto & Transport', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (3, 'Bills & Utilities', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (4, 'Business Services', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (5, 'Education', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (6, 'Entertainment', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (7, 'Fees & Charges', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (8, 'Financial', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (9, 'Food & Dining', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (10, 'Gifts & Donations', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (11, 'Health & Fitness', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (12, 'Home', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (13, 'Income', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (14, 'Investments', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (15, 'Kids', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (16, 'Loans', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (17, 'Technology', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (18, 'Personal Care', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (19, 'Pets', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (20, 'Shopping', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (21, 'Taxes', NULL, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (22, 'Transfer', NULL, TRUE, FALSE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (23, 'Travel', NULL, TRUE, TRUE);

ALTER SEQUENCE maple.category_id_seq RESTART WITH 100;

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Auto Insurance', 2, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Auto Payment', 2, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Gas & Fuel', 2, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Parking', 2, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Public Transportation', 2, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Ride Share', 2, TRUE, TRUE);
    
INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Service & Parts', 2, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Home Phone', 3, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Internet', 3, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Mobile Phone', 3, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Television', 3, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Utilities', 3, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Streaming', 3, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Advertising', 4, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Legal', 4, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Office Supplies', 4, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Printing', 4, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Shipping', 4, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Office Event', 4, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Books & Supplies', 5, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Student Loan', 5, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Tuition', 5, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Amusement', 6, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Arts', 6, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Movies & DVDs', 6, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Music', 6, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Newspapers & Magazines', 6, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'ATM Fee', 7, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Bank Fee', 7, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Finance Charge', 7, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Late Fee', 7, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Service Fee', 7, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Membership Fee', 7, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Trade Commissions', 7, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Financial Advisor', 8, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Safety Deposit Box', 8, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Accountant', 8, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Alcohol & Bars', 9, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Coffee Shops', 9, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Fast Food', 9, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Food Delivery', 9, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Groceries', 9, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Restaurants', 9, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Charity', 10, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Gift', 10, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Dentist', 11, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Doctor', 11, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Eyecare', 11, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Gym', 11, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Health Insurance', 11, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Pharmacy', 11, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Sports', 11, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Furnishings', 12, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Home Improvement', 12, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Home Insurance', 12, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Home Services', 12, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Home Supplies', 12, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Lawn & Garden', 12, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Mortgage & Rent', 12, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Home Owners Association', 12, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Bonus', 13, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Interest Income', 13, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Paycheck', 13, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Reimbursement', 13, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Rental Income', 13, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Returned Purchase', 13, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Buy', 14, TRUE, FALSE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Deposit', 14, TRUE, FALSE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Dividend & Cap Gains', 14, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Sell', 14, TRUE, False);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Withdrawal', 14, TRUE, FALSE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Allowance', 15, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Baby Supplies', 15, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Babysitter & Daycare', 15, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Child Support', 15, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Kids Activities', 15, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Toys', 15, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Loan Fees and Charges', 16, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Loan Insurance', 16, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Loan Interest', 16, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Loan Payment', 16, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Loan Principal', 16, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Domain Names', 17, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Email', 17, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Hosting', 17, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Hair', 18, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Laundry', 18, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Spa & Massage', 18, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Pet Food & Supplies', 19, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Pet Grooming', 19, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Veterinary', 19, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Books', 20, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Clothing', 20, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Electronics & Software', 20, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Hobbies', 20, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Sporting Goods', 20, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Federal Tax', 21, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Local Tax', 21, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Property Tax', 21, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Sales Tax', 21, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'State Tax', 21, TRUE, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Credit Card Payment', 22, TRUE, FALSE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Transfer for Cash Spending', 22, TRUE, FALSE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Air Travel', 23, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Hotel', 23, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Rental Car & Taxi', 23, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Vacation', 23, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Check', 1, TRUE, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected, is_cashflow)
    VALUES (DEFAULT, 'Cash & ATM', 1, TRUE, TRUE);

ALTER SEQUENCE maple.category_id_seq RESTART WITH 1000;