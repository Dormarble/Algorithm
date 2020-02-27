#include<stdio.h>
#include<stdlib.h>
#define MAX 10000

void bfs(int a, int b, int n, int m);

int **isVisited;
char **matrix;

typedef struct {
	int data[MAX];
	int front;
	int rear;
} queue;

queue xQueue;
queue yQueue;

int IsEmpty(queue *q) {
	if (q->front == q->rear)
		return 1;
	else return 0;
}
void pushQueue(queue *q, int value) {
	q->rear = (q->rear + 1) % MAX;
	q->data[q->rear] = value;

}
int popQueue(queue *q) {
	q->front = (q->front + 1) % MAX;
	return q->data[q->front];
}
queue createQueue() {
	queue q;
	q.front = -1;
	q.rear = -1;
	return q;
}

int main() {
	int n, m;
	xQueue = createQueue();
	yQueue = createQueue();

	scanf("%d %d", &n, &m);

	matrix = (char **)calloc(n, sizeof(char *));
	matrix[0] = (char *)calloc(n*m, sizeof(char));
	isVisited = (int **)calloc(n, sizeof(int *));
	isVisited[0] = (int *)calloc(n*m, sizeof(int));
	for (int i = 1; i < n; i++) {
		matrix[i] = matrix[i - 1] + m;
		isVisited[i] = isVisited[i - 1] + m;
	}

	for (int i = 0; i < n; i++) {
		scanf("%s", matrix[i]);
		for (int j = 0; j < m; j++) {
			matrix[i][j] -= '0';
		}
	}

	bfs(0, 0, n, m);

	printf("%d", isVisited[n - 1][m - 1]);
}

void bfs(int a, int b, int n, int m) {
	int moveX[4] = { 1, -1, 0, 0 };
	int moveY[4] = { 0, 0, 1, -1 };

	isVisited[a][b] = 1;
	pushQueue(&xQueue, a);
	pushQueue(&yQueue, b);

	while (!IsEmpty(&xQueue)) {
		int x = popQueue(&xQueue);
		int y = popQueue(&yQueue);

		for (int i = 0; i < 4; i++) {
			int nextX = x + moveX[i];
			int nextY = y + moveY[i];

			if (0 <= nextX && nextX < n && 0 <= nextY && nextY < m) {
				if (matrix[nextX][nextY] == 1 && isVisited[nextX][nextY] == 0) {
					pushQueue(&xQueue, nextX);
					pushQueue(&yQueue, nextY);
					isVisited[nextX][nextY] = isVisited[x][y] + 1;
					if (nextX == n - 1 && nextY == m - 1) {
						return;
					}
				}
			}
		}
	}
}