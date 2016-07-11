import datetime

def before_scenario(context, scenario):
    context.now = datetime.datetime(2023, 3, 23, 11, 23, 5)
    context.brightness = 123
    # setup mocks
    #   - twitter api
    #   - serial (arduino)

