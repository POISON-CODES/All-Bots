CREATE TABLE IF NOT EXISTS tickets (
	CHANNEL integer NOT NULL,
	TNO integer PRIMARY KEY AUTOINCREMENT,
	CLIENT integer NOT NULL,
	ARTIST integer NOT NULL DEFAULT 0,
	CONDITION text NOT NULL DEFAULT 'unoccupied',
	OPEN_TIME integer NOT NULL DEFAULT 0,
	CLOSE_TIME integer NOT NULL DEFAULT 0,
	STYLE text NOT NULL DEFAULT 'unoccupied',
	PANEL text NOT NULL
);

CREATE TABLE IF NOT EXISTS pricing (
	STYLE text NOT NULL,
	INR_PRICE integer NOT NULL,
	DOL_PRICE integer NOT NULL,
	INV_PRICE integer NOT NULL,
	PRIMARY KEY (STYLE)
);

CREATE TABLE IF NOT EXISTS completes (
	ARTIST integer NOT NULL,
	CHANNEL integer NOT NULL,
	CLIENT integer NOT NULL,
	STYLE text NOT NULL,
	LINK text NOT NULL,
	PRICE text NOT NULL,
	PRIMARY KEY (CHANNEL)
);