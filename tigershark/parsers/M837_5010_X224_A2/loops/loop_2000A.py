from tigershark.parsers.M837_5010_X224_A2.loops.loop_2000B import parsed_837_2000B
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2010AA import parsed_837_2010AA
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2010AB import parsed_837_2010AB
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2010AC import parsed_837_2010AC
from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_2000A = Loop(
    "2000A",
    Properties(
        desc="Billing Provider Hierarchical Level",
        looptype="",
        position="0010",
        repeat=">1",
        req_sit="R",
    ),
    Segment(
        "HL",
        Properties(
            desc="Billing Provider Hierarchical Level",
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
                req_sit="N",
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
                codes=["20"],
            ),
        ),
        Element(
            "HL04",
            Properties(
                desc="Hierarchical Child Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=4,
                codes=["1"],
            ),
        ),
    ),
    Segment(
        "PRV",
        Properties(
            desc="Billing Provider Specialty Information",
            position="0030",
            repeat="1",
            req_sit="S",
            syntax="P0203",
        ),
        Element(
            "PRV01",
            Properties(
                desc="Provider Code",
                req_sit="R",
                data_type=("ID", "1", "3"),
                position=1,
                codes=["BI"],
            ),
        ),
        Element(
            "PRV02",
            Properties(
                desc="Reference Identification Qualifier",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=2,
                codes=["PXC"],
            ),
        ),
        Element(
            "PRV03",
            Properties(
                desc="Reference Identification",
                req_sit="R",
                data_type=("AN", "1", "50"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "PRV04",
            Properties(
                desc="State or Province Code",
                req_sit="N",
                data_type=("ID", "2", "2"),
                position=4,
                codes=[],
            ),
        ),
        Composite(
            "C035",
            Properties(
                desc="Provider Specialty Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="05",
            ),
        ),
        Element(
            "PRV06",
            Properties(
                desc="Provider Organization Code",
                req_sit="N",
                data_type=("ID", "3", "3"),
                position=6,
                codes=[],
            ),
        ),
    ),
    Segment(
        "CUR",
        Properties(
            desc="Foreign Currency Information",
            position="0100",
            repeat="1",
            req_sit="S",
            syntax="C0807 C0907 L101112 C1110 C1210 L131415 C1413 C1513 L161718 C1716 C1816 L192021 C2019 C2119",
        ),
        Element(
            "CUR01",
            Properties(
                desc="Entity Identifier Code",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=1,
                codes=["85"],
            ),
        ),
        Element(
            "CUR02",
            Properties(
                desc="Currency Code",
                req_sit="R",
                data_type=("ID", "3", "3"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "CUR03",
            Properties(
                desc="Exchange Rate",
                req_sit="N",
                data_type=("R", "4", "10"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "CUR04",
            Properties(
                desc="Entity Identifier Code",
                req_sit="N",
                data_type=("ID", "2", "3"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "CUR05",
            Properties(
                desc="Currency Code",
                req_sit="N",
                data_type=("ID", "3", "3"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "CUR06",
            Properties(
                desc="Currency Market/Exchange Code",
                req_sit="N",
                data_type=("ID", "3", "3"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "CUR07",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="N",
                data_type=("ID", "3", "3"),
                position=7,
                codes=[],
            ),
        ),
        Element(
            "CUR08",
            Properties(
                desc="Date",
                req_sit="N",
                data_type=("DT", "8", "8"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "CUR09",
            Properties(
                desc="Time",
                req_sit="N",
                data_type=("TM", "4", "8"),
                position=9,
                codes=[],
            ),
        ),
        Element(
            "CUR10",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="N",
                data_type=("ID", "3", "3"),
                position=10,
                codes=[],
            ),
        ),
        Element(
            "CUR11",
            Properties(
                desc="Date",
                req_sit="N",
                data_type=("DT", "8", "8"),
                position=11,
                codes=[],
            ),
        ),
        Element(
            "CUR12",
            Properties(
                desc="Time",
                req_sit="N",
                data_type=("TM", "4", "8"),
                position=12,
                codes=[],
            ),
        ),
        Element(
            "CUR13",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="N",
                data_type=("ID", "3", "3"),
                position=13,
                codes=[],
            ),
        ),
        Element(
            "CUR14",
            Properties(
                desc="Date",
                req_sit="N",
                data_type=("DT", "8", "8"),
                position=14,
                codes=[],
            ),
        ),
        Element(
            "CUR15",
            Properties(
                desc="Time",
                req_sit="N",
                data_type=("TM", "4", "8"),
                position=15,
                codes=[],
            ),
        ),
        Element(
            "CUR16",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="N",
                data_type=("ID", "3", "3"),
                position=16,
                codes=[],
            ),
        ),
        Element(
            "CUR17",
            Properties(
                desc="Date",
                req_sit="N",
                data_type=("DT", "8", "8"),
                position=17,
                codes=[],
            ),
        ),
        Element(
            "CUR18",
            Properties(
                desc="Time",
                req_sit="N",
                data_type=("TM", "4", "8"),
                position=18,
                codes=[],
            ),
        ),
        Element(
            "CUR19",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="N",
                data_type=("ID", "3", "3"),
                position=19,
                codes=[],
            ),
        ),
        Element(
            "CUR20",
            Properties(
                desc="Date",
                req_sit="N",
                data_type=("DT", "8", "8"),
                position=20,
                codes=[],
            ),
        ),
        Element(
            "CUR21",
            Properties(
                desc="Time",
                req_sit="N",
                data_type=("TM", "4", "8"),
                position=21,
                codes=[],
            ),
        ),
    ),
    parsed_837_2010AA,
    parsed_837_2010AB,
    parsed_837_2010AC,
    parsed_837_2000B,
)
