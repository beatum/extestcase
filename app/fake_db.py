"""
Simulating json data
"""

db = [
    {"js": {"name": "Foo", "price": 50.2}},
    {"js": {"bar": {"name": "Bar", "price": 62, "tax": 20.2}}},
    {
        "js": {
            "baz": {"description": None, "price": 50.2, "tax": 10.5, "tags": []}
        }
    },
    {"js": [1, 2, 3]},
    {"js": [1]},
    {"js": []},
]
