package Chapter7.Example1;

public class Example7_1 {
    public static void main(String args[]) {
       RedCowForm form = new RedCowForm("67农场");
       form.showCowMess();        // 输出红牛的信息
       form.cow.speak();          //直接调用红牛的 speak 方法
       
       //RedCowForm.RedCow redCow = new RedCowForm.RedCow(180,119,6000);
       //redCow.speak();          //编译错误,因为 RedCow 是一个非静态内部类，不能直接在外部类之外实例化。
      }   
 }
 