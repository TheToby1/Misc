using UnityEngine;
using System.Collections;

public class GameController : MonoBehaviour {
	public GameObject hazard;
	public Vector3 spawnvalues;
	public int hazardcount;
	public float spawnwait;
	public float startwait;
	public float wavewait;
	public GUIText scoretext;
	public GUIText restarttext;
	public GUIText gameovertext;

	private bool gameover;
	private bool restart;
	public int score;
	
	void Start(){
		gameover = false;
		restart = false;
		restarttext.text = "";
		gameovertext.text = "";
		score = 0;
		updatescore ();
		StartCoroutine (SpawnWaves ());
	}

	void Update(){
		if(restart){
			if(Input.GetKeyDown(KeyCode.R)){
				Application.LoadLevel(Application.loadedLevel);
			}
		}
	}

	IEnumerator SpawnWaves(){
		yield return new WaitForSeconds(startwait);
		while(true){
			for(int i = 0;i<hazardcount;i++){
				Vector3 spawnposition = new Vector3 (Random.Range(-spawnvalues.x, spawnvalues.x), spawnvalues.y, spawnvalues.z);
				Quaternion spawnrotation = Quaternion.identity;
				Instantiate (hazard, spawnposition, spawnrotation);
				yield return new WaitForSeconds(spawnwait);
			}
			yield return new WaitForSeconds(wavewait);

			if (gameover){
				restarttext.text = "Press 'R' for Restart";
				restart = true;
				break;
			}
		}
	}

	public void AddScore(int newScoreValue){
		score += newScoreValue;
		updatescore ();
	}

	void updatescore(){
		scoretext.text = "Score: " + score;
	}

	public void gameOver(){
		gameovertext.text = "Game Over!";
		gameover = true;
	}
}
