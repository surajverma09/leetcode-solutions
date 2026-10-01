/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result; ListNode curr1 = l1; ListNode curr2 = l2; ListNode tail;
        if(l1 == null){
            return l2;
        }
        else if(l2 == null){
            return l1;
        }
        if(l1.val < l2.val){
            result = tail = l1;
            curr1 = curr1.next;  
        }
        else{
            result = tail = l2;
            curr2 = curr2.next;
        }
        if(curr1 == null && curr2 == null){
            return result;
        }
        while(curr1 != null && curr2 != null){
            if(curr1.val < curr2.val){
                tail.next = curr1;
                curr1 = curr1.next;
                tail = tail.next;
            }
            else{
                tail.next = curr2;
                curr2 = curr2.next;
                tail = tail.next;
            }}
         while(curr1 != null || curr2 != null){
            if(curr2!=null){
                tail.next = curr2;
                tail = tail.next;
                curr2 = curr2.next;
            }
            else{
                tail.next = curr1;
                curr1 = curr1.next;
                tail = tail.next;
            }
        }return result;
    }
}