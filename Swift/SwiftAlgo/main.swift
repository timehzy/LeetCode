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
let n3 = ListNode(2)
let n4 = ListNode(1)
let n5 = ListNode(5)
let n7 = ListNode(7)

n1.next = n2
n2.next = n3
n3.next = n4
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


func myReverse(_ head: ListNode?) -> ListNode? {
    if head == nil || head?.next == nil {
        return head
    }
    let n = myReverse(head?.next)
    head?.next?.next = head
    head?.next = nil
    return n
}

func isPalindrome(_ head: ListNode?) -> Bool {
    var slow = head, fast = head
    
    while fast != nil && fast?.next != nil {
        slow = slow?.next
        fast = fast?.next?.next
    }
    // slow 指向中间点，翻转后半部分
    slow = myReverse(slow)
    fast = head
    
    while fast != nil && slow != nil {
        if fast?.val != slow?.val {return false}
        fast = fast?.next
        slow = slow?.next
    }

    return true
}



print(isPalindrome(n1))


func test(_ a:[Int]) -> Int {
    var sum = a.reduce(0) { $0 + $1 }
    var sum2 = 0

    for i in 0..<a.count {
        sum -= a[i]
        if sum == sum2 {return i}
        sum2 += a[i]
    }
    return -1
}

print(test([-20, 30, 10,40,20]))


//func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
//    for i in m..<m+n {
//        nums1[i] = nums2[i - m]
//        for j in 0..<i {
//            if nums1[i] < nums1[j] {
//                let t = nums1[i]
//                for k in stride(from: i, to: j, by: -1) {
//                    nums1[k] = nums1[k - 1]
//                }
//                nums1[j] = t
//                break
//            }
//        }
//    }
//}

func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
    var i = m-1, j = n-1
    
    while i >= 0 || j >= 0 {
        if j < 0 || (i >= 0 && nums2[j] < nums1[i]) {
            nums1[j + i + 1] = nums1[i]
            i -= 1
        } else {
            nums1[j + i + 1] = nums2[j]
            j -= 1
        }
    }
}


var nums1 = [0]
var nums2 = [1]
merge(&nums1, 0, nums2, 1)
print(nums1)




class Solution {
    var nums:[Int]
    
    init(_ nums: [Int]) {
        self.nums = nums
    }
    
    /** Resets the array to its original configuration and return it. */
    func reset() -> [Int] {
        return self.nums
    }
    
    /** Returns a random shuffling of the array. */
    func shuffle() -> [Int] {
        var list = Array(self.nums)
        
        for i in 0..<self.nums.count {
            let index = Int.random(in: i..<self.nums.count)
            let t = list[i]
            list[i] = list[index]
            list[index] = t
            
        }
        
        return list
    }
}

//let obj = Solution([1,2,3])
//let ret_2: [Int] = obj.shuffle()
//let ret_1: [Int] = obj.reset()
//print(ret_1)


class MinStack {
    /** initialize your data structure here. */
    
    var datas:[Int]
    var sortedDatas:[Int]
    
    init() {
        self.datas = [Int]()
        self.sortedDatas = [Int]()
    }
    
    func push(_ x: Int) {
        self.datas.append(x)
        for i in 0..<self.sortedDatas.count {
            if x < sortedDatas[i] {
                sortedDatas.insert(x, at: i)
                return
            }
        }
        self.sortedDatas.append(x)
    }
    
    func pop() {
        sortedDatas.remove(at: sortedDatas.firstIndex(of: datas.last!)!)
        self.datas.removeLast()
    }
    
    func top() -> Int {
        return self.datas.last ?? -1
    }
    
    func getMin() -> Int {
        return self.sortedDatas.first ?? -1
    }
}

let obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)
let ret_4: Int = obj.getMin()
let ret_3: Int = obj.top()
obj.pop()
let ret_5: Int = obj.getMin()

func isValid(_ s: String) -> Bool {
    var incomingStack = [Character]()
    for c in s {
        if c == "(" || c == "{" || c == "[" {
            incomingStack.append(c)
        } else {
            let outC = incomingStack.last
            if (outC == "(" && c == ")")
            || (outC == "{" && c == "}")
            || (outC == "[" && c == "]") {
                incomingStack.removeLast()
            } else {
                return false
            }
        }
    }
    return incomingStack.count == 0
}

