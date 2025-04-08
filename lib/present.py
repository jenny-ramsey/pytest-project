class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents

""" init creates a present with no contents
wrap contents puts something inside the present - wraps it.
it only allows one item to be wrapped and raises an error if you try to wrap it again.
unwrap contents retrieves the contents from the present. 
it raises an error if there is nothing inside. 
"""