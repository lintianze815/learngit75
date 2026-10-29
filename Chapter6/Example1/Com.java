package Chapter6.Example1;

public interface Com { 
    public static final int MAX = 100;  //常量，等价写法：int MAX=100;
    public abstract void on();   //抽象方法，等价写法：void on();
    public abstract float sum(float x ,float y);  // 另一个抽象方法
    
    default int max(int a,int b) {   //default方法
        outPutJava();  //调用接口中的private方法
        return a>b?a:b;
    }
    public static void f() {      // 静态方法
       System.out.println("注意是从Java SE 8开始的");
    }
    private void outPutJava(){          // 私有方法
       System.out.println("Java");
    }
}



