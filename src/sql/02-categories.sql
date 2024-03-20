INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (2, 'Auto & Transport', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (3, 'Bills & Utilities', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (4, 'Business Services', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (5, 'Education', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (6, 'Entertainment', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (7, 'Fees & Charges', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (8, 'Financial', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (9, 'Food & Dining', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (10, 'Gifts & Donations', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (11, 'Health & Fitness', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (12, 'Home', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (13, 'Income', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (14, 'Investments', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (15, 'Kids', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (16, 'Loans', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (17, 'Technology', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (18, 'Personal Care', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (19, 'Pets', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (20, 'Shopping', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (21, 'Taxes', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (22, 'Transfer', NULL);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (23, 'Travel', NULL);

ALTER SEQUENCE maple.category_id_seq RESTART WITH 100;

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Auto Insurance', 2);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Auto Payment', 2);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Gas & Fuel', 2);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Parking', 2);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Public Transportation', 2);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Ride Share', 2);
    
INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Service & Parts', 2);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Home Phone', 3);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Internet', 3);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Mobile Phone', 3);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Television', 3);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Utilities', 3);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Streaming', 3);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Advertising', 4);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Legal', 4);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Office Supplies', 4);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Printing', 4);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Shipping', 4);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Office Event', 4);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Books & Supplies', 5);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Student Loan', 5);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Tuition', 5);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Amusement', 6);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Arts', 6);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Movies & DVDs', 6);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Music', 6);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Newspapers & Magazines', 6);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'ATM Fee', 7);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Bank Fee', 7);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Finance Charge', 7);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Late Fee', 7);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Service Fee', 7);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Membership Fee', 7);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Trade Commissions', 7);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Financial Advisor', 8);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Safety Deposit Box', 8);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Accountant', 8);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Alcohol & Bars', 9);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Coffee Shops', 9);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Fast Food', 9);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Food Delivery', 9);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Groceries', 9);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Restaurants', 9);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Charity', 10);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Gift', 10);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Dentist', 11);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Doctor', 11);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Eyecare', 11);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Gym', 11);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Health Insurance', 11);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Pharmacy', 11);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Sports', 11);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Furnishings', 12);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Home Improvement', 12);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Home Insurance', 12);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Home Services', 12);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Home Supplies', 12);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Lawn & Garden', 12);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Mortgage & Rent', 12);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Home Owners Association', 12);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Bonus', 13);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Interest Income', 13);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Paycheck', 13);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Reimbursement', 13);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Rental Income', 13);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Returned Purchase', 13);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Buy', 14);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Deposit', 14);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Dividend & Cap Gains', 14);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Sell', 14);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Withdrawal', 14);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Allowance', 15);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Baby Supplies', 15);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Babysitter & Daycare', 15);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Child Support', 15);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Kids Activities', 15);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Toys', 15);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Loan Fees and Charges', 16);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Loan Insurance', 16);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Loan Interest', 16);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Loan Payment', 16);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Loan Principal', 16);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Domain Names', 17);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Email', 17);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Hosting', 17);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Hair', 18);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Laundry', 18);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Spa & Massage', 18);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Pet Food & Supplies', 19);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Pet Grooming', 19);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Veterinary', 19);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Books', 20);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Clothing', 20);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Electronics & Software', 20);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Hobbies', 20);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Sporting Goods', 20);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Federal Tax', 21);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Local Tax', 21);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Property Tax', 21);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Sales Tax', 21);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'State Tax', 21);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Credit Card Payment', 22);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Transfer for Cash Spending', 22);


INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Air Travel', 23);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Hotel', 23);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Rental Car & Taxi', 23);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Vacation', 23);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Check', 1);

INSERT INTO maple.category (id, name, parent_category_id)
    VALUES (DEFAULT, 'Cash & ATM', 1);

ALTER SEQUENCE maple.category_id_seq RESTART WITH 1000;