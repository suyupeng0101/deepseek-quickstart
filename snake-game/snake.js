// 贪吃蛇核心逻辑 - 简单实现，便于理解与扩展

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const startBtn = document.getElementById('startBtn');
const pauseBtn = document.getElementById('pauseBtn');
const speedRange = document.getElementById('speedRange');
const scoreEl = document.getElementById('score');

const gridSize = 20; // 每个格子的像素大小
const tileCountX = canvas.width / gridSize;
const tileCountY = canvas.height / gridSize;

let snake = [{x:8, y:8}];          // 蛇身体数组：第0项是头
let velocity = {x:0, y:0};         // 当前速度（格/步）
let food = {x:5, y:5};             // 食物位置（格坐标）
let score = 0;
let running = false;
let gameInterval = null;
let speed = parseInt(speedRange.value, 10); // 毫秒间隔（数值越小速度越快）

/** 重置游戏状态（不会自动开始） */
function resetGame(){
  snake = [{x: Math.floor(tileCountX/2), y: Math.floor(tileCountY/2)}];
  velocity = {x:0, y:0};
  food = randomFood();
  score = 0;
  running = false;
  clearInterval(gameInterval);
  updateSpeedFromRange();
  draw();
  updateScore();
}

/** 随机生成食物（确保不与蛇重叠） */
function randomFood(){
  while(true){
    const pos = {
      x: Math.floor(Math.random() * tileCountX),
      y: Math.floor(Math.random() * tileCountY)
    };
    if(!snake.some(s => s.x === pos.x && s.y === pos.y)) return pos;
  }
}

/** 绘制背景、食物与蛇 */
function draw(){
  // 背景
  ctx.fillStyle = '#0b1220';
  ctx.fillRect(0,0,canvas.width,canvas.height);

  // 网格（可选，注释掉可提高性能）
  // ctx.strokeStyle = 'rgba(255,255,255,0.02)';
  // for(let i=0;i<tileCountX;i++){
  //   ctx.beginPath(); ctx.moveTo(i*gridSize,0); ctx.lineTo(i*gridSize,canvas.height); ctx.stroke();
  // }
  // for(let j=0;j<tileCountY;j++){
  //   ctx.beginPath(); ctx.moveTo(0,j*gridSize); ctx.lineTo(canvas.width,j*gridSize); ctx.stroke();
  // }

  // 食物
  ctx.fillStyle = '#ef4444';
  ctx.fillRect(food.x*gridSize, food.y*gridSize, gridSize, gridSize);

  // 蛇身体
  snake.forEach((s, i) => {
    // 头部使用渐变或高亮
    if(i === 0){
      ctx.fillStyle = '#34d399';
      ctx.fillRect(s.x*gridSize, s.y*gridSize, gridSize, gridSize);
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2;
      ctx.strokeRect(s.x*gridSize+1, s.y*gridSize+1, gridSize-2, gridSize-2);
    } else {
      ctx.fillStyle = '#34d399';
      ctx.fillRect(s.x*gridSize, s.y*gridSize, gridSize, gridSize);
    }
  });
}

/** 游戏一步推进（移动、检测碰撞、吃食物） */
function update(){
  if(!running) return;

  const head = { x: snake[0].x + velocity.x, y: snake[0].y + velocity.y };

  // 墙体碰撞：游戏结束
  if(head.x < 0 || head.x >= tileCountX || head.y < 0 || head.y >= tileCountY){
    gameOver();
    return;
  }

  // 自身碰撞检测
  if(snake.some(s => s.x === head.x && s.y === head.y)){
    gameOver();
    return;
  }

  // 前进：把新头加入数组前端
  snake.unshift(head);

  // 吃到食物
  if(head.x === food.x && head.y === food.y){
    score += 10;
    food = randomFood();
    updateScore();
  } else {
    // 否则删除尾巴（移动效果）
    snake.pop();
  }

  draw();
}

/** 游戏结束处理 */
function gameOver(){
  running = false;
  clearInterval(gameInterval);
  // 简单提示并重置（也可以提供“重试”UI）
  setTimeout(() => {
    alert('游戏结束! 得分: ' + score);
    resetGame();
  }, 10);
}

/** 更新页面上的分数显示 */
function updateScore(){
  scoreEl.textContent = '得分: ' + score;
}

/** 从速度滑块读取并更新计时器（如果在运行则重启计时器） */
function updateSpeedFromRange(){
  const val = parseInt(speedRange.value, 10);
  if(!isNaN(val) && val > 0) speed = val;
  if(gameInterval) {
    clearInterval(gameInterval);
    gameInterval = setInterval(update, speed);
  }
}

/** 处理键盘输入，支持方向键与 WASD。禁止直接反向转弯 */
window.addEventListener('keydown', (e) => {
  const key = e.key;
  // 防止在输入框/表单时误触（若页面后续有表单）
  if (['INPUT','TEXTAREA'].includes(document.activeElement.tagName)) return;

  // 禁止直接反向转弯（例如向上时立即按下向下无效）
  if((key === 'ArrowUp' || key === 'w' || key === 'W') && velocity.y === 1) return;
  if((key === 'ArrowDown' || key === 's' || key === 'S') && velocity.y === -1) return;
  if((key === 'ArrowLeft' || key === 'a' || key === 'A') && velocity.x === 1) return;
  if((key === 'ArrowRight' || key === 'd' || key === 'D') && velocity.x === -1) return;

  let changed = false;
  if(key === 'ArrowUp' || key === 'w' || key === 'W'){ velocity = {x:0, y:-1}; changed = true; }
  if(key === 'ArrowDown' || key === 's' || key === 'S'){ velocity = {x:0, y:1}; changed = true; }
  if(key === 'ArrowLeft' || key === 'a' || key === 'A'){ velocity = {x:-1, y:0}; changed = true; }
  if(key === 'ArrowRight' || key === 'd' || key === 'D'){ velocity = {x:1, y:0}; changed = true; }

  // 如果按键引起速度变化并且游戏未在运行，则启动游戏
  if(changed && !running && (velocity.x !== 0 || velocity.y !== 0)){
    running = true;
    clearInterval(gameInterval);
    gameInterval = setInterval(update, speed);
  }
});

/** 按钮事件绑定 */
startBtn.addEventListener('click', () => {
  // 点击开始则重置并开始新局
  resetGame();
  running = true;
  clearInterval(gameInterval);
  gameInterval = setInterval(update, speed);
});

pauseBtn.addEventListener('click', () => {
  running = !running;
  if(running){
    clearInterval(gameInterval);
    gameInterval = setInterval(update, speed);
    pauseBtn.textContent = '暂停';
  } else {
    clearInterval(gameInterval);
    pauseBtn.textContent = '继续';
  }
});

/** 速度滑块变化时更新速度 */
speedRange.addEventListener('input', () => {
  updateSpeedFromRange();
});

/** 初始化绘制并设置默认状态 */
resetGame();
