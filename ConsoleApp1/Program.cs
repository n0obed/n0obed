using System;
using System.Threading;



namespace ConsoleApp1;
class Program
{
    static void Main(string[] args)
    {
        Console.ForegroundColor = ConsoleColor.Magenta;
        Console.WriteLine(" /$$$$$$$                      /$$                               /$$                          \r\n| $$__  $$                    | $$                              | $$                          \r\n| $$  \\ $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$ \r\n| $$  | $$ /$$__  $$ |____  $$| $$ /$$__  $$ /$$__  $$ /$$_____/| $$__  $$ /$$__  $$ /$$__  $$\r\n| $$  | $$| $$$$$$$$  /$$$$$$$| $$| $$$$$$$$| $$  \\__/|  $$$$$$ | $$  \\ $$| $$  \\ $$| $$  \\ $$\r\n| $$  | $$| $$_____/ /$$__  $$| $$| $$_____/| $$       \\____  $$| $$  | $$| $$  | $$| $$  | $$\r\n| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$| $$       /$$$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$/\r\n|_______/  \\_______/ \\_______/|__/ \\_______/|__/      |_______/ |__/  |__/ \\______/ | $$____/ \r\n                                                                                    | $$      \r\n                                                                                    | $$      \r\n                                                                                    |__/      ");
        Console.WriteLine();
        Thread.Sleep(1000);
        Console.ForegroundColor = ConsoleColor.White;

        
        FindingUser();
        nikhil();

        print("THE END");
        Console.ReadKey();
    }


    public static void FindingUser()
    {
        string userName;
        while (true)
        {
            // may I get your name
            print("\nHi, May I get your name?\n");
            userName = Console.ReadLine().ToLower();
            if (userName == null) { return; }

            // hello user
            print("Hello ");
            Console.ForegroundColor = ConsoleColor.Magenta;
            print(userName);
            Console.ForegroundColor = ConsoleColor.White;
            print(" let me just quickly serach up your profile\n");
            Thread.Sleep(1500);

            // seraching user
            print("Searching for User".ToLower());
            for (int i = 0; i < 3; i++)
            {
                Thread.Sleep(1500);
                Console.Write(".");
            }
            Console.WriteLine();

            // Switch Case
            switch (userName)
            {
                case "jumbo":
                    cls();
                    print("Oh NO! AAAAAAAAAAAAAAA\n");
                    Thread.Sleep(2000);
                    print("Please dont shoot me, here take all the money in the register (╥_╥)\n");
                    Thread.Sleep(6000);
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("                      ███ \r\n                    ███ \r\n                   ██ \r\n                  ██ \r\n                 ███ \r\n        █████████████████████ \r\n     ███████████████████████████ \r\n   ███████████████ ███████████████ \r\n ██████████ ██████ ██████ █████████ \r\n █████████   █████ █████   █████████ \r\n█████████     ████ ████     ████████ \r\n████████       ███ ███       ████████ \r\n██████████████████ ██████████████████ \r\n█████████████████   █████████████████ \r\n████████   ████████████████  ████████ \r\n ███████                     ███████ \r\n  ████████                 ████████ \r\n   ██████████████████████████████ \r\n    ███████████████████████████");
                    Thread.Sleep(1000);
                    print("Do you want to open the Door?\n");
                    Console.ReadKey();
                    Console.WriteLine();
                    spam();

                    break;
                case "nikhil":
                    cls();
                    Thread.Sleep(2000);
                    Console.ForegroundColor = ConsoleColor.Magenta;
                    print("Welcome Back Nikhil!!\n");
                    Console.ForegroundColor = ConsoleColor.White;
                    Thread.Sleep(2500);
                    return;
                default:
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    print("UNKNOWN User Found??\n");
                    Console.ForegroundColor = ConsoleColor.White;
                    break;
            }
            Console.ReadKey();
        }
    }


    public static void nikhil()
    {
        print("Currently you have 2 cars in your inventory\n");
        Thread.Sleep(2000);

        // Cars Initialization
        Car toyota_prado = new();
        Car dodge_chal = new("Challenger", "red", "muscle", 326, 219, 303);
        print("    Quick Comparison    \n");
        CarsClass carClass = new();
        carClass.horses(dodge_chal, toyota_prado);
        carClass.eco(dodge_chal, toyota_prado);
        Thread.Sleep(3500);

        Console.Write("\n  ______ \n /|_||_\\`.__\n(   _    _ _\\\n=`-(_)--(_)-' \n\n");
        Thread.Sleep(2000);
    }

    public static void spam()
    {
        Thread.Sleep(600);
        bodies(1, 1500); // 1.5 seconds
        bodies(2, 1000); // 2 seconds
        bodies(5, 300);  // 1.5 seconds
        bodies(4, 200); // 1.4 seconds, 12 prints so far
        bodies(10, 100); // 1 second
        bodies(842);
    }





    // Helper Functions
    public static void cls()
    {
        for (int i = 0; i< 65; i++)
        {
        Console.WriteLine();
        }
    }
    public static void bodies(int count1, int x=0)
    {
        for (int i=0; i<count1; i++)
        {
            Console.Write("(x_x)");
            Thread.Sleep(x);
        }
    }

    public static void print(string text= "abc", int interval=45)
    {
        foreach (char c in text)
        {
            Console.Write(c.ToString());
            Thread.Sleep(interval);
        }
    }
}

