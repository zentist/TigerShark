from tigershark.parsers.M837_5010_X224_A2.loops.loop_2310A import parsed_837_2310A
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2310B import parsed_837_2310B
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2310C import parsed_837_2310C
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2310D import parsed_837_2310D
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2310E import parsed_837_2310E
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2320 import parsed_837_2320
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2400 import parsed_837_2400
from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_2300 = Loop(
    "2300",
    Properties(
        desc="Claim Information",
        looptype="",
        position="1300",
        repeat="100",
        req_sit="R",
    ),
    Segment(
        "CLM",
        Properties(
            desc="Claim Information",
            position="1300",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "CLM01",
            Properties(
                desc="Claim Submitter's Identifier",
                req_sit="R",
                data_type=("AN", "1", "38"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "CLM02",
            Properties(
                desc="Monetary Amount",
                req_sit="R",
                data_type=("R", "1", "18"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "CLM03",
            Properties(
                desc="Claim Filing Indicator Code",
                req_sit="N",
                data_type=("ID", "1", "2"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "CLM04",
            Properties(
                desc="Non-Institutional Claim Type Code",
                req_sit="N",
                data_type=("ID", "1", "2"),
                position=4,
                codes=[],
            ),
        ),
        Composite(
            "C023",
            Properties(
                desc="Health Care Service Location Information",
                refdes="",
                repeat="",
                req_sit="R",
                seq="05",
            ),
            Element(
                "CLM05-01",
                Properties(
                    desc="Facility Code Value",
                    req_sit="R",
                    data_type=("AN", "1", "2"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "CLM05-02",
                Properties(
                    desc="Facility Code Qualifier",
                    req_sit="R",
                    data_type=("ID", "1", "2"),
                    position=1,
                    codes=["B"],
                ),
            ),
            Element(
                "CLM05-03",
                Properties(
                    desc="Claim Frequency Type Code",
                    req_sit="R",
                    data_type=("ID", "1", "1"),
                    position=2,
                    codes=[],
                ),
            ),
        ),
        Element(
            "CLM06",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=6,
                codes=["Y", "N"],
            ),
        ),
        Element(
            "CLM07",
            Properties(
                desc="Provider Accept Assignment Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=7,
                codes=["A", "C"],
            ),
        ),
        Element(
            "CLM08",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=8,
                codes=["N", "W", "Y"],
            ),
        ),
        Element(
            "CLM09",
            Properties(
                desc="Release of Information Code",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=9,
                codes=["I", "Y"],
            ),
        ),
        Element(
            "CLM10",
            Properties(
                desc="Patient Signature Source Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=10,
                codes=[],
            ),
        ),
        Composite(
            "C024",
            Properties(
                desc="Related Causes Information",
                refdes="",
                repeat="",
                req_sit="S",
                seq="11",
            ),
            Element(
                "CLM11-01",
                Properties(
                    desc="Related-Causes Code",
                    req_sit="R",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=["AA", "EM", "OA"],
                ),
            ),
            Element(
                "CLM11-02",
                Properties(
                    desc="Related-Causes Code",
                    req_sit="S",
                    data_type=("ID", "2", "3"),
                    position=1,
                    codes=[],
                ),
            ),
            Element(
                "CLM11-03",
                Properties(
                    desc="Related-Causes Code",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=1,
                    codes=[],
                ),
            ),
            Element(
                "CLM11-04",
                Properties(
                    desc="State or Province Code",
                    req_sit="S",
                    data_type=("ID", "2", "3"),
                    position=1,
                    codes=[],
                ),
            ),
            Element(
                "CLM11-05",
                Properties(
                    desc="Country Code",
                    req_sit="S",
                    data_type=("ID", "2", "3"),
                    position=4,
                    codes=[],
                ),
            ),
        ),
        Element(
            "CLM12",
            Properties(
                desc="Special Program Code",
                req_sit="S",
                data_type=("ID", "2", "3"),
                position=12,
                codes=["01", "02", "03", "05"],
            ),
        ),
        Element(
            "CLM13",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=13,
                codes=[],
            ),
        ),
        Element(
            "CLM14",
            Properties(
                desc="Level of Service Code",
                req_sit="N",
                data_type=("ID", "1", "3"),
                position=14,
                codes=[],
            ),
        ),
        Element(
            "CLM15",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=15,
                codes=[],
            ),
        ),
        Element(
            "CLM16",
            Properties(
                desc="Provider Agreement Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=16,
                codes=[],
            ),
        ),
        Element(
            "CLM17",
            Properties(
                desc="Claim Status Code",
                req_sit="N",
                data_type=("ID", "1", "2"),
                position=17,
                codes=[],
            ),
        ),
        Element(
            "CLM18",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=18,
                codes=[],
            ),
        ),
        Element(
            "CLM19",
            Properties(
                desc="Claim Submission Reason Code",
                req_sit="S",
                data_type=("ID", "2", "2"),
                position=19,
                codes=["PB"],
            ),
        ),
        Element(
            "CLM20",
            Properties(
                desc="Delay Reason Code",
                req_sit="S",
                data_type=("ID", "1", "2"),
                position=20,
                codes=["1", "10", "11", "15", "2", "3", "4", "5", "6", "7", "8", "9"],
            ),
        ),
    ),
    Segment(
        "DTP",
        Properties(desc="Accident Date", position="1350", repeat="1", req_sit="S", syntax=""),
        Element(
            "DTP01",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="R",
                data_type=("ID", "3", "3"),
                position=1,
                codes=["439"],
            ),
        ),
        Element(
            "DTP02",
            Properties(
                desc="Date Time Period Format Qualifier",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=2,
                codes=["D8"],
            ),
        ),
        Element(
            "DTP03",
            Properties(
                desc="Date Time Period",
                req_sit="R",
                data_type=("AN", "1", "35"),
                position=3,
                codes=[],
            ),
        ),
    ),
    Segment(
        "DTP",
        Properties(
            desc="Appliance Placement Date",
            position="1350",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "DTP01",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="R",
                data_type=("ID", "3", "3"),
                position=1,
                codes=["452"],
            ),
        ),
        Element(
            "DTP02",
            Properties(
                desc="Date Time Period Format Qualifier",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=2,
                codes=["D8"],
            ),
        ),
        Element(
            "DTP03",
            Properties(
                desc="Date Time Period",
                req_sit="R",
                data_type=("AN", "1", "35"),
                position=3,
                codes=[],
            ),
        ),
    ),
    Segment(
        "DTP",
        Properties(desc="Service Date", position="1350", repeat="1", req_sit="S", syntax=""),
        Element(
            "DTP01",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="R",
                data_type=("ID", "3", "3"),
                position=1,
                codes=["472"],
            ),
        ),
        Element(
            "DTP02",
            Properties(
                desc="Date Time Period Format Qualifier",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=2,
                codes=["D8", "RD8"],
            ),
        ),
        Element(
            "DTP03",
            Properties(
                desc="Date Time Period",
                req_sit="R",
                data_type=("AN", "1", "35"),
                position=3,
                codes=[],
            ),
        ),
    ),
    Segment(
        "DTP",
        Properties(
            desc="Repricer Received Date",
            position="1350",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "DTP01",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="R",
                data_type=("ID", "3", "3"),
                position=1,
                codes=["050"],
            ),
        ),
        Element(
            "DTP02",
            Properties(
                desc="Date Time Period Format Qualifier",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=2,
                codes=["D8"],
            ),
        ),
        Element(
            "DTP03",
            Properties(
                desc="Date Time Period",
                req_sit="R",
                data_type=("AN", "1", "35"),
                position=3,
                codes=[],
            ),
        ),
    ),
    Segment(
        "DN1",
        Properties(
            desc="ORTHODONTIC TOTAL MONTHS OF TREATMENT",
            position="1450",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "DN101",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "DN102",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "DN103",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "DN104",
            Properties(
                desc="Description",
                req_sit="S",
                data_type=("AN", "1", "80"),
                position=4,
                codes=[],
            ),
        ),
    ),
    Segment(
        "DN2",
        Properties(
            desc="Tooth Status",
            position="1500",
            repeat="35",
            req_sit="S",
            syntax="P0405",
        ),
        Element(
            "DN201",
            Properties(
                desc="Reference Identification",
                req_sit="R",
                data_type=("AN", "1", "50"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "DN202",
            Properties(
                desc="Tooth Status Code",
                req_sit="R",
                data_type=("ID", "1", "2"),
                position=2,
                codes=["E", "M"],
            ),
        ),
        Element(
            "DN203",
            Properties(
                desc="Quantity",
                req_sit="N",
                data_type=("R", "1", "15"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "DN204",
            Properties(
                desc="Date Time Period Format Qualifier",
                req_sit="N",
                data_type=("ID", "2", "3"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "DN205",
            Properties(
                desc="Date Time Period",
                req_sit="N",
                data_type=("AN", "1", "35"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "DN206",
            Properties(
                desc="Code List Qualifier Code",
                req_sit="N",
                data_type=("ID", "1", "3"),
                position=6,
                codes=[],
            ),
        ),
    ),
    Segment(
        "PWK",
        Properties(
            desc="Claim Supplemental Information",
            position="1550",
            repeat="10",
            req_sit="S",
            syntax="P0506",
        ),
        Element(
            "PWK01",
            Properties(
                desc="Report Type Code",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=1,
                codes=[
                    "B4",
                    "DA",
                    "DG",
                    "EB",
                    "OZ",
                    "P6",
                    "RB",
                    "RR",
                ],
            ),
        ),
        Element(
            "PWK02",
            Properties(
                desc="Report Transmission Code",
                req_sit="R",
                data_type=("ID", "1", "2"),
                position=2,
                codes=["AA", "BM", "EL", "EM", "FT", "FX"],
            ),
        ),
        Element(
            "PWK03",
            Properties(
                desc="Report Copies Needed",
                req_sit="N",
                data_type=("N0", "1", "2"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "PWK04",
            Properties(
                desc="Entity Identifier Code",
                req_sit="N",
                data_type=("ID", "2", "3"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "PWK05",
            Properties(
                desc="Identification Code Qualifier",
                req_sit="S",
                data_type=("ID", "1", "2"),
                position=5,
                codes=["AC"],
            ),
        ),
        Element(
            "PWK06",
            Properties(
                desc="Identification Code",
                req_sit="S",
                data_type=("AN", "2", "80"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "PWK07",
            Properties(
                desc="Description",
                req_sit="N",
                data_type=("AN", "1", "80"),
                position=7,
                codes=[],
            ),
        ),
        Composite(
            "C002",
            Properties(desc="Actions Indicated", refdes="", repeat="", req_sit="N", seq="08"),
        ),
        Element(
            "PWK09",
            Properties(
                desc="Request Category Code",
                req_sit="N",
                data_type=("ID", "1", "2"),
                position=9,
                codes=[],
            ),
        ),
    ),
    Segment(
        "CN1",
        Properties(
            desc="Contract Information",
            position="1600",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "CN101",
            Properties(
                desc="Contract Type Code",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=1,
                codes=["01", "02", "03", "04", "05", "06", "09"],
            ),
        ),
        Element(
            "CN102",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "CN103",
            Properties(
                desc="Percent, Decimal Format",
                req_sit="S",
                data_type=("R", "1", "6"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "CN104",
            Properties(
                desc="Reference Identification",
                req_sit="S",
                data_type=("AN", "1", "50"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "CN105",
            Properties(
                desc="Terms Discount Percent",
                req_sit="S",
                data_type=("R", "1", "6"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "CN106",
            Properties(
                desc="Version Identifier",
                req_sit="S",
                data_type=("AN", "1", "30"),
                position=6,
                codes=[],
            ),
        ),
    ),
    Segment(
        "AMT",
        Properties(
            desc="Patient Amount Paid",
            position="1750",
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
                codes=["F3"],
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
        "REF",
        Properties(
            desc="Predetermination Identification",
            position="1800",
            repeat="1",
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
                codes=["P4"],
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
            desc="Service Authorization Exception Code",
            position="1800",
            repeat="1",
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
                codes=["4N"],
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
            desc="Payer Claim Control Number",
            position="1800",
            repeat="1",
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
                codes=["F8"],
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
            desc="Referral Number",
            position="1800",
            repeat="1",
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
                codes=["9F"],
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
            desc="Prior Authorization",
            position="1800",
            repeat="1",
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
                codes=["G1"],
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
            desc="Repriced Claim Number",
            position="1800",
            repeat="1",
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
                codes=["9A"],
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
            desc="Adjusted Repriced Claim Number",
            position="1800",
            repeat="1",
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
                codes=["9C"],
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
            desc="Claim Identifier For Transmission Intermediaries",
            position="1800",
            repeat="1",
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
                codes=["D9"],
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
        "K3",
        Properties(
            desc="File Information",
            position="1850",
            repeat="10",
            req_sit="S",
            syntax="",
        ),
        Element(
            "K301",
            Properties(
                desc="Fixed Format Information",
                req_sit="R",
                data_type=("AN", "1", "80"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "K302",
            Properties(
                desc="Record Format Code",
                req_sit="N",
                data_type=("ID", "1", "2"),
                position=2,
                codes=[],
            ),
        ),
        Composite(
            "C001",
            Properties(
                desc="Composite Unit of Measure",
                refdes="",
                repeat="",
                req_sit="N",
                seq="03",
            ),
        ),
    ),
    Segment(
        "NTE",
        Properties(desc="Claim Note", position="1900", repeat="5", req_sit="S", syntax=""),
        Element(
            "NTE01",
            Properties(
                desc="Note Reference Code",
                req_sit="R",
                data_type=("ID", "3", "3"),
                position=1,
                codes=[
                    "ALG",
                    "DCP",
                    "DGN",
                    "DME",
                    "MED",
                    "NTR",
                    "ODT",
                    "RHB",
                    "RLH",
                    "RNH",
                    "SET",
                    "SFM",
                    "SPT",
                    "UPI",
                ],
            ),
        ),
        Element(
            "NTE02",
            Properties(
                desc="Description",
                req_sit="R",
                data_type=("AN", "1", "80"),
                position=2,
                codes=[],
            ),
        ),
    ),
    Segment(
        "HI",
        Properties(
            desc="Health Care Diagnosis Code",
            position="2310",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="R",
                seq="01",
            ),
            Element(
                "HI01-01",
                Properties(
                    desc="Code List Qualifier Code",
                    req_sit="R",
                    data_type=("ID", "1", "3"),
                    position=0,
                    codes=["ABK", "BK"],
                ),
            ),
            Element(
                "HI01-02",
                Properties(
                    desc="Industry Code",
                    req_sit="R",
                    data_type=("AN", "1", "30"),
                    position=1,
                    codes=[],
                ),
            ),
            Element(
                "HI01-03",
                Properties(
                    desc="Date Time Period Format Qualifier",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=2,
                    codes=[],
                ),
            ),
            Element(
                "HI01-04",
                Properties(
                    desc="Date Time Period",
                    req_sit="N",
                    data_type=("AN", "1", "35"),
                    position=3,
                    codes=[],
                ),
            ),
            Element(
                "HI01-05",
                Properties(
                    desc="Monetary Amount",
                    req_sit="N",
                    data_type=("R", "1", "18"),
                    position=4,
                    codes=[],
                ),
            ),
            Element(
                "HI01-06",
                Properties(
                    desc="Quantity",
                    req_sit="N",
                    data_type=("R", "1", "15"),
                    position=5,
                    codes=[],
                ),
            ),
            Element(
                "HI01-07",
                Properties(
                    desc="Version Identifier",
                    req_sit="N",
                    data_type=("AN", "1", "30"),
                    position=6,
                    codes=[],
                ),
            ),
            Element(
                "HI01-08",
                Properties(
                    desc="Industry Code",
                    req_sit="N",
                    data_type=("AN", "1", "30"),
                    position=7,
                    codes=[],
                ),
            ),
            Element(
                "HI01-09",
                Properties(
                    desc="Yes/No Condition or Response Code",
                    req_sit="S",
                    data_type=("ID", "1", "1"),
                    position=8,
                    codes=["N", "U", "W", "Y"],
                ),
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="02",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="03",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="04",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="05",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="06",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="07",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="08",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="09",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="10",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="11",
            ),
        ),
        Composite(
            "C022",
            Properties(
                desc="Health Care Code Information",
                refdes="",
                repeat="",
                req_sit="N",
                seq="12",
            ),
        ),
    ),
    Segment(
        "HCP",
        Properties(
            desc="Claim Pricing/Repricing Information",
            position="2410",
            repeat="1",
            req_sit="S",
            syntax="R0113 P0910 P1112",
        ),
        Element(
            "HCP01",
            Properties(
                desc="Pricing Methodology",
                req_sit="R",
                data_type=("ID", "2", "2"),
                position=1,
                codes=[
                    "00",
                    "01",
                    "02",
                    "03",
                    "04",
                    "05",
                    "06",
                    "07",
                    "08",
                    "09",
                    "10",
                    "11",
                    "12",
                    "13",
                    "14",
                ],
            ),
        ),
        Element(
            "HCP02",
            Properties(
                desc="Monetary Amount",
                req_sit="R",
                data_type=("R", "1", "18"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "HCP03",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=3,
                codes=[],
            ),
        ),
        Element(
            "HCP04",
            Properties(
                desc="Reference Identification",
                req_sit="S",
                data_type=("AN", "1", "50"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "HCP05",
            Properties(
                desc="Rate",
                req_sit="S",
                data_type=("R", "1", "9"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "HCP06",
            Properties(
                desc="Reference Identification",
                req_sit="S",
                data_type=("AN", "1", "50"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "HCP07",
            Properties(
                desc="Monetary Amount",
                req_sit="S",
                data_type=("R", "1", "18"),
                position=7,
                codes=[],
            ),
        ),
        Element(
            "HCP08",
            Properties(
                desc="Product/Service ID",
                req_sit="S",
                data_type=("AN", "1", "48"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "HCP09",
            Properties(
                desc="Product/Service ID Qualifier",
                req_sit="N",
                data_type=("ID", "2", "2"),
                position=9,
                codes=[],
            ),
        ),
        Element(
            "HCP10",
            Properties(
                desc="Product/Service ID",
                req_sit="N",
                data_type=("AN", "1", "48"),
                position=10,
                codes=[],
            ),
        ),
        Element(
            "HCP11",
            Properties(
                desc="Unit or Basis for Measurement Code",
                req_sit="S",
                data_type=("ID", "2", "2"),
                position=11,
                codes=["DA", "UN"],
            ),
        ),
        Element(
            "HCP12",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=12,
                codes=[],
            ),
        ),
        Element(
            "HCP13",
            Properties(
                desc="Reject Reason Code",
                req_sit="S",
                data_type=("ID", "2", "2"),
                position=13,
                codes=["T1", "T2", "T3", "T4", "T5", "T6"],
            ),
        ),
        Element(
            "HCP14",
            Properties(
                desc="Policy Compliance Code",
                req_sit="S",
                data_type=("ID", "1", "2"),
                position=14,
                codes=["1", "2", "3", "4", "5"],
            ),
        ),
        Element(
            "HCP15",
            Properties(
                desc="Exception Code",
                req_sit="S",
                data_type=("ID", "1", "2"),
                position=15,
                codes=["1", "2", "3", "4", "5", "6"],
            ),
        ),
    ),
    parsed_837_2310A,
    parsed_837_2310B,
    parsed_837_2310C,
    parsed_837_2310D,
    parsed_837_2310E,
    parsed_837_2320,
    parsed_837_2400,
)
