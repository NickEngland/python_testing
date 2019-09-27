'''
Example file for testing
'''


class ExampleClass:
    count: int = 0

    def add(self, increment):
        self.count += increment

    def get_count(self):
        return self.count

    def range(self):
        range(6)


def print_hello_world():
    print("Hello World")


if __name__ == '__main__':
    print_hello_world()
