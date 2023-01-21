function solution(k, m, score) {
  let result = 0;
  let cnt = 1;
  score.sort((a, b) => b - a);
  for (let i = m - 1; i < score.length; i += m) {
    if (cnt > parseInt(score.length / m)) break;
    result += score[i] * m;
    cnt++;
  }
  return result;
}
