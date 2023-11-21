#include <iostream>
#include "hash_table.hpp"

using namespace std;

hash_table h;

int main() {
  h.add_key(0, 20);
  h.add_key(30, 1);
  printf("h[1] = %d\n", h.query_key(1));
  printf("h[0] = %d\n", h.query_key(0));
  printf("h[9] = %d\n", h.query_key(9));
  return 0;
}