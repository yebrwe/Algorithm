const N, M = 5;
const dx = [0,-1,0,1];
const dy = [-1,0,1,0];
const visited = Array.from(Array(N).fill(Array(M).fill(false)));
const dist = [];
//길 O, 벽 X, 시작 P

function bfs(coord) {
    const q = []
    q.push([0,0,0]);
    while(q.length > 0){
        const [x, y, len] = q.pop();
        for(let i=0; i<4; i++) {
            const px = dx[i] + x;
            const py = dy[i] + y;

            if(px < 0 || py < 0 || px > N || py > N) continue;
            if(visited[px][py]) continue;
            if(px == N-1 && py == M-1) return len + 1;
            if(dist[px][py] == 'O') {
                q.push([px, py, len+1]);
                visited[px][py] = true;
            }
        }
    }
    return -1;
}