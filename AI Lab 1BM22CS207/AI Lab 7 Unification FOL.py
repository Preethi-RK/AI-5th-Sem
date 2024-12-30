def unify(expr1, expr2):
    print(f"Unifying {expr1} with {expr2}")

    # Step 1: Check if either expr1 or expr2 is a variable or constant
    if expr1 == expr2:
        print("Result: Identical terms, no substitution needed.")
        return []  # Return NIL if expressions are identical
    elif is_variable(expr1):
        return failure_if_occurs_check(expr1, expr2)
    elif is_variable(expr2):
        return failure_if_occurs_check(expr2, expr1)

    # Step 2: Check if both are compound expressions with the same predicate
    elif is_compound(expr1) and is_compound(expr2):
        if get_predicate(expr1) != get_predicate(expr2):
            print("Failure: Predicates do not match.")
            return "FAILURE"
        return unify_args(get_arguments(expr1), get_arguments(expr2))

    # Step 3: Incompatible terms
    else:
        print("Failure: Incompatible terms.")
        return "FAILURE"

def unify_args(args1, args2):
    if len(args1) != len(args2):
        print("Failure: Arguments have different lengths.")
        return "FAILURE"

    subst = []
    for a1, a2 in zip(args1, args2):
        s = unify(a1, a2)
        if s == "FAILURE":
            print(f"Failure: Could not unify {a1} with {a2}.")
            return "FAILURE"
        if s:
            subst.extend(s)
            args1 = apply_substitution(s, args1)
            args2 = apply_substitution(s, args2)

    return subst

def is_variable(symbol):
    return isinstance(symbol, str) and symbol.islower()

def is_compound(expression):
    return isinstance(expression, str) and "(" in expression and ")" in expression

def get_predicate(expression):
    return expression.split("(")[0]

def get_arguments(expression):
    args_str = expression[expression.index("(") + 1 : expression.rindex(")")]
    return [arg.strip() for arg in args_str.split(",")]

def failure_if_occurs_check(variable, expression):
    if occurs_check(variable, expression):
        print(f"Failure: Occurs check failed for {variable} in {expression}.")
        return "FAILURE"
    print(f"Substitution: {variable} -> {expression}")
    return [(variable, expression)]

def occurs_check(variable, expression):
    if variable == expression:
        return True
    if is_compound(expression):
        return variable in get_arguments(expression)
    return False

def apply_substitution(subst, expression):
    if isinstance(expression, list):
        return [apply_substitution(subst, sub_expr) for sub_expr in expression]
    elif is_variable(expression):
        for var, value in subst:
            if expression == var:
                return value
    elif is_compound(expression):
        predicate = get_predicate(expression)
        arguments = get_arguments(expression)
        substituted_args = [apply_substitution(subst, arg) for arg in arguments]
        return f"{predicate}({', '.join(substituted_args)})"
    return expression

# Example usage:
expr1 = "P(b,X,f(g(Z)))"
expr2 = "P(Z,f(y),f(y))"
result = unify(expr1, expr2)

print("\nFinal Result:")
if result == "FAILURE":
    print("Unification failed!")
else:
    print("Unification successful!")
    print("Substitutions:", ', '.join(f"{var} -> {val}" for var, val in result))
print("Preethi Narasimhan-1BM22CS207")
