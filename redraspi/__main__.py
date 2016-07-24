import sys

def handler(signum, frame):
    pass

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    from .redraspi import RedRasPi

    app = RedRasPi()
    app.start()

    import signal

    signal.signal(signal.SIGTERM, handler)
    signum = signal.sigwait([signal.SIGTERM])

    if signum == signal.SIGTERM:
        app.stop()

if __name__ == "__main__":
    main()

