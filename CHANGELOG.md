# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2022-04-06

### Changed

- [ZEN-6840](https://zentist.atlassian.net/browse/ZEN-6840) Era marching improvements.
- [ZEN-11436](https://zentist.atlassian.net/browse/ZEN-11436) Fix ERA import failing.
- [ZEN-6974](https://zentist.atlassian.net/browse/ZEN-6974) Fix of CHC ERA parsing.
- Put DTM*050 in dict as received_date.
- Parse DTM*050 in SVC.

## [0.3.2] - 2020-09-14

### Added

- Support for EligibilityOrBenefitAdditionalInformation - `additional_information` property added to
  EligibilityOrBenefit to handle `III*ZZ*` segments
- Adds `place_of_service` enum for corresponding `additional_information` property
- Cleans up unittest warnings (`assertEquals` replaced with `assertEqual`)
- More descriptive and reliable `.to_dict` and `.to_json` methods.

## [0.3.1] - 2017-01-28

### Added

- `to_dict` and `to_json` helper methods. Thanks CloudCray.

## [0.3.0] - 2016-09-16

### Added

- Python 3 support, thanks Lucas Wiman!

## [0.2.9] - 2016-04-14

### Added

- Bugfix for parsing the LS loop in 5010 271.

## [0.2.8] - 2014-10-01

### Added

- Support for parsing 5010 270, 271, and 835 files.
- Support for parsing any X12 file to get ## [and transaction set information.
- Utility APIs for parsing any X12 file.

## [0.2.5] - 2012-10-16

### Added

Lots of 271 bugfixes! Several tests for 271 files have been added. A few
parsing bugs have been fixed.

A nice change is that the parser no longer crashes if there is an invalid code
in an X12 element. This was causing me nothing but grief so I disabled it.
Valid codes are only checked when there is a single valid code for a segment,
since this is important in determining loop boundaries for 271 files.

ParseErrors return a more helpful error message so tracking down a bad line
is much easier.

Important bugfix that prevents an early parser exit if an optional segment
isn't found, but later optional segments are present.

PyX12, which this project depends on, changed its project layout (in version
2.0.0), so the parser generation scripts have been updated to look in the new
directory.

## [0.2.4] - 2012-08-17

### Added

I discovered a bug that caused deductible/co-insurance/co-payments from being
summed if they occurred at the claims-level rather than the adjustments level.
This resulted in underreporting the *actual- amounts. This has been fixed and
unit tests have been added for this case.

I also made adjustments to the directory structure. Tests have been moved up
and the latest version of PyX12 was used to generate the parsers. An old PyX12
tarball is no longer included in this distribution, so instructions were
added to get PyX12 and set it up for parser generation.

## [0.2.3] - 2012-06-26

### Added

Initial support for reading 270/271 files. I'm not sure when I'll add support
for creating X12 files, since I have yet to need to do so. I haven't even
tested creating them.

SegmentAccess, SegmentSequenceAccess, and X12SegmentBridge now all work pretty
well. I didn't really like how the 835 facade was implemented so I spent more
time trying to figure out nicer ways of structuring the 270/271 facades. This
meant understanding and fixing the Segment[Sequence]Access classes. I was able
to avoid a bunch of ugly multiple inheritance tricks and mostly freed myself
from setting properties in __init__ (though not entirely, and I'm not sure
if I even want to totally remove this). I may clean up the 835 facade later,
but I didn't want to introduce any breaking changes in this version.

I am understanding TigerShark more and more as I continue implementing
things that S. Lott didn't get to, however this also means that I'm being
bitten by the complexity of the project more often. There are a lot of good
ideas in this project, and I keep encountering things I didn't expect
(non-sequential hierarchical level grouping in 271 files, wtf??). TigerShark
can handle most of these weird cases with minor bugfixes (which makes me more
confident that this design was right from the start), but I don't think
TigerShark can fully support 270/271 files due to their weird structuring.
I intend to re-write a good portion of TigerShark after implementing several
more formats, since I'll have a clear idea of the kind of requirements have
to be met.

## [0.2.2a] - 2012-05-10

### Added

Nothing big, just a bugfix to ElementSequenceAccess (so it actually works)
and moved two large enum types to an enums module.

Edit: Followup fix to allow unknown values in the enum x12 type, since it's
possible that an insurance company returns an outdated remark code.

## [0.2.1] - 2012-04-18

### Added

I realized that a single EOB file can contain multiple EOBs. This means that
the f835 facade now has a list of all of its individual EOBs as a `facades`
property.

I also fixed a few typos, added a ClaimAdjustments common X12LoopBridge with
the corresponding claim adjustment reasons as an enum x12type, and improved
the tests for 835 files.

This package is now being used in production, and the 835 facade can be
considered somewhat stable.

## [0.2] - 2012-04-05

### Added

I've added a setup.py script and organized the files a bit more. I'm
considering this a major ## [bump because the inclusion of setup.py and
pregenerated parsers makes this a *lot* closer to a fully usable package. I
make no claim that any parser other than the 835 works as expected, since I
have only dealt with 835 files so far.

Development will probably slow down now that things are mostly working. In the
pipeline are auto-generated facades, or facades for 270/271 files, whichever
I need to do first.

If this sort of thing interests you, the awesome biotech startup where I
work is hiring. I can't say much about it other than it involves genes, real
science, and we are currently saving lives and improving the future of
humanity. Do drop me a line.

(Insurance billing is a painful but necessary step in this process.)

## [0.1] - 2012-04-05

### Added

TigerShark was initially developed by [S. Lott](https://github.com/slott56),
et. al. The code was recently released at my request, after I stumbled on a
few blog posts about the project:

1. [Python as Config Language - Forget XML and INI files (Jan 12, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080111205451.html)
2. [Two Python Config-File Design Patterns (Jan 19, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080119082306.html)
3. [Configuration File Scalability - Who Knew? (Revised) (Jan 26, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080126181253.html)
4. [Python as Configuration Language - More Good Ideas (March 28, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080328172746.html)
5. [Synchronicity and Document Object Models. (March 31, 2008)](http://www.itmaybeahack.com/homepage/iblog/C465799452/E20080331113231.html)
6. [POPO and GOPS - Plain Old Python Objects and Good Old Python Syntax (April 1, 2008)](http://www.itmaybeahack.com/homepage/iblog/C412398194/E20080401060105.html)

By the time I found those posts I had been struggling with X12 files for
about two weeks, dealing with broken parsers and PDFs that cost thousands of
dollars that describe the spec over 750 pages in human - but not, or only
barely, machine - readable format. (How the healthcare industry gets away with
getting the government to mandate a proprietary file format which you have to
pay to read is the subject of another rant...).

I was struck by the amount of good, deep thought that went into the decisions
S. Lott made, especially as compared to everything else I had seen. If you
want to contribute to this project, I highly encourage you to go read those
posts first.

What you see in version 0.1 is a series of hacks to get TigerShark working.
I fixed a few bugs, added a facade for 835 files, and added setup instructions
to the readme. The facade code is a mess (I didn't have enough time to fully
understand the descriptor pattern and all of the underlying data structures
Steven used), and I'll have to come back and make it nicer. Ultimately the
facade should be able to be generated straight from the xml files which are
used to build the parser. I removed a bunch of files that didn't appear to
be used anywhere. I didn't try to get the demo django site working, and I'll
either remove it or add instructions for it in a later version.

Many thanks to [S. Lott](https://github.com/slott56) for releasing the code
and answering my questions, and to [John Holland](https://github.com/azoner)
for providing the xml files in his package [pyX12](https://github.com/azoner/pyx12).