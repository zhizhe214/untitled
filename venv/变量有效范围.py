my_grade='三年级二班'
my_class='三年级二班'
def text(name):
    my_name=name
    global my_class
    #my_class='五年级一班'
    print(my_name+'在：'+my_class)

text('杨超')
print(my_class)


def test_variable():
    global height
    height=170
    print(height)

test_variable()
print(height)

for i in list(globals()):
    print(i)