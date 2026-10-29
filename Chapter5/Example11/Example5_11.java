package Chapter5.Example11;


class  Animal {
    void cry() {
    }  
 }
 class Dog extends Animal {
    void cry() {
       System.out.println("汪汪....."); 
    }  
 }
 class Cat extends Animal  {
    void cry() {
       System.out.println("喵喵....."); 
    }  
 }
 public class Example5_11 { 
    public static void main(String args[]) {
       Animal a;

       a = new Dog();
       a.cry(); 
       
       a=new Cat();
       a.cry();
   }
 }
 
