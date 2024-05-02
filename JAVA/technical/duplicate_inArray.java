public class duplicate_inArray{
	public static void main(String[] args){
		int[] arr = {10,50,20,30,10,20,90};

		System.out.println("Duplicate element : ");
		for(int i=0; i<arr.length;i++)
			for(int j=i+1; j< arr.length;j++)
				if(arr[i] == arr[j])
					System.out.print(arr[j]+"\t");
		System.out.println();
		}
}
