function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

// var mergeKLists = function (lists) {
//   const dummy = new ListNode(0);
//   let current = dummy;
//   let tmp = [];
//   for (let i = 0; i < lists.length; i++) {
// 	if (lists[i]) {
// 	  tmp.push(lists[i]);
// 	}
//   }
//   while (tmp.length) {
// 	let min = Infinity;
// 	let minIndex = -1;
// 	for (let i = 0; i < tmp.length; i++) {
// 	  if (tmp[i].val < min) {
// 		min = tmp[i].val;
// 		minIndex = i;
// 	  }
// 	}
// 	current.next = tmp[minIndex];
// 	current = current.next;
// 	tmp[minIndex] = tmp[minIndex].next;
// 	if (!tmp[minIndex]) {
// 	  tmp.splice(minIndex, 1);
// 	}
//   }
//   return dummy.next;

// };

var mergeKLists = function (lists) {
  const dummy = new ListNode(0);
  let current = dummy;
  let listWithoutNull = [];
  for (let i = 0; i < lists.length; i++) {
    if (lists[i]) {
      listWithoutNull.push(lists[i]);
    }
  }
  while (listWithoutNull.length) {
    // sort listWithoutNull
    listWithoutNull.sort((a, b) => a.val - b.val);
    current.next = listWithoutNull[0];
    current = current.next;
    listWithoutNull[0] = listWithoutNull[0].next;
    // remove null
    if (!listWithoutNull[0]) listWithoutNull.shift();
  }
  return dummy.next;
};
const l1 = new ListNode(1, new ListNode(5, new ListNode(7)));
const l2 = new ListNode(2, new ListNode(5, new ListNode(6)));
const l3 = new ListNode(1, new ListNode(5, new ListNode(15)));

const lists = [l1, l2, l3];

let result = mergeKLists(lists);

while (result) {
  console.log(result.val);
  result = result.next;
}
