#include <stdio.h>

// Create a structure called myStructure
struct myStructure {
  int myNum;
  char myLetter;
};

int main() {
  // Create a structure variable of myStructure called s1
  struct myStructure s1;

  // Assign values to members of s1
  s1.myNum = 13;
  s1.myLetter = 'B';

  // Print values
  printf("My number: %d\n", s1.myNum);
  printf("My letter: %c\n", s1.myLetter);

  return 0;
}


#include <stdio.h>

struct myStructure {
  int myNum;
  char myLetter;
};

int main() {
  // Create different struct variables
  struct myStructure s1;
  struct myStructure s2;

  // Assign values to different struct variables
  s1.myNum = 13;
  s1.myLetter = 'B';

  s2.myNum = 20;
  s2.myLetter = 'C';

  // Print values
  printf("s1 number: %d\n", s1.myNum);
  printf("s1 letter: %c\n", s1.myLetter);

  printf("s2 number: %d\n", s2.myNum);
  printf("s2 letter: %c\n", s2.myLetter);

  return 0;
}


#include <stdio.h>
#include <string.h>

struct myStructure {
  int myNum;
  char myLetter;
  char myString[30];  // String
};

int main() {
  struct myStructure s1;

  // Assign a value to the string using the strcpy function
  strcpy(s1.myString, "Some text");

  // Print the value
  printf("My string: %s", s1.myString);

  return 0;
}


#include <stdio.h>
#include <string.h>

// Create a structure
struct myStructure {
  int myNum;
  char myLetter;
  char myString[30];
};

int main() {
  // Create a structure variable and assign values to it
  struct myStructure s1 = {13, 'B', "Some text"};
  
  // Modify values
  s1.myNum = 30;
  s1.myLetter = 'C';
  strcpy(s1.myString, "Something else");

  // Print values
  printf("%d %c %s", s1.myNum, s1.myLetter, s1.myString);

  return 0;
}


#include <stdio.h>
#include <string.h>

struct myStructure {
  int myNum;
  char myLetter;
  char myString[30];
};

int main() {
  // Create a structure variable and assign values to it
  struct myStructure s1 = {13, 'B', "Some text"};

  // Create another structure variable
  struct myStructure s2;

  // Copy s1 values to s2
  s2 = s1;

  // Change s2 values
  s2.myNum = 30;
  s2.myLetter = 'C';
  strcpy(s2.myString, "Something else");

  // Print values
  printf("%d %c %s\n", s1.myNum, s1.myLetter, s1.myString);
  printf("%d %c %s\n", s2.myNum, s2.myLetter, s2.myString);
  return 0;
}


#include <stdio.h>

int main() {
  int myNumbers[] = {25, 50, 75, 100};
  printf("%d", myNumbers[0]);
 
  return 0;
}

#include <stdio.h>

int main() {
  int myNumbers[] = {25, 50, 75, 100};
  myNumbers[0] = 33;

  printf("%d", myNumbers[0]);
 
  return 0;
}

#include <stdio.h>

int main() {
  int myNumbers[] = {25, 50, 75, 100};
  int i;
  
  for (i = 0; i < 4; i++) {
    printf("%d\n", myNumbers[i]);
  }
 
  return 0;
}


#include <stdio.h>

int main() {
  // Declare an array of four integers:
  int myNumbers[4];

  // Add elements to it
  myNumbers[0] = 25;
  myNumbers[1] = 50;
  myNumbers[2] = 75;
  myNumbers[3] = 100;

  printf("%d\n", myNumbers[0]);
 
  return 0;
}


#include <stdio.h>

int main() {
  int myNumbers[] = {10, 25, 50, 75, 100};
  printf("%zu", sizeof(myNumbers));
 
  return 0;
}


#include <stdio.h>

int main() {
  int myNumbers[] = {10, 25, 50, 75, 100};
  int length = sizeof(myNumbers) / sizeof(myNumbers[0]);
  
  printf("%d", length);
  return 0;
}


#include <stdio.h>

int main() {
  int myNumbers[] = {25, 50, 75, 100};
  int i;
  
  for (i = 0; i < 4; i++) {
    printf("%d\n", myNumbers[i]);
  }
 
  return 0;
}



#include <stdio.h>

int main() {
  int myNumbers[] = {25, 50, 75, 100};
  int length = sizeof(myNumbers) / sizeof(myNumbers[0]);
  int i;

  for (i = 0; i < length; i++) {
    printf("%d\n", myNumbers[i]);
  }
  
  return 0;
}


#include <stdio.h>

int main() {
  int matrix[2][3] = { {1, 4, 2}, {3, 6, 8} };
  printf("%d", matrix[0][2]);
 
  return 0;
}

#include <stdio.h>

int main() {
  int matrix[2][3] = { {1, 4, 2}, {3, 6, 8} };
  matrix[0][0] = 9;
  printf("%d", matrix[0][0]);  // Now outputs 9 instead of 1
 
  return 0;
}


#include <stdio.h>

int main() {
  int matrix[2][3] = { {1, 4, 2}, {3, 6, 8} };

  int i, j;
  for (i = 0; i < 2; i++) {
    for (j = 0; j < 3; j++) {
      printf("%d\n", matrix[i][j]);
    }
  }
  
  return 0;
}


#include <stdio.h>

int main() {
  // A 3D array with 2 blocks, each with 4 rows and 3 columns
  int example[2][4][3] = {
    {
      {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}
    },
    {
      {13, 14, 15}, {16, 17, 18}, {19, 20, 21}, {22, 23, 24}
    }
  };

  // Print all elements using 3 nested loops
  for (int i = 0; i < 2; i++) {
    printf("Block %d:\n", i + 1);
    for (int j = 0; j < 4; j++) {
      for (int k = 0; k < 3; k++) {
        printf("%d ", example[i][j][k]);
      }
      printf("\n");
    }
    printf("\n");
  }

  return 0;
}