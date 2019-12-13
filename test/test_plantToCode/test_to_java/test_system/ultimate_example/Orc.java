import java.util.*;

public class Orc implements IAttack, IWalk{

    public String name;
    private int age;
    private Weapon weapon;

    public void attack(int damage) {
        throw new UnsupportedOperationException();
    }

    public void walk() {
        throw new UnsupportedOperationException();
    }

    private void sleep(int hours) {
        throw new UnsupportedOperationException();
    }
}