function build(arr, node, left, right) {
    if(left === right) {
        tree[node] = arr[left];
        return tree[node];
    }
    const mid = parseInt((left + right)/2);
    const leftSum = build(arr, node*2, left, mid);
    const rightSum = build(arr, node*2 + 1, mid+1, right);
    tree[node] = leftSum + rightSum;
    return tree[node];
}
//query(3, 6)
function query(left, right) {
    return _query(left, right, 1, 0, N-1);
}
function _query(left, right, node, nodeLeft, nodeRight) {
    if(left > nodeRight || right < nodeLeft) {
        return 0;
    }
    if(nodeLeft >= left && nodeRight <= right) {
        return tree[node];
    }
    const mid = parseInt((nodeLeft + nodeRight)/2);
    return _query(left, right, node*2, nodeLeft, mid) + _query(left, right, node*2 + 1, mid+1, nodeRight);
}

function update(index, newValue) {
    return _update(index, newValue, 1, 0, N-1);
}
function _update(index, newValue, node, nodeLeft, nodeRight) {
    if(index < nodeLeft || index > nodeRight) {
        return tree[node];
    }
    if(nodeLeft === nodeRight) {    //최하위
        return tree[node] = newValue;
    }
    const mid = parseInt((nodeLeft + nodeRight)/2);
    const leftSum = _update(index, newValue, node*2, nodeLeft, mid);
    const rightSum = _update(index, newValue, node*2+1, mid+1, nodeRight);
    return tree[node] = leftSum + rightSum;
}

const arr = Array.from(Array(101)).map((_, i)=>i);
const N = arr.length;
const tree = Array.from(Array(N*4).fill(0));
function solution() {
    build(arr, 1, 0, N-1);
    update(3, 0);
    console.log(query(1, 3));
}

solution();
