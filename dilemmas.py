# Dilemmas, options, and the respective impact of each option on variables.
dilemmas = [
    {
        "text": "A new technology company wants to open a branch in your country, but it would also displace many local businesses.",
        "options": {
            "a": "Allow the company to open",
            "b": "Deny the company permission"
        },
        "effects": {
            "a": {"gdp": 0.2, "unemployment": 0.1},
            "b": {"gdp": -0.1, "unemployment": -0.1}
        }
    },
    {
        "text": "A new proposed bill would increase spending on infrastructure, but it would also raise taxes on the middle class.",
        "options": {
            "a": "Support the bill",
            "b": "Oppose the bill"
        },
        "effects": {
            "a": {"gdp": 0.2, "poverty": 0.1},
            "b": {"gdp": -0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A neighboring country has been experiencing political turmoil, and refugees are fleeing to your country in large numbers.",
        "options": {
            "a": "Close borders to refugees",
            "b": "Open borders to refugees"
        },
        "effects": {
            "a": {"poverty": 0.1, "foreign_relations": -0.2},
            "b": {"poverty": -0.1, "foreign_relations": 0.2}
        }
    },
    {
        "text": "A new health program is proposed to improve healthcare access for low-income citizens, but it would also increase government debt.",
        "options": {
            "a": "Implement the program",
            "b": "Oppose the program"
        },
        "effects": {
            "a": {"health": 0.2, "gdp": -0.1},
            "b": {"health": -0.1, "gdp": 0.1}
        }
    },
    {
        "text": "A large corporation is accused of polluting a river, causing health problems for nearby residents.",
        "options": {
            "a": "Fine the corporation",
            "b": "Ignore the accusations"
        },
        "effects": {
            "a": {"gdp": -0.1, "health": 0.2},
            "b": {"gdp": 0.1, "health": -0.1}
        }
    },
    {
        "text": "A new education program is proposed to improve education access for low-income students, but it would also increase taxes.",
        "options": {
            "a": "Implement the program",
            "b": "Oppose the program"
        },
        "effects": {
            "a": {"education": 0.2, "poverty": 0.1},
            "b": {"education": -0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A new law is proposed to increase penalties for certain crimes, but it would also increase racial profiling.",
        "options": {
            "a": "Support the law",
            "b": "Oppose the law"
        },
        "effects": {
            "a": {"crime": 0.2, "poverty": 0.1},
            "b": {"crime": -0.2, "poverty": -0.1}
        }
    },
    {
        "text": "A new oil company wants to drill in a protected wilderness area, but it would also bring jobs and economic growth to the region.",
        "options": {
            "a": "Allow the drilling",
            "b": "Deny the drilling"
        },
        "effects": {
            "a": {"gdp": 0.2, "poverty": 0.1},
            "b": {"gdp": -0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A new proposed bill would increase funding for the police force, but it would also lead to a reduction in funding for social services.",
        "options": {
            "a": "Support the bill",
            "b": "Oppose the bill"
        },
        "effects": {
            "a": {"crime": -0.1, "poverty": 0.1},
            "b": {"crime": 0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A new free trade agreement is proposed with a neighboring country, but it would also lead to job losses in certain industries.",
        "options": {
            "a": "Support the agreement",
            "b": "Oppose the agreement"
        },
        "effects": {
            "a": {"gdp": 0.2, "unemployment": 0.1},
            "b": {"gdp": -0.1, "unemployment": -0.1}
        }
    },
    {
        "text": "A new renewable energy program is proposed to reduce dependence on fossil fuels, but it would also increase energy prices.",
        "options": {
            "a": "Implement the program",
            "b": "Oppose the program"
        },
        "effects": {
            "a": {"gdp": 0.1, "poverty": 0.1},
            "b": {"gdp": -0.1, "poverty": -0.1}
        }
    },
    {
        "text": "A new law is proposed to increase regulations on firearms, but it would also restrict citizens' rights to bear arms.",
        "options": {
            "a": "Support the law",
            "b": "Oppose the law"
        },
        "effects": {
            "a": {"crime": -0.2, "poverty": 0.1},
            "b": {"crime": 0.2, "poverty": -0.1}
        }
    },
    {
        "text": "A new law is proposed to legalize marijuana, but it would also increase drug-related crime.",
        "options": {
            "a": "Support the law",
            "b": "Oppose the law"
        },
        "effects": {
            "a": {"gdp": 0.2, "crime": 0.1},
            "b": {"gdp": -0.1, "crime": -0.1}
        }
    },
    {
        "text": "Should your country invest in renewable energy sources or build a new coal-powered plant?",
        "options": {
            "a": "Invest in renewable energy sources",
            "b": "Build a new coal-powered plant"
        },
        "effects": {
            "a": {"gdp": 0.2, "health": 0.2, "foreign_relations": 0.2},
            "b": {"gdp": 0.2, "health": -0.2, "foreign_relations": -0.2}
        }
    },
    {
        "text": "The government is considering a new law that would increase taxes to fund a public health program, but it would also reduce the amount of money that businesses have to spend.",
        "options": {
            "a": "Increase taxes for the public health program",
            "b": "Keep the taxes the same"
        },
        "effects": {
            "a": {"health": 0.3, "gdp": -0.2},
            "b": {"health": -0.1, "gdp": 0.1}
        }
    },
    # Add more dilemmas as needed
]
