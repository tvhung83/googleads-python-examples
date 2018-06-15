# Google AdWords Remarketing examples

A set of CRM-based UserList examples, each example is to upload UserList by each
type:
- EMAIL
- PHONE_NUMBER
- MOBILE_ID
- USER_ID

## How to run?

``` sh
$ cp googleads_sample.yaml googleads.yaml
$ vim googleads.yaml # Update credentials
$ pip install googleads
$ chmod +x run.py
$ ./run.py (email|phone_number|mobile_id|user_id)
```

If you're on macOS and having permission issue, re-run with `sudo` or correct
the target location owner/permission:

``` sh
Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python2.7/site-packages/googleads-12.0.0.dist-info/INSTALLER'
Consider using the `--user` option or check the permissions.
```

## How to enable DEBUG logs?
Update `level` of desired logger in `googleads.yaml`, for example, enable DEBUG
on root logger:

``` yaml

logging:
  (omitted)
  loggers:
    # Configure root logger
    "":
      handlers: [default_handler]
      level: DEBUG
```

See more details [here](https://github.com/googleads/googleads-python-lib)
