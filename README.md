do-not-commit
=====

A pre-commit hook to disallow committing strings

## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Sample `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/ahonnecke/do-not-commit
    rev: v0.0.1
    hooks:
    -   id: do-not-commit
```
