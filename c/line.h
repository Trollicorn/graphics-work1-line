#include <stdio.h>
#include <stdlib.h>

struct rgb {
	int r;
	int g;
	int b;
};

int plot(struct rgb ** graph,int x,int y,int r,int g,int b);

int line(struct rgb ** graph,int x0,int y0,int x1,int y1,int r,int g,int b);

void picmake(struct rgb ** graph, char * filename);
