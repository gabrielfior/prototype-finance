# Prototype

Small boilerplate for delivering JSON-like data from back-end and reading/plotting data on front-end.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

1. Make sure you have Conda installed - if possible Miniconda [link](https://conda.io/docs/user-guide/install/index.html)
2. Create new conda environment from environment.yml file
```bash
conda env create -f environment.yml
```
3. Install npm packages
```bash
cd front-end/
npm install
```

### Running the app

1. Start back-end

```bash
cd python-backend
python app.py
```

The back-end should be running on http://localhost:5000. 

The documentation is available on http://localhost:5000/docs/.

A schema of the Rest API (in OpenAPI format) is available on http://localhost:5000/schema/.

2. Start the front-end

```bash
cd front-end
ng serve
```

The front-end should be running on http://localhost:4200.

## Running the tests

```bash
cd python-backend
pytest
```

## Built With

* [apistar](https://docs.apistar.com/) - The web framework used
* [angular-cli](https://angular.io) - Dependency Management
