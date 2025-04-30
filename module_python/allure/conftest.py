import subprocess
import pytest

def pytest_sessionfinish(session, exitstatus):
    print('\n')
    subprocess.run(
        ["allure", "generate", "allure-results","--clean", "-o", "allure-report"],
        shell=True,
        check=True
    )