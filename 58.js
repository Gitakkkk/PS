function solution(k, score) {
  const result = [];
  let tempArr = [];
  for (let i = 0; i < score.length; i++) {
    tempArr.push(score[i]);
    tempArr.sort((a, b) => b - a);
    if (tempArr.length >= k) tempArr = tempArr.slice(0, k);
    result.push(tempArr[tempArr.length - 1]);
  }
  return result;
}
