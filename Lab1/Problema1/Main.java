package com.company;

import java.util.Arrays;
import java.util.Scanner;

/**1.Sa se determine ultimul (din punct de vedere alfabetic) cuvant care poate aparea
intr-un text care contine mai multe cuvinte separate prin " " (spatiu).
 De ex. ultimul (dpdv alfabetic) cuvant din "Ana are mere rosii si galbene" este cuvantul "si".
 **/

public class Main {

    public static void main(String[] args) {
        // write your code here
        System.out.println("Introduceti propozitia: ");
        Scanner sc = new Scanner(System.in);
        String prop = sc.nextLine();

        String[] cuvinte = prop.split("\\s+");
        Arrays.sort(cuvinte);
        System.out.println(cuvinte[cuvinte.length-1]);


    }
}
