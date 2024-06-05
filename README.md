# Fork of TigerShark library

TigerShark is an X12 EDI message parser that can be tailored to
a specific partner in the health care payment ecosystem.


Version 0.3.4
-------------

This patch cleans up the X12 271 Service Type Codes to bring them in line with current use. This patch also includes 
parsers for the 5010 versions of Professional (X222A1) and Institutional (X223A1) 837 transactions.
* Updates `enums.eligibility.service_type_codes` to include new and missing Service Type Codes
* Adds `enums.eligibility.deprecated_service_type_codes`, a tuple of service type codes that have been deprecated by 
  X12
* Adds `X12_5010_X222A1` and `X12_5010_X223A1` parsers for 837 5010 messages
* This does NOT add or update any facades related to 837 transactions (existing 837 facades only function for 4010 
  messages)
  
The `service_type_codes` dict was last updated in June 2012. Since then, 21 Service Type Codes have been added, 
7 of which have already been deprecated.

13 Service Type Codes have been deprecated by X12 (including 7 added in this patch). All 13 have been 
preserved in `service_type_codes`, as this module may be used to parse existing/old 271 responses. The 
`deprecated_service_type_codes` tuple has been added as a helper to identify which codes are considered inactive.

Note: the code `EO` ("ECHO-OSCAR") appears to have been added in error temporarily as a duplicate of `E0` 
("ECHO-ZERO") for a 4-month span in 2017. The code has been added back in on the chance it made its way into 
any production systems.

New Service Type Codes:

| Code | Label | Date Added | Date Deprecated |
| ---  | ---   | ---        | --- |
| E29 | Technical Cardiac Rehabilitation Services Component | 09/30/2012 | 07/01/2016 |
| E30 | Professional Cardiac Rehabilitation Services Component | 09/30/2012 | 07/01/2016 |
| E31 | Professional Intensive Cardiac Rehabilitation Services Component | 09/30/2012 | 07/01/2016 |
| E32 | Intensive Cardiac Rehabilitation - Technical Component | 06/02/2013 | 05/01/2017 |
| E33 | Intensive Cardiac Rehabilitation | 06/02/2013 |  |
| E34 | Pulmonary Rehabilitation - Technical Component | 06/02/2013 | 05/01/2017 |
| E35 | Pulmonary Rehabilitation - Professional Component | 06/02/2013 | 05/01/2017 |
| E36 | Convenience Care | 06/02/2013 |  |
| E37 | Telemedicine | 07/01/2015 |  |
| E38 | Pharmacist Services | 07/01/2015 |  |
| E39 | Diabetic Education | 03/01/2016 |  |
| E40 | Early Intervention | 11/01/2016 |  |
| EO | Applied Behavioral Analysis Therapy | 03/01/2017 | 07/01/2017 |
| F1 | Medical Coverage | 11/01/2015 |  |
| F2 | Social Work Coverage | 11/01/2015 |  |
| F3 | Dental Coverage | 11/01/2015 |  |
| F4 | Hearing Coverage | 11/01/2015 |  |
| F5 | Prescription Drug Coverage | 11/01/2015 |  |
| F6 | Vision Coverage | 11/01/2015 |  |
| F7 | Orthodontia Coverage | 11/01/2015 |  |
| F8 | Mental Health Coverage | 11/01/2015 |  |

