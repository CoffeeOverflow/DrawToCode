import java.util.*;

public class Weapon {

	public String name;
	private int age;
	protected Attribute attribute;

	public Attribute getAttribute() {
		throw new UnsupportedOperationException();
	}

	public void setAttribute(Attribute attribute) {
		throw new UnsupportedOperationException();
	}
}