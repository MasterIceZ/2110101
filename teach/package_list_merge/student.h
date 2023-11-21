#ifndef __STUDENT_H_
#define __STUDENT_H_
#include <algorithm>

template <typename T>
void CP::list<T>::merge(CP::list<CP::list<T>> &ls) {
  //write your code here
  for(auto &cur: ls) {
    mHeader->prev->next = cur.mHeader->next;
    cur.mHeader->next->prev = mHeader->prev;
    mHeader->prev = cur.mHeader->prev;
    cur.mHeader->prev->next = mHeader;
    cur.mHeader->prev = cur.mHeader;
    cur.mHeader->next = cur.mHeader;
    mSize = mSize + cur.size();
    cur.mSize = 0;
  }
}

#endif
