class ListNode:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return f"{self.__class__.__name__}({self.val})"

    def __str__(self):
        return f"{self.val}"


class LinkedList:
    def __init__(self, iterable=None):
        self.head = ListNode()
        self.tail = self.head
        if iterable:
            for item in iterable:
                self.append(item)

    def __iter__(self):
        current = self.head.next_
        while current:
            yield current.val
            current = current.next_

    def __str__(self):
        return f"{self.__class__.__name__}({', '.join(str(item) for item in self)})"

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(repr(item) for item in self)})"

    def __len__(self):
        return len([item for item in self])

    def __getitem__(self, index):
        current = self.head.next_
        for _ in range(index):
            current = current.next_
        return current.val

    def __setitem__(self, index, value):
        current = self.head.next_
        for _ in range(index):
            current = current.next_
        current.val = value

    def append(self, value):
        self.tail.next_ = ListNode(value)
        self.tail = self.tail.next_

    def prepend(self, value):
        self.head.next_ = ListNode(value, self.head.next_)
        if self.head.next_.next_ is None:
            self.tail = self.head.next_

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        else:
            current = self.head.next_
            for _ in range(index - 1):
                current = current.next_
            current.next_ = ListNode(value, current.next_)
            if current.next_.next_ is None:
                self.tail = current.next_

    def remove(self, value):
        current = self.head
        while current.next_:
            if current.next_.val == value:
                current.next_ = current.next_.next_
                if current.next_ is None:
                    self.tail = current
                break
            current = current.next_

    def remove_at(self, index):
        if index == 0:
            self.head.next_ = self.head.next_.next_
            if self.head.next_ is None:
                self.tail = self.head
        else:
            current = self.head.next_
            for _ in range(index - 1):
                current = current.next_
            current.next_ = current.next_.next_
            if current.next_ is None:
                self.tail = current

    def reverse(self):
        prev = None
        current = self.head.next_
        while current:
            next_ = current.next_
            current.next_ = prev
            prev = current
            current = next_
        self.head.next_ = prev

    def copy(self):
        return LinkedList(self)

    def deepcopy(self):
        return LinkedList(self)

    def clear(self):
        self.head.next_ = None
        self.tail = self.head

    def extend(self, other):
        current = other.head.next_
        while current:
            self.append(current.val)
            current = current.next_

    def pop(self, index=-1):
        if index == -1:
            index = len(self) - 1
        result = self[index]
        del self[index]
        return result

    def index(self, value):
        current = self.head.next_
        index = 0
        while current:
            if current.val == value:
                return index
            index += 1
            current = current.next_
        raise ValueError(f"{value} is not in list")

    def count(self, value):
        return sum(1 for item in self if item == value)

    def sort(self, key=None, reverse=False):
        if key is None:
            key = lambda x: x
        for i in range(len(self) - 1):
            for j in range(i + 1, len(self)):
                if key(self[i]) > key(self[j]):
                    self[i], self[j] = self[j], self[i]
        if reverse:
            self.reverse()

    def __add__(self, other):
        result = LinkedList()
        current = self.head.next_
        while current:
            result.append(current.val)
            current = current.next_
        current = other.head.next_
        while current:
            result.append(current.val)
            current = current.next_
        return result

    def __iadd__(self, other):
        current = other.head.next_
        while current:
            self.append(current.val)
            current = current.next_
        return self

    def __mul__(self, other):
        result = LinkedList()
        for _ in range(other):
            current = self.head.next_
            while current:
                result.append(current.val)
                current = current.next_
        return result

    def __imul__(self, other):
        result = LinkedList()
        for _ in range(other):
            current = self.head.next_
            while current:
                result.append(current.val)
                current = current.next_
        self.clear()
        self.extend(result)
        return self

    def __contains__(self, item):
        current = self.head.next_
        while current:
            if current.val == item:
                return True
            current = current.next_
        return False

    def __reversed__(self):
        return self.reverse()

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        current1 = self.head.next_
        current2 = other.head.next_
        while current1 and current2:
            if current1.val != current2.val:
                return False
            current1 = current1.next_
            current2 = current2.next_
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        current1 = self.head.next_
        current2 = other.head.next_
        while current1 and current2:
            if current1.val >= current2.val:
                return False
            current1 = current1.next_
            current2 = current2.next_
        return True

    def __gt__(self, other):
        current1 = self.head.next_
        current2 = other.head.next_
        while current1 and current2:
            if current1.val <= current2.val:
                return False
            current1 = current1.next_
            current2 = current2.next_
        return True

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __hash__(self):
        return hash(tuple(self))

    def __bool__(self):
        return self.head.next_ is not None

    def __delitem__(self, index):
        self.remove_at(index)

    def __del__(self):
        current = self.head
        while current:
            next_ = current.next_
            del current
            current = next_


if __name__ == '__main__':
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.remove(1)
    lst2 = LinkedList()
    lst2.append(5)
    lst2.append(3)
    lst2.append(4)
    assert lst < lst2
    lst += lst2
    assert lst == LinkedList([2, 5, 3, 4])
    assert lst[0] == 2
    assert lst[1] == 5
    assert 2 in lst
    assert 6 not in lst
    assert len(lst) == 4
    del lst[0]
    assert lst == LinkedList([5, 3, 4])
    lst.reverse()
    assert lst == LinkedList([4, 3, 5])
    lst.insert(2, 10)
    assert lst == LinkedList([4, 3, 10, 5])
    lst.remove_at(2)
    assert lst == LinkedList([4, 3, 5])
    lst3 = lst.copy()
    assert lst3 == lst
    assert lst3 is not lst
    lst4 = lst.deepcopy()
    assert lst4 == lst
    assert lst4 is not lst
    lst.clear()
    assert lst == LinkedList()
    assert lst3 == LinkedList([4, 3, 5])
    assert lst4 == LinkedList([4, 3, 5])
    lst.extend(lst3)
    assert lst == LinkedList([4, 3, 5])
    assert lst.pop() == 5
    assert lst == LinkedList([4, 3])
    assert lst.index(3) == 1
    assert lst.count(3) == 1
    lst.sort()
    assert lst == LinkedList([3, 4])
    lst.sort(reverse=True)
    assert lst == LinkedList([4, 3])
    lst.sort(key=lambda x: -x)
    assert lst == LinkedList([4, 3])
    lst.sort(key=lambda x: -x, reverse=True)
    assert lst == LinkedList([3, 4])
    lst5 = lst + lst3
    assert lst5 == LinkedList([3, 4, 4, 3, 5])
    lst6 = lst * 2
    assert lst6 == LinkedList([3, 4, 3, 4])
    lst6 *= 2
    assert lst6 == LinkedList([3, 4, 3, 4, 3, 4, 3, 4])
