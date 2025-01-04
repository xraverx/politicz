# dilemmas.py
# Store dilemmas in a list of dictionaries, or keep them in JSON/YAML if preferred.

dilemmas_data = [
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
        "t
