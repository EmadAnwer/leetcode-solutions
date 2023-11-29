//https://leetcode.com/problems/intersection-of-two-linked-lists/description/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

class node {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

function arrayToLinkedList(list) {
  const nodes = new node(list[0]);

  let currentNode = nodes;
  for (let i = 1; i < list.length; i++) {
    currentNode.next = new node(list[i]);
    currentNode = currentNode.next;
  }
  return nodes;
}

function printLinkedList(linkedList) {
  let currentNode = linkedList;
  while (currentNode) {
    console.log(currentNode.val);
    currentNode = currentNode.next;
  }
}
var getIntersectionNode = function (headA, headB) {
  let headACurrentNode = headA;

  while (headACurrentNode) {
    let headBCurrentNode = headB;

    while (headBCurrentNode) {
      if (headBCurrentNode == headACurrentNode) return headACurrentNode;

      headBCurrentNode = headBCurrentNode.next;
    }
    headACurrentNode = headACurrentNode.next;
  }
  return null;
};

function testcase() {
  let intersectionNode = new node(8, new node(4, new node(5)));
  let headA = new node(4, new node(1, intersectionNode));
  let headB = new node(5, new node(6, new node(1, intersectionNode)));
  const returnedNode = getIntersectionNode(headA, headB);
  console.log(returnedNode == intersectionNode);
}

testcase();
