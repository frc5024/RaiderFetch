#!/bin/bash
rm -rf dist/*
python3 setup.py sdist bdist_wheel && python3 -m twine upload dist/*
git add .
git commit --allow-empty -m "[Auto Commit] Package deployed to pip"