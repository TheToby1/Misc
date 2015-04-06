package Lab4;

public class recursivelab4 {
	
	final static long startTime = System.currentTimeMillis();
	
	private static int count = 0;
	
	public static void main(String args[]){
		
		int highest = 0;
		long answer = 0;
	
		for(long i = 1; i<10000001L; i++){
			count = 0;
			dothemaths(i);
			
			if(highest<count){
				highest=count;
				answer=i;
			}
			
		
		}
		
		System.out.println(answer + " sequence contains " + highest + " numbers.");
		
		final long endTime = System.currentTimeMillis();

		System.out.println("Total execution time: " + (endTime - startTime) );
		
	}
	
	
	public static int dothemaths(long a){
		count++;
		
		if(a==1){
			return (1);
		}
		else if(a%2==0){
			a = dothemaths(a/2);
		}
		else if(a%2==1){
			a = dothemaths((a*3)+1);
		}
		
		return count;
		
	}

}
