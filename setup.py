from setuptools import setup, find_packages

setup(
    name="cfms_plus",
    version="1.0.0",
    description="Church Management System Plus",
    author="Abigael Lemba",
    author_email="mbitheabigail20@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "frappe",
    ],
)
