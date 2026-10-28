"""Integration test against a real PostgreSQL: create a table, write and read a row.

Uses DATABASE_URL (set by the speed ci GitHub workflow's postgres service), else the local server.
"""
import os
import shutil
import subprocess
import sys

url = os.environ.get("DATABASE_URL", "postgresql://localhost:5432/postgres")
psql = shutil.which("psql") or "/opt/homebrew/opt/postgresql@16/bin/psql"
sql = ("DROP TABLE IF EXISTS speed_ci_sums; CREATE TABLE speed_ci_sums (a int, b int, total int);"
       "INSERT INTO speed_ci_sums VALUES (1, 2, 3); SELECT total FROM speed_ci_sums WHERE a = 1 AND b = 2;"
       "DROP TABLE speed_ci_sums;")
out = subprocess.run([psql, url, "-v", "ON_ERROR_STOP=1", "-tAq", "-c", sql], capture_output=True, text=True)
if out.returncode != 0:
    sys.exit(f"PostgreSQL integration test failed: {out.stderr.strip()}")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import add
assert int(out.stdout.strip()) == add(1, 2), out.stdout
print(f"PostgreSQL integration test passed (database total {out.stdout.strip()} == add(1, 2))")
