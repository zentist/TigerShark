from tigershark.parsers.M837_5010_X224_A2.loops.loop_2010CA import parsed_837_2010CA
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2300 import parsed_837_2300
from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_2000C = Loop(
    "2000C",
    Properties(
        desc="Patient Hierarchical Level",
        looptype="",
        position="0010",
        repeat=">1",
        req_sit="S",
    ),
    Segment(
        "HL",
        Properties(
            desc="Patient Hierarchical Level",
            position="0010",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "HL01",
            Properties(
                desc="Hierarchical ID Number",
                req_sit="R",
                data_type=("AN", "1", "12"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "HL02",
            Properties(
                desc="Hierarchical Parent ID Number",
                req_sit="R",
                data_type=("AN", "1", "12"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "HL03",
            Properties(
                desc="Hierarchical Level Code",
                req_sit="R",
                data_type=("ID", "1", "2"),
                position=3,
                codes=["23"],
            ),
        ),
        Element(
            "HL04",
            Properties(
                desc="Hierarchical Child Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=4,
                codes=["0"],
            ),
        ),
    ),
    Segment(
        "PAT",
        Properties(
            desc="Patient Information",
            position="0070",
            repeat="1",
            req_sit="R",
            syntax="P0506 P0708",
        ),
        Element(
            "PAT01",
            Properties(
                desc="Individual Relationship Code",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=1,
                codes=["01", "19", "20", "21", "39", "40", "53", "G8"],
            ),
        ),
        Element(
            "PAT02",
            Properties(
                desc="Patient Location Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "PAT03",
            Properties(
                desc="Employment Status Code",
                req_sit="N",
                data_type=("ID", "2", "2"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "PAT04",
            Properties(
                desc="Student Status Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "PAT05",
            Properties(
                desc="Date Time Period Format Qualifier",
                req_sit="N",
                data_type=("ID", "2", "3"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "PAT06",
            Properties(
                desc="Date Time Period",
                req_sit="N",
                data_type=("AN", "1", "35"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "PAT07",
            Properties(
                desc="Unit or Basis for Measurement Code",
                req_sit="N",
                data_type=("ID", "2", "2"),
                position=7,
                codes=[],
            ),
        ),
        Element(
            "PAT08",
            Properties(
                desc="Weight",
                req_sit="N",
                data_type=("R", "1", "10"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "PAT09",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=9,
                codes=[],
            ),
        ),
    ),
    parsed_837_2010CA,
    parsed_837_2300,
)
