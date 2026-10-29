package Chapter6.Example1;

public class Example6_1 {
    public static void main(String args[]) {
        AAA a = new AAA();
        
        System.out.println("接口中的常量"+AAA.MAX);
        
        System.out.println("调用on方法(重写的):");
        a.on();
        
        System.out.println("调用sum方法(重写的):"+a.sum(12,18));
        
        System.out.println("调用接口提供的default方法"+a.max(12,78));
        Com.f();   // 调用接口的静态方法
    }
 }
 