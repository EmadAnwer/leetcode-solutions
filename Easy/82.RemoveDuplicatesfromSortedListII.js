//https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var deleteDuplicates = function (head) {
  if (!head || !head.next) return head;

  let dummy = new ListNode(0);
  dummy.next = head;
  let current = dummy;

  while (current.next && current.next.next) {
    if (current.next.val === current.next.next.val) {
      let duplicateValue = current.next.val;
      while (current.next && current.next.val === duplicateValue) {
        current.next = current.next.next;
      }
    } else {
      current = current.next;
    }
  }

  return dummy.next;
};
// [1,1,1,2,3]

const linkedListwithDuplicates = new ListNode(
  1,
  new ListNode(
    1,
    new ListNode(
      1,
      new ListNode(
        2,
        new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(4))))
      )
    )
  )
);
// linkedListwithDuplicates = new ListNode(
//   1,
//   new ListNode(
//     1,
//     new ListNode(
//       3,
//       new ListNode(
//         3,
//         new ListNode(
//           4,
//           new ListNode(4, new ListNode(5, new ListNode(6, new ListNode(6))))
//         )
//       )
//     )
//   )
// );

for (let node = linkedListwithDuplicates; node != null; node = node.next) {
  console.log(node.val);
}

console.log("After removing duplicates");
for (
  let node = deleteDuplicates(linkedListwithDuplicates);
  node != null;
  node = node.next
) {
  console.log(node.val);
}
