from setuptools import setup

setup(
    name='sensors_monitor',
    packages=['sensors_monitor', 'sensors_monitor_core', 'sensors_monitor_rest'],
    include_package_data=True,
    install_requires=[
        'flask',
        'RPi',
        'Adafruit_DHT'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
