from setuptools import setup, find_packages
# from panduza_platform.conf import PLATFORM_VERSION


setup(
    name="panduza_admin_dashboard",

    version="0.0.0",

    author="Panduza Team",

    author_email="panduza.team@gmail.com",

    description='Panduza Admin Dashboard',

    long_description=" ",

    packages=find_packages(),

    # package_dir={"images": "images"},
    # package_data={"images": ["*.jpg"]},
    include_package_data=True,

    zip_safe=False,

    install_requires=[
        'nicegui==1.4.1',
    ],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix"
    ]
)
