#ifndef __STUDENT_H_
#define __STUDENT_H_

#include <vector>
#include "queue.h"

#include <bits/stdc++.h>

template <typename T>
void CP::queue<T>::remove_many(std::vector<size_t> pos)
{
  // your code here
  size_t it = 0, deleting = 1;
  sort(pos.begin(), pos.end());
  for(size_t i=(mFront+pos[it]+1) % mCap; i<(mFront % mCap); i=(i + 1) % mCap) {
    if(1 + it < pos.size() && i == (mFront+pos[1 + it] % mCap)) {
      // std::cerr << "SKIPPING" << mData[i] << "\n";
      deleting++;
      it++;
      continue;
    }
    mData[(mFront + i - deleting) % mCap] = mData[i];
  }
  mSize -= it + 1;
  size_t i = 0;
  while(pos[0] == 0 && pos[(mFront + i) % mCap] == i && i < it) {
    i++;
  }
  mFront += i;
}

#endif
