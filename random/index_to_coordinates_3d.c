#include <stdio.h>

void indexToCoordinates(int i, int width, int height, int depth) {
    int x, y, z;

    x = i % width;
    y = (i / width) % height;
    z = i / (width * height);

    printf("(%d, %d, %d)\n", x, y, z);
}

int main() {
    int matrix_width = 3;
    int matrix_height = 3;
    int matrix_depth = 3;

    // Example index
    int index = 13;

    indexToCoordinates(index, matrix_width, matrix_height, matrix_depth);

    return 0;
}
