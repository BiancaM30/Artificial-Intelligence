package com.company;

import java.util.Arrays;
import java.util.Scanner;

/**Pentru un sir cu n elemente care contine valori din multimea {1, 2, ..., n - 1}
 * astfel incat o singura valoare se repeta de doua ori, sa se identifice acea valoare care se repeta.
 De ex. in sirul [1,2,3,4,2] valoarea 2 apare de doua ori.*/

public class Main {

    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduceti n:");
        n = sc.nextInt();

        System.out.println("Introduceti numerele: ");
        int[] v = new int[n];
        for (int i = 0; i < n; i++) {
            v[i] = sc.nextInt();
        }

        Arrays.sort(v);

        for (int i = 0; i < n - 1; i++) {
            if (v[i] == v[i + 1]){
                System.out.println("Valoarea care se repeta este: " + v[i]);
                break;
            }
        }
    }
}
