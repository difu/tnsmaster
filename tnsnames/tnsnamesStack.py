class TnsnamesStack:
    def __init__(self):
        self._stack = []

    def contains_entry(self, entry):
        """
        Returns True, if stack contains entry, False otherwise
        :param entry: the entry to be checked
        :return: True, if stack contains entry, False otherwise
        :rtype: bool
        """
        if entry in self._stack:
            return True
        else:
            return False

    def push(self, entry):
        self._stack.append(entry)

    @property
    def get_top(self):
        """
        Retuns the element on top of the stack but does NOT remove it

        :rtype: int
        """
        length = len(self._stack)
        if length > 0:
            return self._stack[length - 1]
        else:
            return None

    def is_ontop_of(self, base, top):
        """
        Returns True, if element top is on top of base, False otherwise
        If one element is not in the stack, False is returned
        :param base: the base element
        :param top: the element expected to be on top of base
        :return: True, if top is on  top of base
        :rtype: bool
        """
        if self.contains_entry(base) and self.contains_entry(top):
            if self._stack.index(base) < self._stack.index(top):
                return True
            else:
                return False
        else:
            return False

    @property
    def pop(self):
        """
        Retuns the element on top of the stack and removes it

        :rtype: object
        """
        length = len(self._stack)
        if length > 0:
            return self._stack.pop()
        else:
            return None

    @property
    def stack_size(self):
        """
        Retuns the size if the stack

        :rtype: int
        """
        return len(self._stack)
