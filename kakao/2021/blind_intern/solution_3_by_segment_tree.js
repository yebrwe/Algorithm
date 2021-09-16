
function solution(n, k, cmd) {
    const deleted = [];
    let deleted_top = -1;
    function build(arr, node, nodeLeft, nodeRight) {
        if(nodeRight === nodeLeft) {
            return tree[node] = arr[nodeLeft];
        }
        const mid = parseInt((nodeLeft + nodeRight) / 2);
        const leftVal = build(arr, node*2, nodeLeft, mid);
        const rightVal = build(arr, node*2 + 1, mid+1, nodeRight);
        return tree[node] = leftVal + rightVal;
    }

    function update(index, newVal, node, nodeLeft, nodeRight) {
        if(index > nodeRight || index <nodeLeft) {
            return tree[node];
        }
        if(nodeLeft === nodeRight) {
            return tree[node] = newVal;
        }
        const mid = parseInt((nodeLeft + nodeRight) / 2);
        const leftVal = update(index, newVal, node*2, nodeLeft, mid);
        const rightVal = update(index, newVal, node*2 + 1, mid+1, nodeRight);
        return tree[node] = leftVal + rightVal;
    }
    function query(left, right, node, nodeLeft, nodeRight) {
        if(nodeRight < left || nodeLeft > right) {
            return 0;
        }
        if(nodeLeft >= left && nodeRight <= right) {
            return tree[node];
        }
        const mid = parseInt((nodeLeft+nodeRight)/2);
        return query(left, right, node*2, nodeLeft, mid) + query(left, right, node*2+1, mid+1, nodeRight);
    }

    function search(left, right) {
        return query(left, right, 1, 0, n-1);
    }
    //this is hell.
    function up(n, i) {
        let left = 1;
        let right = i;
        while(left <= right) {
            const mid = parseInt((left / right) / 2);
            if(search(start, end) > n) {
                right = mid + 1;
            }else if(search(start, end) < n) {
                left = mid + 1;
            }else {
                if(tree[mid] == 0) i++;
                break;
            }
        }
        return up(parseInt((start + end) / 2), end, x);
    }
    function remove(index) {
        update(index, 0, 1, 0, n-1);
        deleted[++deleted_top] = index;
    }
    function undo() {
        if(deleted_top === -1) return;
        const index = deleted[deleted_top--];
        update(index, 1, 1, 0, n-1);
    }
    //0~n 의 상태값 구하기
    //U x , D x , C , Z
    const table = Array.from(Array(n).fill(1)); 
    const tree = Array.from(Array(4*n).fill(null));
    
    build(table, 1, 0, n-1);
    remove(1);
    remove(2);
    undo();
    console.log(up(0, 5, 1));
    return tree[1];
}

solution(8, 0, []);
