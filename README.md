# RaiderFetch
[![PyPI version](https://badge.fury.io/py/RaiderFetch.svg)](https://badge.fury.io/py/RaiderFetch) [![CodeFactor](https://www.codefactor.io/repository/github/frc5024/raiderfetch/badge)](https://www.codefactor.io/repository/github/frc5024/raiderfetch)
A python3 library for getting information about the team.

## Installation
To install this library, either use pip:
```sh
python3 -m pip install RaiderFetch
```
or, use setuptools:
```sh
python3 setup.py install
```

## Usage
This is the recommended usage for the library

### Import the library
First, import the library
```python3
import RaiderFetch as rf
```

### Create a fetcher
All of your work will be done through a fetcher class.
```python3
fetcher = rf.Fetcher()
```

A string of another account name can also be passed into the constructor. For example:
```python3
fetcher = rf.Fetcher("team254")
```

### Calling the api
For maximum control over the library, fetching data from the API is done manually. Nothing is returned by this function.
```python3
fetcher.fetch()
```

### Get the activity feed
To get info from GitHub about the team's activity, use this function.
```python3
fetcher.getFeed()
```

### Get a list of team members
To get a list of all current programming team members, use this function. Accounts marked as private will not be shown.

(NOTE: Team captains should have all members set their account to public)
```python3
fetcher.getMembers()
```

### Check if an account is a member of the team
To check if someone is a member of this team, pass their username into this function. A bool is returnewd by this function.
```python3
fetcher.isMember("username")
```

### Get a list of repos
To get a list of all public repos, along with some info about them, use:
```python3
fetcher.getRepos()
```