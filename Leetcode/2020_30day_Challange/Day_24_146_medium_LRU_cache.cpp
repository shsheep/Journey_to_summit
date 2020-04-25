class LRUCache {
public:
    int size;
    int limit;
    int time;
    
    unordered_map<int, int> dict;
    unordered_map<int, int> referenced;
    
    LRUCache(int capacity) {
        size = 0;
        limit = capacity;
        time = 0;
    }
    
    int get(int key) {
        ++time;
        if (dict.find(key) == dict.end())
            return -1;
        
        referenced[key] = time;
        return dict[key];
    }
    
    void put(int key, int value) {
        int lru_key, lru_time = INT_MAX;
        ++time;
        if (dict.find(key) != dict.end()) {
            dict[key] = value;
            referenced[key] = time;
            return;
        }
        dict[key] = value;
        referenced[key] = time;
        ++size;
        if (size > limit) {
            for (unordered_map<int, int>::iterator it = referenced.begin(); it != referenced.end(); ++it) {
                if (it->second < lru_time) {
                    lru_key = it->first;
                    lru_time = it->second;
                }
            }
            dict.erase(lru_key);
            referenced.erase(lru_key);
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

/**
 * Runtime: 292 ms, faster than 11.92% of C++ online submissions for LRU Cache.
 * Memory Usage: 35.4 MB, less than 100.00% of C++ online submissions for LRU Cache.
 **/
