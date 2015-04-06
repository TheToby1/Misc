using UnityEngine;
using System.Collections;

public class Shuffler : MonoBehaviour {
	public float smooth = 2.0F;
	public float tiltAngle = 180.0F;

	private GameObject[] deck;
	private GameObject temp;

	public GameObject card1;
	public GameObject card2;
	public GameObject card3;
	public GameObject card4;
	public GameObject card5;
	public GameObject card6;
	public GameObject card7;
	public GameObject card8;
	public GameObject card9;
	public GameObject card10;
	public GameObject card11;
	public GameObject card12;
	public GameObject card13;
	public GameObject card14;
	public GameObject card15;
	public GameObject card16;
	public GameObject card17;
	public GameObject card18;
	public GameObject card19;
	public GameObject card20;
	public GameObject card21;
	public GameObject card22;
	public GameObject card23;
	public GameObject card24;
	public GameObject card25;
	public GameObject card26;
	public GameObject card27;
	public GameObject card28;
	public GameObject card29;
	public GameObject card30;
	public GameObject card31;
	public GameObject card32;
	public GameObject card33;
	public GameObject card34;
	public GameObject card35;
	public GameObject card36;
	public GameObject card37;
	public GameObject card38;
	public GameObject card39;
	public GameObject card40;
	public GameObject card41;
	public GameObject card42;
	public GameObject card43;
	public GameObject card44;
	public GameObject card45;
	public GameObject card46;
	public GameObject card47;
	public GameObject card48;
	public GameObject card49;
	public GameObject card50;
	public GameObject card51;
	public GameObject card52;

	// Use this for initialization
	void Start () {
		deck = new GameObject[52]; 
		deck [0] = card1;
		deck [1] = card2;
		deck [2] = card3;
		deck [3] = card4;
		deck [4] = card5;
		deck [5] = card6;
		deck [6] = card7;
		deck [7] = card8;
		deck [8] = card9;
		deck [9] = card10;
		deck [10] = card11;
		deck [11] = card12;
		deck [12] = card13;
		deck [13] = card14;
		deck [14] = card15;
		deck [15] = card16;
		deck [16] = card17;
		deck [17] = card18;
		deck [18] = card19;
		deck [19] = card20;
		deck [20] = card21;
		deck [21] = card22;
		deck [22] = card23;
		deck [23] = card24;
		deck [24] = card25;
		deck [25] = card26;
		deck [26] = card27;
		deck [27] = card28;
		deck [28] = card29;
		deck [29] = card30;
		deck [30] = card31;
		deck [31] = card32;
		deck [32] = card33;
		deck [33] = card34;
		deck [34] = card35;
		deck [35] = card36;
		deck [36] = card37;
		deck [37] = card38;
		deck [38] = card39;
		deck [39] = card40;
		deck [40] = card41;
		deck [41] = card42;
		deck [42] = card43;
		deck [43] = card44;
		deck [44] = card45;
		deck [45] = card46;
		deck [46] = card47;
		deck [47] = card48;
		deck [48] = card49;
		deck [49] = card50;
		deck [50] = card51;
		deck [51] = card52;

		int position = 0;
		
		for (int i = 0; i < 52; i++){
			position = Random.Range(0,51);
			temp = deck[position];
			deck[position] = deck[i];
			deck[i] = temp;
		}

		for (int i = 0; i<52;i++){
			float xposition = (float)i;
			deck[i].transform.position = new Vector3 (-3f,(xposition*0.01f),3f);

		}

	
	}
	

	

}
