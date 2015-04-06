using UnityEngine;
using System.Collections;

public class Class1{

	private string suit;
	private string num;
	
	public Class1(){
		suit = " ";
		num = " ";
	}
	
	public void setSuit(string a){
		suit = a;
	}
	
	public void setNum(string a){
		num = a;
	}
	
	public string retSuit(){
		return suit;
	}
	
	public string retNum(){
		return num;
	}

}
