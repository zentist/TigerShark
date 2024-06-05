from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_1000A = Loop(
    "1000A",
    Properties(desc="Submitter Name", looptype="", position="0200", repeat="1", req_sit="R"),
    Segment(
        "NM1",
        Properties(
            desc="Submitter Name",
            position="0200",
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
                codes=["41"],
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
                req_sit="R",
                data_type=("ID", "1", "2"),
                position=8,
                codes=["46"],
            ),
        ),
        Element(
            "NM109",
            Properties(
                desc="Identification Code",
                req_sit="R",
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
        "PER",
        Properties(
            desc="Submitter EDI Contact Information",
            position="0450",
            repeat="2",
            req_sit="R",
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
