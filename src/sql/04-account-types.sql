INSERT INTO maple.account_type (id, name, is_asset)
    VALUES (1, 'Cash', TRUE);

INSERT INTO maple.account_type (id, name, is_asset)
    VALUES (2, 'Credit Card', FALSE);

INSERT INTO maple.account_type (id, name, is_asset)
    VALUES (3, 'Investment', TRUE);

INSERT INTO maple.account_type (id, name, is_asset)
    VALUES (4, 'Loan', FALSE);

INSERT INTO maple.account_type (id, name, is_asset)
    VALUES (5, 'Property', TRUE);

ALTER SEQUENCE maple.account_type_id_seq RESTART WITH 1000;