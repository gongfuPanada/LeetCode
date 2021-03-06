#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 fuel <fuel@fuel-3330>
#
# Distributed under terms of the MIT license.

import collections
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        N = len(num)
        if N<4: return []
        num.sort()
        Min,Max = num[0],num[-1];
        res = []
        sum2Pair = collections.defaultdict(list)
        # 2-sum to list of index-pairs , int->[(int,int)]

        # for all uniq pair of nums (i,j), collect two-sum
        for i in xrange(N-1):
            if(num[i]+Max*3<target): continue # prune
            if(num[i]+Min*3>target): break
            for j in xrange(i+1,N):
                if j!=i+1 and num[j]==num[j-1]: continue

                S2=num[i]+num[j];
                if(S2+Max*2<target): continue # prune
                if(S2+Min*2>target): break
                sum2Pair[num[i]+num[j]].append((i,j))
        # print sum2Pair
        sum2s = sorted(sum2Pair.keys())

        # do two-sum on two-sums
        L,R = 0,len(sum2s)-1
        while(L<=R):
            # print "L,R =",L,R
            sum4 = sum2s[L]+sum2s[R]
            if(sum4==target):
                # print sum2Pair[sum2s[L]],sum2Pair[sum2s[R]]
                for i1,i2 in sum2Pair[sum2s[L]]:
                    if i1!=0 and num[i1]==num[i1-1]: continue
                    for i3,i4 in sum2Pair[sum2s[R]]:
                        if i2<i3: # valid quadruplet
                            if i3!=i2+1 and num[i3]==num[i3-1]: continue
                            res.append([num[i1],num[i2],num[i3],num[i4]])
                L+=1;R-=1
            elif(sum4<target): L+=1
            else: R-=1

        return res

if __name__ == "__main__":
    fourSum = Solution().fourSum
    print fourSum([1,0,-1,0,-2,2],0)
    print fourSum([-3,-2,-1,0,0,1,2,3], 0)
    print fourSum([-1,-5,-5,-3,2,5,0,4],-7)
    print fourSum([1,1,1,1,1,1,2,2],5)
    print fourSum([0,0,0,0],0)
