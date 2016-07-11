def before_scenario(context, scenario):
    context.now = datetime.datetime(2023, 3, 23, 11, 23, 5)
    context.brightness = 123
    # setup mocks
    #   - twitter api
    #   - serial (arduino)

@given(u'I have not yet tweeted today')
def step_impl(context):
    context.last_tweet = []

@given(u'I\'m awake')
def step_impl(context):
    # start redraspi
    pass

@when(u'it is bright enough')
def step_impl(context):
    context.brightness = 700

@then(u'I take a picture')
def step_impl(context):
    # assert picture taken
    #   - system call mock ?
    #   - camera abstraction ?
    pass

@then(u'post it on twitter')
def step_impl(context):
    # assert tweet
    #   - check twitter API mock for PostUpdate
    pass

