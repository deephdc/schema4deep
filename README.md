# schema4deep
Metadata validator for DEEP data science applications.

## Motivation
schema4deep validates the metadata used by the DEEP applications. The metadata
will be eventually used by the
[DEEP open catalog](https://marketplace.deep-hybrid-datacloud.eu/) to describe
and give access to the applications.

## Implementation
The [schema](schema4deep/schemata/deep-apps.json) has been implemented according to [JSON
schema specification](https://json-schema.org/) (Draft 7), using [Python's
jsonschema](https://pypi.org/project/jsonschema/) module.

Once schema4deep is deployed, the `deep-app-schema-validator` CLI tool is
provided, which accepts schema instance files as input parameters.

## Installation
```
$ pip install git+https://github.com/deephdc/schema4apps
```

## Usage
```
$ deep-app-schema-validator instances/sample.mods.json
```
