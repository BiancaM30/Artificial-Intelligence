package com.company;

/**
 * Considerandu-se o matrice cu n x m elemente binare (0 sau 1) sortate crescator pe linii, sa
 * se identifice indexul liniei care contine cele mai multe elemente de 1.
 * <p>
 * De ex. in matricea
 * [[0,0,0,1,1],
 * [0,1,1,1,1],
 * [0,0,1,1,1]]
 * a doua linie contine cele mai multe elemente 1.
 */
public class Main {

    public static void main(String[] args) {
        // write your code here
        int[][] mat = {
                {0, 0, 0, 1, 1},
                {0, 1, 1, 1, 1},
                {0, 0, 1, 1, 1}
        };
        int nrLinii = mat.length;
        int nrColoane = mat[0].length;

        int maxim = -1;

        int j = nrColoane - 1;
        for (int i = 0; i < nrLinii; i++) {
            while (j >= 0 && mat[i][j] == 1) {
                j = j - 1; // il mutam pe j din dreapta inspre stanga pana dam de cel mai din stanga 0
                maxim = i;
            }
        }

        maxim++; //incepem indexarea liniilor de la 1
        System.out.println("Coloana cu cei mai multi de 1 este: " + maxim);
    }
}
