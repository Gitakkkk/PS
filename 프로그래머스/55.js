function solution(lottos, win_nums) {
  const result = [6, 6];
  const zeros = lottos.filter((e) => e === 0).length;
  let rank = 0;
  for (let i = 0; i < lottos.length; i++) {
    if (win_nums.includes(lottos[i])) {
      rank++;
      if (rank > 1) {
        result[0]--;
        result[1]--;
      }
    }
  }
  result[0] -= zeros;
  if (result[0] === 0) result[0] = 1;
  return result;
}
