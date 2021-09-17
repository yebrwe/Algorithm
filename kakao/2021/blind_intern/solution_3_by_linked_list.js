//==========================================
//Linked List
//author: hklee
//date: 2021.09.17
//github: http://github.com/yebrwe/Algorithm
//==========================================
class LinkedList {
    constructor(arr) {
        this.head = new Node(-1);
        this.tail = new Node(-1);
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.deleted = Array.from(Array(1000000).fill(0));
        this.deleted_top = -1;
        this.current = this.head;

        if(!arr) return;
        for(const o of arr) {
            this.add(o);
        }
        this.current = this.head;
    }
    add(value) {
        const newNode = new Node(value);
        const currentPrevNode = this.current;
        const currentNextNode = this.current.next;
        newNode.prev = currentPrevNode;
        newNode.next = currentPrevNode.next;
        currentPrevNode.next = newNode;
        currentNextNode.prev = newNode;
        this.current = newNode;
    }
    remove() {
        if(this.current === this.head || this.current === this.tail) return;
        const prevNode = this.current.prev;
        const nextNode = this.current.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
        this.deleted[++this.deleted_top] = this.current;
        if(nextNode === this.tail) {
            this.current = prevNode;
        }else {
            this.current = nextNode;
        }
    }

    restore() {
        if(this.deleted_top === -1) return;
        const node = this.deleted[this.deleted_top--];
        const prevNode = node.prev;
        const nextNode = node.next;
        prevNode.next = nextNode.prev = node;
    }

    next() {
        if(this.current.next === this.tail) return;//throw 'current node is tail.';
        this.current = this.current.next;
        return this;
    }

    prev() {
        if(this.current.prev === this.head) return;//throw 'current node is head.';
        this.current = this.current.prev;
        return this;
    }
}
class Node {
    constructor(value) {
        this.prev = null;
        this.next = null;
        this.value = value;
    }
}
function range(n) {
    return Array.from(Array(n).fill(0).map((_, i)=>i))
}
function solution(n, k, cmd) {
    const arr = range(n);
    const list = new LinkedList(arr);
    list.current = list.head.next;
    while(true) {
        if(list.current.value === k) break;
        list.next();
    }
    
    for(const c of cmd) {
        if(c === 'Z') {
            list.restore();
        }else if(c === 'C') {
            list.remove();
        } else {    // 'U'  or  'D'
            const [dir, n] = c.split(' ');
            for(let i=0; i<n; i++) {
                if(dir === 'U') list.prev();
                if(dir === 'D') list.next();
            }
        }
    }
    let answer = '';
    list.current = list.head.next;
    for(let i=0; i<n; i++) {
        if(list.current.value === i) {
            answer += 'O';
            list.next();
        } else {
            answer += 'X';
        }
    }
    
    return answer;
}