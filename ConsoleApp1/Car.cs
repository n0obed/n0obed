using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Car
    {
        public string name;
        public string color;
        public string type;
        public int topSpeed;
        public int price;
        public int horsePower;
        public Car(string Name= "Prado", string Color = "red", string Type1 = "SUV", int TopSpeed = 220, int Price = 110, int HorsePower = 249)
        {
            name = Name;
            color = Color;
            type = Type1;
            topSpeed = TopSpeed;
            price = Price;
            horsePower = HorsePower;
        }
    }
}
