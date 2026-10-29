package Chapter7.Example2;

public abstract class Bank {      //抽象类
    int money;
    public Bank(){                //无参数的构造函数将money初始化为100
        money = 100;
    }
    public Bank(int money){       //有参数的构造函数允许在创建对象时指定money的初始值
       this.money = money;
    }
    public abstract void output();      //抽象方法，每个子类必须重写该方法
}


