// Learn C#
// C# (C-Sharp) is a programming language developed by Microsoft that runs on the .NET Framework.
// C# is used to develop web apps, desktop apps, mobile apps, games and much more.


using System;

namespace HelloWorld
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Hello World!");    
    }
  }
}


// What is C#?
// C# is pronounced "C-Sharp".

// It is an object-oriented programming language created by Microsoft that runs on the .NET Framework.

// C# has roots from the C family, and the language is close to other popular languages like C++ and Java.

// The first version was released in year 2002. The latest version, C# 13, was released in November 2024.

// C# is used for:

// Mobile applications
// Desktop applications
// Web applications
// Web services
// Web sites
// Games
// VR
// Database applications
// And much, much more!


// Why Use C#?
// It is one of the most popular programming languages in the world
// It is easy to learn and simple to use
// It has huge community support
// C# is an object-oriented language which gives a clear structure to programs and allows code to be reused, lowering development costs
// As C# is close to C, C++ and Java, it makes it easy for programmers to switch to C# or vice versa


// Example explained
// Line 1: using System means that we can use classes from the System namespace.

// Line 2: A blank line. C# ignores white space. However, multiple lines makes the code more readable.

// Line 3: namespace is used to organize your code, and it is a container for classes and other namespaces.

// Line 4: The curly braces {} marks the beginning and the end of a block of code.

// Line 5: class is a container for data and methods, which brings functionality to your program. Every line of code that runs in C# must be inside a class. In our example, we named the class Program.

// Don't worry if you don't understand how using System, namespace and class works. Just think of it as something that (almost) always appears in your program, and that you will learn more about them in a later chapter.

// Line 7: Another thing that always appear in a C# program is the Main method. Any code inside its curly brackets {} will be executed. You don't have to understand the keywords before and after Main. You will get to know them bit by bit while reading this tutorial.

// Line 9: Console is a class of the System namespace, which has a WriteLine() method that is used to output/print text. In our example, it will output "Hello World!".

// If you omit the using System line, you would have to write System.Console.WriteLine() to print/output text.

// Note: Every C# statement ends with a semicolon ;.

// Note: C# is case-sensitive; "MyClass" and "myclass" have different meaning.

// Note: Unlike Java, the name of the C# file does not have to match the class name, but they often do (for better organization). When saving the file, save it using a proper name and add ".cs" to the end of the filename. To run the example above on your computer, make sure that C# is properly installed: Go to the Get Started Chapter for how to install C#. The output should be:




// C# Variables
// Variables are containers for storing data values.

// In C#, there are different types of variables (defined with different keywords), for example:

// int - stores integers (whole numbers), without decimals, such as 123 or -123
// double - stores floating point numbers, with decimals, such as 19.99 or -19.99
// char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes
// string - stores text, such as "Hello World". String values are surrounded by double quotes
// bool - stores values with two states: true or false

using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      string name = "John";
      Console.WriteLine(name);  
     }
  }
}


using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      const int myNum = 15;
      myNum = 20;
      Console.WriteLine(myNum);
    }
  }
}


using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      string firstName = "John ";
      string lastName = "Doe";
      string fullName = firstName + lastName;
      Console.WriteLine(fullName);
    }
  }
}


using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      int x = 5, y = 6, z = 50;
      Console.WriteLine(x + y + z);
    }
  }
}


using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      int x, y, z;
      x = y = z = 50;
      Console.WriteLine(x + y + z);
    }
  }
}