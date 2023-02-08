function solution(n) {
  var answer = [];
  str = n.toString().split('');
  for (let i = 0; i < str.length; i++) {
    answer.push(Number(str[i]));
  }
  answer.reverse();
  return answer;
}
