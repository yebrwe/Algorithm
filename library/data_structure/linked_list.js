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
        if(this.current === this.tail) throw 'current node is tail.';
        this.current = this.current.next;
        return this;
    }

    prev() {
        if(this.current === this.head) throw 'current node is head.';
        this.current = this.current.prev;
        return this;
    }

    print() {
        let node = this.head;
        while(node.next !== this.tail) {
            node = node.next;
            console.log(node.value);
        }
    }

    reversePrint() {
        let node = this.tail;
        while(node.prev !== this.head) {
            node = node.prev;
            console.log(node.value);
        }
    }
}
class Node {
    constructor(value) {
        this.prev = null;
        this.next = null;
        this.value = value;
    }
}


function test() {
    const list = new LinkedList([1,2,3]);
    list.next().next().next().next().prev().prev().prev();
    console.log(list.current.value);
    list.print();
}

test();
