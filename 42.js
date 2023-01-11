function solution(nums) {
  const max = nums.length / 2;
  const arr = nums.sort((a, b) => a - b);
  let cnt = 1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i - 1] && arr[i - 1] !== arr[i]) cnt++;
    if (cnt >= max) break;
  }

  return cnt;
}
