package Chapter6.Example7;

public class AdvertisementBoard { //负责创建广告牌
    Advertisement adver;
    public void setAdvertisement(Advertisement adver){
        this.adver = adver;
    }
    public void show() {
        if(adver == null){
           System.out.println("广告招商中");
        }
        else {
           adver.showAdvertisement(); //接口回调
        }
   }
}
