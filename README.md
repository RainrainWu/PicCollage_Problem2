# PicCollage_Problem2

Solution for PicCollage interview step 3 problem 2.

# Getting Started
## Prerequisites
- Python 3.8
- [poetry 1.0.5](https://python-poetry.org/docs/)
- [invoke 1.4.1](http://www.pyinvoke.org/)

## Setup Environment
```
$ inv env.dev
$ export PYTHONPATH=$PYTHONPATH:$PWD
```

## Run Program
```
$ sh scripts/mongo.sh
$ poetry run python shortener/app.py
```

## Welcome Page

visit `http://localhost:5000`

![](https://i.imgur.com/IhNzBgg.png)

## Submission

The following section is a demo function with requests module, please refer to `tests/test_fvt.py` for advanced operation. Tag is not necessary at this part, the service will auto generate one if "tag" key not found within payload.

```python=
resp = requests.post(
    "http://localhost:5000/user/submit",
    json={"tag": YOUR_TAG, "source": YOUR_SOURCE_URL}
)
```

The response body will contains a json object, the value of "flag" key is the shortened flag.
```
{"flag": YOUR_FLAG}
```

For example:

```json=
{"flag": YV-abab}
```

## Redirection
Attach YOUR_FLAG you just obtained above to the url, visit http://localhost:5000/YOUR_FLAG and the server will redirect for you. For example:

![](https://i.imgur.com/80IuFth.png)

## Dashboard
You can also check the dashboard for all of current redirections, visit http://localhost:5000/admin/dashboard.

![](https://i.imgur.com/GSoqVNQ.png)

## Metrix
Shortener will tracking the visited times for all redirections, visit http://localhost:5000/user/metrix/YOUR_FLAG with YOUR_FLAG above. For example:

![](https://i.imgur.com/U6Sed2e.png)

# Development

## Test

- unit test
```
$ inv test.unit
```

- functional verification test (could be execute only when the server is running).
```
$ inv test.fvt
```

## Configuration

Please refer to `shortener/config.py` for advanced information.

# Contributors
- [Rain Wu](https://github.com/RainrainWu)