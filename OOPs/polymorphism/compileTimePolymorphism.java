package OOPs.polymorphism;

// Achieved by Method Overloading

// In Java, method overloading is when multiple methods have the same name but different parameter
// lists (either by number or type of parameters). 
// This allows the method to perform different actions depending on the argument types or the number of arguments.

// NOTE:
// Compile time is the time it takes to convert a programming language into machine code, 
// while runtime is the time it takes to run the program:

class Addition {
    public int add(int a, int b) {
        System.out.println("First add got called");
        return a + b;
    }

    public double add(double a, double b) {
        System.out.println("Second add got called");
        return a + b;
    }

    public int add(int a, int b, int c) {
        System.out.println("Third add got called");
        return a + b + c;
    }
}

public class compileTimePolymorphism {
    public static void main(String[] args) {
        Addition add = new Addition();

        System.out.println(add.add(2, 3));
    }

}
