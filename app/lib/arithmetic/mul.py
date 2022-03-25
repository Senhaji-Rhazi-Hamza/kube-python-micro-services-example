
def my_mul(*args):
    if args:
        return args[0] * my_mul(* args[1:])
    return 1