class HashableDic:
    def __init__(self, data=None):
        self.data = {}
        self._hash_needs_update = True
        if data:
            for key, value in data.items():
                self.add(key, value) 
        self._hash = None
    
    def __eq__(self, other) -> bool:
        if isinstance(other, HashableDic):
            return self.data == other.data
        return False
    
    def __hash__(self) -> int:
        if self._hash_needs_update:
            self._hash = hash(tuple(sorted(self.data.items())))
            self._hash_needs_update = False         
        return self._hash
    
    def __repr__(self) -> str:
        return str(self.data)
    
    def add(self, *args):
        if not args:
            raise ValueError("At least one argument is required.")
        
        if len(args) == 1:
            dictionary = args[0]
            if not isinstance(dictionary, dict):
                raise ValueError("Expected a dictionary as the argument.")
            if not self._is_dictionary_addable(dictionary):
                raise ValueError("Dictionary with different structure cannot be added.")
            dictionary = self._make_hashable(dictionary)
            self.data.update(dictionary)
        else: 
            key, value = args
            key = self._make_hashable(key)
            value = self._make_hashable(value)
            self.data[key] = value

        self._hash_needs_update = True  

    def _is_dictionary_addable(self, dictionary: dict) -> bool:
        if not self.data:
            return True

        first_key, first_value = next(iter(dictionary.items()))
        test_key, test_value = next(iter(self.data.items()))

        return isinstance(first_key, type(test_key)) and isinstance(first_value, type(test_value))

    def remove(self, key):
        key = self._make_hashable(key)
        if key in self.data:
            del self.data[key]
            self._hash_needs_update = True

    def get(self, key):
        key = self._make_hashable(key)
        return self.data.get(key)

    def __getitem__(self, key):
        key = self._make_hashable(key)        
        return self.data[key]
    
    def __setitem__(self, key, value):
        key = self._make_hashable(key)
        value = self._make_hashable(value)
        self.data[key] = value
        self._hash_needs_update = True
        
    def __iter__(self):
        return iter(self.data.items())

    def __contains__(self, key):
        key = self._make_hashable(key)
        return key in self.data
    
    def _make_hashable(self, item):
        if isinstance(item, dict):
            return HashableDic({self._make_hashable(k): self._make_hashable(v) for k, v in item.items()})
        
        if isinstance(item, list):
            return tuple(self._make_hashable(i) for i in item)
        
        if isinstance(item, tuple):
            return tuple(self._make_hashable(i) for i in item)
        
        if isinstance(item, set):
            return frozenset(self._make_hashable(i) for i in item)
        
        return item
    


 


 

