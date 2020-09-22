# Shell Database

## Installation

You can intall shell-database from `pypi.org`:
```console
> pip install shell_database
```

## Getting started

### Adding a new key value pair
```
> shdb add name "John Doe"
```

### Adding a new key value pair with encryption

```
> shdb add password <your_password> --encrypt
```

### Getting the value of a key

```console
> shdb get name
John Doe
```

### Decrypting and encrypted value

```console
> shdb get password
b'51b8684c4dc77da0979f1b647caa707c'

> shdb get password --decrypt
<your_password>
```

### Integrating with other tools

```console
> shdb add az-rg azure-resource-group-123

> az postgres db create --resource-group $(shdb get az-rg) --server-name server_name --name database
```

## License


## Disclaimer
