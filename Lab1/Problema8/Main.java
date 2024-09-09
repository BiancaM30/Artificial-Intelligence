package com.company;

import java.util.ArrayDeque;
import java.util.Queue;

/**
 * Sa se genereze toate numerele (in reprezentare binara) cuprinse intre 1 si n.
 * De ex. daca n = 4, numerele sunt: 1, 10, 11, 100.
 */

public class Main {

    public static void main(String[] args) {
        // write your code here

        int n = 6;

        Queue<String> coada = new ArrayDeque<>();
        coada.add("1");

        for (int i = 1; i <= n; i++) {

            String frontElement = coada.peek();
            coada.add(frontElement + '0');
            coada.add(frontElement + '1');

            System.out.print(frontElement + ' ');
            coada.remove();
        }
    }
}
