import exc_hand as eh
import sys
import traceback as tb

def main():
    try:
        eh.test()
    except:
        print(tb.print_exc())
        sys.exit(1)

if __name__ == '__main__':
    main()