More on service type codes on the [official X12 website](https://x12.org/codes/service-type-codes).
* _Note: Use the 
"Show All" filter to view current and deprecated codes (page only displays current codes by default.)_


Version 0.3.3
-------------

* Adds `in_plan_network_type` to `EligibilityOrBenefitInformation` for explicit values
* Adds `out_of_plan_network` for completion's sake
* Note that `in_plan_network`, `out_of_plan_network`, and `both_in_out_network` all return `False` when no value is set, although `None` would probably be more appropriate
* It may be more intuitive if `in_plan_network` and `out_of_plan_network` returned `True` when `both_in_out_network` is `True`, but the behavior is preserved for backwards compatibility


Version 0.3.4
-------------

This patch cleans up the X12 271 Service Type Codes to bring them in line with current use. This patch also includes 
parsers for the 5010 versions of Professional (X222A1) and Institutional (X223A1) 837 transactions.
* Updates `enums.eligibility.service_type_codes` to include new and missing Service Type Codes
* Adds `enums.eligibility.deprecated_service_type_codes`, a tuple of service type codes that have been deprecated by 
  X12
* Adds `X12_5010_X222A1` and `X12_5010_X223A1` parsers for 837 5010 messages
* This does NOT add or update any facades related to 837 transactions (existing 837 facades only function for 4010 
  messages)
  
The `service_type_codes` dict was last updated in June 2012. Since then, 21 Service Type Codes have been added, 
7 of which have already been deprecated.

13 Service Type Codes have been deprecated by X12 (including 7 added in this patch). All 13 have been 
preserved in `service_type_codes`, as this module may be used to parse existing/old 271 responses. The 
`deprecated_service_type_codes` tuple has been added as a helper to identify which codes are considered inactive.

Note: the code `EO` ("ECHO-OSCAR") appears to have been added in error temporarily as a duplicate of `E0` 
("ECHO-ZERO") for a 4-month span in 2017. The code has been added back in on the chance it made its way into 
any production systems.

New Service Type Codes:

| Code | Label | Date Added | Date Deprecated |
| ---  | ---   | ---        | --- |
| E29 | Technical Cardiac Rehabilitation Services Component | 09/30/2012 | 07/01/2016 |
| E30 | Professional Cardiac Rehabilitation Services Component | 09/30/2012 | 07/01/2016 |
| E31 | Professional Intensive Cardiac Rehabilitation Services Component | 09/30/2012 | 07/01/2016 |
| E32 | Intensive Cardiac Rehabilitation - Technical Component | 06/02/2013 | 05/01/2017 |
| E33 | Intensive Cardiac Rehabilitation | 06/02/2013 |  |
| E34 | Pulmonary Rehabilitation - Technical Component | 06/02/2013 | 05/01/2017 |
| E35 | Pulmonary Rehabilitation - Professional Component | 06/02/2013 | 05/01/2017 |
| E36 | Convenience Care | 06/02/2013 |  |
| E37 | Telemedicine | 07/01/2015 |  |
| E38 | Pharmacist Services | 07/01/2015 |  |
| E39 | Diabetic Education | 03/01/2016 |  |
| E40 | Early Intervention | 11/01/2016 |  |
| EO | Applied Behavioral Analysis Therapy | 03/01/2017 | 07/01/2017 |
| F1 | Medical Coverage | 11/01/2015 |  |
| F2 | Social Work Coverage | 11/01/2015 |  |
| F3 | Dental Coverage | 11/01/2015 |  |
| F4 | Hearing Coverage | 11/01/2015 |  |
| F5 | Prescription Drug Coverage | 11/01/2015 |  |
| F6 | Vision Coverage | 11/01/2015 |  |
| F7 | Orthodontia Coverage | 11/01/2015 |  |
| F8 | Mental Health Coverage | 11/01/2015 |  |

More on service type codes on the [official X12 website](https://x12.org/codes/service-type-codes).
* _Note: Use the 
"Show All" filter to view current and deprecated codes (page only displays current codes by default.)_


Version 0.3.3
-------------

* Adds `in_plan_network_type` to `EligibilityOrBenefitInformation` for explicit values
* Adds `out_of_plan_network` for completion's sake
* Note that `in_plan_network`, `out_of_plan_network`, and `both_in_out_network` all return `False` when no value is set, although `None` would probably be more appropriate
* It may be more intuitive if `in_plan_network` and `out_of_plan_network` returned `True` when `both_in_out_network` is `True`, but the behavior is preserved for backwards compatibility

## Installation

```shell
python setup.py install
```

## Rolling out changes

1. Read [an article](https://www.notion.so/zentist/External-Dependencies-ee5587b0f685407d86faf19519b25df1#1e0ff803633f4572b2e2a5d944325ba1).
2. Make changes and commit.
3. Decide on a new version number, follow a [semantic versioning](https://semver.org/spec/v2.0.0.html).
4. Put a tag of a new version on the latest commit in the `master` branch. The tag should represent a new version in the
   format `vX.X.X`,
   where `X.X.X` is a version. For instance, `v1.0.0`.
5. Add all changes into [CHANGELOG.md](CHANGELOG.md). Follow the instructions in the head of the file.
6. Make a push of the new tag into remote repository.
7. Update the version in the dependencies for the necessary projects, e.g. zen-app. Follow [an article](https://www.notion.so/zentist/External-Dependencies-ee5587b0f685407d86faf19519b25df1#f703f94f4fc74e64842542699beb3e07).

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
