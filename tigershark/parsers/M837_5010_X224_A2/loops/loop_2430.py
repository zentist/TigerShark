from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_2430 = Loop(
    "2430",
    Properties(
        desc="Line Adjudication Information",
        looptype="",
        position="5400",
        repeat="15",
        req_sit="S",
    ),
    Segment(
        "SVD",
        Properties(
            desc="Line Adjudication Information",
            position="5400",
            repeat="1",
            req_sit="S",
            syntax="",
        ),
        Element(
            "SVD01",
            Properties(
                desc="Identification Code",
                req_sit="R",
                data_type=("AN", "2", "80"),
                position=1,
                codes=[],
            ),
        ),
        Element(
            "SVD02",
            Properties(
                desc="Monetary Amount",
                req_sit="R",
                data_type=("R", "1", "18"),
                position=2,
                codes=[],
            ),
        ),
        Composite(
            "C003",
            Properties(
                desc="Composite Medical Procedure Identifier",
                refdes="",
                repeat="",
                req_sit="S",
                seq="03",
            ),
            Element(
                "SVD03-01",
                Properties(
                    desc="Product/Service ID Qualifier",
                    req_sit="R",
                    data_type=("ID", "2", "2"),
                    position=0,
                    codes=["ER", "HC", "HP", "IV", "WK"],
                ),
            ),
            Element(
                "SVD03-02",
                Properties(
                    desc="Product/Service ID",
                    req_sit="R",
                    data_type=("AN", "1", "48"),
                    position=1,
                    codes=[],
                ),
            ),
            Element(
                "SVD03-03",
                Properties(
                    desc="Procedure Modifier",
                    req_sit="S",
                    data_type=("AN", "2", "2"),
                    position=2,
                    codes=[],
                ),
            ),
            Element(
                "SVD03-04",
                Properties(
                    desc="Procedure Modifier",
                    req_sit="S",
                    data_type=("AN", "2", "2"),
                    position=3,
                    codes=[],
                ),
            ),
            Element(
                "SVD03-05",
                Properties(
                    desc="Procedure Modifier",
                    req_sit="S",
                    data_type=("AN", "2", "2"),
                    position=4,
                    codes=[],
                ),
            ),
            Element(
                "SVD03-06",
                Properties(
                    desc="Procedure Modifier",
                    req_sit="S",
                    data_type=("AN", "2", "2"),
                    position=5,
                    codes=[],
                ),
            ),
            Element(
                "SVD03-07",
                Properties(
                    desc="Description",
                    req_sit="S",
                    data_type=("AN", "1", "80"),
                    position=6,
                    codes=[],
                ),
            ),
            Element(
                "SVD03-08",
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
            "SVD04",
            Properties(
                desc="Product/Service ID",
                req_sit="R",
                data_type=("AN", "1", "48"),
                position=4,
                codes=[],
            ),
        ),
        Element(
            "SVD05",
            Properties(
                desc="Quantity",
                req_sit="R",
                data_type=("R", "1", "15"),
                position=5,
                codes=[],
            ),
        ),
        Element(
            "SVD06",
            Properties(
                desc="Assigned Number",
                req_sit="S",
                data_type=("N0", "1", "6"),
                position=6,
                codes=[],
            ),
        ),
    ),
    Segment(
        "CAS",
        Properties(
            desc="Line Adjustment",
            position="5450",
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
        "DTP",
        Properties(
            desc="Line Check or Remittance Date",
            position="5500",
            repeat="1",
            req_sit="R",
            syntax="",
        ),
        Element(
            "DTP01",
            Properties(
                desc="Date/Time Qualifier",
                req_sit="R",
                data_type=("ID", "3", "3"),
                position=1,
                codes=["573"],
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
        "AMT",
        Properties(
            desc="Remaining Patient Liability",
            position="5505",
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
)
