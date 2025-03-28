package com.tahminator.leetcode.l0210_course_schedule_ii;

class Solution {
  public int[] findOrder(int numCourses, int[][] prerequisites) {
    Map<Integer, Integer> courseToPrereq = new HashMap<>();
    Map<Integer, List<Integer>> courseToNext = new HashMap<>();

    for (int[] edge : prerequisites) {
      int course = edge[0];
      int prereq = edge[1];

      int c = courseToPrereq.computeIfAbsent(course, k -> 0);
      courseToPrereq.put(course, ++c);

      courseToNext.computeIfAbsent(prereq, k -> new ArrayList<>()).add(course);
    }

    Queue<Integer> q = new ArrayDeque<>();
    for (int course = 0; course < numCourses; course++) {
      if (!courseToPrereq.containsKey(course)) {
        q.offer(course);
      }
    }

    int[] res = new int[numCourses];
    int i = 0;
    while (!q.isEmpty()) {
      int course = q.poll();
      
      res[i++] = course;
      
      List<Integer> children = courseToNext.getOrDefault(course, new ArrayList<>());

      for (int child : children) {
        int c = courseToPrereq.get(child);
        courseToPrereq.put(child, --c);
        if (c == 0) {
          q.offer(child);
        }
      }
    }
    
    return i == numCourses ? res : new int[0];
  }
}
