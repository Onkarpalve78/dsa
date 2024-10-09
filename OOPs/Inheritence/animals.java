package OOPs.Inheritence;

// import java.util.Scanner;

class Animal {
    String name;

    public Animal(String naam) {
        this.name = naam;
    }

    public void eat() {
        System.out.println(this.name + " is eating");
    }

    public void sleep() {
        System.out.println(this.name + " is sleeping");
    }
}

class Dog extends Animal {
    String sound;

    public Dog(String sounds) {
        super(sounds);
        this.sound = sounds;
    }

    public void routine() {
        this.eat();
        this.sleep();
        System.out.println("Nigga does " + this.sound);
    }
}

// This class makes this code multilevel inheritence
class Puppy extends Dog {
    public Puppy(String name) {
        super(name);

    }

    void schedule() {
        this.routine();
    }
}

public class animals {

    public static void main(String[] args) {
        // Scanner scan = new Scanner(System.in);
        // String name = scan.nextLine();
        Animal a = new Animal("Dog");

        Dog d = new Dog("Barks");

        d.routine();

        Puppy p = new Puppy("Puppy");

        p.schedule();
    }
}
