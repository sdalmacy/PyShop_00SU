Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Operations to perform:
  Synchronize unmigrated apps: messages, staticfiles
  Apply all migrations: admin, auth, contenttypes, orders, payments, products, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying products.0001_initial... OK
  Applying products.0002_offer... OK
  Applying products.0003_auto_20250615_1740... OK
  Applying orders.0001_initial... OK
  Applying payments.0001_initial... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).
test_index_view_displays_products (products.tests.IndexViewTest.test_index_view_displays_products) ... ok
test_root_url_serves_index (products.tests.IndexViewTest.test_root_url_serves_index) ... ok
test_new_view_returns_message (products.tests.NewViewTest.test_new_view_returns_message) ... ok
test_create_product (products.tests.ProductModelTest.test_create_product) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.013s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
