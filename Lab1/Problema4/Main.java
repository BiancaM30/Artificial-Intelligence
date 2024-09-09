package com.company;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Sa se determine cuvintele unui text care apar exact o singura data in acel text.
 * De ex. cuvintele care apar o singura data in "ana are ana are mere rosii ana"
 * sunt: 'mere' și 'rosii'.
 */

public class Main {

    public static void main(String[] args) {
        // write your code here
        System.out.println("Introduceti propozitia: ");
        Scanner sc = new Scanner(System.in);
        String prop = sc.nextLine();

        String[] listaCuvinte = prop.split("\\s+");

        //Retinem intr-un HashMap toate perechile de forma (cuvant, nr_aparitii)
        Map<String, Integer> mapCuvinte = new HashMap<String, Integer>();

        for (int i = 0; i < listaCuvinte.length; i++) {
            String key = listaCuvinte[i];

            if (mapCuvinte.get(key) != null) {
                mapCuvinte.put(key, mapCuvinte.get(key) + 1);
            } else {
                mapCuvinte.put(key, 1);
            }
        }
        for (Map.Entry<String, Integer> entry : mapCuvinte.entrySet()) {
            if (entry.getValue() == 1) {
                System.out.println(entry.getKey());
            }
        }
    }

}
