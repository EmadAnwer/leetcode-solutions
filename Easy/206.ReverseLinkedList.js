//https://leetcode.com/problems/reverse-linked-list/description/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var reverseList = function (head) {
	let current = head;
	let prev = null;
	let next = null;
	while (current != null) {
		next = current.next;
		current.next = prev;
		prev = current;
		current = next;
	}
	return prev;
};

const linkedList1 = new ListNode(
  1,
  new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))
);

for (let node = linkedList1; node != null; node = node.next) {
  console.log(node.val);
}

for (let node = reverseList(linkedList1); node != null; node = node.next) {
  console.log(node.val);
}
