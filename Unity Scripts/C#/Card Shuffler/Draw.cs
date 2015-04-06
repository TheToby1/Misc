using UnityEngine;
using System.Collections;

public class Draw : MonoBehaviour {

	public float smooth = 2.0F;
	public float tiltAngle = 180.0F;
	private float position;
	private float move;

	void Update() {

		position = transform.position.y;

		if(position==0.50f){
			move= 0f;
		}
		else if(position==0.51f){
			move= 3f;
		}
		else if(position>0.48f&&position<0.49f){
			move= -3f;
		}

		if(position>0.48f){
			MoveTowardsTarget (move, 2f, 0f);
		}
	}


	public void MoveTowardsTarget(float x, float y, float z) {


		//move towards where ever you like)
		Vector3 targetPosition = new Vector3(x,y,z);
		
		Vector3 currentPosition = this.transform.position;
		//first, check to see if we're close enough to the target
		if(Vector3.Distance(currentPosition, targetPosition) > .1f) { 
			Vector3 directionOfTravel = targetPosition - currentPosition;
			//now normalize the direction, we only want the direction information
			directionOfTravel.Normalize();
			//scale the movement on each axis by the directionOfTravel vector components
			
			this.transform.Translate(
				(directionOfTravel.x * smooth * Time.deltaTime),
				(directionOfTravel.y * smooth * Time.deltaTime),
				(directionOfTravel.z * smooth * Time.deltaTime),
				Space.World);
		}

		StartCoroutine(waiter());
	}
	
	public IEnumerator waiter() {

		yield return new WaitForSeconds(4f);

			float tiltAroundX = Input.GetAxis("Vertical") + tiltAngle;
			Quaternion target = Quaternion.Euler(tiltAroundX, 0.0f, 0.0f);
			transform.rotation = Quaternion.Slerp(transform.rotation, target, Time.deltaTime * smooth);
		
	}
	
}