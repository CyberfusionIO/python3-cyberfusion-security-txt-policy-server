# Security TXT Policy Server

Security TXT Policy Server serves `.well-known/security.txt` files.

# Install

## Generic

Run the following command to create a source distribution:

```
python3 setup.py sdist
```

## PyPI

Run the following command to install the package from PyPI:

```
pip3 install security-txt-policy-server
```

# Configure

## App

The following environment variables may be specified:

```
; The app name is used in several places for this app to identify itself (string)
; Default: security-txt-policy-server
APP_NAME=

; The server will bind to this host (string)
; Default: ::1
LISTEN_HOST=

; The server will listen to this port (integer)
; Default: 8080
LISTEN_PORT=

; IP addresses of proxies that are trusted with proxy headers (comma separated list of strings)
; Default: ::1
TRUSTED_PROXY_ADDRESSES=

; The path to your JSON database (string)
; Default: none
DATABASE_PATH=
```

Only `DATABASE_PATH` is required to be set. We recommend setting it to `/var/lib/security-txt-policy-server.json`.

## JSON Database

Find an example JSON database in `security-txt-policy-server.json`.

Properties:

* `domains`. List of domains that this security.txt policy is served for.
* `expires_timestamp`. UNIX timestamp of security.txt 'Expires' field.
* `email_contacts`. (Do not add prefix `mailto:` which is required by security.txt - the server does this.)
* `url_contacts`
* `encryption_key_urls`
* `acknowledgment_urls`
* `preferred_languages`
* `policy_urls`
* `opening_urls`

Find information about these properties on https://securitytxt.org/.

# Usage

## Start

Start Security TXT Policy Server manually with:

```
bin/security-txt-policy-server
```

Find the systemd configuration in `security-txt-policy-server.service`.

## SSL

Use a proxy that terminates SSL. E.g. [HAProxy](http://www.haproxy.org/).

# Tests

Run tests with pytest:

```
DATABASE_PATH=security-txt-policy-server.json pytest tests/
```

The tests must be run from the project root.
