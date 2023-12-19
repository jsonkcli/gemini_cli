from setuptools import setup

setup(
    name='gemini',
    version='0.1.0',
    description='A command-line tool for interacting with the LLM models.',
    url='https://github.com/jsonkcli/gemini_cli',
    author='Jason Cli',
    author_email='json@aquireai.com',
    license='MIT',
    packages=['gemini'],
    entry_points={
        'console_scripts': [
            'gemini = gemini.cli:main',
        ],
    },
)
