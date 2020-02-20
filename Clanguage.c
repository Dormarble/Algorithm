#include<stdio.h>
#include<stdlib.h>

int main(void) {
	int n = 0;
	int pathNum = 0;
	int **adj;
	const int INF = 10000000;

	scanf("%d", &n);
	adj = (int**)calloc(sizeof(int*), n);
	
	for (int i= 0; i < n; i++) {
		adj[i] = (int*)calloc(sizeof(int), n);
			for (int j = 0; j < n; j++) {
				if (i == j){
					adj[i][j] = 0;
				}
				else {
					adj[i][j] = INF;
				}
			}
	}
	scanf("%d", &pathNum);
	for (int i = 0; i < pathNum; i++) {
		int a, b, weight;

		scanf("%d %d %d", &a, &b, &weight);
		a--;
		b--;
		if (weight < adj[a][b]){
			adj[a][b] = weight;
		}
	}
	for (int k = 0; k < n; k++) {
		for (int j = 0; j < n; j++) {
			if (adj[k][j] == INF) {
				continue;
			}
			for (int i = 0; i < n; i++) {
				if (adj[i][j] > adj[i][k] + adj[k][j]){
					adj[i][j] = adj[i][k] + adj[k][j];
				}
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (adj[i][j] == INF) {
				adj[i][j] = 0;
			}
			printf("%d ", adj[i][j]);
		}
		printf("\n");
	}
}