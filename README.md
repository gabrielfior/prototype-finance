# Prototype

Boilerplate code for delivering JSON-like data from back-end and reading/plotting data on front-end.

## Getting started

### Prerequisites

1. Make sure you have Conda installed - if possible Miniconda [link](https://conda.io/docs/user-guide/install/index.html)
2. Clone this repository
```bash
git clone https://github.com/gabrielfior/prototype-finance.git
cd prototype-finance
```
3. Create new conda environment from environment.yml file
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

It should be running on http://localhost:5000. 

The documentation is available on http://localhost:5000/docs/.

A schema of the Rest API (in OpenAPI format) is available on http://localhost:5000/schema/.

2. Start the front-end

```bash
cd front-end
ng serve
```

The front-end should be running on http://localhost:4200.

## Running back-end tests

```bash
cd python-backend
pytest
```

## Built With

* [apistar](https://docs.apistar.com/) - Python Web API framework - Nice for easy docs and schema generation
* [angular-cli](https://angular.io) - Development tools and libraries specialized for Angular
* [ngx-charts](https://swimlane.github.io/ngx-charts/) - Declarative Charting Framework for Angular
