import java.util.ArrayList;
import java.util.List;

enum Directions { N, NE, E, SE, S, SW, W, NW }

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Offsets {
    int a;
    int b;

    public Offsets(int a, int b) {
        this.a = a;
        this.b = b;
    }
}

class StackList {
    private List<Point> data;
    private int capacity;
    private int ptr;

    public StackList(int maxlen) {
        ptr = 0;
        capacity = maxlen;
        data = new ArrayList<>(maxlen);
    }

    public void push(Point x) {
        if (ptr >= capacity)
            throw new RuntimeException("Stack is full");
        data.add(x);
        ptr++;
    }

    public Point pop() {
        if (ptr <= 0)
            throw new RuntimeException("Stack is empty");
        Point p = data.remove(ptr - 1);
        ptr--;
        return p;
    }

    public boolean isEmpty() {
        return ptr <= 0;
    }
}

public class MazingProblem {
    static Offsets[] moves = new Offsets[8];
    private static final int WALL = 1;
    private static final int VISITED = 2;
    private static final int PATH = 3;

    public static void path(int[][] maze, int[][] mark, int ix, int iy) {
        mark[1][1] = VISITED;
        StackList st = new StackList(50);
        Point start = new Point(1, 1);
        st.push(start);

        boolean found = false;
        while (!st.isEmpty() && !found) {
            Point current = st.pop();
            int x = current.x;
            int y = current.y;

            for (int k = 0; k < 8; k++) {
                int nextrow = x + moves[k].a;
                int nextcol = y + moves[k].b;

                if (isValidMove(maze, mark, nextrow, nextcol)) {
                    Point nextPoint = new Point(nextrow, nextcol);
                    st.push(nextPoint);
                    mark[nextrow][nextcol] = VISITED;

                    if (nextrow == ix && nextcol == iy) {
                        found = true;
                        break;
                    }
                } else {
                    mark[ix][iy] = PATH;
                }
            }
        }

        if (found) {
            mark[ix][iy] = PATH;
        }
    }

    public static boolean isValidMove(int[][] maze, int[][] mark, int row, int col) {
        if (row < 0 || row >= maze.length || col < 0 || col >= maze[0].length) {
            return false; // 범위를 벗어난 경우
        }

        if (maze[row][col] == WALL || mark[row][col] == VISITED) {
            return false; // 벽이거나 이미 방문한 곳인 경우
        }

        return true;
    }

    public static void main(String[] args) {
        int[][] maze = {
                {0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1},
                {1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1},
                {0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1},
                {1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0},
                {1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1},
                {0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1},
                {0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1},
                {0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1},
                {0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1},
                {1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0},
                {0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
                {0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0}
        };

        int[][] mark = new int[12][15];

        for (int ia = 0; ia < 8; ia++) {
            moves[ia] = new Offsets(0, 0);
        }

        moves[0].a = -1;
        moves[0].b = 0;
        moves[1].a = -1;
        moves[1].b = 1;
        moves[2].a = 0;
        moves[2].b = 1;
        moves[3].a = 1;
        moves[3].b = 1;
        moves[4].a = 1;
        moves[4].b = 0;
        moves[5].a = 1;
        moves[5].b = -1;
        moves[6].a = 0;
        moves[6].b = -1;
        moves[7].a = -1;
        moves[7].b = -1;

        for (int i = 0; i <= 11; i++) {
            for (int j = 0; j <= 14; j++) {
                System.out.print(maze[i][j] + " ");
            }
            System.out.println();
        }

        path(maze, mark, 10, 13); // 출구 좌표 (10, 13)

        System.out.println("Mark 배열:");

        for (int i = 0; i <= 11; i++) {
            for (int j = 0; j <= 14; j++) {
                System.out.print(mark[i][j] + " ");
            }
            System.out.println();
        }
    }
}
