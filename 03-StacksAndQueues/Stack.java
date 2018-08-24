import java.util.LinkedList;
public class Stack {
	LinkedList<Integer> stack;
	public Stack() {
		this.stack = new LinkedList<Integer>();
	}
	public void push(int val) {
		this.stack.add(val);
	}
	public int pop() {
		int result = this.stack.tail();
		return this.stack.pop();
	}
	public void printStack() {
		System.out.println(this.stack);
	}
	public static void main(String[] args) {
		Stack test = new Stack();
		test.printStack();
		test.push(1);
		test.printStack();
		test.push(3);
		test.push(5);
		test.printStack();
		int result = test.pop();
		System.out.println("result: " + result);
		test.printStack();
	}	
}
		
