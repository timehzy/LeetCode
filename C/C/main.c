//
//  main.c
//  C
//
//  Created by Michael-Nine on 2019/3/9.
//  Copyright © 2019 Michael. All rights reserved.
//

#include <stdio.h>
#include <stdbool.h>

//Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

//bool hasCycle(struct ListNode *head) {
//    if (head == NULL || head->next == NULL) return false;
//    struct ListNode *slow = head;
//    struct ListNode *fast = head->next;
//    while (slow->val != fast->val) {
//        if (fast == NULL || fast->next == NULL || fast->next->next == NULL) return false;
//        slow = slow->next;
//        fast = fast->next->next;
//    }
//    return true;
//}
bool hasCycle(struct ListNode *head) {
    if (head == NULL || head->next == NULL) return false;
    
    struct ListNode *slow = head, *fast = head;
    
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (fast && fast->val == slow->val) return true;
    }
    return false;
}

void merge(int* nums1, int m, int* nums2, int n) {
    for (int i = m; i < m + n; i++) {
        nums1[i] = nums2[i - m];
        for (int j=0; j < i; j++) {
            if (nums1[i] < nums1[j]) {
                int t = nums1[i];
                for (int k = i; k > j; k--) {
                    nums1[k] = nums1[k - 1];
                }
                nums1[i] = t;
                break;
            }
        }
    }
}

bool isBadVersion(int version) {
    return version > 1;
}

int firstBadVersion(int n) {
    // 若n不是错误版本，则翻倍向后找到错误版本，然后与最近的正确版本形成区间进行折半查找；若n是错误版本，则直接进行折半查找
    int firstBadVersion = n;
    int lastGoodVersion = 0;
    while (!isBadVersion(firstBadVersion)) {
        lastGoodVersion = firstBadVersion;
        firstBadVersion += firstBadVersion;
    }

    int mid = (firstBadVersion + lastGoodVersion) / 2;
    while (firstBadVersion - lastGoodVersion > 0) {
        if (isBadVersion(mid)) {
            firstBadVersion = mid - 1;
        } else {
            lastGoodVersion = mid + 1;
        }
        mid = (firstBadVersion + lastGoodVersion) / 2;
    }

    return isBadVersion(mid) ? mid : mid + 1;
}

int missingNumber(int* nums, int numsSize) {
    int t1 = 0, t2 = numsSize;
    for (int i=0; i<numsSize; i++) {
        t1 += nums[i];
        t2 += i;
    }
    return t2 - t1;
}

uint32_t reverseBits(uint32_t n) {
    uint32_t res = 0;
    for (int i=0; i<32; i++) {
        uint32_t c = (n >> i) & 1;
        res |= (c << (31 - i));
    }
    return res;
}

int hammingDistance(int x, int y) {
    int res = 0;
    for (int i=0; i<32; i++) if (((x >> i) & 1) != ((y >> i) & 1)) res++;
    return res;
}

int main(int argc, const char * argv[]) {
//    struct ListNode node1;
//    struct ListNode node2;
//    struct ListNode node3;
//    struct ListNode node4;
//    struct ListNode node5;
//    node1.val = 1;
//    node2.val = 2;
//    node3.val = 3;
//    node4.val = 4;
//    node5.val = 5;
//
//    node1.next = &node2;
//    node2.next = &node3;
//    node3.next = &node1;
//
//    bool has = hasCycle(&node1);
//    int nums1[6] = {1,2,3,0,0,0};
//    int nums2[3] = {2,5,6};
//    merge(nums1, 3, nums2, 3);//[1,2,2,3,5,6]
//    printf("%d", firstBadVersion(4));
//    printf("%d", firstBadVersion(2));
    
//    int a[] = {3,0,1};
//    int b[] = {9,6,4,2,3,5,7,0,1};
//    printf("%d", missingNumber(a, 3));
//    printf("%d", missingNumber(b, 9));
    
    printf("%d", reverseBits(43261596));
    return 0;
}
