//
//  main.swift
//  LeetCodeProject
//
//  Created by Michael-Nine on 2019/2/16.
//  Copyright © 2019 Michael. All rights reserved.
//

import Foundation

func myAtoi(_ str: String) -> Int {
    var strArray = [Character]()
    var blank = true
    
    // 将字符串转为数组并去掉头部空格
    for c in str {
        if c == " " && blank {
            continue
        } else if c != " " && blank {
            blank = false
        }
        strArray.append(c)
    }
    
    guard strArray.count > 0 else {return 0}
    let firstChar = strArray.first!
    let firstCharIntValue = firstChar.unicodeScalars.first!.value
    
    guard firstChar == "+" || firstChar == "-" || (firstCharIntValue > 47 && firstCharIntValue < 58) else {return 0}
    
    let isNegative = firstChar == "-"
    if firstChar == "+" || firstChar == "-" {strArray.remove(at: 0)}
    
    var num:Int? = nil
    
    for d in strArray {
        if num == nil && isDigit(d) == false  {
            return 0
        } else {
            if num == nil {
                num = 0
            }
            if isDigit(d) {
                num = num! * 10 + Int(d.unicodeScalars.first!.value) - 48
                if num! > Int32.max {
                    return isNegative ? Int(Int32.min) : Int(Int32.max)
                }
            } else {
                num = isNegative ? num! * -1 : num!
                return num!
            }
        }
    }
    
    if num == nil {
        return 0
    } else {
        return isNegative ? num! * -1 : num!
    }
}

func isDigit(_ char:Character) -> Bool {
    let charInt = char.unicodeScalars.first!.value
    return charInt > 47 && charInt < 58
}

//print(myAtoi("42")) // 42
//print(myAtoi("   -42")) // -42
//print(myAtoi("4193 with words")) // 4193
//print(myAtoi("words and 987")) // 0
//print(myAtoi("-91283472332"))// Int32.min
//print(myAtoi("+")) //0
//print(myAtoi("20000000000000000000"))

func strStr(_ haystack: String, _ needle: String) -> Int {
    if needle.count == 0 {return 0}
    for i in 0..<haystack.count {
        let c = haystack[haystack.index(haystack.startIndex, offsetBy: i)]
        if c == needle[needle.startIndex] {
            let startIndex = haystack.index(haystack.startIndex, offsetBy: i)
            if haystack.count - i < needle.count {return -1}
            let endIndex = haystack.index(startIndex, offsetBy: needle.count)
            let str = haystack[startIndex..<endIndex]
            if str == needle  {return i}
        }
    }
    return -1
}

//print(strStr("hello", "ll"))
//print(strStr("aaaaa", "bba"))
//print(strStr("er", ""))
//print(strStr("a", "ab"))


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}

func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
    var node:ListNode?
    var currentNode:ListNode?
    var lnode1 = l1
    var lnode2 = l2
    var needPlus1 = false
    
    while lnode1 != nil || lnode2 != nil || needPlus1 {
        var newNode:ListNode?
        if lnode1 != nil && lnode2 != nil {
            let res = lnode1!.val + lnode2!.val + (needPlus1 ? 1 : 0)
            newNode = ListNode(dealResult(res, needPlus1: &needPlus1))
        } else if lnode1 != nil {
            let res = lnode1!.val + (needPlus1 ? 1 : 0)
            newNode = ListNode(dealResult(res, needPlus1: &needPlus1))
        } else if lnode2 != nil {
            let res = lnode2!.val + (needPlus1 ? 1 : 0)
            newNode = ListNode(dealResult(res, needPlus1: &needPlus1))
        } else {
            newNode = ListNode(1)
            needPlus1 = false
        }
        if node == nil {
            node = newNode
            currentNode = newNode
        } else {
            currentNode!.next = newNode
            currentNode = currentNode?.next
        }
        lnode1 = lnode1?.next
        lnode2 = lnode2?.next
    }
    return node
}

func dealResult(_ res:Int, needPlus1:inout Bool) -> Int {
    if res >= 10 {
        needPlus1 = true
        return res - 10
    } else {
        needPlus1 = false
        return res
    }
}

//输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
//输出：7 -> 0 -> 8
//原因：342 + 465 = 807
//let node1 = ListNode(2)
//let node2 = ListNode(4)
//let node3 = ListNode(3)
//node1.next = node2
//node2.next = node3
//
//let node4 = ListNode(5)
//let node5 = ListNode(6)
//let node6 = ListNode(4)
//node4.next = node5
//node5.next = node6
//addTwoNumbers(node1, node4) // 708
//
//let node7 = ListNode(5)
//let node8 = ListNode(5)
//addTwoNumbers(node7, node8) // 01
//
//let node9 = ListNode(1)
//let node10 = ListNode(9)
//let node11 = ListNode(9)
//node10.next = node11

//addTwoNumbers(node9, node10) // 001


