class Node():

    def __init__(self, node_type, value, links=None, add_back=False):
        ''' A node should have 3 properties:
            1. A type (str, label for value type), ex: 'name', 'haircolor', 'age'
            2. A value (any)
            3. A link to other nodes

            A node should be kept in a set (python built-in type:
                https://docs.python.org/2/library/sets.html)
            of other nodes that share it's 'type' field. Thus,
            the 'value' for each node should be unique within its
            type. Links to other nodes should be nodes of other
            'types'.
        '''
        self._type = node_type
        self._value = value
        self._links = set()
        if links and type(links) == set:
            self.add_links(links, add_back)

    def add_link(self, node, add_back=False):
        ''' adds the given node to self._links
            will not add the node if types match, and return True
        '''
        assert self.is_instance(node), 'not node or node inheritor type for {}'.format(repr(node))
        self._links = self._links.union({node})
        if add_back:
            node.add_link(self)

    def add_links(self, nodes, add_back=False):
        ''' nodes is expected to be a set (python built-in type) of Node instances.
        '''
        for node in nodes:
            self.add_link(node, add_back)

    def __str__(self):
        ''' '''
        links = len(self._links)
        return "Node({}, {}, {})".format(str(self._type), str(self._value), links)

    def __repr__(self):
        links = '{'
        for index, l in enumerate(self._links):
            if index > 0: links += ', '
            links += str(l)
        links += '}'
        return "Node({}, {}, {})".format(repr(self._type), repr(self._value), links)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._type == other._type and self._value == other._value
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self.__repr__())

    def is_instance(self, other):
        return isinstance(other, Node)

    def get_type(self):
        ''' '''
        return self._type

    def get_value(self):
        ''' '''
        return self._value

    def get_links(self):
        ''' '''
        return self._links


class Category(set):

    def __init__(self, category_name, node_list=None):
        ''' '''
        super(Category, self).__init__()
        self._type = category_name
        if node_list:
            for node in node_list:
                self.add(node)

    def get_type(self):
        ''' '''
        return self._type

    def add_node(self, node):
        ''' '''
        try:
            assert node.get_type() == self.get_type()
            self.add(node)
        except AssertionError:
            print('Node._type({}) != Category._type({})'.format(node.get_type, self.get_type))
            print('\tNode(type:{}, value:{})'.format(node.get_type, node.get_value))

    def __str__(self):
        ''' '''
        s = super(Category, self).__str__()
        s = s.replace('Category(', 'Category(\n{}\n)'.format(self._type) + '{')
        s = s.replace('{Node(', '{\n\tNode(')
        s = s.replace(', Node(', ',\n\tNode(')
        if s[-1] == ')':
            s = s[:-1] + '}'
        return s


if __name__ == '__main__':
    #Working on an example
    # import node_example
    # node_example.main()

    print("node.py module does nothing presently")
