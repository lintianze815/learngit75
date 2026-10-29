package Chapter5.Example3;

public class CheapGoods extends Goods {
    public int weight;
    public void newSetWeight(int w) {
       weight=w;
       System.out.println("int型的weight="+weight);
    }
    public double newGetPrice() {
        double price = weight*1;
        return price;
    }
}
