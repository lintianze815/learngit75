package Chapter5.Example10;

class  Hominid {         //父类 类人猿
    void crySpeak(String s) {
        System.out.println(s); 
    }  
 }
 class People extends Hominid {   //子类 人类
    void computer(int a,int b) {  //子类新增方法
       int c=a*b;
       System.out.println(c); 
    }
    void crySpeak(String s) {     //子类重写了crySpeak方法
       System.out.println("***"+s+"***"); 
    }  
 }
 public class Example5_10 {
    public static void main(String args[]) {
       Hominid monkey;  
       People zhangsan = new People(); 

       System.out.println(zhangsan instanceof People); //检查 zhangsan 是否是 People 类的实例 
       
       monkey = zhangsan ; //monkey是People对象zhangsan的上转型对象
       System.out.println(monkey instanceof People); //输出true 

       monkey.crySpeak("I love this game");//等同于zhangsan.crySpeak("I love this game");
       //monkey.computer(10,10);非法，monkey不能直接调用子类自己新增的方法

       People people=(People)monkey; //把上转型对象强制转化为子类的对象
       people.computer(10,10);
    }
 }
 