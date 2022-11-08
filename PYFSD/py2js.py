from ast import dump, parse, Assign, Attribute, Subscript, Name, Constant, Lambda, arg, Call


code = """
doc["#abc"].onclick = lambda event, element: console.log("Here")
doc["#def"].onclick = lambda e: console.log("also Here")
"""

def get(stm) -> None:
    if isinstance(stm, list):
        if len(stm) == 1:
            return get(stm[0])

        return [get(s) for s in stm]

    elif isinstance(stm, Assign):
        return transplile_assign(stm)

    elif isinstance(stm, Attribute):
        return transplile_attribute(stm)

    elif isinstance(stm, Subscript):
        return transplile_sub_script(stm)

    elif isinstance(stm, Name):
        return transplile_name(stm)

    elif isinstance(stm, Constant):
        return transplile_constant(stm)
    
    elif isinstance(stm, Lambda):
        return transplile_lambda(stm)

    elif isinstance(stm, arg):
        return transplile_arg(stm)

    elif isinstance(stm, Call):
        return transplile_call(stm)

    elif isinstance(stm, str):
        return '"{}"'.format(stm)


    else:
        return str(stm)

def transplile_call(stmt: Call):
    print(dump(stmt))
    return "{}({})".format(
        get(stmt.func),
        get(stmt.args)
    )

def transplile_arg(stmt: arg):
    return stmt.arg

def transplile_assign(stm: Assign) -> str:
    return "let {} = {};".format(
        get(stm.targets),
        get(stm.value)
    )

def transplile_name(stmt: Name):
    return "{}".format(
        get(stmt.id)
    )


def transplile_constant(stmt: Constant):
    return "{}".format(
        get(stmt.value)
    )


def transplile_lambda(stmt: Lambda):
    args = ",".join(get(f) for f in stmt.args.args)
    return "(({})=>{{ {} }})".format(
        args,
        get(stmt.body)
    )

def transplile_attribute(stmt: Attribute):
    return "{}[{}] ".format(
        get(stmt.value),
        get(stmt.attr)
    )


def transplile_sub_script(stmt: Subscript):
    return "{}[{}]".format(
        get(stmt.value),
        get(stmt.slice)
    )


for stmt in parse(code).body:
    print(get(stmt))
