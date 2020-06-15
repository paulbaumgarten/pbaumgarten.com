$(document).ready(function(){
	var canvas = document.getElementById("canvas1");
	var ctx = canvas.getContext('2d');
	function game(){
		
		
		$('#hi').show();
		$('#hi2').show();
		$('#hi3').show();
		ctx.fillStyle = "#c4c4c4"
		ctx.fillRect(0,0,500,500);
		//variables
		var bgMusic;
		var eat;
		var fail;
		var lose;
		bgMusic = new Audio("bgMusic.mp3");
		eat = new Audio("eat.mp3");
		fail = new Audio("fail.mp3");
		lose = new Audio("gameOver.mp3");
		bgMusic.volume = 0.1;
		eat.volume = 0.3;
		fail.volume = 1;
		bgMusic.play();

		var target = "";
		var score = 0;
		var movTime  = 4;
		var timer = 300;
		var alive = true;

		var redX = 250;
		var redY = 250;

		var blueX;
		var blueY;

		var greenX;
		var greenY;

		var yellowX;
		var yellowY;

		var purpleX;
		var purpleY;

		var whiteX;
		var whiteY;

		var skyBlueX;
		var skyBlueY;

		var pinkX;
		var pinkY;

		var limeX;
		var limeY;

		var orangeX;
		var orangeY;

		var beigeX;
		var beigeY;
		//functions
		function drawPlayer() {
			ctx.fillStyle = 'red';
			ctx.beginPath();
			ctx.arc(redX,redY,10,0,2*Math.PI);
			ctx.lineWidth = 1.5;
			ctx.stroke();
			//ctx.fill();
		}
		function drawBlue(){
			ctx.fillStyle = '#130c7a';
			ctx.beginPath();
			ctx.arc(blueX,blueY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawGreen(){
			ctx.fillStyle = '#095e0a';
			ctx.beginPath();
			ctx.arc(greenX,greenY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawYellow(){
			ctx.fillStyle = '#dbcc2b';
			ctx.beginPath();
			ctx.arc(yellowX,yellowY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawPurple(){
			ctx.fillStyle = '#ba4ae0';
			ctx.beginPath();
			ctx.arc(purpleX,purpleY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawWhite(){
			ctx.fillStyle = '#ffffff';
			ctx.beginPath();
			ctx.arc(whiteX,whiteY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawskyBlue(){
			ctx.fillStyle = '#1ec3e8';
			ctx.beginPath();
			ctx.arc(skyBlueX,skyBlueY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawPink(){
			ctx.fillStyle = '#fc3783';
			ctx.beginPath();
			ctx.arc(pinkX,pinkY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawLime(){
			ctx.fillStyle = '#6cfc37';
			ctx.beginPath();
			ctx.arc(limeX,limeY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawOrange(){
			ctx.fillStyle = '#f47a0e';
			ctx.beginPath();
			ctx.arc(orangeX,orangeY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawBeige(){
			ctx.fillStyle = '#eaeab4';
			ctx.beginPath();
			ctx.arc(beigeX,beigeY,10,0,2*Math.PI);
			ctx.fill();
		}

		function drawWall(){
			
		}


		function clear() {
			ctx.fillStyle = '#c4c4c4'
			ctx.fillRect(0,0,500,500);
		}
		clear();

		function checker(target){
			if (target=="blue") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score++;
					eat.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
			}
			else if (target=="green") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score++;
					eat.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
			}
			else if (target=="yellow") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score++;
					eat.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
			}
			else if (target=="purple") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score++;
					eat.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
			}
			else if (target=="white") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score++;
					eat.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
			}
			else if (target=="sky blue") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score++;
					eat.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
			}
			else if (target=="pink") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score++;
					eat.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
			}
			else if (target=="lime") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score++;
					eat.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
			}
			else if (target=="orange") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score++;
					eat.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score -= 5;
					fail.play();
				}

			}
			else if (target=="beige") {
				if (redX==greenX && redY==greenY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX == blueX&&redY == blueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==yellowX && redY==yellowY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==purpleX && redY==purpleY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==whiteX && redY==whiteY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==skyBlueX && redY==skyBlueY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==pinkX && redY==pinkY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==limeX && redY==limeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==orangeX && redY==orangeY) {
					changePosition();
					score -= 5;
					fail.play();
				}
				else if (redX==beigeX && redY==beigeY) {
					changePosition();
					score++;
					eat.play();
				}
			}
		}


		function randomOdd(){
			var num = Math.floor(Math.random() * (49 - 1)) + 1;
			if((num % 2) == 0){
	  			return num + 1;
	 		}
	 		else {
	  			return num;
	 		}
		}

		function changePosition(){
			if (alive==true) {
				
				blueX = randomOdd()*10;
				blueY = randomOdd()*10;

				greenX = randomOdd()*10;
				greenY = randomOdd()*10;

				yellowX = randomOdd()*10;
				yellowY = randomOdd()*10;

				purpleX = randomOdd()*10;
				purpleY = randomOdd()*10;

				whiteX = randomOdd()*10;
				whiteY = randomOdd()*10;

				skyBlueX = randomOdd()*10;
				skyBlueY = randomOdd()*10;

				pinkX = randomOdd()*10;
				pinkY = randomOdd()*10;

				limeX = randomOdd()*10;
				limeY = randomOdd()*10;

				orangeX = randomOdd()*10;
				orangeY = randomOdd()*10;

				beigeX = randomOdd()*10;
				beigeY = randomOdd()*10;

				clear();
				drawPlayer();
				drawBlue();
				drawGreen();
				drawYellow();
				drawPurple();
				drawWhite();
				drawskyBlue();
				drawPink();
				drawLime();
				drawOrange();
				drawBeige();
				randomTarget();
				movTime = 3;
			}
		}

		function randomTarget(){
			var number = Math.floor((Math.random()*10)+1);
			if (number==1) {
				target = "green";
				$('#hi').css('color','#095e0a');
			}
			else if (number==2) {
				target = "blue";
				$('#hi').css('color','#130c7a');
			}
			else if (number==3) {
				target = "yellow";
				$('#hi').css('color','#dbcc2b');
			}
			else if (number==4) {
				target = "purple";
				$('#hi').css('color','#ba4ae0');
			}
			else if (number==5) {
				target = "white";
				$('#hi').css('color','#ffffff');
			}
			else if (number==6) {
				target = "sky blue";
				$('#hi').css('color','#1ec3e8');
			}
			else if (number==7) {
				target = "pink";
				$('#hi').css('color','#fc3783');
			}
			else if (number==8) {
				target = "lime";
				$('#hi').css('color','#6cfc37');
			}
			else if (number==9) {
				target = "orange";
				$('#hi').css('color','#f47a0e');
			}
			else if (number==0) {
				target = "beige";
				$('#hi').css('color','#eaeab4');
			}
		}
		

		drawPlayer();
		drawGreen();
		drawBlue();
		drawYellow();
		drawPurple();
		drawWhite();
		drawskyBlue();
		drawPink();
		drawLime();
		drawOrange();
		drawBeige();

		//red movement
		$(document).keydown(function(event){
			if (alive==true) {
				clear();
				var key = event.which;
				if (key==37) {
					//left
					redX -= 20;
				}
				else if (key==39) {
					//right
					redX += 20;	
				}
				else if (key==38) {
					//up
					redY -= 20;	
				}
				else if (key==40) {
					//down
					redY += 20;		
				}

				if (redX<10) {
					redX+=20;
				}
				if (redY<10) {
					redY+=20;
				}
				if (redX>490) {
					redX-=20;
				}
				if (redY>490) {
					redY-=20;
				}
				drawPlayer();
				drawGreen();
				drawBlue();
				drawYellow();
				drawPurple();
				drawWhite();
				drawskyBlue();
				drawPink();
				drawLime();
				drawOrange();
				drawBeige();
			}
			
		});
		
		changePosition();
		function runGame(){
			if (alive==true) {
				checker(target);
				document.getElementById("hi").innerHTML = "Target:"+target;
				document.getElementById("hi2").innerHTML = "Score:"+ score;
			}
			else if (alive==false) {
				//ctx.clearRect(0,0,500,500);
				$('#hi').hide();
				$('#hi2').hide();
				$('#hi3').hide();
				bgMusic.stop();
			}
			
			
		}

		var run = setInterval(runGame, 50);
		var moveTime = setInterval(function(){
			if (movTime==0) {
				changePosition();
			}
			else {
			movTime--;
			}},1000);

		var startTime;
		startTime = setInterval(function(){
			if (timer==0) {
				clearInterval(startTime);
				alive = false;
				end(score,lose);
		}
			else{
				timer--;
				document.getElementById('hi3').innerHTML = timer;
			}
			console.log(timer);
		},1000);			
	}

	function story(){
		$('#hi').hide();
		$('#hi2').hide();
		$('#hi3').hide();
		var img = document.getElementById("dot");
		ctx.drawImage(img, 40,190);
		$('#canvas1').one("click",function(){
			var img = document.getElementById("we");
			ctx.drawImage(img, 0,0);
			setTimeout(function(){
				var img = document.getElementById("need");
				ctx.drawImage(img, 0,0);
			},100);
			setTimeout(function(){
				var img = document.getElementById("your");
				ctx.drawImage(img, 0,0);
			},200);
			setTimeout(function(){
				var img = document.getElementById("help");
				ctx.drawImage(img, 0,0);
			},300);
			$('#canvas1').one("click",function(){
				var img = document.getElementById("text1");
				ctx.drawImage(img, 0,0);
				$('#canvas1').one("click",function(){
					game();
					return;
				});
			});

		});

	}

	function end(score,lose) {
		lose.play();
		ctx.clearRect(0,0,500,500);
		ctx.fillStyle = "#000000"
		ctx.fillRect(0,0,500,500);

		ctx.fillStyle = "#ffffff"
		ctx.textAlign = "center";
		ctx.font = "40px Righteous";

		ctx.fillText("GAME OVER",250,250);

		setTimeout(function(){
			ctx.fillStyle = "#000000"
			ctx.fillRect(0,0,500,500);
			ctx.fillStyle = "#ffffff"
			ctx.fillText("Score: "+score,250,250);
		},2000);

		setTimeout(function(){
			ctx.fillStyle = "#000000"
			ctx.fillRect(0,0,500,500);
			ctx.fillStyle = "#ffffff";
			if (score<0) {
				ctx.fillText("Level: YOU'RE FIRED!",250,250);
			}
			else if (score<20&&score>0) {
				ctx.fillText("Level: Are you even trying?",250,250);
			}
			else if (score<40&&score>20) {
				ctx.fillText("Level: You can do better",250,250);
			}
			else if (score<60&&score>40) {
				ctx.fillText("Level: Good work",250,250);
			}
			else if (score<80&&score>60) {
				ctx.fillText("Level: Master Monster Hunter",250,250);
			}
			else if (score>100) {
				ctx.fillText("Level: You have been promoted to Captian of the Ship",250,250);
			}
		},4000);
		
		setTimeout(function(){location.reload()},7000);
		
	}
	//Page
	story();
});