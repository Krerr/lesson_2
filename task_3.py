import yaml

data = {
    "list": ["one", "two", "tree"],
    "number": 4,
    "dist": {
        "first": 1,
        "second": 2
    }
}

file = "file.yaml"


def write_data_to_yaml():
    with open(file, "w") as r_file:
        yaml.dump(data, r_file, default_flow_style=False)

def read_data_from_yaml():
    with open(file, "r") as r_file:
        obj =  yaml.load(r_file)
        print(obj)



write_data_to_yaml()


read_data_from_yaml()

