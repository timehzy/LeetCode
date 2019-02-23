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
let node1 = ListNode(2)
let node2 = ListNode(4)
let node3 = ListNode(3)
node1.next = node2
node2.next = node3

let node4 = ListNode(5)
let node5 = ListNode(6)
let node6 = ListNode(4)
node4.next = node5
node5.next = node6
addTwoNumbers(node1, node4) // 708

let node7 = ListNode(5)
let node8 = ListNode(5)
addTwoNumbers(node7, node8) // 01

let node9 = ListNode(1)
let node10 = ListNode(9)
let node11 = ListNode(9)
node10.next = node11

addTwoNumbers(node9, node10) // 001


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

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix([]))
print(longestCommonPrefix([""]))
print(longestCommonPrefix(["aa","a"]))

