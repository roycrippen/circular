package com.aaa;

public class A {

  public static String getStr() {
    return D.toLowerCaseD("String_From_Class_A");
  }

  public static String toLowerCaseA(String s) {
    return s.toLowerCase();
  }

  public static String toUpperCaseA() {
    return B.toUpperCaseB();
  }

  public static void main(String[] args) {
    System.out.println(toUpperCaseA());
  }
}
