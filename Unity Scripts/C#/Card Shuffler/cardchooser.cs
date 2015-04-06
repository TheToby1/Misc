using UnityEngine;
using System.Collections;

public class cardchooser : MonoBehaviour{

	public GUIText card1;
	public GUIText card2;
	public GUIText card3;

	private Class1[] deck;
	private Class1 temp;
	
	void Start(){
		card1.text = "";
		card2.text = "";
		card3.text = "";
		Class1[] deck = deckCon ();
		deck = shuffle (deck);
		/*deck = new Class1[52];
		string[] values = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
		
		for(int i =0;i<52;i++){
			deck[i] = new Class1();
		}
		
		for(int i = 0; i<13 ; i++){
			deck[i].setSuit("Hearts");
			deck[i].setNum(values[i]);
		}
		for(int i = 13; i<26 ; i++){
			deck[i].setSuit("Diamonds");
			deck[i].setNum(values[i-13]);
		}
		for(int i = 26; i<39 ; i++){
			deck[i].setSuit("Spades");
			deck[i].setNum(values[i-26]);
		}
		for(int i = 39; i<52 ; i++){
			deck[i].setSuit("Clubs");
			deck[i].setNum(values[i-39]);
		}*/


		/*int position = 0;
		
		for (int i = 0; i < 52; i++)
		{
			position = Random.Range(0,51);
			temp = deck[position];
			deck[position] = deck[i];
			deck[i] = temp;
		}*/

		writegui (deck);


	
	}

	public Class1[] deckCon(){
		deck = new Class1[52];
		string[] values = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
		
		for(int i =0;i<52;i++){
			deck[i] = new Class1();
		}
		
		for(int i = 0; i<13 ; i++){
			deck[i].setSuit("Hearts");
			deck[i].setNum(values[i]);
		}
		for(int i = 13; i<26 ; i++){
			deck[i].setSuit("Diamonds");
			deck[i].setNum(values[i-13]);
		}
		for(int i = 26; i<39 ; i++){
			deck[i].setSuit("Spades");
			deck[i].setNum(values[i-26]);
		}
		for(int i = 39; i<52 ; i++){
			deck[i].setSuit("Clubs");
			deck[i].setNum(values[i-39]);
		}
		return deck;
	}

	public Class1[] shuffle(Class1[] deck){

		int position = 0;
		
		for (int i = 0; i < 52; i++)
		{
			position = Random.Range(0,51);
			temp = deck[position];
			deck[position] = deck[i];
			deck[i] = temp;
		}
		return deck;
	}

	public void writegui(Class1[] deck){
		StartCoroutine (gui (deck));

	}

	public IEnumerator gui(Class1[] deck) {
		
		yield return new WaitForSeconds(6f);
		card1.text = "The " + deck [49].retNum () + " of " + "\n" + deck [49].retSuit ();
		card2.text = "The " + deck [50].retNum () + " of " + "\n" + deck [50].retSuit ();
		card3.text = "The " + deck [51].retNum () + " of " + "\n" + deck [51].retSuit ();
	}



}