func countAndSay(_ n: Int) -> String {
    var result = ["1"]
    for _ in 1..<n {
        var temp = [String]()
        var j = 0
        var count = 0
        var c = result.first!
        
        while j < result.count {
            let curNum = result[j]
            if curNum == c {
                count += 1
                j += 1
                continue
            } else {
                temp.append(contentsOf: [String(count), c])
                c = curNum
                count = 0
            }
        }
        if count != 0 {temp.append(contentsOf: [String(count), c])}
        result = temp
    }

    var str = String()
    for c in result {str.append(c)}

    return str
}

//print(countAndSay(1))
//print(countAndSay(2))
//print(countAndSay(3))
//print(countAndSay(4))
//print(countAndSay(5))
//print(countAndSay(6))


//func longestCommonPrefix(_ strs: [String]) -> String {
//    if strs.count == 0 {return ""}
//    var prefix = ""
//    var tag = true
//    var flag = 0
//
//    while tag {
//        var currentPrefix:Character?
//
//        for i in 0..<strs.count {
//            let str = strs[i]
//            if str.count < prefix.count {
//                if i > 0 {prefix.removeLast()}
//                tag = false
//                break
//            }
//            if flag >= str.count {
//                tag = false
//                break
//            }
//            let c = str[str.index(str.startIndex, offsetBy: flag)]
//            if i == 0 {
//                prefix.append(c)
//                currentPrefix = c
//            } else {
//                if c != currentPrefix {
//                    prefix.removeLast()
//                    tag = false
//                    break
//                }
//            }
//        }
//        flag += 1
//    }
//    return prefix
//}

func longestCommonPrefix(_ strs: [String]) -> String {
    if strs.count == 0 {
        return ""
    } else if strs.count == 1 {
        return strs.first!
    } else {
        var prefix = strs.first!
        
        for i in 1..<strs.count {
            let str = strs[i]
            while !str.hasPrefix(prefix) {
                prefix = commonPrefix(str1: prefix, str2: str)
                if prefix.isEmpty {
                    return ""
                }
            }
        }
        return prefix
    }
}

func commonPrefix(str1: String, str2: String) -> String {
    let count = min(str1.count, str2.count)
    var prefix = ""
    
    for i in 0..<count {
        let str1_i = str1[str1.index(str1.startIndex, offsetBy: i)]
        let str2_i = str2[str2.index(str2.startIndex, offsetBy: i)]
        if str1_i == str2_i {
            prefix.append(str1_i)
        } else {
            break
        }
    }
    return prefix
}

//print(longestCommonPrefix(["flower","flow","flight"]))
//print(longestCommonPrefix(["dog","racecar","car"]))
//print(longestCommonPrefix([]))
//print(longestCommonPrefix([""]))
//print(longestCommonPrefix(["aa","a"]))


func generate(_ numRows: Int) -> [[Int]] {
    var r = [[Int]]()
    for i in 0..<numRows {
        var t = [Int]()
        for j in 0...i {
            if j == 0 || j == i {
                t.append(1)
            } else {
                t.append(r[i - 1][j - 1] + r[i - 1][j])
            }
        }
        r.append(t)
    }
    return r
}

//print(generate(5))


func clumsy(_ N: Int) -> Int {
    var minus = [Int]()//保存需要相减数
    var plus = [Int]()//保存需要相加的数
    var t = 0
    var op = 0//通过对4取模获得当前的操作
    
    for i in 0..<N {
        let operationNum = N - i
        
        if op % 4 == 0 {
            t = operationNum
        } else if op % 4 == 1 {
            t *= operationNum
        } else if op % 4 == 2 {
            t /= operationNum
        } else if op % 4 == 3 {
            plus.append(operationNum)
        }
        if i == N-1 || op%4 == 3 {
            minus.append(t)
        }
        op += 1
    }
    
    var res = 0
    // 用求差数组的第一项减去后面所有项
    for i in 0..<minus.count {
        if i == 0 {
            res = minus[i]
        } else {
            res -= minus[i]
        }
    }
    // 求和数组求和
    res += plus.reduce(0) {return $0 + $1}
    
    return res
}


print(clumsy(10))


func bitwiseComplement(_ N: Int) -> Int {
    var res = N
    var flag = 1
    
    for _ in 0...Int(log2((Double(N)))) {
        res ^= flag
        flag <<= 1
    }
    
    return res
}


//print(bitwiseComplement(4194303))
//print(bitwiseComplement(7))
//print(bitwiseComplement(10))


func numPairsDivisibleBy60(_ time: [Int]) -> Int {
    var count = 0
    var countDict = [Int : Int]()
    
    for i in 0..<time.count - 1 {
        if countDict.keys.contains(time[i]) {
            count += countDict[time[i]]!
            countDict[time[i]] = countDict[time[i]]! - 1
        } else {
            for (k, v) in countDict {
                if (k + time[i])%60 == 0 {
                    countDict[k] = v - 1
                }
            }
            var iCount = 0
            for j in (i + 1)..<time.count {
                if (time[i] + time[j]) % 60 == 0 {
                    iCount += 1
                }
            }
            
            if iCount > 0 {
                count += iCount
                countDict[time[i]] = iCount
            }
        }
    }
    
    return count
}


