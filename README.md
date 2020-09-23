# Shell Database

[![CircleCI](https://img.shields.io/circleci/build/github/jcoelho93/shell-database/master?logo=circleci)](https://app.circleci.com/pipelines/github/jcoelho93/shell-database)
[![PyPI](https://img.shields.io/pypi/v/shell-database)](https://pypi.org/project/shell-database/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/shell-database?logo=python)
![PyPI - Downloads](https://img.shields.io/pypi/dm/shell-database)
[![PyPI - License](https://img.shields.io/pypi/l/shell-database)](https://github.com/jcoelho93/shell-database/blob/master/LICENSE)


A key value store straight from your terminal.

## Installation

You can install shell-database from `pypi.org`:
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

MIT License

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.