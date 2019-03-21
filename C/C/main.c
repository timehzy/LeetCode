//
//  main.c
//  C
//
//  Created by Michael-Nine on 2019/3/9.
//  Copyright © 2019 Michael. All rights reserved.
//

#include <stdio.h>

//uint32_t count = 0;
//while (n) {
//    n &= n-1;
//    count++;
//}
//return count;
int hammingWeight(uint32_t n) {
    uint32_t c = 0;
    while (n == 1) {
        if ((n&1) == 1) {// 最右位是1
            c++;
        }
        n >>= 1;
    }
    return c;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    printf("Hello, World!\n");
    return 0;
}
