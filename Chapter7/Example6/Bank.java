package Chapter7.Example6;

public class Bank {  //定义 Bank 类
    private int money;
    
    public void income(int in,int out) throws BankException {  // income 方法声明可能抛出 BankException
       if(in<=0||out>=0||in+out<=0) {  //如果入账金额小于等于0、支出金额大于等于0或者两者之和小于等于0
          throw new BankException(in,out); //方法抛出异常，导致方法结束
       }
       
       int netIncome=in+out;
       System.out.printf("本次计算出的纯收入是:%d元\n",netIncome);
       money=money+netIncome;
    } 
    public int getMoney() {
       return money;
    } 
}

