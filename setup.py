from setuptools import setup, find_packages


setup(
    name='RailwayInfo',
    version='1.0.0',
    author='CleaverCreator',
    author_email='liuhanbo333@icloud.com',
    packages=find_packages(),
    zip_safe=False,
    platforms=['Linux', 'Macos'],
    install_requires=['pymysql'],
    python_requires='>=3.9',
    description='Railway info tools',
    long_description="""
                    Seeing GitHub
                                    """,
    license='MIT',
    url='https://github.com/CleverCreater/RailwayInfo',
    classifiers=[],
)
