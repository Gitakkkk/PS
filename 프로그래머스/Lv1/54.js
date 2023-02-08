function solution(s) {
  const result = [];
  for (let i = 0; i < s.length; i++) {
    const arr = [];
    let idx = s.indexOf(s[i]);
    if (idx === i) result.push(-1);
    else {
      while (idx != -1) {
        arr.push(idx);
        idx = s.indexOf(s[i], idx + 1);
      }
      result.push(arr[arr.length - 1] - arr[arr.length - 2]);
    }
  }
  return result;
}

function solution(s) {
  const result = [];
  const arr = [];
  for (let i = 0; i < s.length; i++) {
    if (s.indexOf(s[i]) === i) {
      result.push(-1);
      arr.push(s[i]);
    } else {
      result.push(arr.length - arr.lastIndexOf(s[i]));
      arr.push(s[i]);
    }
  }
  return result;
}
