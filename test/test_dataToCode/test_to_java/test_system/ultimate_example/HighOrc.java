import java.util.*;

public class HighOrc extends Orc {

	protected ISpell spell;

	@override
	public void attack(int damage) {
		throw new UnsupportedOperationException();
	}

	@override
	private void sleep(int hours) {
		throw new UnsupportedOperationException();
	}
}