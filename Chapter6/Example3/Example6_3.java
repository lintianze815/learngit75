package Chapter6.Example3;

interface  ShowMessage {
    void Display(String s);   //接口的抽象方法
 }

 public class Example6_3 {
    public static void main(String args[]) {
        ShowMessage sm;   //声明接口变量。
        
        sm=(s)->{         //使用Lambda表达式，，用于实现 ShowMessage 接口中的 Display 方法。，并将引用赋给接口变量sm
            System.out.println("tvtvtvtv");
            System.out.println(s);
            System.out.println("tvtvtvtv");  
        };
        
        sm.Display("长城牌电视机"); //调用第一个Lambda表达式的实现
        
        sm=(s)->{         //再次使用Lambda表达式实现了 ShowMessage 接口中的 Display 方法，并将引用赋给接口变量sm
            System.out.println("pcpcpcpc");
            System.out.println(s);
            System.out.println("pcpcpcpc");  
        };
        
        sm.Display("华为个人电脑"); //接口回调Lambada表达式实现的接口方法。
    } 
 }
 