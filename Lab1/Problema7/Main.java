package com.company;

import java.util.Arrays;

/**
 * Sa se determine al k-lea cel mai mare element al unui sir de numere cu n elemente (k < n).
 * De ex. al 2-lea cel mai mare element din sirul [7,4,6,3,9,1] este 7.
 */

public class Main {

    public static void main(String[] args) {
        // write your code here

        int k = 2;
        int[] v = {7, 4, 6, 3, 9, 1};

        Arrays.sort(v);

        System.out.println("Al k-lea cel mai mare element este: " + v[v.length-k]);
    }
}
