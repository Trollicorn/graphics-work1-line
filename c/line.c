#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#include "line.h"
 
int plot(struct rgb ** graph, int x, int y, int r, int g, int b){
	graph[y][x].r = r;
	graph[y][x].g = g;
	graph[y][x].b = b;
}

int line(struct rgb ** graph, int x0,int y0,int x1,int y1,int r,int g,int b){
	
	if (x1 < x0){
		int tempX = x0;
		int tempY = y0;
		x0 = x1;
		y0 = y1;
		x1 = tempX;
		y1 = tempY;
	}	

	int x = x0; int y = y0;
	int A = y1-y0;
	int B = x0-x1;
	int d = A + B;

	//octant I and II
	if (y1 - y0 > 0){
		//octant I
		if (A < -1 * B){
			d += A;
			while (x <= x1){
				plot(graph,x,y,r,g,b);
				if (d>0){ //point is below line
					y++;
					d += 2*B;
				}
				x++;
				d += 2*A;
			} 
		}
		else{ //octant II
			d += B;
			while (y <= y1){
				plot(graph,x,y,r,g,b);
				if (d>0){ //point is to right of line
					x++;
					d += 2*A;
				}
				y++;
				d += 2*B;
			} 
		}
	}
	else{ //octant VII and VIII
		if (A < B){ //octant VIII
			d += A;
			while (x <= x1){
				plot(graph,x,y,r,g,b);
				if (d<0){ //point is below line
					y--;
					d += 2*B;
				}
				x++;
				d += 2*A;
			} 
		}
		else{ //octant VII
			d += A;
			while (y <= y1){
				plot(graph,x,y,r,g,b);
				if (d<0){ //point is below line
					x--;
					d += 2*B;
				}
				y++;
				d += 2*A;
			} 
		}
	}
	return 1;
}

void picmake(struct rgb ** graph, char * filename){
	FILE *f;
	f = fopen(filename,"w");
	fprintf(f, "P3 500 500 255\n");
	for (int y = 0; y < 500; y++){
		for (int x = 0; x < 500; x++){
			fprintf(f,"%d %d %d ",graph[y][x].r,graph[y][x].g,graph[y][x].b);	
		}
		fprintf(f,"\n");
	}
	fclose(f);
}

int main(){
	struct rgb ** graph = calloc(sizeof(struct rgb),500*500);
	line(graph,100,150,400,200,255,255,255);
	picmake(graph,"pic.ppm");
}
