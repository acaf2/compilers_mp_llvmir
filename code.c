int foo(int x, int y)
{
    return x*y;
}

int bar(int x, int y){

    return x/y;
}

int far(int x, int y, int z){
    int a;
    int b;
    int c;
    a = 3;
    b = 4;
    c = 5;
    a = b*b + c*c;
    return a+bar(foo(a,b/2), b);
}

int boo(){
    int a = 12; 
    int b = 32;
    a = -(b+a)+(-(b-13));
    b = (2+2)/2;
    return 0;
}

int main() {
    int a = 32;
    int b = 16;
    int c = far(a*b, b,c/a);
    int d;
    b = a*2;
    d = foo(a,b) + foo(a,b);
    d = a+a;
    return a + b;
}

