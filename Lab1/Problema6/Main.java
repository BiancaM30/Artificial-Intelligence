package com.company;

import java.util.HashMap;
import java.util.Map;

/**
 * Pentru un sir cu n numere intregi care contine si duplicate,
 * sa se determine elementul majoritar (care apare de mai mult de n / 2 ori).
 * De ex. 2 este elementul majoritar in sirul [2,8,7,2,2,5,2,3,1,2,2].
 */

public class Main {

    public static void main(String[] args) {
        // write your code here

        int n = 11;
        int[] v = {2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2};

        boolean gasit = false;
        //Retinem intr-un HashMap toate perechile de forma (cheie, nr_aparitii)
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (int i = 0; i < v.length; i++) {
            Integer key = v[i];

            if (map.get(key) != null) {
                map.put(key, map.get(key) + 1);
                if (map.get(key) + 1 > n / 2) {
                    System.out.println("Elementul majoritar este: " + key);
                    gasit = true;
                    break;
                }
            } else {
                map.put(key, 1);
            }
        }

        if (gasit == false) System.out.println("Nu exista element majoritar");
    }
}
