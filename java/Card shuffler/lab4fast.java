package Lab4;

public class lab4fast {
	
	final static long startTime = System.currentTimeMillis();
	
	public static void main(String args[]){
		
		int count=0,highest =0;
		long startnum=0,answer=0;
		
		
		for(long i = 5L; i >= 2; i--){
			
			startnum=i;
			count = 1;
			
			while(startnum>1){
				if((startnum & 1) == 0){
					startnum = startnum >> 1;
//					long tz = Long.numberOfTrailingZeros(startnum);
//					count+= tz;
//					startnum >>= tz;
					
				}
				else {
					startnum = (3*startnum+1) >> 1;
					count++;
				}
				count++;
				
			}
			
			if(highest<count){
				highest=count;
				answer=i;
			}
		}
		
		System.out.println(answer + " sequence contains " + highest + " numbers.");
		
		final long endTime = System.currentTimeMillis();

		System.out.println("Total execution time: " + (endTime - startTime) );

	}
}
