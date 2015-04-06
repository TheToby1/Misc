package Lab4;


public class lab4billion {
	
	final static long startTime = System.currentTimeMillis();
	
	public static void main(String args[]){
		
		int count=0;
		long startnum=0,answer=0;
		
		long[][] highest = new long[10][2];
		
		for(int i=0;i<10;i++){
			highest[i][0] = 0;
			highest[i][1] = 0;
		}
		
		
		for(long i = 10000000000L; i>2; i--){
			startnum=i;
			count = 1;
			answer = startnum;
			
			while(startnum>1){
				if((startnum & 1) == 0){
					startnum=startnum>>1;
				}
				else{
					startnum = (3*startnum+1)>>1;
					count++;
				}
				count++;
			}
			
			for(int x = 0;x<10;x++){
				if(highest[x][1]<count){
					for(int j =9; j >x;j--){
						highest[j][1]=highest[j-1][1];
						highest[j][0]=highest[j-1][0];
					}
					highest[x][1]=count;
					highest[x][0]=answer;
					x=10;
				}
				
			}
			
		}
		
		for(int i = 0;i<10;i++){
			System.out.println((i+1) + " " + highest[i][0] + " has " + highest[i][1]);
		}

		final long endTime = System.currentTimeMillis();

		System.out.println("Total execution time: " + (endTime - startTime) );
	}

}
