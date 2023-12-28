//https://leetcode.com/problems/sort-list/description/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

// var sortList = function (head) {
//   if (!head || !head.next) return head;
//   let i = head;

//   let j;
//   while (i.next) {
//     j = i.next;

//     while (j) {
//       if (i.val > j.val) {
//         [i.val, j.val] = [j.val, i.val];
//       }
//       j = j.next;
//     }
//     i = i.next;
//   }
//   return head;
// };


var sortList = function (head) {
	if (!head || !head.next) return head;
	let current = head;
	let arr = [];
	while (current) {
		arr.push(current.val);
		current = current.next;
	}
	arr.sort((a, b) => a - b);
	current = head;
	let i = 0;
	while (current) {
		current.val = arr[i];
		i++;
		current = current.next;
	}
	return head;
  };
const list = new ListNode(5, new ListNode(1, new ListNode(3, new ListNode(4))));
let current = list;
while (current) {
  console.log(current.val);
  current = current.next;
}
console.log("-------------------");
const Head = sortList(list);
current = Head;
while (current) {
  console.log(current.val);
  current = current.next;
}
