package Chapter5.Example13;

class Rectangle {
    public double width;
    public double height;
}

class Circle {
    public double radius;
}

public class no_obey_OCP {
    public double calculateArea(Object shape) {
        if (shape instanceof Rectangle) {
            Rectangle rect = (Rectangle) shape;
            return rect.width * rect.height;
        } else if (shape instanceof Circle) {
            Circle circle = (Circle) shape;
            return Math.PI * circle.radius * circle.radius;
        }
        return 0;
    }
}

//在这个例子中，每次增加一个新的形状（比如三角形），你就必须修改 calculateArea 方法。
//这违反了开-闭原则，因为你在扩展功能时不得不修改现有的代码。