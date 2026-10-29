package Chapter5.Example8;

class Student {
    int number;
    String name;
    Student() {
    }
    Student(int number,String name) {
       this.number=number;
       this.name=name;
       System.out.println("我的名字是:"+name+ "学号是:"+number);
    }
  }

 class UniverStudent extends Student {
    boolean isMarry;

    UniverStudent(int number,String name,boolean b) {
       super(number,name);   //调用父类的构造方法
       isMarry=b;
       System.out.println("结婚了吗="+isMarry);
    }
 }
 
 public class


 Example5_8 {
    public static void main(String args[]) {
       UniverStudent zhang=new UniverStudent(9901,"何晓林",false);
    }
 }
 
 
 