//print(numPairsDivisibleBy60([60,120,60,120,60,120]))
//print(numPairsDivisibleBy60([283,338,207,325,321,166,9,303,344,299,156,443,309,281,264,353,244,369,99,97,66,109,228,164,371,282,69,234,122,239,234,91,304,435,51,213,357,463,246,150,111,494,351,234,145,343,122,361,53,290,373,435,302,287,279,290,122,154,70,72,225,209,65,370,25,253,175,262,336,250,78,201,293,374,325,426,236,106,123,430,393,49,154,250,116,295,9,348,344,107,393,310,424,281,292,466,401,297,13,52,191,414,302,75,155,280,114,388,358,418,475,429,69,465,118,259,294,59,386,256,410,81,176,282,274,166,322,315,28,289,403,283,236,143,397,45,420,59,367,154,19,308,55,484]))


func merge(a:inout [Int], l:Int, h:Int) {
    let mid = (l + h) / 2
    var i = l, j = mid+1
    let t = Array(a)
    
    for k in l...h {
        if i > mid {
            a[k] = t[j]
            j += 1
        } else if j > h {
            a[k] = t[i]
            i += 1
        } else if t[i] <= t[j] {
            a[k] = t[i]
            i += 1
        } else {
            a[k] = t[j]
            j += 1
        }
    }
}


func mergeSort(_ a:inout [Int], l:Int, h:Int) {
    if l == h {return}
    let mid = (l + h) / 2
    mergeSort(&a, l: l, h: mid)
    mergeSort(&a, l: mid + 1, h: h)
    merge(a: &a, l: l, h: h)
}

func exch(a:inout [Int], i:Int, j:Int) {
    if i == j {return}
    a[i] ^= a[j]
    a[j] ^= a[i]
    a[i] ^= a[j]
}

func partision(a:inout [Int], l:Int, h:Int) -> Int {
    var t = a[l], i = l, j = h + 1
    while true {
        repeat {
            i += 1
            if i == h {break}
        } while a[i] < t

        repeat {
            j -= 1
            if j == l {break}
        } while a[j] > t
        
        if i >= j {break}
        exch(a: &a, i: i, j: j)
    }
    exch(a: &a, i: l, j: j)
    return j
}

func quickSort(a:inout [Int], l:Int, h:Int) {
    if l >= h {return}
    let p = partision(a: &a, l: l, h: h)
    quickSort(a: &a, l: l, h: p - 1)
    quickSort(a: &a, l: p + 1, h: h)
}
//
//var a = [3, 12, 44, 9, 1, 21, 16, 31, 11, 7, 5]
//quickSort(a: &a, l: 0, h: a.count-1)
//print(a)


func so(a:[[Int]], startIndex:Int) -> [Int] {
    if a.count == 0 {return []}
    let top = startIndex
    let bottom = a.count-startIndex-1
    if bottom < top {return []}
    let left = startIndex < (a[startIndex].count-1)/2 ? startIndex : (a[startIndex].count-1)/2
    let right = a[startIndex].count-startIndex-1 > left ? a[startIndex].count-startIndex-1 : left
    if right < left || top == bottom && left == right && top != left {return []}
    var res = Array(a[top][left...right])
    if top < bottom {for i in top+1...bottom {res.append(a[i][right])}}
    if top < bottom && left < right {for i in stride(from: right-1, through: left, by: -1) {res.append(a[bottom][i])}}
    if top < bottom && left < right {for i in stride(from: bottom-1, to: top, by: -1) {res.append(a[i][left])}}
    res.append(contentsOf: so(a: a, startIndex: startIndex+1))
    return res;
}

print(so(a: [[1],[2],[3]], startIndex: 0))
print(so(a: [], startIndex: 0))
print(so(a: [[1,2,3,4],[5,6,7,8],[9,10,11,12]], startIndex: 0))//[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(so(a: [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], startIndex: 0))//[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
print(so(a: [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]], startIndex: 0))//[2, 3, 4, 7, 10, 13, 16, 15, 14, 11, 8, 5, 6, 9, 12, 9]
print(so(a: [[2,3]], startIndex: 0))//[2, 3]
print(so(a: [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]], startIndex: 0))//[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
print(so(a: [[1,2,3],[4,5,6],[7,8,9]], startIndex: 0))//[1, 2, 3, 6, 9, 8, 7, 4, 5]
print(so(a: [[2,5],[8,4],[0,-1]], startIndex: 0))
//[[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]] 未通过
////[[1,2,3,4],
// [5,6,7,8],
// [9,10,11,12]
// [13,14,15,16]]

//[[2,3,4],
// [5,6,7],
// [8,9,10],
// [11,12,13],
// [14,15,16]
//]
