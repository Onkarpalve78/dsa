package OOPs.Abstraction;

// You cannot instantiate an abstract class (i.e., you cannot create objects of an abstract class).
// A subclass must implement all abstract methods of
// the parent abstract class unless the subclass itself is also abstract.
// The purpose of an abstract class is to define a blueprint for other classes.

abstract class Superhero {
    // abstract method
    abstract void kind();

    // concrete method
    public void brave() {
        System.out.println("This superhero must be brave");
    }

}

class Superman extends Superhero {
    public void kind() {
        System.out.println("Superman is very Kind!");
    }
}

abstract class AntiHero extends Superhero {
    @Override
    public void kind() {
        System.out.println("This superhero is not kind!");
    }

    @Override
    public void brave() {
        System.out.println("This superhero is kinda brave kinda crazy!");
    }
}

class Deadpool extends AntiHero {
    public void name() {
        System.out.println("And then we have Deadpool, ");
    }
}

public class abstractClasses {

    public static void main(String[] args) {
        // Superhero s= new Superhero(); not allowed cuz abstract classes cannot be
        // instantiated

        Superman sm = new Superman();
        sm.kind();
        sm.brave();

        Deadpool dp = new Deadpool();
        dp.name();
        dp.kind();
        dp.brave();

    }
}
