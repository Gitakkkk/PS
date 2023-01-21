function solution(n, arr1, arr2) {
  const first = [];
  const second = [];

  for (let i = 0; i < arr1.length; i++) {
    num_arr1 = arr1[i].toString(2).padStart(n, '0');
    num_arr2 = arr2[i].toString(2).padStart(n, '0');
    first.push(num_arr1.split(''));
    second.push(num_arr2.split(''));
  }
  for (let i = 0; i < first.length; i++) {
    for (let j = 0; j < first[i].length; j++) {
      if (second[i][j] === '1') first[i][j] = '1';
      if (second[i][j] === '0' && first[i][j] === '0') first[i][j] = ' ';
      if (first[i][j] === '1') first[i][j] = '#';
      else first[i][j] = ' ';
    }
    first[i] = first[i].join('');
  }
  return first;
}
