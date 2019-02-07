#include <stdio.h>
#include <stdlib.h>

struct pic {
	struct rgb color[500][500];
};

struct rgb {
	int r;
	int g;
	int b;
};

struct pic graphify(struct pic);

int plot(struct pic graph,int x,int y,int r,int g,int b);

int line(struct pic graph,int x0,int y0,int x1,int y1,int r,int g,int b);
