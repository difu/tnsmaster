from unittest import TestCase

from tnsnames.tnsnamesStack import TnsnamesStack

__author__ = 'dirkfuchs'


class TestTnsnamesStack(TestCase):
    def setUp(self):
        self._first_element = "First"
        self._second_element = "Second"
        self._third_element = "Third"
        pass

    def test_stack_pop_empty(self):
        the_stack = TnsnamesStack()
        self.assertEqual(the_stack.stack_size, 0, "Length should be 0")
        self.assertEqual(the_stack.pop, None, "Should be none ")

    def test_push_pop(self):
        the_stack = TnsnamesStack()

        the_stack.push(self._first_element)
        self.assertEqual(the_stack.stack_size, 1, "The size should be 1, because one element was put on top")
        self.assertEqual(the_stack.get_top, self._first_element, "Wrong element on top")
        self.assertEqual(the_stack.stack_size, 1, "The size should still be 1 after get_top")
        self.assertEqual(the_stack.pop, self._first_element, "Wrong element on top")
        self.assertEqual(the_stack.stack_size, 0, "The size should 0 after pop")

        the_stack.push(self._first_element)
        the_stack.push(self._second_element)
        the_stack.push(self._third_element)
        self.assertEqual(the_stack.stack_size, 3, "The size should be 3")

    def test_contains(self):
        the_stack = TnsnamesStack()
        self.assertEquals(the_stack.contains_entry("DOESNOTEXIST"), False, "Should not have found element")
        the_stack.push(self._first_element)
        the_stack.push(self._second_element)
        self.assertEqual(the_stack.contains_entry(self._first_element), True, "Should contain first element")
        self.assertEqual(the_stack.contains_entry(self._second_element), True, "Should contain 2nd element")
        self.assertEquals(the_stack.contains_entry(self._third_element), False, "Should not have found 3rd element")

    def test_is_ontop(self):
        the_stack = TnsnamesStack()
        self.assertEquals(the_stack.is_ontop_of(self._first_element, self._second_element), False,
                          "Should not have found element")
        the_stack.push(self._first_element)
        the_stack.push(self._second_element)
        self.assertEquals(the_stack.is_ontop_of(self._second_element, self._first_element), False,
                          "2nd should be on top of 1st")
        self.assertEquals(the_stack.is_ontop_of(self._first_element, self._second_element), True,
                          "2nd should be on top of 1st")
        self.assertEquals(the_stack.is_ontop_of(self._first_element, self._first_element), False,
                          "element cannot be on top of itself")
