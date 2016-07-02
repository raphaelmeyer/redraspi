try:
    from config import Settings
except ImportError:
    from defaults import Defaults as Settings

settings = Settings()