//print(isValid("()"))
//print(isValid("()[]{}"))
//print(isValid("(]"))
//print(isValid("([)]"))
//print(isValid("{[]}"))
//print(isValid("["))


func fizzBuzz(_ n: Int) -> [String] {
    var res = [String]()
    
    for i in 1...n {
        if i % 3 == 0 && i % 5 == 0 {
            res.append("FizzBuzz")
        } else if i % 3 == 0 {
            res.append("Fizz")
        } else if i % 5 == 0 {
            res.append("Buzz")
        } else {
            res.append(String(i))
        }
    }
    
    return res
}

print(fizzBuzz(15))


func romanToInt(_ s: String) -> Int {
    let dict:[Character : Int] = ["I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000]
    var res = 0
    var pre = 0
    for c in s.reversed() {
        let curVal = dict[c]
        if curVal! >= pre {
            res += curVal!
        } else {
            res -= curVal!
        }
        pre = curVal!
    }
    return res
}

print(romanToInt("MCMXCIV"))


func isPowerOfThree(_ n: Int) -> Bool {
    return n > 0 && (Int(pow(Double(3), Double(33))) % n == 0)
}


//print(isPowerOfThree(27))
//print(isPowerOfThree(9))
//print(isPowerOfThree(0))
//print(isPowerOfThree(45))
//print(isPowerOfThree(1))


func countPrimes(_ n:Int) -> Int {
    if n < 3 {return 0}
    if n == 3 {return 1}
    var res = 0
    var arr = Array(repeating: true, count: n)
    arr[0] = false
    arr[1] = false
    for i in 2...Int(sqrt(Double(n))) {
        if arr[i] == true {
            for j in stride(from: 2, to: ceil(Double(n)/Double(i)), by: 1) {
                arr[i * Int(j)] = false
            }
        }
    }
    for r in arr {
        if r == true {res += 1}
    }
    return res
}


print(countPrimes(2))




class MyLinkedList {
    class Node {
        var val:Int
        var next:Node?
        var prev:Node?
        
        init(_ val:Int) {
            self.val = val
        }
    }
    
    var head: Node?
    var tail: Node?
    var length:Int = 0
    
    init() {}
    
    func get(_ index: Int) -> Int {
        guard index < length else {
            return -1
        }
        var i = index
        var curNode = head
        
        while i > 0 {
            curNode = curNode?.next
            i -= 1
        }
        
        return curNode!.val
    }
    
    func addAtHead(_ val: Int) {
        let node = Node(val)
        if tail == nil {
            tail = node
        }
        head?.prev = node
        node.next = head
        head = node
        length += 1
    }
    
    func addAtTail(_ val: Int) {
        let node = Node(val)
        if head == nil {
            head = node
        }
        tail?.next = node
        node.prev = tail
        tail = node
        length += 1
    }
    
    func addAtIndex(_ index: Int, _ val: Int) {
        guard index <= length else {
            return
        }
        if index == length {
            addAtTail(val)
        } else if index == 0 {
            addAtHead(val)
        } else {
            let newNode = Node(val)
            let curNode = getNode(index)
            let prevNode = curNode?.prev
            prevNode?.next = newNode
            newNode.prev = prevNode
            newNode.next = curNode
            curNode?.prev = newNode
            length += 1
        }
    }
    
    func getNode(_ index:Int) -> Node? {
        guard index < length else {
            return nil
        }
        var node = head
        var count = 0
        
        while count < index {
            node = node?.next
            count += 1
        }
        
        return node
    }
    
    func deleteAtIndex(_ index: Int) {
        guard index < length else {
            return
        }
        var t = 0
        var node = head
        
        while t < index {
            node = node?.next
            t += 1
        }
        
        node?.prev?.next = node?.next
        node?.next?.prev = node?.prev
        
        if index == length - 1 {tail = node?.prev}
        if index == 0 {head = node?.next}
        
        length -= 1
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * let obj = MyLinkedList()
 * let ret_1: Int = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index, val)
 * obj.deleteAtIndex(index)
 */
let operation = ["MyLinkedList","addAtHead","get","addAtTail","deleteAtIndex","addAtHead","deleteAtIndex","get","addAtTail","addAtHead","addAtTail","addAtTail","addAtTail","addAtIndex","get","addAtIndex","addAtHead","deleteAtIndex","addAtIndex","addAtHead","addAtIndex","deleteAtIndex","get","addAtTail","deleteAtIndex","deleteAtIndex","addAtTail","addAtTail","addAtIndex","addAtHead","get","get","addAtTail","addAtTail","addAtTail","addAtTail","addAtIndex","addAtIndex","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","addAtHead","deleteAtIndex","addAtHead","get","addAtHead","get","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtTail","deleteAtIndex","get","addAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtIndex","deleteAtIndex","deleteAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtTail","addAtHead","addAtTail","addAtIndex","deleteAtIndex","deleteAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","get","addAtIndex","get","addAtHead","addAtHead","addAtHead","addAtIndex","addAtIndex","get","addAtHead","get","get","addAtTail","addAtHead","addAtHead","addAtTail","addAtTail","get","addAtTail"]

let val = [[],[8],[1],[81],[2],[26],[2],[1],[24],[15],[0],[13],[1],[6,33],[6],[2,91],[82],[6],[4,11],[3],[7,14],[1],[6],[99],[11],[7],[5],[92],[7,92],[57],[2],[6],[39],[51],[3],[22],[5,26],[9,52],[69],[5,58],[79],[7],[41],[33],[88],[44],[8],[72],[93],[18],[1],[9],[46],[9],[92],[71],[69],[11,54],[27],[83],[12],[20],[19,97],[77],[36],[3],[35],[16,68],[22],[36],[17],[62],[89],[61],[6],[92],[28,69],[23],[28],[7,4],[0],[24],[52],[1],[23,3],[7],[6],[68],[79],[45,90],[41,52],[28],[25],[9],[32],[11],[90],[24],[98],[36],[34],[26]]

var link:MyLinkedList?
var result = [Int]()

for i in 0..<operation.count {
    let c = operation[i]
    if c == "MyLinkedList" {
        link = MyLinkedList()
        result.append(-1)
    } else if c == "get" {
        result.append(link!.get(val[i][0]))
    } else if c == "addAtHead" {
        link!.addAtHead(val[i][0])
        result.append(-1)
    } else if c == "addAtTail" {
        link!.addAtTail(val[i][0])
        result.append(-1)
    } else if c == "addAtIndex" {
        link!.addAtIndex(val[i][0], val[i][1])
        result.append(-1)
    } else if c == "deleteAtIndex" {
        link!.deleteAtIndex(val[i][0])
        result.append(-1)
    }
}
print(result)


func pivotIndex(_ nums: [Int]) -> Int {
    var sum = nums.reduce(0) {return $0 + $1}
    var leftSum = 0
    
    for i in 0..<nums.count {
        sum -= nums[i]
        if leftSum == sum {return i}
        leftSum += nums[i]
    }
    
    return -1
}

print(pivotIndex([1, 2, 3]))


func dominantIndex(_ nums: [Int]) -> Int {
    var biggest = 0
    var secondBig = 0
    var index = 0
    
    
    for i in 0..<nums.count {
        let num = nums[i]
        if num > biggest {
            secondBig = biggest
            biggest = num
            index = i
        } else if num > secondBig {
            secondBig = num
        }
    }
    
    if secondBig * 2 <= biggest {
        return index
    } else {
        return -1
    }
}

print(dominantIndex([3, 6, 1, 0]))


func plusOne(_ digits: [Int]) -> [Int] {
    var res = digits
    
    for i in stride(from: res.count - 1, through: 0, by: -1) {
        res[i] = res[i] + 1
        if res[i] >= 10 {
            res[i] -= 10
            if i == 0 {res.insert(1, at: 0)}
        } else {
            break;
        }
    }
    
    return res
}


print(plusOne([9,9,9]))


func spiralOrder(_ matrix: [[Int]]) -> [Int] {
    var lt = 0
    var rt = matrix.first!.count
    var rb = matrix.count
    var lb = matrix.count
    
    var res = [Int]()
    
    for i in 0..<Int(sqrt(Double(matrix.count))) {
        for j in lt..<rt {
            res.append(matrix[i][j])
        }
//        for j in
        
    }
    
    return res
}


func so(a:[[Int]], startRow:Int, startCol:Int) -> [Int] {
    if a.count == 1 {
        return a.first!
    } else {
        
    }
    
    var res = [Int]()
    res.append(contentsOf: so(a: a, startRow: <#T##Int#>, startCol: <#T##Int#>))
    for num in a.first! {
        res.append(num)
    }
    
    return res
}
