package com.company;

import java.util.HashMap;
import java.util.Map;

/**
 * Sa se determine produsul scalar a doi vectori rari care contin numere reale.
 * Un vector este rar atunci când contine multe elemente nule.
 * Vectorii pot avea oricate dimensiuni.
 * De ex. produsul scalar a 2 vectori unidimensionali [1,0,2,0,3] si [1,2,0,3,1] este 4.
 */
public class Main {

    public static void main(String[] args) {
        // write your code here

        //stocam doar valorile nenule ca perechi (index, valoare)
        Map<Integer, Integer> map1 = new HashMap<Integer, Integer>();
        map1.put(0, 1);
        map1.put(2, 2);
        map1.put(4, 3);

        Map<Integer, Integer> map2 = new HashMap<Integer, Integer>();
        map2.put(0, 1);
        map2.put(1, 2);
        map2.put(3, 3);
        map2.put(4, 1);

        int produsScalar = 0;

        if (map1.size() > map2.size()) {
            for (Map.Entry<Integer, Integer> entry : map1.entrySet()) {
                if (map2.containsKey(entry.getKey())) {
                    produsScalar += entry.getValue() * map2.get(entry.getKey()).intValue();
                }
            }
        } else {
            for (Map.Entry<Integer, Integer> entry : map2.entrySet()) {
                if (map1.containsKey(entry.getKey())) {
                    produsScalar += entry.getValue() * map1.get(entry.getKey()).intValue();
                }
            }
        }

        System.out.println("Produsul scalar este: " + produsScalar);


    }
}
