import example


def test_hello_world():
    example.print_hello_world()


def test_class():
    counter = example.ExampleClass()
    assert (0 == counter.get_count())
    counter.add(10)
    assert (10 == counter.get_count())
