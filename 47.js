function solution(t, p) {
  let result = 0;
  const splitArr = t.split('');
  const joinArr = [];
  for (let i = 0; i < t.length; i++) {
    if (t.substr(i, p.length).length < p.length) continue;
    joinArr.push(t.substr(i, p.length));
  }
  joinArr.map((e) => {
    if (Number(e) <= Number(p)) result++;
  });
  return result;
}
