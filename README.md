[![license](https://img.shields.io/badge/licence-GPL--3-blue.svg)](https://github.com/lgruelas/Python-DataScience-Snippets/blob/master/LICENSE)

# Python Snippets for Machine Learning and Statistics algorithms

Python snippets for Machine Learning, Statistics and in general Data Science methods. I will avoid, as far as I can, the use of libraries like spicy, sklearn, etc. The porpouse of this repository is to give a easy to understand resource for algorithms implementations, using only numpy and pandas to manage the data and an implementation from scratch.

With this said, I want to clarify that the use of these codes is not convinient in a real world problem (for that already exist tons of wonderfull libraries), I only reccomend it to studie porpouses. 

I have done this to my better understanding, but I made it public in case that these code could help someone else to understand an algorithm.

## Getting Started

You can choose to install the function package locally or in a virtualenv, bellow are the instuctions for the virtualenv.

### Prerequisites

* Linux
* Python 3.6
* Matplotlib
* Numpy
* Pytest
* virtualenv --In case you want to use it

### Local instructions

Python and dependencies:
```
sudo dnf -y install python
sudo dnf -y install pip
pip istall --user numpy
pip install --user matplotlib
pip install --user pytest
```

### Installing
Install the package with 
```
```
now you can just import it with `import simpleStatsFunc`

### Virtual Enviroment instructions

First you need no install virtualenv

```
sudo dnf -y install python
sudo dnf -y install pip
pip install --user virtualenv
```

then create the virtualenv in the main folder (Python-DataScience-Snippets)

```
virtualenv -p python3 virtualenv_fortest
```

Every time you want to use the project, you must activate it

```
source virtualenv_forest/bin/activate
```

then you can install the dependencies

```
pip istall numpy
pip install matplotlib
pip install pytest
```

and then install the package with
```
```

to deactive the virtualenv just type `deactivate`
## Built With

* [Python](https://www.python.org/downloads/)


## Authors

* **Germán Ruelas** - *Developer* - [GitHub](https://github.com/lgruelas)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GPL 3 License - see the [LICENSE.md](LICENSE.md) file for details

## Project Status

I'm starting it

## List of algorithms

### Artificial Neural Networks
* [Simple Perceptron](https://github.com/lgruelas/Python-DataScience-Snippets/tree/master/ANN/Perceptron)
* [Adaline] (https://github.com/lgruelas/Python-DataScience-Snippets/tree/master/ANN/)

### Other
* [One Versus All classification](https://github.com/lgruelas/Python-DataScience-Snippets/tree/master/ANN/Perceptron)
* [K-folds Cross Validation] (https://github.com/lgruelas/Python-DataScience-Snippets/tree/master/ANN/)

