package Chapter7.Example8;

public class CargoBoat {
    int realContent;  //装载的重量
    int maxContent;   //最大装载量
    public void setMaxContent(int c) {
        maxContent = c;
    }
    public void loading(int m) throws DangerException {
      realContent += m;
      if(realContent>maxContent) {
          throw new DangerException(); 
      }
   }
}
