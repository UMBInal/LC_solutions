class Solution {
    public double myPow(double x, int n) {
    
        if(n<0){
            return (1/x) * pow(1/x, -n-1);
        }
        else{
            return pow(x,n);
        }

    }

    double pow(double base, int n){

        if(n ==0){
            return 1;
        }
        else{
            return base * pow(base, n-1);
        }

    }


}