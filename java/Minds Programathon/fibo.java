package minds;

import java.math.*;
import java.util.*;

public class fibo {
	
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		int numtimes = scan.nextInt();
		int[] times = new int[numtimes];
        int max=0;
		for(int j =0;j<numtimes;j++){
			times[j] = scan.nextInt();
			if (times[j]>max) max = times[j];
		}

		
			
			int[]answers = new int [max];
            answers[0]= 0;
			int i = 1;
			int count = 1;
			BigInteger fib1 = BigInteger.ONE;
			BigInteger fib2 = fib1;
			BigInteger fib3 = BigInteger.ZERO;
			while(i<answers.length) {
				count++;
				if(length(fib3) == i) {
					answers[i]=count; 
					i++;
				}
				fib3 = fib2.add(fib1);
				fib1 = fib2;
				fib2 = fib3;
			}
			
			for(int j=0;j<times.length;j++){
				System.out.println(answers[times[j]-1]);
			}
			
			
		

			
		
	}
	
	public static int length(BigInteger huge) {
	    int digits = 0;
	    int bits = huge.bitLength();
	    // Serious reductions.
	    while (bits > 4) {
	      // 4 > log[2](10) so we should not reduce it too far.
	      int reduce = bits / 4;
	      // Divide by 10^reduce
	      huge = huge.divide(BigInteger.TEN.pow(reduce));
	      // Removed that many decimal digits.
	      digits += reduce;
	      // Recalculate bitLength
	      bits = huge.bitLength();
	    }
	    // Now 4 bits or less - add 1 if necessary.
	    if ( huge.intValue() > 9 ) {
	      digits += 1;
	    }
	    return digits;
	  }
	
	

}
