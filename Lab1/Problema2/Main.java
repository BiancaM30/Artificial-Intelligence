package com.company;

import java.util.Scanner;

/**Sa se determine distanta Euclideana intre doua locatii identificate prin perechi de numere.
 *De ex. distanta intre (1,5) si (4,1) este 5.0
 * */
public class Main {

    public static void main(String[] args) {
        int xA, yA, xB, yB;
        Scanner sc=new Scanner(System.in);
        System.out.println("Introduceti xA");
        xA=sc.nextInt();
        System.out.println("Introduceti yA");
        yA=sc.nextInt();
        System.out.println("Introduceti xB");
        xB=sc.nextInt();
        System.out.println("Introduceti yB");
        yB=sc.nextInt();

        double distanta = Math.sqrt((xB - xA) * (xB - xA) + (yB - yA) * (yB - yA));
        System.out.println("distanta intre " + "(" + xA + "," + yA + ") si" + " (" + xB + "," + yB + ") este " + distanta);
    }
}
