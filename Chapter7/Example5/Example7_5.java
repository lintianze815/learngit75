package Chapter7.Example5;

public class Example7_5 {
    public static void main(String args[ ]) {
       int n = 0,m = 0,t = 1000;
       
       try {  
            m = Integer.parseInt("8888");  //尝试将字符串 "8888" 转换为整数
            n = Integer.parseInt("ab89"); //"ab89" 不是一个有效的整数表示,发生异常,转向catch
            t = 7777;  //t没有机会被赋值,潜在未执行代码
       }
       catch(NumberFormatException e) {  //捕获并处理NumberFormatException异常，打印出异常信息（即错误消息）。
            System.out.println("发生异常:"+e.getMessage());
       }
       System.out.println("n="+n+",m="+m+",t="+t);
       
       try {  
            System.out.println("故意抛出I/O异常！");
            throw new java.io.IOException("我是故意的");//程序故意抛出一个新的java.io.IOException，并附带一条自定义的消息："我是故意的"。
            //System.out.println("这个输出语句肯定没有机会执行,所以必须注释掉，否则编译出错");不可达代码
       }
       catch(java.io.IOException e) {
             System.out.println("发生异常:"+e.getMessage()); //捕获并处理IOException异常，打印出异常信息（即自定义的错误消息）。
       }
    }
 }
 