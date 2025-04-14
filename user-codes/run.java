import java.util.*;
class Main{
        public static void main(String args[]){
              Scanner in = new Scanner(System.in);
              int n = in.nextInt();
              int arr[] = new int[n];
              for(int i=0;i<n;i++){
                  arr[i] = in.nextInt();
              }
              int trgt = in.nextInt();
          int ans = coinChange(n-1,arr,trgt);
          System.out.println("Number of coins : "+ans);
        }
  static int coinChange(int i,int coins[],int trgt){
    if(trgt==0) return 1;
    if(i<0 || trgt<0) return 0;
    int nt = coinChange(i-1,coins,trgt);
    int tk = coinChange(i,coins,trgt-coins[i]);
    return nt+tk;
  }
}