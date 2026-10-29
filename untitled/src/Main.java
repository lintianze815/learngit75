import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=====简易计算器=====");
        System.out.println("支持：+ - * /，输入exit退出程序");

        while (true) {
            System.out.print("\n请输入第一个数字：");
            String num1Str = scanner.next();
            if (num1Str.equals("exit")) break;
            double num1 = Double.parseDouble(num1Str);

            System.out.print("请输入运算符(+ - * /)：");
            String op = scanner.next();
            if (op.equals("exit")) break;

            System.out.print("请输入第二个数字：");
            String num2Str = scanner.next();
            if (num2Str.equals("exit")) break;
            double num2 = Double.parseDouble(num2Str);

            double result = 0;
            boolean flag = true;
            switch (op) {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    if (num2 == 0) {
                        System.out.println("错误：除数不能为0！");
                        flag = false;
                    } else {
                        result = num1 / num2;
                    }
                    break;
                default:
                    System.out.println("运算符输入错误！");
                    flag = false;
                    break;
            }
            if (flag) {
                System.out.printf("计算结果：%.2f %s %.2f = %.2f%n", num1, op, num2, result);
            }
        }
        System.out.println("计算器已退出");
        scanner.close();
    }
}


