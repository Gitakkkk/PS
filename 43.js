function solution(a, b, n) {
  // 마트에 줘야 하는 병 수 a, a개를 주면 마트가 주는 병수 b, 가지고 있는 빈 병 수 n
  let result = 0;
  if (a > n) return cnt;
  let earn = parseInt(n / a) * b;
  let exist = parseInt(n % a);
  let cnt = earn + exist;
  while (true) {
    result += earn;
    if (a > cnt) return result;
    earn = parseInt(cnt / a) * b;
    exist = parseInt(cnt % a);
    cnt = earn + exist;
  }
}
