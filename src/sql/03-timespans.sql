INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (2, 'Quarterly', '3 months', TRUE);

INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (3, 'Semi-Annually', '6 months', TRUE);

INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (4, 'Yearly', '1 year', TRUE);

INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (5, 'Weekly', '7 days', FALSE);

INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (6, 'Every 2 Weeks', '14 days', FALSE);

INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (7, 'Every 28 Days', '28 days', FALSE);

INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (8, 'Every 30 Days', '30 days', FALSE);

INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (9, 'Every 31 Days', '31 days', FALSE);

INSERT INTO maple.timespan (id, name, span, allowed_for_budget)
    VALUES (10, 'Every 90 Days', '90 days', FALSE);

ALTER SEQUENCE maple.timespan_id_seq RESTART WITH 1000;