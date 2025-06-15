Creating test database for alias 'default'...
System check identified some issues:

WARNINGS:
products.Brand: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the ProductsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
products.Category: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the ProductsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
products.Offer: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the ProductsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
products.Product: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the ProductsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.

System check identified 4 issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.012s

OK
Destroying test database for alias 'default'...
