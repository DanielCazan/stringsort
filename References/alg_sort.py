class ArraySorter:
    def __init__(self, sortable_array, verbose=False):
        self.sortable_array = sortable_array
        self.verbose=verbose

    def sort_functions(
        self,
        sort_op,
        verbose=True
    ):
        self.verbose = verbose

        if sort_op == "selection":
            print("Performing a selection sort")
            self._sort_selection()
        elif sort_op == "insertion":
            print("Performing an insertion sort")
            self._sort_insertion()
        elif sort_op == "quick":
            print("Performing a quick sort")
            self._sort_quick()
        elif sort_op == "merge":
            print("Performing a merge sort")
            self._sort_merge()
        elif sort_op == "bubble":
            print("Performing a bubble sort")
            self._sort_bubble()
        elif sort_op == "bucket":
            print("Performing a bucket sort")
            self._sort_bucket()
        elif sort_op == "heap":
            print("Performing a heap sort")
            self._sort_heap_min()
        else:
            print("Unsupported sort type")

    # https://www.geeksforgeeks.org/heap-sort/
    def _sort_heap_min(self):
        print("O(nlogn) to sort")
        print("Re-ordering to match rules of a min-heap")
        print("\t\t1) Every parent has child nodes that are smaller than its self")
        print("\t\t2) Every level of the tree is full except form last, and full left to right")
        print("\t\tAdditionally, a heap is special because it can be stored / treated as an array")

        sortable_array = self.sortable_array

        # build the heap, from the end to the beginning
        # range(start, end if this is true, step value)
        for node in range(len(sortable_array)-1, -1, -1):
            self._build_heap_min(sortable_array, len(sortable_array), node)

        # to 'sort' extract out by swapping top (smallest) with last, then re-hepify
        # re-hepifying will produce no changes except at the top which will just go straight down a few levels
        for node in range(len(sortable_array)-1, 0, -1):
            print("Swapping root [0]{0} with last node [{1}]{2}".format(
                sortable_array[0], node, sortable_array[node]))
            sortable_array[0], sortable_array[node] = sortable_array[node], sortable_array[0]
            # the loop acts as a countdown for 'node', since the size of the array we check is constantly 1 smaller
            # the array isn't changing but we do not look past it
            self._build_heap_min(sortable_array, node, 0)

        # the array was extracted in reverse order, can reverse it
        print("Reversed min-array: {0}".format(list(reversed(sortable_array))))

    def _build_heap_min(self, sortable_array, size_of_heap, current_root):
        if self.verbose:
            print("\nChecking root [{0}]{1} from array {2}".format(
                current_root, sortable_array[current_root], sortable_array))

        smallest_index = current_root
        left_child = self._heap_left_child(current_root)
        right_child = self._heap_right_child(current_root)

        # if the child exists and its value is smaller, mark it
        if left_child < size_of_heap and sortable_array[left_child] < sortable_array[current_root]:
            smallest_index = left_child
        if right_child < size_of_heap and sortable_array[right_child] < sortable_array[smallest_index]:
            smallest_index = right_child
        if self.verbose:
            left_value = right_value = -1
            if left_child < size_of_heap:
                left_value = sortable_array[left_child]
            if right_child < size_of_heap:
                right_value = sortable_array[right_child]
            print("\tComparing (left)[{0}]{1} <- (root)[{2}]{3} -> (right)[{4}]{5} \t (smallest) [{6}]".format(
                left_child, left_value,
                current_root, sortable_array[current_root],
                right_child, right_value,
                smallest_index
            ))

        # see if we need to do any swaps
        if smallest_index != current_root:
            if self.verbose:
                print("\tSwapping [{0}]{1} and [{2}]{3}".format(
                    smallest_index, sortable_array[smallest_index],
                    current_root, sortable_array[current_root]
                ))
            # can swap elements in an array directly instead of doing 'swap'
            sortable_array[smallest_index], sortable_array[current_root] = \
                sortable_array[current_root], sortable_array[smallest_index]
            # then check if the tree needs adjusting on the index we just changed
            self._build_heap_min(sortable_array, size_of_heap, smallest_index)
        if self.verbose:
            print("Build for root {0}.  Current: \t{1}".format(current_root, sortable_array))

    @staticmethod
    def _heap_left_child(parent_index):
        return 2 * parent_index + 1

    @staticmethod
    def _heap_right_child(parent_index):
        return 2 * parent_index + 2

    @staticmethod
    def _heap_parent(child_index):
        return (child_index - 1) // 2

    def _sort_bucket(self, sortable_array=None):
        if sortable_array is None:
            print("Avg is O(n+numBuckets), Worse could be O(n2)")
            print("\tSplit set into multiple buckets.  Insert-sort into buckets.  Concat back up")
            sortable_array = self.sortable_array

        print("\tIf range unknown, can traverse once to determine maximum")
        max_value = 0
        for elem in sortable_array:
            if elem > max_value:
                max_value = elem

        print("\tChoosing 5 buckets, the number is slightly arbitrary")
        bucket_1 = []
        bucket_2 = []
        bucket_3 = []
        bucket_4 = []
        bucket_5 = []
        for elem in sortable_array:
            if elem < max_value // 5:
                self._insert_into_array(bucket_1, elem)
            elif elem < max_value // 5 * 2:
                self._insert_into_array(bucket_2, elem)
            elif elem < max_value // 5 * 3:
                self._insert_into_array(bucket_3, elem)
            elif elem < max_value // 5 * 4:
                self._insert_into_array(bucket_4, elem)
            else:
                self._insert_into_array(bucket_5, elem)
            if self.verbose:
                print("\tInserted {0}.  Buckets: [1]{1} [2]{2} [3]{3} [4]{4} [5]{5}".format(
                    elem, bucket_1, bucket_2, bucket_3, bucket_4, bucket_5
                ))
        sorted_list = bucket_1 + bucket_2 + bucket_3 + bucket_4 + bucket_5
        print("Sorted list: {0}".format(sorted_list))

    def _insert_into_array(self, sortable_array, new_element):
        for i in range(len(sortable_array)):
            if sortable_array[i] > new_element:
                sortable_array.insert(i, new_element)
                return
        sortable_array.append(new_element)

    def _sort_bubble(self):
        print("O(n2) - Easy to implement, very bad")
        print("\tFor every two numbers, swap if larger is to the right.  Repeat until no more changes")

        sortable_array = self.sortable_array

        did_swap = True
        while did_swap:
            did_swap = False
            for i in range(len(sortable_array)-1):
                if sortable_array[i] > sortable_array[i+1]:
                    if self.verbose:
                        print("\tSwapping [{0}]{1} and [{2}]{3} in array {4}".format(
                            i, sortable_array[i], i+1, sortable_array[i+1], sortable_array
                        ))
                    self._swap(sortable_array, i, i+1)
                    did_swap = True
        print("Swapped array: {0}".format(sortable_array))

    def _sort_merge(self, sortable_array=None):
        if sortable_array is None:
            print("Divide&Conquer. Good for large lists that don't fit in memory.  O(n log n)")
            print("\tDivide list into two halves, recursive.  Merge back up recursively")
            sortable_array = self.sortable_array
        print("\tSort merging array: {0}".format(sortable_array))

        if len(sortable_array) < 2:
            return sortable_array

        mid_index = len(sortable_array) // 2

        left_half = sortable_array[:mid_index]
        right_half = sortable_array[mid_index:]

        print("\tSort merging [left] {0} [right] {1}".format(left_half, right_half))
        sorted_left = self._sort_merge(left_half)
        sorted_right = self._sort_merge(right_half)
        sorted_array = self._merge_sorted(sorted_left, sorted_right)
        print("Sorted array: {0}".format(sorted_array))
        return sorted_array

    @staticmethod
    def _merge_sorted(array_1, array_2):
        print("\t\tMerging [1]: {0}".format(array_1))
        print("\t\tMerging [2]: {0}".format(array_2))
        a1 = 0
        a2 = 0
        sorted_array = []
        while a1 < len(array_1) and a2 < len(array_2):
            if array_1[a1] < array_2[a2]:
                sorted_array.append(array_1[a1])
                a1=a1+1
            else:
                sorted_array.append(array_2[a2])
                a2=a2+1
        while a1 < len(array_1):
            sorted_array.append(array_1[a1])
            a1 = a1+1
        while a2 < len(array_2):
            sorted_array.append(array_2[a2])
            a2 = a2+1
        print("\t\tMerged sorted: {0}".format(sorted_array))
        return sorted_array

    def _sort_quick(self, sortable_array=None):
        if sortable_array is None:
            print("Divide&Conquer. Slightly unstable. Space O(logn). Avg O(n log n) Median O(n) Worst O(n^2). Fast in-place")
            print("Take a pivot value (usually mid). Move values to left/right. Repeat till recombine back out")
            sortable_array = self.sortable_array
        print("Array: {0}".format(sortable_array))

        mid_index = len(sortable_array) // 2
        array_less = []
        array_greater = []
        array_equal = []

        if len(sortable_array) > 1:
            for i in range(len(sortable_array)):
                if sortable_array[i] < sortable_array[mid_index]:
                    array_less.append(sortable_array[i])
                elif sortable_array[i] > sortable_array[mid_index]:
                    array_greater.append(sortable_array[i])
                else:
                    array_equal.append(sortable_array[i])
            sorted_list = self._sort_quick(array_less) + self._sort_quick(array_equal) + self._sort_quick(array_greater)
        else:
            sorted_list = sortable_array
        print("Quick sorted pass: {0}".format(sorted_list))
        return sorted_list

    def _sort_insertion(self):
        print("Simple. Stable. In-Place.  O(n) to add to sorted list.  O(n^2) if unsorted")
        print("Takes each element.  Inserts it into correct place of sorted (left) part of list.  Can be an insert")

        sortable_array = self.sortable_array
        print("Array: {0}".format(sortable_array))
        for index_fwd in range(1, len(sortable_array)):
            if sortable_array[index_fwd] >= sortable_array[index_fwd-1]:
                if self.verbose:
                    print("\tElement [{0}]{1} is already greater than {2}".format(
                        index_fwd, sortable_array[index_fwd], sortable_array[index_fwd-1]))
                    continue
            for index_insert in range(index_fwd):
                if sortable_array[index_fwd] < sortable_array[index_insert]:
                    print("\t\tElement [{0}]{1} is smaller than [{2}]{3}".format(
                        index_fwd, sortable_array[index_fwd], index_insert, sortable_array[index_insert]))
                    sortable_array.insert(index_insert, sortable_array[index_fwd])
                    del sortable_array[index_fwd+1]
                    break
            print("\nPost Selection sort: {0}\n".format(sortable_array))

    def _sort_selection(self):
        print("Simple. Not-stable. In-place. O(n^2), but O(n) actual moves.")
        print("Search for smallest element, then swap it with 1st element")

        sortable_array = self.sortable_array
        print("Array: {0}".format(sortable_array))
        for i in range(len(sortable_array)):
            smallest = i
            for j in range(i+1, len(sortable_array)):
                if sortable_array[j] < sortable_array[smallest]:
                    smallest = j
                    if self.verbose:
                        print("\t\t[{0}]{1} was smaller than [{2}]{3}".format(
                            j, sortable_array[j], smallest, sortable_array[smallest]))
            print("\t\tSwapping [{0}]{1} to [{2}]".format(smallest, sortable_array[smallest], i))
            self._swap(sortable_array, i, smallest)
            print("\tNew array: {0}\n".format(sortable_array))
        print("\nPost Selection sort: {0}\n".format(sortable_array))

    @staticmethod
    def _swap(
            sortable_array,
            index_1,
            index_2
    ):
        # temp = sortable_array[index_1]
        # sortable_array[index_1] = sortable_array[index_2]
        # sortable_array[index_2] = temp
        sortable_array[index_1], sortable_array[index_2] = sortable_array[index_2], sortable_array[index_1]