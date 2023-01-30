class OddListNode:
    def __init__(self, value) -> None:
        self.value: int = value
        self.next: OddListNode = None

    def push_back(self, value: int) -> None:
        if self.next == None:
            self.next = OddListNode(value=value)
        else:
            self.next.push_back(value=value)

    def pop(self):
        # Remove value from first single node
        if self.next == None:
            self.value = None

        else:
            # If this is penultimate node, then remove last node
            if self.next.next == None:
                self.next = None
            else:
                self.next.pop()

    def print(self):
        print(self.value, end="")
        if self.next != None:
            print(" --> ", end="")
            self.next.print()

    def remove_odds_elements(self, __is_head=True, __previous=None):
        '''
        Removing all nodes with odd value from linked list
        '''

        if self.value % 2 != 0:
            # If this is first element in the list
            if __is_head:
                if self.next != None:
                    self.value = self.next.value
                    self.next = self.next.next

                else:
                    # If this is single element in the list, just remove the value
                    self.value = None
            else:
                # If this is rear element in the list
                if self.next == None:
                    # Remove last node
                    __previous.next = None

                # If this is not first and not last node with odd value
                else:
                    # Remove current node and replace pointers
                    __previous.next = self.next

        # Continue list traversing, if this is not the last element
        if self.next != None:
            if not __is_head:
                if __previous.next == self.next:
                    self.next.remove_odds_elements(False, __previous)
            self.next.remove_odds_elements(False, self)


if __name__ == '__main__':
    head = OddListNode(1)
    for i in range(2, 13):
        head.push_back(i)

    head.print()
    print()
    head.remove_odds_elements()
    print()
    head.print()

    head.pop()
    print()
    head.print()
