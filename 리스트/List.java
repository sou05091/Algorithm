package 리스트;
import java.util.Random;
import java.util.Scanner;

class Node1 {
	int data;
	Node1 link;

	public Node1(int element) {
		data = element;
		link = null;
	}
}

class LinkedList1 {
	Node1 first;
	// 생성자
	public LinkedList1() {
		first = null;
		//연결리스트가 비어있는지 first == null;
		//연결 리스트 노드가 1개인지 확인하는법 first.next == 1;
		//연결리스트가 2개인 연결방법 확인 first.next.next == 2;
		//꼬리 노드인지 확인법 p.next == null;
	}
	public void removeFirst() {
		if(first != null) {
			first = first.link;
		}
	}
	public int Delete(int element) // delete the element
	{
		if(first != null) {
			if(first.link == null) {
				removeFirst();
			} else {
				Node1 ptr = first; //스캔중인 노드
				Node1 pre = first; //스캔중인 노드의 앞쪽 노드
				while(ptr.link != null) {
					pre = ptr;
					ptr = ptr.link;
				}
				pre.link = null;
			}
		}
		return 0;
	}

	public void Show() { // 전체 리스트를 순서대로 출력한다.
		Node1 ptr = first;
		while(ptr != null) {
			System.out.println(ptr.data);
			ptr = ptr.link;
		}
	}

	public void Add(int element) // 임의 값을 삽입할 때 리스트가 오름차순으로 정렬이 되도록 한다
	{
		Node1 nd = new Node1(element); // 삽입할 새로운 노드
		Node1 q = null; // 이전노드
		Node1 p = first; // 현재노드
		if (p == null) {// first가 널값인 경우(값이 없을때) 부모노드
			first = nd;
			//q = first.link;
			return;
		}
		while (!(p == null)) {
			{
				if (element < p.data) { // element가 current의 data보다 작을 때
		            if (q == null) { // 맨 앞에 삽입할 경우
		                nd.link = p;
		                first = nd;
		            } else {
		                q.link = nd;
		                nd.link = p;
		            }
		            return;
				} else if (element > p.data) { //element가 current의 data보다 클 때
					q = p;
					p = p.link;
					//return;
					if (p == null) {
						q.link = nd;
						return;
					}
				} else if (element < p.data) { //나중에 또 비교
					nd.link = p;
					q.link = p;
					return;
				}
			}
		}
	}

	public boolean Search(int data) { // 전체 리스트를 순서대로 출력한다.
		Node1 ptr = first;
		while(ptr != null) {
			if (ptr.data == data) {
				return true;
			} else {
				return false;
			}
		}
		return true;
	}
}

public class List {
	enum Menu {
		Add("삽입"), Delete("삭제"), Show("인쇄"), Search("검색"), Exit("종료");

		private final String message; // 표시할 문자열

		static Menu MenuAt(int idx) { // 순서가 idx번째인 열거를 반환
			for (Menu m : Menu.values())
				if (m.ordinal() == idx)
					return m;
			return null;
		}

		Menu(String string) { // 생성자(constructor)
			message = string;
		}

		String getMessage() { // 표시할 문자열을 반환
			return message;
		}
	}

	// --- 메뉴 선택 ---//
	static Menu SelectMenu() {
		Scanner sc = new Scanner(System.in);
		int key;
		do {
			for (Menu m : Menu.values()) {
				System.out.printf("(%d) %s  ", m.ordinal(), m.getMessage());
				if ((m.ordinal() % 3) == 2 && m.ordinal() != Menu.Exit.ordinal())
					System.out.println();
			}
			System.out.print(" : ");
			key = sc.nextInt();
		} while (key < Menu.Add.ordinal() || key > Menu.Exit.ordinal());
		return Menu.MenuAt(key);
	}

	public static void main(String[] args) {
		Menu menu; // 메뉴
		Random rand = new Random();
		System.out.println("Linked List");
		LinkedList1 l = new LinkedList1();
		Scanner sc = new Scanner(System.in);
		int data = 0;
		System.out.println("inserted");
		l.Show();
		do {
			switch (menu = SelectMenu()) {
			case Add: // 머리노드 삽입
				data = rand.nextInt(20);
				double d = Math.random();
				data = (int) (d * 50);
				l.Add(data);
				break;
			case Delete: // 머리 노드 삭제
				data = sc.nextInt();
				int num = l.Delete(data);
				System.out.println("삭제된 데이터는 " + num);
				break;
			case Show: // 꼬리 노드 삭제
				l.Show();
				break;
			case Search: // 회원 번호 검색
				int n = sc.nextInt();
				boolean result = l.Search(n);
				if (result == false)
					System.out.println("검색 값 = " + n + "데이터가 없습니다.");
				else
					System.out.println("검색 값 = " + n + "데이터가 존재합니다.");
				break;
			case Exit: // 꼬리 노드 삭제
				break;
			}
		} while (menu != Menu.Exit);
	}
}