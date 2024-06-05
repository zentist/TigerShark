from tigershark.parsers.M837_5010_X224_A2.loops.loop_2420A import parsed_837_2420A
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2420B import parsed_837_2420B
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2420C import parsed_837_2420C
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2420D import parsed_837_2420D
from tigershark.parsers.M837_5010_X224_A2.loops.loop_2430 import parsed_837_2430
from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_2400 = Loop(
    "2400",
    Properties(
        desc="Service Line Number",
        looptype="",
        position="3650",
        repeat="50",
        req_sit="R",
    ),
    Segment(
        "LX",
        Properties(
            desc="Service Line Number",
            position="3650",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "LX01",
            Properties(
                desc="Assigned Number",
                req_sit="R",
                data_type=("N0", "1", "6"),
                position=1,
                codes=[],
            ),
        ),
    ),
    Segment(
        "SV3",
        Properties(
            desc="Dental Service",
            position="3800",
            repeat="1",
            req_sit="R",
            syntax="R0102 P0405",
        ),
        Composite(
            "C003",
            Properties(
                desc="Composite Medical Procedure Identifier",
                refdes="",
                repeat="",
                req_sit="S",
                seq="01",
            ),
            Element(
                "SV301-01",
                Properties(
                    desc="Product/Service ID Qualifier",
                    req_sit="R",
                    data_type=("ID", "2", "2"),
                    position=0,
                    codes=["AD"],
                ),
            ),
            Element(
                "SV301-02",
                Properties(
                    desc="Product/Service ID",
                    req_sit="R",
                    data_type=("AN", "1", "48"),
                    position=1,
                    codes=[],
                ),
            ),
            Element(
                "SV301-03",
                Properties(
                    desc="Procedure Modifier",
                    req_sit="S",
                    data_type=("AN", "2", "2"),
                    position=2,
                    codes=[],
                ),
            ),
            Element(
                "SV301-04",
                Properties(
                    desc="Procedure Modifier",
                    req_sit="S",
                    data_type=("AN", "2", "2"),
                    position=3,
                    codes=[],
                ),
            ),
            Element(
                "SV301-05",
                Properties(
                    desc="Procedure Modifier",
                    req_sit="S",
                    data_type=("AN", "2", "2"),
                    position=4,
                    codes=[],
                ),
            ),
            Element(
                "SV301-06",
                Properties(
                    desc="Procedure Modifier",
                    req_sit="S",
                    data_type=("AN", "2", "2"),
                    position=5,
                    codes=[],
                ),
            ),
            Element(
                "SV301-07",
                Properties(
                    desc="Description",
                    req_sit="S",
                    data_type=("AN", "1", "80"),
                    position=6,
                    codes=[],
                ),
            ),
            Element(
                "SV301-08",
                Properties(
                    desc="Product/Service ID",
                    req_sit="N",
                    data_type=("AN", "1", "48"),
                    position=7,
                    codes=[],
                ),
            ),
        ),
        Element(
            "SV302",
            Properties(
                desc="Monetary Amount",
                req_sit="R",
                data_type=("R", "1", "18"),
                position=2,
                codes=[],
            ),
        ),
        Element(
            "SV303",
            Properties(
                desc="Facility Code Value",
                req_sit="S",
                data_type=("AN", "1", "2"),
                position=3,
                codes=[],
            ),
        ),
        Composite(
            "C006",
            Properties(
                desc="Composite Medical Procedure Identifier",
                refdes="",
                repeat="",
                req_sit="S",
                seq="04",
            ),
            Element(
                "SV304-01",
                Properties(
                    desc="Oral Cavity Designation Code",
                    req_sit="R",
                    data_type=("ID", "1", "3"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "SV304-02",
                Properties(
                    desc="Oral Cavity Designation Code",
                    req_sit="S",
                    data_type=("ID", "1", "3"),
                    position=1,
                    codes=[],
                ),
            ),
            Element(
                "SV304-03",
                Properties(
                    desc="Oral Cavity Designation Code",
                    req_sit="S",
                    data_type=("ID", "1", "3"),
                    position=2,
                    codes=[],
                ),
            ),
            Element(
                "SV304-04",
                Properties(
                    desc="Oral Cavity Designation Code",
                    req_sit="S",
                    data_type=("ID", "1", "3"),
                    position=2,
                    codes=[],
                ),
            ),
            Element(
                "SV304-05",
                Properties(
                    desc="Oral Cavity Designation Code",
                    req_sit="S",
                    data_type=("ID", "1", "3"),
                    position=2,
                    codes=[],
                ),
            ),
        ),
        Element(
            "SV305",
            Properties(
                desc="Prosthesis, Crown or Inlay Code",
                req_sit="S",
                data_type=("ID", "1", "1"),
                position=5,
                codes=["I", "R"],
            ),
        ),
        Element(
            "SV306",
            Properties(
                desc="Quantity",
                req_sit="S",
                data_type=("R", "1", "15"),
                position=6,
                codes=[],
            ),
        ),
        Element(
            "SV307",
            Properties(
                desc="Description",
                req_sit="N",
                data_type=("ID", "1", "80"),
                position=7,
                codes=[],
            ),
        ),
        Element(
            "SV308",
            Properties(
                desc="Copay Status Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "SV309",
            Properties(
                desc="Provider Agreement Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=8,
                codes=[],
            ),
        ),
        Element(
            "SV310",
            Properties(
                desc="Yes/No Condition or Response Code",
                req_sit="N",
                data_type=("ID", "1", "1"),
                position=8,
                codes=[],
            ),
        ),
        Composite(
            "C004",
            Properties(
                desc="Composite Medical Procedure Identifier",
                refdes="",
                repeat="",
                req_sit="S",
                seq="11",
            ),
            Element(
                "SV311-01",
                Properties(
                    desc="Diagnosis Code Pointer",
                    req_sit="R",
                    data_type=("N0", "1", "2"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "SV311-02",
                Properties(
                    desc="Diagnosis Code Pointer",
                    req_sit="S",
                    data_type=("N0", "1", "2"),
                    position=1,
                    codes=[],
                ),
            ),
            Element(
                "SV311-03",
                Properties(
                    desc="Diagnosis Code Pointer",
                    req_sit="S",
                    data_type=("N0", "1", "2"),
                    position=2,
                    codes=[],
                ),
            ),
            Element(
                "SV311-04",
                Properties(
                    desc="Diagnosis Code Pointer",
                    req_sit="S",
                    data_type=("N0", "1", "2"),
                    position=2,
                    codes=[],
                ),
            ),
        ),
    ),
    Segment(
        "TOO",
        Properties(syntax="", req_sit="S", repeat="32", pos="3820", desc="Tooth Information"),
        Element(
            "TOO01",
            Properties(
                desc="Code List Qualifier Code",
                req_sit="R",
                data_type=("ID", "1", "3"),
                position=1,
                codes=["JP"],
            ),
        ),
        Element(
            "TOO02",
            Properties(
                desc="Industry Code",
                req_sit="S",
                data_type=("AN", "1", "30"),
                position=2,
                codes=[],
            ),
        ),
        Composite(
            "C005",
            Properties(req_sit="S", refdes="", seq="03", desc="Tooth Surface"),
            Element(
                "TOO03-01",
                Properties(
                    desc="Tooth Surface Code",
                    req_sit="R",
                    data_type=("ID", "1", "2"),
                    position=0,
                    codes=["B", "D", "F", "I", "L", "M", "O"],
                ),
            ),
            Element(
                "TOO03-02",
                Properties(
                    desc="Tooth Surface Code",
                    req_sit="S",
                    data_type=("ID", "1", "2"),
                    position=1,
                    codes=["B", "D", "F", "I", "L", "M", "O"],
                ),
            ),
            Element(
                "TOO03-03",
                Properties(
                    desc="Tooth Surface Code",
                    req_sit="S",
                    data_type=("ID", "1", "2"),
                    position=2,
                    codes=["B", "D", "F", "I", "L", "M", "O"],
                ),
            ),
            Element(
                "TOO03-04",
                Properties(
                    desc="Tooth Surface Code",
                    req_sit="S",
                    data_type=("ID", "1", "2"),
                    position=3,
                    codes=["B", "D", "F", "I", "L", "M", "O"],
                ),
            ),
            Element(
                "TOO03-05",
                Properties(
                    desc="Tooth Surface Code",
                    req_sit="S",
                    data_type=("ID", "1", "2"),
                    position=4,
                    codes=["B", "D", "F", "I", "L", "M", "O"],
                ),
            ),
        ),
    ),
    Segment(
        "DTP",
        Properties(
            desc="Date - Service Date",
            position="4550",
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
            desc="Date - Prior Placement",
            position="4550",
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
            desc="Date - Appliance Placement",
            position="4550",
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
            desc="Date - Replacement",
            position="4550",
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
            desc="Date - Treatment Start",
            position="4550",
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
            desc="Date - Treatment Completion",
            position="4550",
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
        "CN1",
        Properties(
            desc="Contract Information",
            position="4650",
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
                codes=["02", "03", "04", "05", "06", "09"],
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
        "REF",
        Properties(
            desc="SERVICE PREDETERMINATION IDENTIFICATION",
            position="4700",
            repeat="5",
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
                codes=["G3"],
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
            Properties(
                desc="Reference Identifier",
                refdes="",
                repeat="",
                req_sit="S",
                seq="04",
                syntax="P0304 P0506",
            ),
            Element(
                "REF04-01",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="R",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=["2U"],
                ),
            ),
            Element(
                "REF04-02",
                Properties(
                    desc="Reference Identification",
                    req_sit="R",
                    data_type=("AN", "1", "5"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-03",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-04",
                Properties(
                    desc="Reference Identification",
                    req_sit="N",
                    data_type=("AN", "1", "50"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-05",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-06",
                Properties(
                    desc="Reference Identification",
                    req_sit="N",
                    data_type=("AN", "1", "50"),
                    position=0,
                    codes=[],
                ),
            ),
        ),
    ),
    Segment(
        "REF",
        Properties(
            desc="PRIOR AUTHORIZATION",
            position="4700",
            repeat="5",
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
            Properties(
                desc="Reference Identifier",
                refdes="",
                repeat="",
                req_sit="S",
                seq="04",
                syntax="P0304 P0506",
            ),
            Element(
                "REF04-01",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="R",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=["2U"],
                ),
            ),
            Element(
                "REF04-02",
                Properties(
                    desc="Reference Identification",
                    req_sit="R",
                    data_type=("AN", "1", "5"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-03",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-04",
                Properties(
                    desc="Reference Identification",
                    req_sit="N",
                    data_type=("AN", "1", "50"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-05",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-06",
                Properties(
                    desc="Reference Identification",
                    req_sit="N",
                    data_type=("AN", "1", "50"),
                    position=0,
                    codes=[],
                ),
            ),
        ),
    ),
    Segment(
        "REF",
        Properties(
            desc="Line Item Control Number",
            position="4700",
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
                codes=["6R"],
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
            desc="Repriced Line Item Reference Number",
            position="4700",
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
                codes=["9B"],
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
            position="4700",
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
                codes=["9D"],
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
            position="4700",
            repeat="5",
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
            Properties(
                desc="Reference Identifier",
                refdes="",
                repeat="",
                req_sit="S",
                seq="04",
                syntax="P0304 P0506",
            ),
            Element(
                "REF04-01",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="R",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=["2U"],
                ),
            ),
            Element(
                "REF04-02",
                Properties(
                    desc="Reference Identification",
                    req_sit="R",
                    data_type=("AN", "1", "5"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-03",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-04",
                Properties(
                    desc="Reference Identification",
                    req_sit="N",
                    data_type=("AN", "1", "50"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-05",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=0,
                    codes=[],
                ),
            ),
            Element(
                "REF04-06",
                Properties(
                    desc="Reference Identification",
                    req_sit="N",
                    data_type=("AN", "1", "50"),
                    position=0,
                    codes=[],
                ),
            ),
        ),
    ),
    Segment(
        "AMT",
        Properties(
            desc="Sales Tax Amount",
            position="4750",
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
                codes=["GT"],
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
        "K3",
        Properties(
            desc="File Information",
            position="4800",
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
        "HCP",
        Properties(
            desc="Line Pricing/Repricing Information",
            position="4920",
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
                req_sit="S",
                data_type=("ID", "2", "2"),
                position=9,
                codes=["ER", "HC", "HP", "IV", "WK"],
            ),
        ),
        Element(
            "HCP10",
            Properties(
                desc="Product/Service ID",
                req_sit="S",
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
    parsed_837_2420A,
    parsed_837_2420B,
    parsed_837_2420C,
    parsed_837_2420D,
    parsed_837_2430,
)
