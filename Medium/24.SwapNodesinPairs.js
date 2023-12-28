//https://leetcode.com/problems/swap-nodes-in-pairs/description/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var swapPairs = function (head) {
  if (!head.next || !head) return head;
  let dummy = new ListNode(0);
  dummy.next = head;
  let current = dummy;

  let tmp1 = current.next;
  let tmp2 = current.next.next.next;

  while (current.next && current.next.next) {
    current.next = current.next.next;
    current.next.next = tmp1;
    current.next.next.next = tmp2;
    current = current.next.next;
    tmp1 = current.next;
    tmp2 = current.next?.next?.next;
  }

  console.log(current);

  return dummy.next;
};

const list = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
let current = list;
while (current) {
  console.log(current.val);
  current = current.next;
}
console.log("-------------------");
const Head = swapPairs(list);
current = Head;
while (current) {
  console.log(current.val);
  current = current.next;
}
