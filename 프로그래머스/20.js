function solution(s) {
  if (s.length % 2 === 1) return s.slice(parseInt(s.length / 2), parseInt(s.length / 2) + 1);
  else return s.slice(s.length / 2 - 1, s.length / 2 + 1);
}
