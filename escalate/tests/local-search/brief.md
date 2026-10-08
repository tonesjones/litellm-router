# Escalation Brief

## Objective
Discount codes should work in any letter case.

## Success Criteria
All tests in `tests/test_pricing.py` pass.

## Current State
`test_uppercase_code` now fails too, after Attempt 1.

## Evidence
```
FAILED tests/test_pricing.py::test_lowercase_code - assert 100.0 == 90
```

## Relevant Code
`apply_discount` in `shop/pricing.py`.

## Attempts
### Attempt 1
Added `code.lower()` inside `apply_discount`. `test_lowercase_code` still fails and `test_uppercase_code` started failing.
### Attempt 2
Considered adding lowercase keys for each code. Didn't do it because it doubles the data and misses mixed case.

## Current Hypotheses
`round()` in `apply_discount` returns the wrong value.

## Exact Question for Reviewer
Why does `apply_discount` ignore lowercase codes, and what's the right fix?
