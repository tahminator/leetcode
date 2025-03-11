package com.tahminator.leetcode.l0207_course_schedule;

class Solution {
  public boolean canFinish(int numCourses, int[][] prerequisites) {
    Map<Integer, Integer> courseToCounter = new HashMap<>();
    Map<Integer, List<Integer>> prereqToCourse = new HashMap<>();

    for (int[] edge : prerequisites) {
      int course = edge[0];
      int prereq = edge[1];

      int c = courseToCounter.computeIfAbsent(course, k -> 0);
      courseToCounter.put(course, c++);
      prereqToCourse.computeIfAbsent(prereq, k -> new ArrayList<>()).add(course);
    }

    for (var kv : prereqToCourse.entrySet()) {
      System.out.println("k: " + kv.getKey());
      System.out.println("v: " + kv.getValue());
    }

    List<Integer> res = new ArrayList<>();
    Queue<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < numCourses; i++) {
      if (!courseToCounter.containsKey(i)) {
        q.offer(i);
      }
    }

    while (!q.isEmpty()) {
      int course = q.poll();

      // if (seen.contains(v)) {
      //   return false;
      // }

      res.add(course);
      List<Integer> children = prereqToCourse.get(course);
      for (int child : children) {
        int count = courseToCounter.get(child);
        count--;
        courseToCounter.put(child, count);
        if (count == 0) {
          q.offer(child);
        }
      }
    }

    return numCourses == res.size();
  }
}
