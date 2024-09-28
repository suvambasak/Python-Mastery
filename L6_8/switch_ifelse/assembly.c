#include <stdio.h>

int main()
{

    int x;

    x = 1000;

    // if (x == 10)
    //     return 'A';
    // else if (x == 9)
    //     return 'B';
    // else if (x == 8)
    //     return 'C';
    // else if (x == 7)
    //     return 'D';
    // else if (x == 6)
    //     return 'E';
    // else if (x == 5)
    //     return 'F';
    // else if (x == 4)
    //     return 'G';
    // else if (x == 3)
    //     return 'G';
    // else if (x == 2)
    //     return 'I';
    // else if (x == 1)
    //     return 'J';
    // else if (x == 0)
    //     return 'K';
    // else
    //     return 'E';

    switch (x)
    {
    case 10:
        return 'A';
    case 9:
        return 'B';
    case 8:
        return 'C';
    case 7:
        return 'D';
    case 6:
        return 'E';
    case 5:
        return 'F';
    case 4:
        return 'G';
    case 3:
        return 'G';
    case 2:
        return 'I';
    case 1:
        return 'J';
    case 0:
        return 'K';
    default:
        return 'E';
    }

    return 0;
}