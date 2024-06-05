from tigershark.parsers.M837_5010_X224_A2.loops.loop_2000C import parsed_837_2000C
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2010BA import parsed_837_2010BA
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2010BB import parsed_837_2010BB
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2300 import parsed_837_2300
from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_2000B = Loop(
    "2000B",
    Properties(
        desc="Subscriber Hierarchical Level",
        looptype="",
        position="0010",
        repeat=">1",
        req_sit="R",
    ),
    Segment(
        "HL",
        Properties(
            desc="Subscriber Hierarchical Level",
            position="0010",
            repeat="1",
            req_sit="R",
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
                codes=["22"],
            ),
        ),
        Element(
            "HL04",
            Properties(
                desc="Hierarchical Child Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=4,
                codes=["0", "1"],
            ),
        ),
    ),
    Segment(
        "SBR",
        Properties(
            desc="Subscriber Information",
            position="0050",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "SBR01",
            Properties(
                desc="Payer Responsibility Sequence Number Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=1,
                codes=["A", "B", "C", "D", "E", "F", "G", "H", "P", "S", "T", "U"],
            ),
        ),
        Element(
            "SBR02",
            Properties(
                desc="Individual Relationship Code",
                req_sit="S",
                data_type=("ID", "2", "2"),
                position=2,
                codes=["18"],
            ),
        ),
        Element(
            "SBR03",
            Properties(
                desc="Reference Identification",
                req_sit="S",
                data_type=("AN", "1", "50"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "SBR04",
            Properties(
                desc="Name",
                req_sit="S",
                data_type=("AN", "1", "60"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "SBR05",
            Properties(
                desc="Insurance Type Code",
                req_sit="N",
                data_type=("ID", "1", "3"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "SBR06",
            Properties(
                desc="Coordination of Benefits Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "SBR07",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=7,
                codes=[],
            ),
        ),
        Element(
            "SBR08",
            Properties(
                desc="Employment Status Code",
                req_sit="N",
                data_type=("ID", "2", "2"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "SBR09",
            Properties(
                desc="Claim Filing Indicator Code",
                req_sit="S",
                data_type=("ID", "1", "2"),
                position=9,
                codes=[
                    "11",
                    "12",
                    "13",
                    "14",
                    "15",
                    "16",
                    "17",
                    "AM",
                    "BL",
                    "CH",
                    "CI",
                    "DS",
                    "FI",
                    "HM",
                    "LM",
                    "MA",
                    "MB",
                    "MC",
                    "OF",
                    "TV",
                    "VA",
                    "WC",
                    "ZZ",
                ],
            ),
        ),
    ),
    parsed_837_2010BA,
    parsed_837_2010BB,
    parsed_837_2300,
    parsed_837_2000C,
)
