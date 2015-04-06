package minds;
import java.util.Scanner;

public class pidevide4 { 
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int times = scan.nextInt();
		int[] nums = new int[times];
		for(int i =0;i<times;i++){
			nums[i]=scan.nextInt();
			double pi = 0;
			double denominator = 1;
			
			//Actual pi estimate
			for (long x = 0; x < nums[i]; x++){
				pi = ((x&1)==0) ? pi + (1 / denominator):pi - (1 / denominator);
				denominator+=2;
			}
			System.out.println((double)Math.round(pi * 1000000000000000L) / 1000000000000000L);
			//end of pi estimate
		}
		scan.close();
	}
}
