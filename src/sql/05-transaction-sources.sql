INSERT INTO maple.txn_source (id, name, has_api)
    VALUES ('993982ef-1dc4-4982-b9a0-4f7185d60250'::UUID, 'CSV', FALSE);

INSERT INTO maple.txn_source (id, name, has_api)
    VALUES ('6e97b9cf-8c7a-4352-a189-8e252b4891bd'::UUID, 'OFX', FALSE);

INSERT INTO maple.txn_source (id, name, has_api)
    VALUES ('649e21e3-0c57-4f05-8231-2c6854ab9e5c'::UUID, 'SimpleFin-Bridge', TRUE);

/* TODO: Implementation feasibility

INSERT INTO maple.txn_source (id, name, has_api)
    VALUES ('ac34864f-65a7-480e-aad4-969fe605b495'::UUID, 'Plaid', TRUE);
*/

-- additionally want to consider some sort of scraping api
