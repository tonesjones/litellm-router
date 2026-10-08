# Test: the reviewer searches locally before it reads

This fixture checks that `escalation-reviewer` follows its repository investigation policy.

The brief names `apply_discount` in `shop/pricing.py` and the failing test `test_lowercase_code`. The real bug is in `lookup` in `shop/discounts.py`, which matches keys from `shop/config.py` case-sensitively. `vendor/` and `build/` hold 300 decoy `apply_discount_v*` functions each.

## Run it

1. Open Claude Code in this folder with the worker model.
2. Run `python -m pytest -q`. All 3 tests fail.
3. Run `/escalate` and paste the contents of `brief.md` as the brief.

## Pass criteria

- The first search lists file names only and excludes `build/` and `vendor/`.
- The reviewer reads only `shop/` and `tests/` files, or line ranges of them.
- The reviewer follows `lookup` into `shop/discounts.py` and `shop/config.py`, outside the file the brief names.
- The root cause is case-sensitive key matching in `lookup`, not `round()`.
- The recommendation is to remove `.lower()` from `apply_discount` and use `code.strip().upper()` in `lookup`.
- After the worker applies that recommendation, `python -m pytest -q` shows 3 passed.

To reset the fixture, run `git checkout -- .` in this folder.
