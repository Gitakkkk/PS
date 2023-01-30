function solution(s) {
  const arr = s.split('');
  if (/[a-z]/.test(arr[0])) arr[0] = arr[0].toUpperCase();
  for (let i = 1; i < arr.length; i++) {
    if (arr[i - 1] === ' ') arr[i] = arr[i].toUpperCase();
    else if (arr[i - 1] !== ' ') arr[i] = arr[i].toLowerCase();
  }
  return arr.join('');
}
