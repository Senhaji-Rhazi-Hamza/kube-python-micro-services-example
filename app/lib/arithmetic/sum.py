
def my_sum(*args):
    if args:
        return args[0] + my_sum(* args[1:])
    return 0