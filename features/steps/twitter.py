
@given(u'I have not yet tweeted today')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have not yet tweeted today')

@when(u'it is bright enough')
def step_impl(context):
    raise NotImplementedError(u'STEP: When it is bright enough')

@then(u'I take a picture')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I take a picture')

@then(u'post it on twitter')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then post it on twitter')

