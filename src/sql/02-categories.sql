INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (2, 'Auto & Transport', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (3, 'Bills & Utilities', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (4, 'Business Services', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (5, 'Education', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (6, 'Entertainment', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (7, 'Fees & Charges', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (8, 'Financial', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (9, 'Food & Dining', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (10, 'Gifts & Donations', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (11, 'Health & Fitness', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (12, 'Home', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (13, 'Income', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (14, 'Investments', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (15, 'Kids', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (16, 'Loans', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (17, 'Technology', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (18, 'Personal Care', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (19, 'Pets', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (20, 'Shopping', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (21, 'Taxes', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (22, 'Transfer', NULL, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (23, 'Travel', NULL, TRUE);

ALTER SEQUENCE maple.category_id_seq RESTART WITH 100;

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Auto Insurance', 2, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Auto Payment', 2, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Gas & Fuel', 2, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Parking', 2, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Public Transportation', 2, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Ride Share', 2, TRUE);
    
INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Service & Parts', 2, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Home Phone', 3, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Internet', 3, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Mobile Phone', 3, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Television', 3, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Utilities', 3, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Streaming', 3, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Advertising', 4, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Legal', 4, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Office Supplies', 4, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Printing', 4, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Shipping', 4, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Office Event', 4, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Books & Supplies', 5, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Student Loan', 5, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Tuition', 5, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Amusement', 6, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Arts', 6, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Movies & DVDs', 6, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Music', 6, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Newspapers & Magazines', 6, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'ATM Fee', 7, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Bank Fee', 7, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Finance Charge', 7, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Late Fee', 7, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Service Fee', 7, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Membership Fee', 7, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Trade Commissions', 7, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Financial Advisor', 8, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Safety Deposit Box', 8, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Accountant', 8, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Alcohol & Bars', 9, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Coffee Shops', 9, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Fast Food', 9, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Food Delivery', 9, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Groceries', 9, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Restaurants', 9, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Charity', 10, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Gift', 10, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Dentist', 11, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Doctor', 11, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Eyecare', 11, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Gym', 11, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Health Insurance', 11, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Pharmacy', 11, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Sports', 11, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Furnishings', 12, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Home Improvement', 12, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Home Insurance', 12, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Home Services', 12, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Home Supplies', 12, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Lawn & Garden', 12, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Mortgage & Rent', 12, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Home Owners Association', 12, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Bonus', 13, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Interest Income', 13, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Paycheck', 13, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Reimbursement', 13, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Rental Income', 13, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Returned Purchase', 13, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Buy', 14, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Deposit', 14, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Dividend & Cap Gains', 14, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Sell', 14, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Withdrawal', 14, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Allowance', 15, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Baby Supplies', 15, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Babysitter & Daycare', 15, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Child Support', 15, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Kids Activities', 15, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Toys', 15, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Loan Fees and Charges', 16, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Loan Insurance', 16, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Loan Interest', 16, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Loan Payment', 16, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Loan Principal', 16, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Domain Names', 17, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Email', 17, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Hosting', 17, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Hair', 18, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Laundry', 18, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Spa & Massage', 18, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Pet Food & Supplies', 19, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Pet Grooming', 19, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Veterinary', 19, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Books', 20, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Clothing', 20, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Electronics & Software', 20, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Hobbies', 20, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Sporting Goods', 20, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Federal Tax', 21, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Local Tax', 21, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Property Tax', 21, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Sales Tax', 21, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'State Tax', 21, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Credit Card Payment', 22, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Transfer for Cash Spending', 22, TRUE);


INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Air Travel', 23, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Hotel', 23, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Rental Car & Taxi', 23, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Vacation', 23, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Check', 1, TRUE);

INSERT INTO maple.category (id, name, parent_category_id, is_protected)
    VALUES (DEFAULT, 'Cash & ATM', 1, TRUE);

ALTER SEQUENCE maple.category_id_seq RESTART WITH 1000;