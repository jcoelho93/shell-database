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

MIT License

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.