from setuptools import setup, find_packages


REQUIREMENTS = [
    'aiohttp==2.0.7',
    'pymorphy2[fast]==0.8',
    'gensim==2.0.0',
    'regex>=2017.4.29',
]

setup(
    name='pinkerton',
    version='0.0.1',
    description='Named entity linking and disambiguation service for russian language',
    url='https://github.com/bureaucratic-labs/pinkerton',
    author='Dmitry Veselov',
    author_email='d.a.veselov@yandex.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='natural language processing, named entity linking, wikification',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
)
