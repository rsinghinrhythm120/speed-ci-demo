# speed ci live demo

A tiny Python project checked by [SPEED](https://github.com/ArulaAI/workbench) `speed ci` on every pull request
and push to main: evals, lint, typecheck, tests, e2e, a custom API check, a PostgreSQL integration test,
SPEED's secret scan, Semgrep, pip-audit, Trivy, Gitleaks and CodeQL. Each check runs as its own parallel
job; the `speed-ci` job combines them, and findings go to the Security tab.
