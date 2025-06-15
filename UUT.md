# Units Under Test

This project includes Django applications with basic e-commerce functionality.
The following units are covered by tests:

- `Product` model: verifies product creation and field assignments.
- `index` view: ensures the index page renders with products listed.
- `new` view: checks the new arrivals view returns the expected message.

The test suite can be run with:

```bash
python manage.py test
```

Test output from a recent run is stored in `test_results.md`.
