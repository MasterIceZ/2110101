#ifndef __STUDENT_H_
#define __STUDENT_H_

#include <vector>
#include "queue.h"

#include <bits/stdc++.h>

template <typename T>
void CP::queue<T>::remove_many(std::vector<size_t> pos)
{
  // your code here
  size_t cur = mFront, pos_index = 0, queue_index = mFront;
  sort(pos.begin(), pos.end());
  for(size_t i=0; i<mSize; ++i) {
    if(pos_index == pos.size() || i != pos[pos_index]) {
      mData[cur] = mData[queue_index];
      cur = (cur + 1) % mCap;
    }
    else if(i == pos[pos_index]) {
      pos_index += 1;
    }
    queue_index = (queue_index + 1) % mCap;
  }
  mSize -= pos.size();
}

#endif
