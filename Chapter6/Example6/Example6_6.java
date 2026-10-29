package Chapter6.Example6;

interface SpeakHello {
    void speakHello();           //接口的抽象方法
}

class Chinese implements SpeakHello {    //实现了 SpeakHello 接口，并提供了 speakHello 方法的具体实现，输出中文问候语。
   public  void speakHello() {
       System.out.println("中国人习惯问候语：你好,吃饭了吗? ");
   }
}

class English implements SpeakHello {  //同样实现了 SpeakHello 接口，并提供了 speakHello 方法的具体实现，输出英文问候语。
    public  void speakHello() {
       System.out.println("英国人习惯问候语:你好,天气不错 ");
    }
}

class KindHello {     //KindHello类
   public void lookHello(SpeakHello hello) { //这个方法接受一个 SpeakHello 类型的参数 hello。这意味着你可以传递任何实现了 SpeakHello 接口的对象给这个方法。
       hello.speakHello();                    //在方法内部，调用了传入对象的 speakHello 方法。由于 hello 是 SpeakHello 类型的变量，它实际上会调用具体实现类中的 speakHello 方法（即接口回调）。
   }
}

public class Example6_6 {
   public static void main(String args[]) {
       KindHello a = new KindHello();  
       Chinese  ccc  = new Chinese();
       a.lookHello(ccc );   //调用 Chinese 类的 speakHello 方法
       a.lookHello(new English());   //调用 English 类的 speakHello 方法
       a.lookHello( ()->{
       System.out.println("码农习惯问候语：no bug");} );//用 Lambda 表达式 (()->{...}) 来实现 SpeakHello 接口的 speakHello 方法。Lambda 表达式的主体 {...} 提供了 speakHello 方法的具体实现      
   }
}
