package com.company;

import java.util.ArrayList;
import java.util.List;

/**
 * Considerandu-se o matrice cu n x m elemente intregi si o lista cu perechi formate din
 * coordonatele a 2 casute din matrice ((p,q) si (r,s)), sa se calculeze suma elementelor
 * din sub-matricile identificate de fieare pereche.
 * <p>
 * De ex, pt matricea
 * [[0, 2, 5, 4, 1],
 * [4, 8, 2, 3, 7],
 * [6, 3, 4, 6, 2],
 * [7, 3, 1, 8, 3],
 * [1, 5, 7, 9, 4]]
 * si lista de perechi ((1, 1) si (3, 3)), ((2, 2) si (4, 4)), suma elementelor din prima sub-matrice este 38,
 * iar suma elementelor din a 2-a sub-matrice este 44.
 */
public class Main {

    public static void main(String[] args) {
        // write your code here
        int[][] matrix =
                {
                        {0, 2, 5, 4, 1},
                        {4, 8, 2, 3, 7},
                        {6, 3, 4, 6, 2},
                        {7, 3, 1, 8, 3},
                        {1, 5, 7, 9, 4}
                };
        PerechiCoordonate p1 = new PerechiCoordonate(1, 1, 3, 3);
        PerechiCoordonate p2 = new PerechiCoordonate(2, 2, 4, 4);
        List<PerechiCoordonate> lista = new ArrayList<PerechiCoordonate>();
        lista.add(p1);
        lista.add(p2);

        int nrLinii = matrix.length;
        int nrColoane = matrix[0].length;

        //Calculam o intr-o matrice auxiliara toate sumele submatricilor avand coltul din stanga sus
        //in (0,0) si cel din dreapta jos in (i,j)
        int sum[][] = new int[nrLinii][nrColoane];

        // initializam prima linie si apoi prima coloana
        for (int col = 1; col < nrColoane; col++) {
            sum[0][col] = matrix[0][col] + sum[0][col - 1];
        }
        for (int l = 1; l < nrLinii; l++) {
            sum[l][0] = matrix[l][0] + sum[l - 1][0];
        }

        //calculam sumele pentru restul matricei
        for (int i = 1; i < nrLinii; i++) {
            for (int j = 1; j < nrColoane; j++) {
                sum[i][j] = matrix[i][j] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
            }
        }

        //parcurgem lista de perechi de coordonate
        for (PerechiCoordonate pereche : lista) {
            int p = pereche.getP();
            int q = pereche.getQ();
            int r = pereche.getR();
            int s = pereche.getS();
            // suma elementelor din submatricea determinata de ((p,q) si (r,s))
            int sumaSubmatrice = sum[r][s] - sum[r][q - 1] - sum[p - 1][s] + sum[p - 1][q - 1];

            System.out.println("Pentru perechea: (" + p + ',' + q + "),(" + r + ',' + s + ") suma este " + sumaSubmatrice);
        }
    }
}

