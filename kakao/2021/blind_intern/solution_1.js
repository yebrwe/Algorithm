const numbers = [
    ['zero', 0],
    ['one', 1],
    ['two', 2],
    ['three', 3],
    ['four', 4],
    ['five', 5],
    ['six', 6],
    ['seven', 7],
    ['eight', 8],
    ['nine', 9],
];
function solution(s) {
    var answer = 0;
    
    for(const number of numbers) {
        const regex = new RegExp(number[0],'g');
        s = s.replace(regex, number[1]);
    }
    answer = Number(s);
    return answer;
}