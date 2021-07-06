#include <stdio.h>

int main() {
    int c;
    int shift = 13;
    while ((c =getchar()) !=EOF) {
        if (c >= 'a' && c <= 'm') {
            c = c + shift;
        } else if (c >= 'n' && c <= 'z') {
            c = c - shift;
        } else if (c >= 'A' && c <= 'M') {
            c = c + shift;
        } else if (c >= 'N' && c <= 'Z') {
            c = c - shift;
        }

        putchar(c);
    }
}
