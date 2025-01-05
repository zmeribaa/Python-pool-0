def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
        return 0
    elif isinstance(object, float) and str(object) == 'nan':
        print(f"Cheese: {object} <class 'float'>")
        return 0
    elif object == 0:
        print(f"Zero: {object} <class 'int'>")
        return 0
    elif object == '':
        print(f"Empty: <class 'str'>")
        return 0
    elif object is False:
        print(f"Fake: {object} <class 'bool'>")
        return 0
    else:
        print("Type not Found")
        return 1
