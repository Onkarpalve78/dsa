package OOPs.polymorphism;

// Achieved by method overriding
// In Java, runtime polymorphism occurs when a subclass overrides a method of its superclass. 
// The decision about which method to call is made at runtime based on the type of the object.
class Vehicle {
    void whatItDoes() {
        System.out.println("A vehicle helps in transportation");
    }
}

class Car extends Vehicle {
    @Override
    void whatItDoes() {
        System.out.println("A car helps people travel on road.");
    }

}

class CargoShip extends Vehicle {
    @Override
    void whatItDoes() {
        System.out.println("A cargo ship helps in transportation of cargo by the ocean.");
    }
}

public class runTimePolymorphism {
    public static void main(String[] args) {
        Vehicle v = new Vehicle();
        v.whatItDoes();

        Car c = new Car();
        c.whatItDoes();

        CargoShip cs = new CargoShip();
        cs.whatItDoes();
    }

}
