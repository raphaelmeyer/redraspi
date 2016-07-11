import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    from .redraspi import RedRasPi

    app = RedRasPi()
    app.start()

if __name__ == "__main__":
    main()

