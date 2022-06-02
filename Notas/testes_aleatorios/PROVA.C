int main()

{
    int x;

    char ch;

    float f;

    ch = x = 300;

    printf("x=%d ch=%d\n", x, ch);

    x = ch = f = 98.8999;

    printf("f= %.4f ch=%c x=%d \n", f, ch, x);

    return 0;
}