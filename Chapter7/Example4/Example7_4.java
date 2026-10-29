package Chapter7.Example4;

interface SpeakHello {
    void speak();
}

class  HelloMachine {
  public void turnOn(SpeakHello hello) {
      hello.speak();
  }
}

public class Example7_4 {
  public static void main(String args[]) {
     HelloMachine machine = new HelloMachine();
     machine.turnOn( ()->{        //向形参传递Lambada表达式的值。
                          System.out.println("hello,you are welcome!");
                     }); 
     machine.turnOn( ()->{       //向形参传递Lambada表达式的值。
                          System.out.println("你好，欢迎光临!");
                     }); 
  } 
}
