package com.tahminator.leetcode.l0853_car_fleet;

class Solution {
  public int carFleet(int target, int[] position, int[] speed) {
    Map.Entry<Double, Double>[] cars = new Map.Entry[position.length];
    for (int i = 0; i < position.length; i++) {
      cars[i] = Map.entry((double) position[i], (double) (target - position[i]) / speed[i]);
    }

    Arrays.sort(cars, (a, b) -> Double.compare(a.getKey(), b.getKey()));

    int res = 0;
    double prev = 0;
    for (int i = position.length - 1; i >= 0; i--) {
      double d = cars[i].getValue();
      if (d > prev) {
        prev = d;
        res++;
      }
    }

    return res;
  }
}
