package com.company;

public class PerechiCoordonate {
    private int p, q; //colt stanga sus
    private int r, s; //colt dreapta jos

    public PerechiCoordonate(int p, int q, int r, int s) {
        this.p = p;
        this.q = q;
        this.r = r;
        this.s = s;
    }

    public int getP() {
        return p;
    }

    public void setP(int p) {
        this.p = p;
    }

    public int getQ() {
        return q;
    }

    public void setQ(int q) {
        this.q = q;
    }

    public int getR() {
        return r;
    }

    public void setR(int r) {
        this.r = r;
    }

    public int getS() {
        return s;
    }

    public void setS(int s) {
        this.s = s;
    }
}
