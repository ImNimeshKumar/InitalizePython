# Accepting keyword with arguments

def person(name, **data):
    print(name)
    print(data)

person("musk", automobile = "tesla", spaceAgency = "spaceX", hyperloop = "boringCompany")