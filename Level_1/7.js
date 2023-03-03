function solution(s) {
  const lower = s.toLowerCase().split('');
  let cnt = [0, 0];
  for (let i = 0; i < lower.length; i++) {
    if (lower[i] === 'p') cnt[0]++;
    else if (lower[i] === 'y') cnt[1]++;
  }
  return cnt[0] === cnt[1] ? true : false;
}
