package minds;
import java.util.Scanner;

public class pi { 
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		while(true){
			System.out.println("How accurate do you want to be? (Bigger numbers means more accurate)");
			long count = scan.nextLong();
			long startTime = System.nanoTime();
			double pi = 0;
			double denominator = 1;
			
			//Actual pi estimate
			for (long x = 0; x < count; x++){
				pi = ((x&1)==0) ? pi + (1 / denominator):pi - (1 / denominator);
				denominator+=2;
			}
			//pi = pi * 4;
			System.out.println(pi);
			//end of pi estimate
			
			System.out.println("Total execution time: " + ((System.nanoTime() - startTime)/1000000) + "ms" );
			
			System.out.println("Type 1 if you want to estimate again.");
			if(!(scan.nextInt()==1)) break;
		}
		scan.close();
	}
}