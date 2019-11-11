

var stage;
var canvas = document.getElementById('canvas');
var width = canvas.width;
var height = canvas.height;


function border(x, y, w, h, l){
	//create objects
	borderWidth = borderHeight = 10
	var right = new createjs.Shape(); 
	var left = new createjs.Shape();
	var top = new createjs.Shape();
	var bot = new createjs.Shape();

	//populate shape information
	right.graphics.beginFill("Black").drawRect(x + l - w, y, w, h);
	left.graphics.beginFill("Black").drawRect(x, y, w, h);
	top.graphics.beginFill("Black").drawRect(x, y, l, w);
	bot.graphics.beginFill("Black").drawRect(x, y + h - w, l, w);

	//append borders to stages
	stage.addChild(right);
	stage.addChild(left);
	stage.addChild(top);
	stage.addChild(bot);
}

function bar(x,y,n,l){

	let marginX = 50;
	let marginY = 250;
	let length = 50;
	let lines = 5;
	let lineThickness = 2;
	let height = 75;
	let width = (canvas.width - marginX*2)/4;
	let space = 75 / 5;

	x += marginX + width * n
	y += marginY + height * l;
	let temp = y;
	let padding = 2;

	if (n == 0){
		renderClef(x - 35, y - 30);
	}

	var line = new createjs.Shape();
	for (i = 0; i < lines; i++){
		line.graphics.beginFill("Black").drawRect(x, temp, width, lineThickness);
		temp += space;
		stage.addChild(line);
	}

	var end = new createjs.Shape();
	end.graphics.beginFill("Black").drawRect(x+width, y, lineThickness, height - space + padding);
	stage.addChild(end);
}

function line(l){
	
	nBars = 4;
	let space = (canvas.height - 300*2) / 4;
	let x = 0;
	let y = space * l;
	for (let i = 0; i < nBars; i++){
		bar(x,y,i,l);
	}

}

function score(){
	
	for (let i = 0; i < 4; i++){
		line(i);
	}

}

function title(){
	var text = new createjs.Text("Demo", "100px Arial", "#000000");
	text.y = 150;
	text.x = canvas.width / 2 - 125;
	text.textBaseline = "alphabetic";
	stage.addChild(text);

}

function handleImageLoad(event){
	var image = event.target;
	var bitmap = new createjs.Bitmap(image);
	stage.addChild(bitmap);

}


function renderClef(x,y){
	var bmp = new createjs.Bitmap('tclef.svg');
	bmp.scale = 0.1;
	bmp.x = x;
	bmp.y = y;
	stage.addChild(bmp);
}


function init(){
	
	stage = new createjs.Stage("canvas");

	border(0,0,10,height,width);
	title();
	score();

	createjs.Ticker.on("tick", stage);
}
