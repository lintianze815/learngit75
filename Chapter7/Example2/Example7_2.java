package Chapter7.Example2;

public class Example7_2 {
    public static void main(String args[]) {
        ShowBank showBank = new ShowBank();
        
        // 使用匿名类扩展 Bank 并传递给 showMess 方法,用的不带参数的构造函数
        showBank.showMess(new Bank() { 
            public void output() {              //匿名类作为子类重写抽象方法
                money+=100;
                System.out.printf("中国银行资金：%3d\n",money); 
            }  
        }
        );
        
        // 使用匿名类扩展 Bank 并传递给 showMess 方法，这次使用带参数的构造函数
        showBank.showMess(new Bank(500) { 
            public void output() {
                money+=100;
                System.out.printf("建设银行资金：%3d\n",money); 
            }  
        }
        );
   } 
}


