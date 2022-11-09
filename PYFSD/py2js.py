from ast import (
    FunctionDef,
    arguments,
    Attribute,
    Subscript,
    Constant,
    Assign,
    Lambda,
    parse,
    Name,
    Call,
    dump,
    arg,
    arg
)



code = """
@doc["abc"].click
def on_some_click(event, element):
    return element

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

    elif isinstance(stm, FunctionDef):
        return transplile_funcdef(stm)

    elif isinstance(stm, arguments):
        return transplile_arguments(stm)

    elif isinstance(stm, )

    elif isinstance(stm, str):
        return stm

    else:
        return str(stm)

def transplile_arguments(stmt: arguments):
    print(dump(stmt, indent=2))
    return ",".join(get(stmt.args))


def transplile_funcdef(stmt: FunctionDef):
    print(dump(stmt, indent=2))
    # a {{}} is an escape for a bracket
    return "function {name}({args}){{ {body} }}".format(
        name=get(stmt.name),
        args=",".join(get(stmt.args)),
        body=";".join(get(stmt.body))
    )

def transplile_call(stmt: Call):
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
    return "\"{}\"".format(
        get(stmt.value)
    )


def transplile_lambda(stmt: Lambda):
    args = ",".join(get(f) for f in stmt.args.args)
    return "(({})=>{{ {} }})".format(
        args,
        get(stmt.body)
    )

def transplile_attribute(stmt: Attribute):
    return "{}.{}".format(
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
