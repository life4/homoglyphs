pandoc --from=markdown --to=rst --output=README.rst README.md
rm dist/*.tar.gz
python3 setup.py sdist
twine upload dist/*
