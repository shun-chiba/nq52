-- Table: nq52.dev_stock

-- DROP TABLE nq52.dev_stock;

CREATE TABLE nq52.dev_stock
(
    campany_cd integer NOT NULL,
    trade_date date NOT NULL,
    open real,
    high real,
    low real,
    close real,
    volume real,
    adj_close real,
    ave_price real,
    CONSTRAINT dev_stock_pkey PRIMARY KEY (trade_date, campany_cd)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE nq52.dev_stock
    OWNER to postgres;