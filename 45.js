function solution(answers) {
  const result = [];
  const ranks = [0, 0, 0];
  const one = [1, 2, 3, 4, 5];
  const two = [2, 1, 2, 3, 2, 4, 2, 5];
  const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  for (let i = 0; i < answers.length; i++) {
    if (one[i % 5] === answers[i]) ranks[0]++;
    if (two[i % 8] === answers[i]) ranks[1]++;
    if (three[i % 10] === answers[i]) ranks[2]++;
  }
  const max = Math.max(...ranks);
  for (let i = 0; i < ranks.length; i++) {
    if (ranks[i] === max) result.push(i + 1);
  }
  return result;
}
