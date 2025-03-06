package com.tahminator.leetcode.l2579_count_total_number_of_colored_cells;

class Solution {
    /**
     * This appears to be some sort of sequence question.
     * Every iteration increases by some order of 4 * (n - 1).
     * For example, n = 2 -> 4 * (1) = 4 new cells.
     * But the original always starts with 1 cell, so you always have to add by one.
     * But this doesn't consider all the previous cells.
     * This part is a common concept in Discrete Math, where the summation from 
     * i = 1 to k where we just add 1 (in other words 1 + 2 + 3 ... k) can be
     * rewritten as (k * (k + 1) / 2). We can apply the same concept to this:
     * 4 * (1 + 2 + 3 ... n - 1) can just be 4 * (n * (n - 1) / 2). And we add + 1
     * to account for the base case. We can simply 4 / 2 to just be * 2.
     *
     * Need to stick a long somewhere to stop n * (n - 1) from overflowing. So we multiply by 1L.
     */
    public long coloredCells(int n) {
        return 1 + (4 * (1L * n * (n - 1) / 2));
    }
}
