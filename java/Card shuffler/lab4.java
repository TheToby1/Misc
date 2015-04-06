package Lab4;
import java.util.Scanner;
public class lab4 {
	
	public static void main(String args[]){
		
		Scanner scan = new Scanner(System.in);
		long startnum;
		int test=0,count=1;
		
		System.out.println("Please input a starting number.");
		startnum = scan.nextLong();
		
		do{
			if(startnum==1){
				test++;
			}
			else if(startnum%2==0){
				startnum=startnum/2;
				count++;
				System.out.println(startnum);
			}
			else if(startnum%2==1){
				startnum = (3*(startnum))+1;
				count++;
				System.out.println(startnum);
			}
			
			
		}while(test==0);
		System.out.println("Sequence contains " + count + " numbers.");
		
		scan.close();
	}
	

}
