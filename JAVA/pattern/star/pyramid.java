public  class pyramid{
    public static void main(String[] args) {
        int rows = 9;
        for(int i=0;i<rows;i++){
            for(int j=0;j<rows-i-1;j++){
                System.out.print(" ");
            }

            for(int k=0;k<=i;k++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}