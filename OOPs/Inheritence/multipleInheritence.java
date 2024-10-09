package OOPs.Inheritence;

interface CanRun {
    void run();
}

interface CanBark {
    void bark(); // abstract methods(methods without a body) cannot specify body

    default void nigga() { // but by using default keyword you can create concrete methods(methods with a
                           // body)
        System.out.println("you a nigga");
    }

    static void diddler() {
        // You can define static methods in interfaces, which can be called on the
        // interface itself.
        System.out.println("Certified diddler");
    }
}

class Doggy implements CanRun, CanBark {
    public void run() {
        System.out.println("Doggy runs");
    }

    public void bark() {
        System.out.println("Doggy barks");
    }
}

public class multipleInheritence {
    public static void main(String[] args) {
        Doggy d = new Doggy();
        d.bark();
        d.run();
        d.nigga();

        CanBark.diddler();
    }

}
