"""Installer for the {{ cookiecutter.python_package_name }} package."""

from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="{{ cookiecutter.python_package_name }}",
    version="{{ cookiecutter.__version_package }}",
    description="{{ cookiecutter.description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        {%- if cookiecutter.__feature_distribution == '1' %}
        "Framework :: Plone :: Distribution",
        {%- endif %}
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    url="https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.python_package_name }}",
    project_urls={
        "PyPI": "https://pypi.org/project/{{ cookiecutter.python_package_name }}",
        "Source": "https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.python_package_name }}",
        "Tracker": "https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.python_package_name }}/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=[{{ cookiecutter.__package_namespaces }}],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        "Products.CMFPlone",
        "plone.api",
        {% if cookiecutter.__feature_headless == '1' -%}
        "plone.restapi",
        "plone.volto",
        {%- endif %}
    ],
    extras_require={
        "test": [
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "plone.app.testing",
            {% if cookiecutter.__feature_headless == "0" and cookiecutter.plone_version >= "6.1" -%}
            "plone.classicui",
            {%- endif -%}
            "plone.restapi[test]",
            "pytest",
            "pytest-cov",
            "pytest-plone>=0.5.0",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = {{ cookiecutter.python_package_name }}.locales.update:update_locale
    """,
)
