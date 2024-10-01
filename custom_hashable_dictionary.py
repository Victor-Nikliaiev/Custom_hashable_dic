class HashableDic:
    """
    A class to create a hashable dictionary.

    A hashable dictionary can be used as a key in another dictionary or as an element in a set.
    """

    def __init__(self, data=None):
        """
        Initialize the HashableDic object.

        Args:
            data (dict): The data to use for the dictionary. Defaults to an empty dictionary.
        """
        if data is None:
            data = {}
        self.data = {}
        for key, value in data.items():
            self.add(key, value) 
        self._hash = None
    
    def __eq__(self, other):
        """
        Compares two HashableDic objects for equality.

        Args:
            other (HashableDic): The other HashableDic object to compare.

        Returns:
            bool: True if the two objects are equal, False otherwise.
        """
        return isinstance(other, HashableDic) and self.data == other.data
    
    def __hash__(self):
        """
        Returns the hash value of the dictionary.

        The hash value is calculated only once and then stored. The hash value is
        the hash of a tuple of the sorted items of the dictionary. This ensures that
        the hash value is the same for two dictionaries with the same items, even
        if the order of the items is different.
        """
        if self._hash == None:
            self._hash = hash(tuple(sorted(self.data.items())))
        return self._hash
    
    def __repr__(self):
        """
        Returns a string representation of the dictionary.

        The string representation is a string in the same format as a standard
        dictionary. The string representation is useful for debugging and for
        logging.

        Returns:
            str: A string representation of the dictionary.
        """
        return str(self.data)
    
    def add(self, *args):
        """
        Adds a key-value pair to the dictionary.

        Args:
            key (Any): The key of the item to add.
            value (Any): The value of the item to add.

        Raises:
            ValueError: If the dictionary contains a different structure.
        """ 
        count = len(args)
        if not count:
            raise ValueError("At least one argument is required.")
        
        if count == 1:
            [dictionary] = args
            if type(dictionary) != dict:
                raise ValueError("For one value a dictionary is required.")
            if not self._isDictionaryAddable(dictionary):
                raise ValueError("Dictionary with different structure cannot be added.")
            dictionary = self._make_hashable(dictionary)
            if dictionary in self.data.keys() or dictionary in self.data.values():
                return
            self.data.update(dictionary)
            self._hash = None
            return
        
        [key, value] = args
        if not key or not value:
            raise ValueError("Both key and value are required, or at least dictionary.")
        key = self._make_hashable(key)
        value = self._make_hashable(value)
        self.data[key] = value  
        self._hash = None

    

    def _isDictionaryAddable(self, dictionary):
        if not self.data:
            return True

        data_item = list(self.data.items())[0]
        dict_item = list(dictionary.items())[0]

        if type(data_item[0]) != type(dict_item[0]):
            return False
        if type(data_item[1]) != type(dict_item[1]):
            return False
        return True        

    def remove(self, key):
        """
        Removes a key-value pair from the dictionary.

        Args:
            key (Any): The key of the item to remove.

        Raises:
            KeyError: If the key is not in the dictionary.
        """
        key = self._make_hashable(key)
        if key in self.data:
            del self.data[key]
            self._hash = None

    def get(self, key):
        """
        Retrieves a value by its key.

        Args:
            key (Any): The key of the item to retrieve.

        Returns:
            Any: The value associated with the given key.

        Raises:
            KeyError: If the key is not in the dictionary.
        """
        key = self._make_hashable(key)
        return self.data.get(key)

    def __getitem__(self, key):
        """
        Retrieves a value by its key.

        Args:
            key (Any): The key of the item to retrieve.

        Returns:
            Any: The value associated with the given key.

        Raises:
            KeyError: If the key is not in the dictionary.
        """
        key = self._make_hashable(key)        
        return self.data[key]
    
    def __setitem__(self, key, value):
        """
        Sets a value for a given key.

        Args:
            key (Any): The key of the item to set.
            value (Any): The value to set for the given key.

        Raises:
            KeyError: If the key is not in the dictionary.
        """

        key = self._make_hashable(key)
        value = self._make_hashable(value)
        self.data[key] = value
        self._hash = None
        
    def __iter__(self):
        """
        Allows iteration over the dictionary's items.

        Yields:
            tuple: A tuple of each key-value pair in the dictionary, in the order they were added.
        """
        for key, value in self.data.items():             
            yield key, value  

    def __contains__(self, key):
        """
        Checks if a key exists in the dictionary.

        Args:
            key (Any): The key to check for.

        Returns:
            bool: True if the key exists in the dictionary, False otherwise.
        """
        key = self._make_hashable(key)
        return key in self.data
    
    def _make_hashable(self, item):
        """
        Converts the given item into a hashable object.

        If the item is a dictionary, it is converted into a HashableDic object.
        Otherwise, the item is returned unchanged.

        Args:
            item (Any): The item to make hashable.

        Returns:
            Any: The hashable version of the item.
        """
        if isinstance(item, dict):
            return HashableDic({self._make_hashable(k): self._make_hashable(v) for k, v in item.items()})
        return item
    


 


 

