package Chapter5.Example12;

// 定义一个抽象类 Animal
abstract class Animal {
    // 抽象方法，没有具体实现
    public abstract void makeSound();

    // 普通方法，有具体实现
    public void eat() {
        System.out.println("This animal eats food.");
    }
}

// Dog 类继承自 Animal 并实现 makeSound 方法，必须写，因为抽象类规定你必须写
class Dog extends Animal {
    public void makeSound() {    
        System.out.println("The dog barks.");
    }
}

public class Example5_12 {
    public static void main(String[] args) {

        // Animal myAnimal = new Animal(); // 错误,不能这样做，因为 Animal 是抽象类不能被实例化

        // 创建 Dog 对象，Dog 继承自 Animal 并实现了 makeSound 方法
        Animal myDog = new Dog();
        myDog.makeSound(); // 输出: The dog barks.
        myDog.eat();       // 输出: This animal eats food.
    }
}
