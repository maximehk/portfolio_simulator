import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='portfolio simulator',  
     version='0.1',
     packages=['portfolio_simulator'] ,
     author="Maxime",
     author_email="",
     description="A library that helps you run financial simulations using your financial assets as input.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/maximehk/portfolio_simulator",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
