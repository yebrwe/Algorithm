const deleted = Array.from(Array(1000000).fill(0));
let deleted_top = -1;

function move(node, dir, n) {
    let targetNode = node;
    for(let i=0; i<n; i++) {
        if(dir === 'U') {
            if(!targetNode.prev) break;
            targetNode = targetNode.prev;
        }else if(dir === 'D') {
            if(!targetNode.next) break;
            targetNode = targetNode.next;
        }
    }
    return targetNode;
}

function remove(node){
    const prevNode = node.prev;
    const nextNode = node.next;
    if(prevNode) prevNode.next = nextNode;
    if(nextNode) nextNode.prev = prevNode;    
    
    //되돌리기 관련 로직 추가할것!
    deleted[++deleted_top]=node;
    return nextNode ? nextNode : prevNode;
}
function undo() {
    if(deleted_top === -1) return;
    const node = deleted[deleted_top--];
    const prevNode = node.prev;
    const nextNode = node.next;
    
    if(prevNode) prevNode.next = node;
    if(nextNode) nextNode.prev = node;
}
function solution(n, k, cmd) {
    let answer = '';
    //----HEAD----
    const head = {
        prev: null,
        next: null,
        position: -1,
    };
    let node = head;
    let prevNode = node;
    for(let i=0; i<n; i++) {
        node.next = {
            prev: node,
            next: null,
            position: i,
        };
        prevNode = node;
        node = node.next;
    }
    //----TAIL----
    node = {
        prev: prevNode,
        next: null,
        position: -1,
    }
    let selectNode = head;
    while(true) {
        if(selectNode.position === k) break;
        selectNode = selectNode.next;
    }
    
    for(const c of cmd) {
        if(c === 'Z') {
            undo();
        }else if(c === 'C') {
            selectNode = remove(selectNode);
        } else {    // 'U'  or  'D'
            const [dir, n] = c.split(' ');
            selectNode = move(selectNode, dir, n);
        }
    }
    let current_node = head.next;
    for(let i=0; i<n; i++) {
        if(current_node.position === i) {
            answer += 'O';
            if(current_node.next) {
                current_node = current_node.next;    
            }
        } else {
            answer += 'X';
        }
    }
    
    return answer;
}