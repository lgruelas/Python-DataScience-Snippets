[![license](https://img.shields.io/badge/licence-GPL--3-blue.svg)](https://github.com/lgruelas/Python-DataScience-Snippets/blob/master/LICENSE)

# Python Snippets for Machine Learning and Statistics algorithms

Python snippets for Machine Learning, Statistics and in general Data Science methods. I will avoid, as far as I can, the use of libraries like spicy, sklearn, etc. The porpouse of this repository is to give a easy to understand resource for algorithms implementations, using only numpy and pandas to manage the data and an implementation from scratch.

With this said, I want to clarify that the use of these codes is not convinient in a real world problem (for that already exist tons of wonderfull libraries), I only reccomend it to studie porpouses. 

I have done this to my better understanding, but I made it public in case that this code could help someone else to understand an algorithm.

## Table of contents

1. [Getting Started](#Getting-Started)
    1. [Prerequisites](#prerequisites)
    2. [Virtual Enviroment instructions](#virtual-enviroment-instructions)
    3. [Local instructions](#local-instructions)
    4. [Installing](#installing)
2. [Built With](#built-with)
3. [Authors](#authors)
4. [License](#license)
5. [Project status](#project-status)
6. [List of Algorithms](#list-of-algorithms)
    1. [ANN](#artificial-neural-networks)
    2. [Other](#other)

## Getting Started

You can choose to install the function package locally or in a virtualenv, bellow are the instuctions for the virtualenv.

### Prerequisites

* Linux
* Python 2.7
* virtualenv --In case you want to use it

This ones should get installed in the way, but if not, install them manually (I describe how in the next steps).

* Matplotlib
* Numpy
* Pytest

### Virtual Enviroment instructions

__Recommended__

First you need no install python and virtualenv

```
sudo dnf -y install python2
sudo dnf -y install python2-pip
pip2 install --user virtualenv
```

then create the virtualenv in the main folder (Python-DataScience-Snippets)

```
virtualenv -p python2 virtualenv_fortest
```

Every time you want to use the project, you must activate it with:

```
source virtualenv_forest/bin/activate
```

and then install the package with
```
chmod +x setpu.sh
./setup.sh
```

If something goes wrong, please try install the dependencies manually:

```
pip istall numpy
pip install matplotlib
pip install pytest
```

to check the installation use:
```
python
import pystatslearn
```

to deactive the virtualenv just type `deactivate`

### Local instructions

Python and dependencies:
```
sudo dnf -y install python2
sudo dnf -y install python2-pip
```

### Installing
Install the package with 
```
chmod -x setup.sh
./setup.sh
```

If something goes wrong, please try install the dependencies manually:

```
pip2 istall --user numpy
pip2 install --user matplotlib
pip2 install --user pytest
```

to check the installation use:
```
python2
import pystatslib
```

## Built With

* [Python](https://www.python.org/downloads/)


## Authors

* **Germán Ruelas** - *Developer* - [GitHub](https://github.com/lgruelas)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GPL 3 License - see the [LICENSE.md](LICENSE.md) file for details

## Project Status

I'm starting it, when I have enough time I will migrate it to __Python 3__.

## List of algorithms

### Artificial Neural Networks
* [Simple Perceptron](https://github.com/lgruelas/Python-DataScience-Snippets/tree/master/ANN/Perceptron)
* [Adaline](https://github.com/lgruelas/Python-DataScience-Snippets/tree/master/ANN/)

### Other
* [One Versus All classification](https://github.com/lgruelas/Python-DataScience-Snippets/tree/master/ANN/Perceptron)
* [K-folds Cross Validation](https://github.com/lgruelas/Python-DataScience-Snippets/tree/master/ANN/)

