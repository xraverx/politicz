# Dilemmas, options, and the respective impact of each option on variables.
dilemmas = [
    {
        "text": "A new technology company wants to open a branch in your country, but it would also displace many local businesses.",
        "options": {
            "A": "Allow the company to open",
            "B": "Deny the company permission"
        },
        "effects": {
            "A": {"gdp": 0.2, "unemployment": 0.1},
            "B": {"gdp": -0.1, "unemployment": -0.1}
        }
    },
    {
        "text": "A new proposed bill would increase spending on infrastructure, but it would also raise taxes on the middle class.",
        "options": {
            "A": "Support the bill",
            "B": "Oppose the bill"
        },
        "effects": {
            "A": {"gdp": 0.2, "poverty": 0.1},
            "B": {"gdp": -0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A neighboring country has been experiencing political turmoil, and refugees are fleeing to your country in large numbers.",
        "options": {
            "A": "Close borders to refugees",
            "B": "Open borders to refugees"
        },
        "effects": {
            "A": {"poverty": 0.1, "foreign_relations": -0.2},
            "B": {"poverty": -0.1, "foreign_relations": 0.2}
        }
    },
    {
        "text": "A new health program is proposed to improve healthcare access for low-income citizens, but it would also increase government debt.",
        "options": {
            "A": "Implement the program",
            "B": "Oppose the program"
        },
        "effects": {
            "A": {"health": 0.2, "gdp": -0.1},
            "B": {"health": -0.1, "gdp": 0.1}
        }
    },
    {
        "text": "A large corporation is accused of polluting a river, causing health problems for nearby residents.",
        "options": {
            "A": "Fine the corporation",
            "B": "Ignore the accusations"
        },
        "effects": {
            "A": {"gdp": -0.1, "health": 0.2},
            "B": {"gdp": 0.1, "health": -0.1}
        }
    },
    {
        "text": "A new education program is proposed to improve education access for low-income students, but it would also increase taxes.",
        "options": {
            "A": "Implement the program",
            "B": "Oppose the program"
        },
        "effects": {
            "A": {"education": 0.2, "poverty": 0.1},
            "B": {"education": -0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A new law is proposed to increase penalties for certain crimes, but it would also increase racial profiling.",
        "options": {
            "A": "Support the law",
            "B": "Oppose the law"
        },
        "effects": {
            "A": {"crime": 0.2, "poverty": 0.1},
            "B": {"crime": -0.2, "poverty": -0.1}
        }
    },
    {
        "text": "A new oil company wants to drill in a protected wilderness area, but it would also bring jobs and economic growth to the region.",
        "options": {
            "A": "Allow the drilling",
            "B": "Deny the drilling"
        },
        "effects": {
            "A": {"gdp": 0.2, "poverty": 0.1},
            "B": {"gdp": -0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A new proposed bill would increase funding for the police force, but it would also lead to a reduction in funding for social services.",
        "options": {
            "A": "Support the bill",
            "B": "Oppose the bill"
        },
        "effects": {
            "A": {"crime": -0.1, "poverty": 0.1},
            "B": {"crime": 0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A new free trade agreement is proposed with a neighboring country, but it would also lead to job losses in certain industries.",
        "options": {
            "A": "Support the agreement",
            "B": "Oppose the agreement"
        },
        "effects": {
            "A": {"gdp": 0.2, "unemployment": 0.1},
            "B": {"gdp": -0.1, "unemployment": -0.1}
        }
    },
    {
        "text": "A new renewable energy program is proposed to reduce dependence on fossil fuels, but it would also increase energy prices.",
        "options": {
            "A": "Implement the program",
            "B": "Oppose the program"
        },
        "effects": {
            "A": {"gdp": 0.1, "poverty": 0.1},
            "B": {"gdp": -0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A new law is proposed to increase regulations on firearms, but it would also restrict citizens' rights to bear arms.",
        "options": {
            "A": "Support the law",
            "B": "Oppose the law"
        },
        "effects": {
            "A": {"crime": -0.2, "poverty": 0.1},
            "B": {"crime": 0.2, "poverty": -0.1}
        }
    },
    {
        "text": "A new law is proposed to legalize marijuana, but it would also increase drug-related crime.",
        "options": {
            "A": "Support the law",
            "B": "Oppose the law"
        },
        "effects": {
            "A": {"gdp": 0.2, "crime": 0.1},
            "B": {"gdp": -0.1, "crime": -0.1}
        }
    },
    # Add more dilemmas as needed
]
