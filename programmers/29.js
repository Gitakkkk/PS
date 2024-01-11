function solution(arr) {
  let result = [...arr];
  let answer = [];
  for (let i = 0; i < result.length; i++) {
    result[i] !== result[i + 1] ? answer.push(result[i]) : null;
  }
  return answer;
}
