from setuptools import setup, find_packages
hypen_e_dot='-e .'
def get_requirements(filename):
    with open(filename) as f:
        req = [line.strip() for line in f if line.strip()]
        if hypen_e_dot in req:
            req.remove(hypen_e_dot)
    return req


setup(
    name='my_mlproject',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    
    author='Yashendra Rajput', 
    author_email='yashendra.rajput@example.com',
    description='A simple machine learning project'
)