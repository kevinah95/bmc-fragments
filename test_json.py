import json
d = {
    "base_seq": {
        "seq_original": "",
        "length_original": 0,
        "length_final": 0,
        "mode": "USER|RAND|PROB"
    },
    "repeat": {
        "source": "",
        "times": {
            "a": {
                "selected": False,
                "times": 0
            },
            "b": {
                "selected": False
            }
        },
        "distance": {
            "a": {
                "selected": False,
                "fst_pos": 0,
                "distance": 0
            },
            "b": {
                "selected": False,
                "average": 0
            }
        },
        "errors": {
            "possible_errors": {
                "base_change": {
                    "selected": False,
                    "average_distance": 0
                },
                "deleted": {
                    "selected": False,
                    "average_distance": 0
                },
                "insertion": {
                    "selected": False,
                    "average_distance": 0
                }
            }
        },
        "reverse_orientation": {
            "probability": 0
        }
    }
}


# print(d['repeat']['times']['a'])
for k, v in d['repeat']['times'].items():
    if v['selected']:
        print(k, v)

# save dict to json
with open('data.json', 'w') as fp:
    json.dump(d, fp)
