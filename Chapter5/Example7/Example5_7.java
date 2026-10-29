package Chapter5.Example7;

class Sum { 
    int n;
    float f() { 
       float sum=0;
       for(int i=1;i<=n;i++)
          sum=sum+i;
       return sum;  
    }
}
class Average extends Sum {
    int n;     //重新声明变量n，这个n是子类自己的
    float f() {    //c重写方法f
      float c;
      super.n=n;   //用super使用父类的n，将子类中的n值赋给父类中的n
      c=super.f();  //计算从1到n的所有整数的和（调用了父类的方法）
      return c/n; 
    }
   float g() {
       float c;
       c=super.f();  //直接调用super.f();来获取从1到n的所有整数的和。
       return c/2; 
   }
}
public class
Example5_7 {
   public static void main(String args[]) {
       Average aver=new Average();  //创建了Average类的一个实例
       aver.n=100;  //置子类中的n为100
       float resultOne=aver.f(); //先将子类中的n（100）传递给父类的n,，然后计算从1到100的和，并返回这个和除以100的结果（即平均值）。
       float resultTwo=aver.g(); 
       System.out.println("resultOne="+resultOne);
       System.out.println("resultTwo="+resultTwo);
   }
}


