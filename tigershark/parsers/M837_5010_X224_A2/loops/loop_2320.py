from tigershark.parsers.M837_5010_X224_A2.loops.loop_2330A import parsed_837_2330A
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2330B import parsed_837_2330B
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2330C import parsed_837_2330C
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2330D import parsed_837_2330D
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2330E import parsed_837_2330E
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2330F import parsed_837_2330F
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2330G import parsed_837_2330G
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2330H import parsed_837_2330H
from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_2320 = Loop(
    "2320",
    Properties(
        desc="Other Subscriber Information",
        looptype="",
        position="2900",
        repeat="10",
        req_sit="S",
    ),
    Segment(
        "SBR",
        Properties(
            desc="Other Subscriber Information",
            position="2900",
            repeat="1",
            req_sit="S",
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
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=2,
                codes=["01", "18", "19", "20", "21", "39", "40", "53", "G8"],
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
    Segment(
        "CAS",
        Properties(
            desc="Claim Level Adjustments",
            position="2950",
            repeat="5",
            req_sit="S",
            syntax="L050607 C0605 C0705 L080910 C0908 C1008 L111213 C1211 C1311 L141516 C1514 C1614 L171819 C1817 C1917",
        ),
        Element(
            "CAS01",
            Properties(
                desc="Claim Adjustment Group Code",
                req_sit="R",
                data_type=("ID", "1", "2"),
                position=1,
                codes=["CO", "CR", "OA", "PI", "PR"],
            ),
        ),
        Element(
            "CAS02",
            Properties(
                desc="Claim Adjustment Reason Code",
                req_sit="R",
                data_type=("ID", "1", "5"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "CAS03",
            Properties(
                desc="Monetary Amount",
                req_sit="R",
                data_type=("R", "1", "18"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "CAS04",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "CAS05",
            Properties(
                desc="Claim Adjustment Reason Code",
                req_sit="S",
                data_type=("ID", "1", "5"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "CAS06",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "CAS07",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=7,
                codes=[],
            ),
        ),
        Element(
            "CAS08",
            Properties(
                desc="Claim Adjustment Reason Code",
                req_sit="S",
                data_type=("ID", "1", "5"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "CAS09",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=9,
                codes=[],
            ),
        ),
        Element(
            "CAS10",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=10,
                codes=[],
            ),
        ),
        Element(
            "CAS11",
            Properties(
                desc="Claim Adjustment Reason Code",
                req_sit="S",
                data_type=("ID", "1", "5"),
                position=11,
                codes=[],
            ),
        ),
        Element(
            "CAS12",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=12,
                codes=[],
            ),
        ),
        Element(
            "CAS13",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=13,
                codes=[],
            ),
        ),
        Element(
            "CAS14",
            Properties(
                desc="Claim Adjustment Reason Code",
                req_sit="S",
                data_type=("ID", "1", "5"),
                position=14,
                codes=[],
            ),
        ),
        Element(
            "CAS15",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=15,
                codes=[],
            ),
        ),
        Element(
            "CAS16",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=16,
                codes=[],
            ),
        ),
        Element(
            "CAS17",
            Properties(
                desc="Claim Adjustment Reason Code",
                req_sit="S",
                data_type=("ID", "1", "5"),
                position=17,
                codes=[],
            ),
        ),
        Element(
            "CAS18",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=18,
                codes=[],
            ),
        ),
        Element(
            "CAS19",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=19,
                codes=[],
            ),
        ),
    ),
    Segment(
        "AMT",
        Properties(
            desc="Coordination of Benefits (COB) Payer Paid Amount",
            position="3000",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "AMT01",
            Properties(
                desc="Amount Qualifier Code",
                req_sit="R",
                data_type=("ID", "1", "3"),
                position=1,
                codes=["D"],
            ),
        ),
        Element(
            "AMT02",
            Properties(
                desc="Monetary Amount",
                req_sit="R",
                data_type=("R", "1", "18"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "AMT03",
            Properties(
                desc="Credit/Debit Flag Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=3,
                codes=[],
            ),
        ),
    ),
    Segment(
        "AMT",
        Properties(
            desc="Remaining Patient Liability",
            position="3000",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "AMT01",
            Properties(
                desc="Amount Qualifier Code",
                req_sit="R",
                data_type=("ID", "1", "3"),
                position=1,
                codes=["EAF"],
            ),
        ),
        Element(
            "AMT02",
            Properties(
                desc="Monetary Amount",
                req_sit="R",
                data_type=("R", "1", "18"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "AMT03",
            Properties(
                desc="Credit/Debit Flag Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=3,
                codes=[],
            ),
        ),
    ),
    Segment(
        "AMT",
        Properties(
            desc="Coordination of Benefits (COB) Total Non-Covered Amount",
            position="3000",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "AMT01",
            Properties(
                desc="Amount Qualifier Code",
                req_sit="R",
                data_type=("ID", "1", "3"),
                position=1,
                codes=["A8"],
            ),
        ),
        Element(
            "AMT02",
            Properties(
                desc="Monetary Amount",
                req_sit="R",
                data_type=("R", "1", "18"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "AMT03",
            Properties(
                desc="Credit/Debit Flag Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=3,
                codes=[],
            ),
        ),
    ),
    Segment(
        "DMG",
        Properties(syntax="", req_sit="S", repeat="1", pos="3000", desc="Subscriber Demographic Information"),
        Element(
            "DMG01",
            Properties(
                desc="Date Time Period Format Qualifier",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=1,
                codes=["D8"],
            ),
        ),
        Element("DMG02", Properties(desc="Date Time Period", req_sit="R", data_type=("AN", "1", "35"), position=2, codes=[])),
        Element(
            "DMG03",
            Properties(desc="Gender Code", req_sit="R", data_type=("ID", "1", "1"), position=3, codes=["F", "M", "U"]),
        ),
        Element(
            "DMG04",
            Properties(desc="Marital Status Code", req_sit="N", data_type=("ID", "1", "1"), position=4, codes=[]),
        ),
        Element(
            "DMG05",
            Properties(desc="Race or Ethnicity Code", req_sit="N", data_type=("ID", "1", "1"), position=5, codes=[]),
        ),
        Element(
            "DMG06",
            Properties(desc="Citizenship Status Code", req_sit="N", data_type=("ID", "1", "2"), position=6, codes=[]),
        ),
        Element("DMG07", Properties(desc="Country Code", req_sit="N", data_type=("ID", "2", "3"), position=7, codes=[])),
        Element(
            "DMG08",
            Properties(desc="Basis of Verification Code", req_sit="N", data_type=("ID", "1", "2"), position=8, codes=[]),
        ),
        Element("DMG09", Properties(desc="Quantity", req_sit="N", data_type=("R", "1", "15"), position=9, codes=[])),
    ),
    Segment(
        "OI",
        Properties(
            desc="Other Insurance Coverage Information",
            position="3100",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "OI01",
            Properties(
                desc="Claim Filing Indicator Code",
                req_sit="N",
                data_type=("ID", "1", "2"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "OI02",
            Properties(
                desc="Claim Submission Reason Code",
                req_sit="N",
                data_type=("ID", "2", "2"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "OI03",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=3,
                codes=["N", "W", "Y"],
            ),
        ),
        Element(
            "OI04",
            Properties(
                desc="Patient Signature Source Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "OI05",
            Properties(
                desc="Provider Agreement Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "OI06",
            Properties(
                desc="Release of Information Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=6,
                codes=["I", "Y"],
            ),
        ),
    ),
    Segment(
        "MOA",
        Properties(
            desc="Outpatient Adjudication Information",
            position="3200",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "MOA01",
            Properties(
                desc="Percentage as Decimal",
                req_sit="S",
                data_type=("R", "1", "10"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "MOA02",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "MOA03",
            Properties(
                desc="Reference Identification",
                req_sit="S",
                data_type=("AN", "1", "50"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "MOA04",
            Properties(
                desc="Reference Identification",
                req_sit="S",
                data_type=("AN", "1", "50"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "MOA05",
            Properties(
                desc="Reference Identification",
                req_sit="S",
                data_type=("AN", "1", "50"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "MOA06",
            Properties(
                desc="Reference Identification",
                req_sit="S",
                data_type=("AN", "1", "50"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "MOA07",
            Properties(
                desc="Reference Identification",
                req_sit="S",
                data_type=("AN", "1", "50"),
                position=7,
                codes=[],
            ),
        ),
        Element(
            "MOA08",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "MOA09",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=9,
                codes=[],
            ),
        ),
    ),
    parsed_837_2330A,
    parsed_837_2330B,
    parsed_837_2330C,
    parsed_837_2330D,
    parsed_837_2330E,
    parsed_837_2330F,
    parsed_837_2330G,
    parsed_837_2330H,
)
