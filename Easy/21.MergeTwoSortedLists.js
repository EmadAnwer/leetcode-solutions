//https://leetcode.com/problems/merge-two-sorted-lists/description/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var mergeTwoLists = function (list1, list2) {
  if (!list1 || !list2) return list1 || list2;

  const dummy = new ListNode(0);
  let current = dummy;

  while (list1 && list2) {
    if (list1.val < list2.val) {
      current.next = list1;
      list1 = list1.next;
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    current = current.next;
  }

  current.next = list1 || list2;

  return dummy.next;
};

const linked1 = new ListNode(
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
const linked2 = new ListNode(
  1,
  new ListNode(
    1,
    new ListNode(
      3,
      new ListNode(
        3,
        new ListNode(
          4,
          new ListNode(4, new ListNode(5, new ListNode(6, new ListNode(6))))
        )
      )
    )
  )
);

let merged = mergeTwoLists(linked1, linked2);

while (merged) {
  console.log(merged.val);
  merged = merged.next;
}
