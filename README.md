PGen
====
Build Status
------------
[![Build Status](https://drone.io/github.com/Afonasev/PGen/status.png)](https://drone.io/github.com/Afonasev/PGen/latest)

Version
-------
0.2.0

Description
-----------
Online/Cli passwords generator.

Cli interface use case:
-----------------------
```bash
$ manage.py gen
Login: user
Site: site.com
Password:
Repeat for confirmation:
Your key: 22e0c92883
```

```bash
$ manage.py gen --length 5
...
Your key: 22e0c
```

```bash
$ manage.py gen -l 5
...
Your key: 22e0c
```

License
-------

The MIT License (MIT)

Copyright (c) 2014 Afonasev Eugene

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
