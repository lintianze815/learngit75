package Chapter7.Example2;

public class ShowBank {
    void showMess(Bank bank) {       //接受一个bank类型的参数，并调用output方法
       bank.output();       //可以传入任何实现了 Bank 抽象类的具体子类（包括匿名类）的实例。
    } 
}


