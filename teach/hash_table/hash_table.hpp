#ifndef __ICY_HASH_TABLE__
#define __ICY_HASH_TABLE__

const int HASH_SIZE = 50000017;

#include <cstdbool>

// Linear Probing from toi10_catcodes
struct hash_table {
  int have_key[HASH_SIZE], key_value[HASH_SIZE];
  void add_key(int key, int value) {
    int current_key = key % HASH_SIZE;
    while(key_value[current_key] != 0) {
      current_key = (current_key + 1) % HASH_SIZE;
    }
    key_value[current_key] = value;
    have_key[current_key] = key;
  }
  int query_key(int key) {
    int current_key = key % HASH_SIZE;
    while(key_value[current_key] != 0) {
      if(have_key[current_key] == key) {
        return key_value[current_key];
      }
      current_key = (current_key + 1) % HASH_SIZE;
    }
    return 0;
  }
};

#endif