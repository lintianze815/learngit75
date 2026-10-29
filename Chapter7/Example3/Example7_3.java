package Chapter7.Example3;

interface SpeakHello {  //定义接口和抽象方法，任何实现这个接口的类都必须提供 speak() 方法的具体实现。
    void speak();
}

class  HelloMachine {
  public void turnOn(SpeakHello hello) {   //方法 turnOn，它接受一个 SpeakHello 类型的参数
      hello.speak();   //调用了传入对象的 speak() 方法,这意味着无论你传递的是哪个实现了 SpeakHello 接口的对象，都会执行其 speak() 方法的具体实现。
  }
}

public class Example7_3 {
  public static void main(String args[]) {
     HelloMachine machine = new HelloMachine();
     
     // 使用匿名类实现 SpeakHello 接口并传递给 turnOn 方法
     machine.turnOn( new SpeakHello(){
        public void speak() {
            System.out.println("hello,you are welcome!");
        }
    } 
    ); 
     
    // 另一个匿名类实现 SpeakHello 接口并传递给 turnOn 方法
    machine.turnOn( new SpeakHello(){
        public void speak() {
            System.out.println("你好，欢迎光临!");
        }
    } 
    ); 
  } 
}
