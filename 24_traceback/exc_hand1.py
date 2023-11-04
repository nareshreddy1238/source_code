import traceback as tb
def test():
    try:
        if sal < 0 :
            raise Exception('Salary Can not be Less Than 0.')
    except Exception as exc:
        print("An Exception Occured. ", exc.__class__.__name__)
        raise ## exception is carry forward to main function
