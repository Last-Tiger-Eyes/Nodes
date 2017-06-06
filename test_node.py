import unittest
from node import Node, Category


class TestNodeMethods(unittest.TestCase):

    def setUp(self):
        ''' '''
        self.node_type = "$"

        self.value1 = 5
        self.links1 = None
        self.add_back1 = False
        self.node1 = Node(node_type=self.node_type, value=self.value1, links=self.links1, add_back=self.add_back1)

        self.value2 = 12
        self.links2 = None
        self.add_back2 = False
        self.node2 = Node(node_type=self.node_type, value=self.value2, links=self.links2, add_back=self.add_back2)

        self.node_type3 = "product name"
        self.value3 = "sunglasses"
        self.links3 = {self.node1, self.node2}
        self.add_back3 = True
        self.node3 = Node(node_type=self.node_type3, value=self.value3, links=self.links3, add_back=self.add_back3)

    def test_init(self):
        ''' '''
        self.assertEqual(self.node_type, self.node1._type)
        self.assertEqual(self.node_type, self.node2._type)
        self.assertEqual(self.node_type3, self.node3._type)

        self.assertEqual(self.value1, self.node1._value)
        self.assertEqual(self.value2, self.node2._value)
        self.assertEqual(self.value3, self.node3._value)
        # self.assertFalse(True)

    def test_add_link(self):
        ''' '''
        self.assertFalse(True)

    def test_add_links(self):
        ''' '''
        self.assertEqual({self.node3}, self.node1._links)

        print('node1: ', str(self.node1))
        print('node2: ', str(self.node2))
        print('node3: ', str(self.node3))
        print('********************')
        print('{self.node3}: ', str({self.node3}))
        print('node1._links: ', str(self.node1._links))
        print('{self.node3} == self.node1._links', str({self.node3} == self.node1._links))
        print('self.node1._links.issubset({self.node3})', str(self.node1._links.issubset({self.node3})))
        print('********************')
        print('{self.node3}: ', str({self.node3}))
        print('node2._links: ', str(self.node2._links))
        print('{self.node3} == self.node2._links', str({self.node3} == self.node2._links))
        print('self.node2._links.issubset({self.node3})', str(self.node2._links.issubset({self.node3})))
        # TODO: WHAT THE F*CK IS WRONG WITH THIS COMPARISON!?!?!?!
        self.assertEqual({self.node3}, self.node2._links)
        self.assertEqual(self.links3, self.node3._links)

        self.assertFalse(True)

    def test___str__(self):
        ''' '''
        self.assertEqual('Node($, 5, 1)', str(self.node1))
        self.assertEqual('Node($, 12, 1)', str(self.node2))
        self.assertEqual('Node(product name, sunglasses, 2)', str(self.node3))

    def test___repr__(self):
        ''' '''
        self.assertEqual("Node('$', 5, {Node(product name, sunglasses, 2)})", repr(self.node1))
        self.assertEqual("Node('$', 12, {Node(product name, sunglasses, 2)})", repr(self.node2))
        self.assertEqual("Node('product name', 'sunglasses', {Node($, 5, 1), Node($, 12, 1)})", repr(self.node3))

    def test___eq__(self):
        ''' '''
        self.assertTrue(self.node1 == self.node1)
        self.assertTrue(self.node2 == self.node2)
        self.assertTrue(self.node3 == self.node3)
        self.assertFalse(self.node1 == self.node2)
        self.assertFalse(self.node1 == self.node3)
        self.assertFalse(self.node2 == self.node3)

    def test___ne__(self):
        ''' '''
        self.assertTrue(self.node1 != self.node2)
        self.assertTrue(self.node1 != self.node3)
        self.assertTrue(self.node2 != self.node3)
        self.assertFalse(self.node1 != self.node1)
        self.assertFalse(self.node2 != self.node2)
        self.assertFalse(self.node3 != self.node3)

    def test___hash__(self):
        ''' '''
        n1_hsh = hash(repr(self.node1))
        self.assertEqual(n1_hsh, self.node1.__hash__())

    def test_is_instance(self):
        ''' '''
        self.assertTrue(self.node1.is_instance(self.node2))
        self.assertTrue(self.node1.is_instance(self.node3))
        self.assertTrue(self.node2.is_instance(self.node1))
        self.assertTrue(self.node2.is_instance(self.node3))
        self.assertTrue(self.node3.is_instance(self.node1))
        self.assertTrue(self.node3.is_instance(self.node2))

    def test_get_type(self):
        ''' '''
        self.assertEqual(self.node1.get_type(), self.node1._type)
        self.assertEqual(self.node1.get_type(), self.node2.get_type())
        self.assertEqual(self.node2.get_type(), self.node2._type)
        self.assertEqual(self.node3.get_type(), self.node3._type)
        self.assertNotEqual(self.node1.get_type(), self.node3.get_type())
        self.assertNotEqual(self.node1.get_type(), self.node3._type)
        self.assertNotEqual(self.node2.get_type(), self.node3.get_type())
        self.assertNotEqual(self.node2.get_type(), self.node3._type)

    def test_get_value(self):
        ''' '''
        self.assertEqual(5, self.node1.get_value())
        self.assertEqual(self.node1._value, self.node1.get_value())
        self.assertEqual(12, self.node2.get_value())
        self.assertEqual(self.node2._value, self.node2.get_value())
        self.assertEqual('sunglasses', self.node3.get_value())
        self.assertEqual(self.node3._value, self.node3.get_value())

    def test_get_links(self):
        ''' '''
        set_of_n3 = {self.node3}
        self.assertEqual(self.node1.get_links(), self.node1._links)
        self.assertEqual(self.node1.get_links(), set_of_n3)
        self.assertEqual(self.node2.get_links(), self.node2._links)
        # TODO: use debugger to figure out why this is failing
        self.assertEqual(self.node2.get_links(), set_of_n3) # comes up not equal -- issue with set comparison?
        self.assertEqual(self.node3.get_links(), self.node3._links)
        self.assertEqual(self.node3.get_links(), {self.node1, self.node2})


# class TestCategoryMethods(unittest.TestCase):
#
#     def setUp(self):
#         ''' '''
#         self.category0 = Category(category_name="$", node_list=None)
#
#         self.node1 = Node("$", 1)
#         self.node2 = Node("$", 2)
#         self.node3 = Node("$", 3)
#         nodes_list1 = [self.node1, self.node2, self.node3]
#         self.category1 = Category(category_name="$", node_list=nodes_list1)
#
#         # self.node4 = Node("")
#         nodes_list3 = []
#         self.category2 = Category(category_name="", node_list=nodes_list3)
#
#     def test___init__(self):
#         ''' '''
#         self.assertFalse(True)
#
#     def test_get_type(self):
#         ''' '''
#         self.assertFalse(True)
#
#     def test_add_node(self):
#         ''' '''
#         self.assertFalse(True)
#
#     def test___str__(self):
#         ''' '''
#         self.assertFalse(True)

if __name__ == '__main__':
    unittest.main()
