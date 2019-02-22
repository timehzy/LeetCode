//
//  main.swift
//  SwiftAlgo
//
//  Created by haozhenyi on 2019/2/19.
//  Copyright © 2019 Michael. All rights reserved.
//

import Foundation

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

//func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
//    var nodeArr = [ListNode?]()
//    var result = head
//    var node = head
//
//    while node != nil {
//        nodeArr.append(node)
//        node = node?.next
//    }
//
//    if n == nodeArr.count {
//        result = head?.next
//    } else {
//        nodeArr[nodeArr.count - n - 1]?.next = nodeArr[nodeArr.count - n - 1]?.next?.next
//    }
//    return result
//}

func removeNthFromEnd(_ head: ListNode?, _ n: Int) -> ListNode? {
    var count = n
    var node1 = head
    var node2 = head
    
    while count > 0 {
        if node1?.next != nil {
            node1 = node1?.next
            count -= 1
        } else {
            return head?.next
        }
    }
    
    while node1?.next != nil {
        node1 = node1?.next
        node2 = node2?.next
    }
    
    node2?.next = node2?.next?.next
    return head
}

let n1 = ListNode(1)
let n2 = ListNode(2)
let n3 = ListNode(3)
let n4 = ListNode(4)
let n5 = ListNode(5)
let n7 = ListNode(7)

//n1.next = n3
//n3.next = n5
//n2.next = n4
//n4.next = n7



//removeNthFromEnd(n1, 2)





//func reverseList(_ head: ListNode?) -> ListNode? {
//    var a = head
//    var previous:ListNode? = nil
//    var temp:ListNode?
//
//    while a != nil {
//        temp = a?.next
//        a?.next = previous
//        previous = a
//        a = temp
//    }
//
//    return previous
//}


func reverseList(_ head: ListNode?) -> ListNode? {
    if head == nil || head?.next == nil {
        return head
    }
    let h = reverseList(head?.next)
    head?.next?.next = head
    head?.next = nil
    return h
}

//let node = reverseList(n1)
//print(node)



func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
    var n1 = l1
    var n2 = l2
    var newNode:ListNode?

    if n1 != nil && n2 != nil {
        if n1!.val < n2!.val {
            newNode = n1
            n1 = n1?.next
        } else {
            newNode = n2
            n2 = n2?.next
        }
    } else if n1 != nil {
        newNode = n1
        n1 = n1?.next
    } else if n2 != nil {
        newNode = n2
        n2 = n2?.next
    }
    let res = newNode


    while n1 != nil && n2 != nil {
        if n1!.val < n2!.val {
            newNode?.next = n1
            n1 = n1?.next
        } else {
            newNode?.next = n2
            n2 = n2?.next
        }
        newNode = newNode?.next
    }

    if n1 != nil {
        newNode?.next = n1
    } else if n2 != nil {
        newNode?.next = n2
    }

    return res
}

//func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
//    if l1 == nil{
//        return l2
//    }
//    if l2 == nil{
//        return l1
//    }
//    var res:ListNode?
//    if l1!.val >= l2!.val{
//        res = l2
//        res?.next = mergeTwoLists(l1,l2?.next)
//    }else{
//        res = l1
//        res?.next = mergeTwoLists(l1?.next,l2)
//    }
//    return res
//}

//let re = mergeTwoLists(n1, n2)
//print(re)

extension ListNode : Hashable {
    public func hash(into hasher: inout Hasher) {
        hasher.combine(self.val)
    }
    
    public static func == (lhs: ListNode, rhs: ListNode) -> Bool {
        return lhs.val == rhs.val
    }
}

func isPalindrome(_ head: ListNode?) -> Bool {
    if head == nil || head?.next == nil {return true}
    var table = [ListNode : Int]()
    var node = head
    while node != nil {
        let val = table[node!]
        if val == nil {
            table[node!] = 1
        } else {
            return true
        }
        node = node?.next
    }
    return false
}

isPalindrome(n1)
