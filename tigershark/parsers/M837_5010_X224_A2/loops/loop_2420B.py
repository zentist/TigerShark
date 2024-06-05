from tigershark.X12.parse import Composite, Element, Loop, Properties, Segment

parsed_837_2420B = Loop(
    "2420B",
    Properties(
        desc="Assistant Surgeon Name",
        looptype="",
        position="5000",
        repeat="1",
        req_sit="S",
    ),
    Segment(
        "NM1",
        Properties(
            desc="Assistant Surgeon Name",
            position="5000",
            repeat="1",
            req_sit="S",
            syntax="P0809 C1110 C1203",
        ),
        Element(
            "NM101",
            Properties(
                desc="Entity Identifier Code",
                req_sit="R",
                data_type=("ID", "2", "3"),
                position=1,
                codes=["ZZ"],
            ),
        ),
        Element(
            "NM102",
            Properties(
                desc="Entity Type Qualifier",
                req_sit="R",
                data_type=("ID", "1", "1"),
                position=2,
                codes=["1"],
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
                req_sit="S",
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
        "PRV",
        Properties(
            desc="Assistant Surgeon Specialty Information",
            position="2550",
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
                codes=["RF"],
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
        "REF",
        Properties(
            desc="Assistant Surgeon Secondary Identification",
            position="5250",
            repeat="20",
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
                codes=["0B", "1G", "G2", "LU"],
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
            Properties(desc="Reference Identifier", refdes="", repeat="", req_sit="S", seq="04"),
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
                    data_type=("AN", "1", "50"),
                    position=1,
                    codes=[],
                ),
            ),
            Element(
                "REF04-03",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=2,
                    codes=[],
                ),
            ),
            Element(
                "REF04-04",
                Properties(
                    desc="Reference Identification",
                    req_sit="N",
                    data_type=("AN", "1", "50"),
                    position=3,
                    codes=[],
                ),
            ),
            Element(
                "REF04-05",
                Properties(
                    desc="Reference Identification Qualifier",
                    req_sit="N",
                    data_type=("ID", "2", "3"),
                    position=4,
                    codes=[],
                ),
            ),
            Element(
                "REF04-06",
                Properties(
                    desc="Reference Identification",
                    req_sit="N",
                    data_type=("AN", "1", "50"),
                    position=5,
                    codes=[],
                ),
            ),
        ),
    ),
)
