#
# Created manually based on the guide 05010x224A2
#
from tigershark.X12.parse import Element, Loop, Message, Properties, Segment

from .loops import parsed_837_1000A, parsed_837_1000B, parsed_837_2000A

parsed_837_DETAIL = Loop(
    "DETAIL",
    Properties(
        desc="Table 2 - Detail",
        looptype="wrapper",
        position="0010",
        repeat=">1",
        req_sit="R",
    ),
    parsed_837_2000A,
)
parsed_837_HEADER = Loop(
    "HEADER",
    Properties(desc="Header", looptype="wrapper", position="0110", repeat="1", req_sit="R"),
    Segment(
        "BHT",
        Properties(
            desc="Beginning of Hierarchical Transaction",
            position="0100",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "BHT01",
            Properties(
                desc="Hierarchical Structure Code",
                req_sit="R",
                data_type=("ID", "4", "4"),
                position=1,
                codes=["0019"],
            ),
        ),
        Element(
            "BHT02",
            Properties(
                desc="Transaction Set Purpose Code",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=2,
                codes=["00", "18"],
            ),
        ),
        Element(
            "BHT03",
            Properties(
                desc="Reference Identification",
                req_sit="R",
                data_type=("AN", "1", "50"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "BHT04",
            Properties(
                desc="Date",
                req_sit="R",
                data_type=("DT", "8", "8"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "BHT05",
            Properties(
                desc="Time",
                req_sit="R",
                data_type=("TM", "4", "8"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "BHT06",
            Properties(
                desc="Transaction Type Code",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=6,
                codes=["31", "CH", "RP"],
            ),
        ),
    ),
    parsed_837_1000A,
    parsed_837_1000B,
)


parsed_837_ST_LOOP = Loop(
    "ST_LOOP",
    Properties(
        desc="Transaction Set Header",
        looptype="explicit",
        position="0050",
        repeat=">1",
        req_sit="R",
    ),
    Segment(
        "ST",
        Properties(
            desc="Transaction Set Header",
            position="0050",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "ST01",
            Properties(
                desc="Transaction Set Identifier Code",
                req_sit="R",
                data_type=("ID", "3", "3"),
                position=1,
                codes=["837"],
            ),
        ),
        Element(
            "ST02",
            Properties(
                desc="Transaction Set Control Number",
                req_sit="R",
                data_type=("AN", "4", "9"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "ST03",
            Properties(
                desc="Implementation Convention Reference",
                req_sit="R",
                data_type=("AN", "1", "35"),
                position=3,
                codes=["005010X224"],
            ),
        ),
    ),
    parsed_837_HEADER,
    parsed_837_DETAIL,
    Segment(
        "SE",
        Properties(
            desc="Transaction Set Trailer",
            position="5550",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "SE01",
            Properties(
                desc="Number of Included Segments",
                req_sit="R",
                data_type=("N0", "1", "10"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "SE02",
            Properties(
                desc="Transaction Set Control Number",
                req_sit="R",
                data_type=("AN", "4", "9"),
                position=2,
                codes=[],
            ),
        ),
    ),
)
parsed_837_GS_LOOP = Loop(
    "GS_LOOP",
    Properties(
        desc="Functional Group Header",
        looptype="explicit",
        position="0200",
        repeat=">1",
        req_sit="R",
    ),
    Segment(
        "GS",
        Properties(
            desc="Functional Group Header",
            position="0100",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "GS01",
            Properties(
                desc="Functional Identifier Code",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=1,
                codes=["HC"],
            ),
        ),
        Element(
            "GS02",
            Properties(
                desc="Application Senders Code",
                req_sit="R",
                data_type=("AN", "2", "15"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "GS03",
            Properties(
                desc="Application Receiver’s Code",
                req_sit="R",
                data_type=("AN", "2", "15"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "GS04",
            Properties(
                desc="Date",
                req_sit="R",
                data_type=("DT", "8", "8"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "GS05",
            Properties(
                desc="Time",
                req_sit="R",
                data_type=("TM", "4", "8"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "GS06",
            Properties(
                desc="Group Control Number",
                req_sit="R",
                data_type=("N0", "1", "9"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "GS07",
            Properties(
                desc="Responsible Agency Code",
                req_sit="R",
                data_type=("ID", "1", "2"),
                position=7,
                codes=["X"],
            ),
        ),
        Element(
            "GS08",
            Properties(
                desc="Version / Release / Industry Identifier Code",
                req_sit="R",
                data_type=("AN", "1", "12"),
                position=8,
                codes=["005010X224"],
            ),
        ),
    ),
    parsed_837_ST_LOOP,
    Segment(
        "GE",
        Properties(
            desc="Functional Group Trailer",
            position="0300",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "GE01",
            Properties(
                desc="Number of Transaction Sets Included",
                req_sit="R",
                data_type=("N0", "1", "6"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "GE02",
            Properties(
                desc="Group Control Number",
                req_sit="R",
                data_type=("N0", "1", "9"),
                position=2,
                codes=[],
            ),
        ),
    ),
)
parsed_837_ISA_LOOP = Loop(
    "ISA_LOOP",
    Properties(
        desc="Interchange Control Header",
        looptype="explicit",
        position="0010",
        repeat=">1",
        req_sit="R",
    ),
    Segment(
        "ISA",
        Properties(
            desc="Interchange Control Header",
            position="0100",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "ISA01",
            Properties(
                desc="I01",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=1,
                codes=["00", "03"],
            ),
        ),
        Element(
            "ISA02",
            Properties(
                desc="I02",
                req_sit="R",
                data_type=("AN", "10", "10"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "ISA03",
            Properties(
                desc="I03",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=3,
                codes=["00", "01"],
            ),
        ),
        Element(
            "ISA04",
            Properties(
                desc="I04",
                req_sit="R",
                data_type=("AN", "10", "10"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "ISA05",
            Properties(
                desc="I05",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=5,
                codes=["01", "14", "20", "27", "28", "29", "30", "33", "ZZ"],
            ),
        ),
        Element(
            "ISA06",
            Properties(
                desc="I06",
                req_sit="R",
                data_type=("AN", "15", "15"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "ISA07",
            Properties(
                desc="I05",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=7,
                codes=["01", "14", "20", "27", "28", "29", "30", "33", "ZZ"],
            ),
        ),
        Element(
            "ISA08",
            Properties(
                desc="I07",
                req_sit="R",
                data_type=("AN", "15", "15"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "ISA09",
            Properties(
                desc="I08",
                req_sit="R",
                data_type=("DT", "6", "6"),
                position=9,
                codes=[],
            ),
        ),
        Element(
            "ISA10",
            Properties(
                desc="I09",
                req_sit="R",
                data_type=("TM", "4", "4"),
                position=10,
                codes=[],
            ),
        ),
        Element(
            "ISA11",
            Properties(
                desc="I65",
                req_sit="R",
                data_type=("AN", "1", "1"),
                position=11,
                codes=[],
            ),
        ),
        Element(
            "ISA12",
            Properties(
                desc="I11",
                req_sit="R",
                data_type=("ID", "5", "5"),
                position=12,
                codes=["00501"],
            ),
        ),
        Element(
            "ISA13",
            Properties(
                desc="I12",
                req_sit="R",
                data_type=("N0", "9", "9"),
                position=13,
                codes=[],
            ),
        ),
        Element(
            "ISA14",
            Properties(
                desc="I13",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=14,
                codes=["0", "1"],
            ),
        ),
        Element(
            "ISA15",
            Properties(
                desc="I14",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=15,
                codes=["P", "T"],
            ),
        ),
        Element(
            "ISA16",
            Properties(
                desc="I15",
                req_sit="R",
                data_type=("AN", "1", "1"),
                position=16,
                codes=[],
            ),
        ),
    ),
    parsed_837_GS_LOOP,
    Segment(
        "IEA",
        Properties(
            desc="Interchange Control Trailer",
            position="0300",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "IEA01",
            Properties(
                desc="I16",
                req_sit="R",
                data_type=("N0", "1", "5"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "IEA02",
            Properties(
                desc="I12",
                req_sit="R",
                data_type=("N0", "9", "9"),
                position=2,
                codes=[],
            ),
        ),
    ),
)
parsed_837 = Message(
    "837",
    Properties(desc="HIPAA Health Care Claim - Dental 005010X224A2 837"),
    parsed_837_ISA_LOOP,
)
