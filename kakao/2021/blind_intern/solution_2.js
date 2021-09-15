//2. 거리두기 확인하기
function solution(places) {
    var answer = [];
    for(const place of places) {
        const people = [];
        for(let i=0; i<place.length; i++) {
            for(let j=0; j<place.length; j++) {
                if(place[i][j] == 'P') people.push([i, j]);
            }
        }
        let rule = 1;
        for(const person of people) {
            rule = bfs(person, place);
            if(!rule) break;
        }
        answer.push(rule);
    }
    
    return answer;
}

function bfs(person, place) {
    const q=[person];
    const dx = [-1,0,1,0];
    const dy = [0,-1,0,-1];
    const visited = [];
    for(let i=0; i<place.length; i++){
        const arr = [];
        for(let j=0; j<place[i].length; j++) {
            arr.push(false);
        }
        visited.push(arr);
    }
    while(q.length>0){
        const [px, py] = q.pop();
        visited[px][py] = true;
        for(let i=0; i<4; i++) {
            const x = px + dx[i];
            const y = py + dy[i];
            const dist = Math.abs(person[0]-x)+Math.abs(person[1]-y);
            
            if(x < 0 || y< 0 || x>=place.length || y>=place[0].length) continue;
            if(visited[x][y]) continue;
            if(place[x][y] == 'X') continue;
            if(place[x][y] == 'P' && dist <= 2) return 0;
            q.unshift([x, y]);
        }
    }
    return 1;
}