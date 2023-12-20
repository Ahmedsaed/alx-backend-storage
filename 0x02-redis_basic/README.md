# 0x02. Redis Basic

## Resources
Read or watch:
- [Redis Commands](https://intranet.alxswe.com/rltoken/lQ8ANhVfxDTxDr2UDSyQRA)
- [Redis Python Client](https://intranet.alxswe.com/rltoken/imfgFhAZPlg7YMZ_tHvFZw)
- [How to Use Redis With Python](https://intranet.alxswe.com/rltoken/7SluvFvgckwVgsvrfOf1CQ)
- [Redis Crash Course Tutorial](https://intranet.alxswe.com/rltoken/hJVo3XwMMFFoApyX8zPXvA)

## Learning Objectives
- Learn how to perform basic operations using Redis
- Understand how to use Redis as a simple caching solution

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- Files should end with a newline
- A `README.md` file at the root of the project folder is mandatory
- The first line of all files should be `#!/usr/bin/env python3`
- Code should adhere to the `pycodestyle` style (version 2.5)
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- Functions and methods should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should be meaningful sentences explaining the purpose of the module, class, or method (length will be verified)
- All functions and coroutines must be type-annotated.

## Installing Redis on Ubuntu 18.04
```
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.confUsing Redis in a ContainerRedis server is stopped by default. When starting a container, use: service redis-server start
```