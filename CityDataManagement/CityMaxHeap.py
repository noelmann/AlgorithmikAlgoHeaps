from typing import List
from CityDataManagement.City import City
from CityDataManagement.AbstractCityHeap import AbstractCityHeap


class CityMaxHeap(AbstractCityHeap):
    """
    Class with the responsibility to create a Max-Heap-structure based on unstructured data.
    (Every Parents Key must be greater than its children Key)

    """

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        """
        Creation of a Max-City-Heap.

        :param raw_city_data:    A unsorted List of Cities
        :param recursive:    Should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
        :param floyd:       Should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.
                            For removal the approach specified in :param recursiv will be used.
        """
        super().__init__(raw_city_data, recursive, floyd)

    def heapify_up_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative upwards.
        """
        i = self.currentHeapLastIndex - 1
        while self.has_parent(i):
            p = self.get_parent_index(i)
            if self.get_city_population(i) > self.get_parent_population(i):
                self.swap_nodes(i,p)
                i = p

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        # TODO: implement me!
        ...

    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions for a Max-Heap via Floyds Heap Construction Algorithmus.

        """
        # TODO: implement me!
        ...

    def heapify_down_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        i = 0
        while self.has_left_child(i):
            BiggestChildIndex = self.get_left_child_index(i)

            if self.has_right_child(i) and self.get_right_child_population(i) > self.get_left_child_population(i):
                BiggestChildIndex = self.get_right_child_index(i)

            if self.get_city_population(BiggestChildIndex) > self.get_city_population(i):
                self.swap_nodes(i, BiggestChildIndex)
                i = BiggestChildIndex
            else:
                return


    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        # TODO: implement me!
        ...

    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        root = self.heapStorage[0]
        print("Old root:"+root)
        self.heapStorage[0] = self.heapStorage[-1]
        self.heapStorage.pop()
        self.heapify_down_iterative()
        print("New root:"+self.heapStorage[0])