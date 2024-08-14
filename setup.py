"""A setuptools based setup module."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="security_txt_policy_server",
    version="1.0.2",
    description="security-txt-policy-server serves `.well-known/security.txt` files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Cyberfusion",
    author_email="support@cyberfusion.io",
    url="https://github.com/CyberfusionIO/security-txt-policy-server",
    platforms=["linux"],
    packages=find_packages(
        include=[
            "security_txt_policy_server",
            "security_txt_policy_server.*",
        ]
    ),
    data_files=[],
    entry_points={
        "console_scripts": [
            "security-txt-policy-server=security_txt_policy_server.server:main"
        ]
    },
    install_requires=[
        "starlette==0.38.2",
        "uvicorn==0.30.6",
        "validators==0.33.0",
    ],
)
