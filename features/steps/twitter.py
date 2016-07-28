
@given(u'I have not yet tweeted today')
def step_impl(context):
    context.last_tweet = []

@when(u'it gets bright enough')
def step_impl(context):
    context.brightness = 700

@then(u'I take a picture')
def step_impl(context):
    context.camera_instance.take_picture.assert_called_once_with()

@then(u'I post the picture on twitter with a comment')
def step_impl(context):
    context.twitter_instance.PostUpdate.assert_called_once_with()

