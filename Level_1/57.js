function solution(n, lost, reserve) {
  let result = n;
  const overlap = [];
  lost.map((v) => {
    if (reserve.includes(v)) overlap.push(v);
  });
  for (let i = 0; i < overlap.length; i++) {
    lost = lost.filter((v) => v !== overlap[i]);
    reserve = reserve.filter((v) => v !== overlap[i]);
  }
  for (let i = 1; i <= n; i++) {
    if (lost.includes(i)) {
      if (reserve.includes(i)) {
        reserve = reserve.filter((v) => v !== i);
        continue;
      }
      if (reserve.includes(i - 1)) {
        reserve = reserve.filter((v) => v !== i - 1);
        continue;
      }
      if (reserve.includes(i + 1)) {
        reserve = reserve.filter((v) => v !== i + 1);
        continue;
      }
      result--;
    }
  }
  return result;
}
