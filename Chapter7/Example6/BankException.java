package Chapter7.Example6;

public class BankException extends Exception {   //定义自定义异常类 BankException
    String message;
    
    public BankException(int m,int n) {   //构造函数，接收入账和支出金额作为参数
        message="入账资金"+m+"是负数或支出"+n+"是正数，不符合系统要求.";
    }
    public String warnMess() {   //返回异常的具体消息。
        return message;  
    }
 } 
 