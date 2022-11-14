from inspect import getsource
from ast import (
    FunctionDef,
    arguments,
    Attribute,
    Subscript,
    Constant,
    Assign,
    Lambda,
    Return,
    BinOp,
    parse,
    Name,
    Call,
    dump,
    Expr,
    Mult,
    Div,
    Add,
    Sub,
    arg,
)


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

    elif isinstance(stm, Return):
        return transplile_return(stm)

    elif isinstance(stm, Expr):
        return transplile_expr(stm)

    elif isinstance(stm, BinOp):
        return transplile_binop(stm)

    elif isinstance(stm, Add):
        return "+"

    elif isinstance(stm, Sub):
        return "-"

    elif isinstance(stm, Mult):
        return "*"

    elif isinstance(stm, Div):
        return " / "

    elif isinstance(stm, str):
        return stm

    elif isinstance(stm, int):
        return stm

    else:
        return str(stm)


def transplile_binop(stmt: BinOp):
    return "{l} {op} {r}".format(
        l=x if isinstance(x := stmt.left, int) else get(x),
        op=get(stmt.op),
        r=x if isinstance(x := stmt.right, int) else get(x),
    )


def transplile_expr(stmt: Expr):
    return get(stmt.value)


def transplile_return(stmt: Return):
    return "return {};".format(get(stmt.value))


def transplile_arguments(stmt: arguments):
    return ",".join(get(stmt.args))


def transplile_funcdef(stmt: FunctionDef):
    # a {{}} is an escape for a bracket
    return "function {name}({args}){{ {body} }}".format(
        name=get(stmt.name),
        args=get(stmt.args),
        body=get(stmt.body) if len(stmt.body) == 1 else ";".join(get(stmt.body)),
    )


def transplile_call(stmt: Call):
    if get(stmt.func) == "set":
        return "{} = {}".format(
            get(stmt.args[0]),
            get(stmt.args[1]),
        )

    return "{}({})".format(
        get(stmt.func),
        get(stmt.args),
    )


def transplile_arg(stmt: arg):
    return stmt.arg


def transplile_assign(stm: Assign) -> str:
    print(dump(stm, indent=2))
    return "let {} = {}".format(
        get(stm.targets),
        get(stm.value),
    )


def transplile_name(stmt: Name):
    return "{}".format(
        get(stmt.id),
    )


def transplile_constant(stmt: Constant):
    if isinstance(stmt.value, str):
        return '"{}"'.format(
            get(stmt.value),
        )

    return "{}".format(
        get(stmt.value),
    )


def transplile_lambda(stmt: Lambda):
    args = ",".join(get(f) for f in stmt.args.args)
    return "(({})=>{{ {} }})".format(
        args,
        get(stmt.body),
    )


def transplile_attribute(stmt: Attribute):
    return "{}.{}".format(
        get(stmt.value),
        get(stmt.attr),
    )


def transplile_sub_script(stmt: Subscript):
    return "{}[{}]".format(
        get(stmt.value),
        get(stmt.slice),
    )


def jsifiy(fnc):
    return "".join(get(stmt) for stmt in parse(getsource(fnc)).body)
