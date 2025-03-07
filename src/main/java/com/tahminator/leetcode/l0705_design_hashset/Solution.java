package com.tahminator.leetcode.l705_design_hashset;

/**
 * We will implement this similar to a hashmap, where 
 * we will have a set maximum (due to hashing), and a linked list
 * wto avoid collisions.
 */
class MyHashSet {
    private class Node {
      public int val;
      public Node next;

      public Node() {}

      public Node(int val) {
        this.val = val;
      }

      public Node(int val, Node next) {
        this.val = val;
        this.next = next;
      }
    }

    private final Node[] map;

    // private void printLinkedList(Node head) {
    //   Node curr = head;
    //   while (curr != null) {
    //     System.out.println(curr.val);
    //     curr = curr.next;
    //   }
    //   System.out.println("");
    // }

    private int hash(int key) {
      return key % 1000;
    }

    public MyHashSet() {
      map = new Node[1000];

      for (int i = 0; i < 1000; i++) {
        // Dummy nodes to make removal operations easier.
        map[i] = new Node(-1);
      }
    }
  
    /**
     * -1, 2
     * check 2, 2 == key
     */
    public void add(int key) {
      int hash = hash(key);

      Node head = map[hash];
      Node curr = head;

      // printLinkedList(head);
      
      while (curr.next != null) {
        if (curr.next.val == key) {
          return;
        }

        curr = curr.next;
      }

      Node next = new Node(key);
      curr.next = next;
      // printLinkedList(head);
    }
    
    public void remove(int key) {
      int hash = hash(key);

      Node head = map[hash];
      Node curr = head;

      while (curr.next != null) {
        if (curr.next.val == key) {
          break;
        }
        curr = curr.next;
      }

      if (curr.next == null) {
        return;
      }

      curr.next = curr.next.next;

    }
    
    public boolean contains(int key) {
      int hash = hash(key);

      Node head = map[hash];
      Node curr = head.next;

      while (curr != null) {
        if (curr.val == key) {
          return true;
        }
        curr = curr.next; 
      }

      return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */
