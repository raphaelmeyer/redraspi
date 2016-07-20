
@given(u'I have not yet tweeted today')
def step_impl(context):
    context.last_tweet = []

@given(u'I\'m awake')
def step_impl(context):
    from redraspi import redraspi
    context.app = redraspi.RedRasPi()
    context.app.start()

@when(u'it is bright enough')
def step_impl(context):
    context.brightness = 700

@then(u'I take a picture')
def step_impl(context):
    # assert picture taken
    #   - system call mock ?
    #   - camera abstraction ?
    pass

@then(u'I post the picture on twitter')
def step_impl(context):
    context.twitter_instance.PostUpdate.assert_called_with()
    # assert tweet
    #   - check twitter API mock for PostUpdate

