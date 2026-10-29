package Chapter5.Example13;

// 抽象类 Shape
abstract class Shape {
    public abstract double calculateArea();
}

// 具体形状类 Rectangle 实现 Shape
class Rectangle extends Shape {
    public double width;
    public double height;

    @Override
    public double calculateArea() {
        return width * height;
    }
}

// 具体形状类 Circle 实现 Shape
class Circle extends Shape {
    public double radius;

    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
}

// 计算器类 obey_OCP
class obey_OCP {
    public double calculateArea(Shape shape) {
        return shape.calculateArea();
    }
}

// 测试类 TestOCP
public class TestOCP1 { // 
    public static void main(String[] args) {
        obey_OCP calculator = new obey_OCP();

        // 创建矩形实例并计算面积
        Rectangle rectangle = new Rectangle();
        rectangle.width = 10;
        rectangle.height = 5;
        System.out.println("Rectangle area: " + calculator.calculateArea(rectangle));

        // 创建圆形实例并计算面积
        Circle circle = new Circle();
        circle.radius = 7;
        System.out.println("Circle area: " + calculator.calculateArea(circle));
    }
}

//使用一个抽象类或接口来定义一个通用的行为（如计算面积），然后让每个具体形状类去实现它：
//在这个改进后的版本中，如果需要添加一个新的形状（例如三角形），
//只需创建一个新的类并实现 calculateArea 方法，而不需要修改 AreaCalculator 类。
//这样就实现了对扩展开放，对修改关闭。