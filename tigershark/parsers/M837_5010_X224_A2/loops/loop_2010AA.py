from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_2010AA = Loop(
    "2010AA",
    Properties(
        desc="Billing Provider Name",
        looptype="",
        position="0150",
        repeat="1",
        req_sit="R",
    ),
    Segment(
        "NM1",
        Properties(
            desc="Billing Provider Name",
            position="0150",
            repeat="1",
            req_sit="R",
            syntax="P0809 C1110 C1203",
        ),
        Element(
            "NM101",
            Properties(
                desc="Entity Identifier Code",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=1,
                codes=["85"],
            ),
        ),
        Element(
            "NM102",
            Properties(
                desc="Entity Type Qualifier",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=2,
                codes=["1", "2"],
            ),
        ),
        Element(
            "NM103",
            Properties(
                desc="Name Last or Organization Name",
                req_sit="R",
                data_type=("AN", "1", "60"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "NM104",
            Properties(
                desc="Name First",
                req_sit="S",
                data_type=("AN", "1", "35"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "NM105",
            Properties(
                desc="Name Middle",
                req_sit="S",
                data_type=("AN", "1", "25"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "NM106",
            Properties(
                desc="Name Prefix",
                req_sit="N",
                data_type=("AN", "1", "10"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "NM107",
            Properties(
                desc="Name Suffix",
                req_sit="N",
                data_type=("AN", "1", "10"),
                position=7,
                codes=[],
            ),
        ),
        Element(
            "NM108",
            Properties(
                desc="Identification Code Qualifier",
                req_sit="S",
                data_type=("ID", "1", "2"),
                position=8,
                codes=["XX"],
            ),
        ),
        Element(
            "NM109",
            Properties(
                desc="Identification Code",
                req_sit="S",
                data_type=("AN", "2", "80"),
                position=9,
                codes=[],
            ),
        ),
        Element(
            "NM110",
            Properties(
                desc="Entity Relationship Code",
                req_sit="N",
                data_type=("ID", "2", "2"),
                position=10,
                codes=[],
            ),
        ),
        Element(
            "NM111",
            Properties(
                desc="Entity Identifier Code",
                req_sit="N",
                data_type=("ID", "2", "3"),
                position=11,
                codes=[],
            ),
        ),
        Element(
            "NM112",
            Properties(
                desc="Name Last or Organization Name",
                req_sit="N",
                data_type=("AN", "1", "60"),
                position=12,
                codes=[],
            ),
        ),
    ),
    Segment(
        "N3",
        Properties(
            desc="Billing Provider Address",
            position="0250",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "N301",
            Properties(
                desc="Address Information",
                req_sit="R",
                data_type=("AN", "1", "55"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "N302",
            Properties(
                desc="Address Information",
                req_sit="S",
                data_type=("AN", "1", "55"),
                position=2,
                codes=[],
            ),
        ),
    ),
    Segment(
        "N4",
        Properties(
            desc="Billing Provider City, State, ZIP Code",
            position="0300",
            repeat="1",
            req_sit="R",
            syntax="E0207 C0605 C0704",
        ),
        Element(
            "N401",
            Properties(
                desc="City Name",
                req_sit="R",
                data_type=("AN", "2", "30"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "N402",
            Properties(
                desc="State or Province Code",
                req_sit="S",
                data_type=("ID", "2", "2"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "N403",
            Properties(
                desc="Postal Code",
                req_sit="S",
                data_type=("ID", "3", "15"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "N404",
            Properties(
                desc="Country Code",
                req_sit="S",
                data_type=("ID", "2", "3"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "N405",
            Properties(
                desc="Location Qualifier",
                req_sit="N",
                data_type=("ID", "1", "2"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "N406",
            Properties(
                desc="Location Identifier",
                req_sit="N",
                data_type=("AN", "1", "30"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "N407",
            Properties(
                desc="Country Subdivision Code",
                req_sit="S",
                data_type=("ID", "1", "3"),
                position=7,
                codes=[],
            ),
        ),
    ),
    Segment(
        "REF",
        Properties(
            desc="Billing Provider Tax Identification",
            position="0350",
            repeat="1",
            req_sit="R",
            syntax="R0203",
        ),
        Element(
            "REF01",
            Properties(
                desc="Reference Identification Qualifier",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=1,
                codes=["EI", "SY"],
            ),
        ),
        Element(
            "REF02",
            Properties(
                desc="Reference Identification",
                req_sit="R",
                data_type=("AN", "1", "50"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "REF03",
            Properties(
                desc="Description",
                req_sit="N",
                data_type=("AN", "1", "80"),
                position=3,
                codes=[],
            ),
        ),
        Composite(
            "C040",
            Properties(desc="Reference Identifier", refdes="", repeat="", req_sit="N", seq="04"),
        ),
    ),
    Segment(
        "REF",
        Properties(
            desc="Billing Provider UPIN/License Information",
            position="0350",
            repeat="2",
            req_sit="S",
            syntax="R0203",
        ),
        Element(
            "REF01",
            Properties(
                desc="Reference Identification Qualifier",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=1,
                codes=["0B", "1G"],
            ),
        ),
        Element(
            "REF02",
            Properties(
                desc="Reference Identification",
                req_sit="R",
                data_type=("AN", "1", "50"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "REF03",
            Properties(
                desc="Description",
                req_sit="N",
                data_type=("AN", "1", "80"),
                position=3,
                codes=[],
            ),
        ),
        Composite(
            "C040",
            Properties(desc="Reference Identifier", refdes="", repeat="", req_sit="N", seq="04"),
        ),
    ),
    Segment(
        "PER",
        Properties(
            desc="Billing Provider Contact Information",
            position="0400",
            repeat="2",
            req_sit="S",
            syntax="P0304 P0506 P0708",
        ),
        Element(
            "PER01",
            Properties(
                desc="Contact Function Code",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=1,
                codes=["IC"],
            ),
        ),
        Element(
            "PER02",
            Properties(
                desc="Name",
                req_sit="S",
                data_type=("AN", "1", "60"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "PER03",
            Properties(
                desc="Communication Number Qualifier",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=3,
                codes=["EM", "FX", "TE"],
            ),
        ),
        Element(
            "PER04",
            Properties(
                desc="Communication Number",
                req_sit="R",
                data_type=("AN", "1", "256"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "PER05",
            Properties(
                desc="Communication Number Qualifier",
                req_sit="S",
                data_type=("ID", "2", "2"),
                position=5,
                codes=["EM", "EX", "FX", "TE"],
            ),
        ),
        Element(
            "PER06",
            Properties(
                desc="Communication Number",
                req_sit="S",
                data_type=("AN", "1", "256"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "PER07",
            Properties(
                desc="Communication Number Qualifier",
                req_sit="S",
                data_type=("ID", "2", "2"),
                position=7,
                codes=["EM", "EX", "FX", "TE"],
            ),
        ),
        Element(
            "PER08",
            Properties(
                desc="Communication Number",
                req_sit="S",
                data_type=("AN", "1", "256"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "PER09",
            Properties(
                desc="Contact Inquiry Reference",
                req_sit="N",
                data_type=("AN", "1", "20"),
                position=9,
                codes=[],
            ),
        ),
    ),
)
