using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class CarsClass
    {
        //name, color, type, topspeed, price, hp
        



        // functions
        public void horses(Car car1, Car car2)
        {
            string val = (car1.horsePower >= car2.horsePower) ? val = car1.name : val = car2.name;
            Program.print(val + " is found to be more powerful!\n");
        }
        public void speed(Car car1, Car car2)
        {
            string val = (car1.topSpeed >= car2.topSpeed) ? val = car1.name : val = car2.name;
            Program.print(val + " is found to be more faster!\n");
        }
        public void eco(Car car1, Car car2)
        {
            string val = (car1.price <= car2.price) ? val = car1.name : val = car2.name;
            Program.print(val + " is found to be more economical!\n");
        }
    }
}
