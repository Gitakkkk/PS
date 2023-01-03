function solution(s) {
  let arr = s.split(' ');
  let result = '';
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      if (j % 2 === 0) result = result + arr[i][j].toUpperCase();
      else result = result + arr[i][j].toLowerCase();
    }
    i < arr.length - 1 ? (result = result + ' ') : null;
  }
  return result;
}
