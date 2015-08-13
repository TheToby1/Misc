using UnityEngine;
using System.Collections;

public class DestroyByContact : MonoBehaviour {
	public GameObject explosion;
	public GameObject playerexplosion;
	public int scorevalue;
	private GameController gamecontroller;

	void Start(){
		GameObject gamecontrollerobject = GameObject.FindWithTag ("GameController");
		if(gamecontrollerobject!=null){
			gamecontroller = gamecontrollerobject.GetComponent<GameController>();
		}
		if(gamecontroller == null){
			Debug.Log ("Cannot fine 'GameController' script");
		}
	}

	void OnTriggerEnter(Collider other) {
		if(other.tag == "Boundary") return;

		Instantiate (explosion, GetComponent<Transform>().position, GetComponent<Transform>().rotation);
		if(other.tag == "Player"){ 
			Instantiate (playerexplosion, other.GetComponent<Transform>().position, other.GetComponent<Transform>().rotation);
			gamecontroller.gameOver ();
		}
		gamecontroller.AddScore (scorevalue);
		Destroy(other.gameObject);
		Destroy(gameObject);
	}
}
