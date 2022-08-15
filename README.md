# Fork of TigerShark library

TigerShark is an X12 EDI message parser that can be tailored to
a specific partner in the health care payment ecosystem.

## Installation

```shell
python setup.py install
```

## Rolling out changes

1. Read [an article](https://www.notion.so/zentist/External-Dependencies-ee5587b0f685407d86faf19519b25df1#1e0ff803633f4572b2e2a5d944325ba1).
2. Make changes and commit.
2. Decide on a new version number, follow a [semantic versioning](https://semver.org/spec/v2.0.0.html).
3. Put a tag of a new version on the latest commit in the `master` branch. The tag should represent a new version in the
   format `vX.X.X`,
   where `X.X.X` is a version. For instance, `v1.0.0`.
4. Add all changes into `CHANGELOG.md`. Follow the instructions in the head of the file.
5. Make a push the new tag into remote repository.
6. Update the version in the dependencies for the necessary projects, e.g. zen-app. Follow [an article](https://www.notion.so/zentist/External-Dependencies-ee5587b0f685407d86faf19519b25df1#f703f94f4fc74e64842542699beb3e07).

## Manually Generating the Parsers

The `setup.py` script will install default parsers, but you might want to
generate your own, or you're fixing the generation script and need to test.
You can either convert all of the 4010 xml files in `Downloads/pyx12-1.5.0.zip`
or convert a file individually (which gives you more control over the result).

### Generating All Parsers From PyX12 archive

If you just want to generate all of the parsers, you can use the
`generate_all_parsers` script:

```shell
git clone https://github.com/azoner/pyx12.git
cd pyx12
python setup.py sdist --formats=gztar,zip
cd ../
python tools/generate_all_parsers.py pyx12/dist/pyx12-*.zip -d parsers
```

This will generate all parsers in a directory called `parsers`.

### Generating A Single Parser

You can also just create a single parser from an unzipped pyx12 source:

```shell
git clone https://github.com/azoner/pyx12.git
cd parsers
python ../tools/convertPyX12.py 835.4010.X091.A1.xml M835_4010_X091_A1.py -b ../pyx12/pyx12/map/ -n parsed_835
```

This will generate a `M835_4010_X091_A1.py` parser in your current directory.

## Usage

### Using a Parser

```python
from tigershark.parsers import M835_4010_X091_A1

m = M835_4010_X091_A1.parsed_835
with open('/Users/sbuss/remits/95567.63695.20120314.150150528.ERA.835.edi', 'r') as f:
    parsed = m.unmarshall(f.read().strip())
```

### Using a Facade

Once you have parsed an X12 file, you can build a Facade around it:

```python
from tigershark.facade.f835 import f835_4010

f = F835_4010(parsed)
```

Now you can access the segments of the X12 file in an easy and pythonic way

```python
>> > print(f.payee.zip)
94066
>> > print(f.payer.name)
United
Healthcare
>> > print(len(f.claims))
150
```

## Tests

If you are kind enough to create a facade, *please* add unit tests. To run
the tests that currently exist, run the following in the current directory.

```shell
python -m unittest discover
```

To limit tests to the `tests` directory (ignoring all tests in the `web` directory), run the following:

```shell
python -m unittest discover -s 'tests'
```

Note that if you first `cd tests` and then run the unit tests, they will fail
because the tests expect certain files to be in certain paths.
