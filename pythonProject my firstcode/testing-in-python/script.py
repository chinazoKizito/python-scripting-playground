def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        elif num == 0:
            return 5
        else:
            return "please enter number"
    except ValueError as err:
        return err


