from behave import *

# @given('launch browser')
# def new_method(context):
#     print("Method Implemented")
#
@given(u'launched browser')
def step_impl(context):
    print('File implemented')
    raise NotImplementedError(u'STEP: When launched browser')

@when(u'launched browser')
def step_impl(context):
    print('File implemented')
    raise NotImplementedError(u'STEP: When launched browser')


@then(u'Browser launched')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Browser launched')
