package Chapter6.Example2;

interface  ShowMessage {
    void Display (String s);   // 抽象方法，需要在实现类中提供具体实现
    
    default void outPutStart(){        // 默认方法，提供了默认实现
       System.out.println("********");
    }
 }
 class TV implements ShowMessage {
    public void Display (String s) {
        System.out.println("tvtvtvtv");
        System.out.println(s);
        System.out.println("tvtvtvtv");
    }
 }
 class PC implements ShowMessage {
    public void Display (String s) { 
        System.out.println("pcpcpcpc");
        System.out.println(s);
        System.out.println("pcpcpcpc");
    }

    public void show(){
         System.out.println("biubiubiu");
    }
 }
 public class Example6_2 {
    public static void main(String args[]) {
        ShowMessage sm;                  //声明接口变量
        
        sm=new TV();                     // 将 TV 对象的引用赋给接口变量
        sm.Display ("长城牌电视机");      //接口回调,调用 TV 类中重写的 Display 方法
        
        sm=new PC();                     //将 PC 对象的引用赋给接口变量
        sm.outPutStart();                //调用接口中的默认方法 outPutStart
        sm.Display ("华为个人电脑");    //接口回调,调用 PC 类中重写的 Display 方法
        sm.outPutStart();                //调用接口中的默认方法 outPutStart
        //sm.show();
    } 
 }
 