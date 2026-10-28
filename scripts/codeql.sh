#!/bin/sh
# CodeQL security and quality queries for Python. Prints SARIF on stdout; progress goes to stderr.
set -e
work="${RUNNER_TEMP:-${TMPDIR:-/tmp}}/speed-ci-codeql"
mkdir -p "$work"
codeql database create "$work/db" --language=python --source-root=. --overwrite --quiet >&2
codeql database analyze "$work/db" codeql/python-queries:codeql-suites/python-security-and-quality.qls \
    --download --format=sarif-latest --output="$work/results.sarif" --quiet >&2
cat "$work/results.sarif"
