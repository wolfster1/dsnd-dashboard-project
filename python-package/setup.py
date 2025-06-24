from pathlib import Path
from setuptools import setup, find_packages

cwd = Path(__file__).resolve().parent
requirements = (cwd / 'employee_events' / 'requirements.txt').read_text().split('\n')

setup_args = dict(
    name='employee_events',
    version='1.0',
    description='SQL Query API',
    packages=find_packages(),
    package_data={'': ['employee_events.db', 'requirements.txt']},
    install_requirements=requirements,
    )

if __name__ == "__main__":
    setup(**setup_args)


