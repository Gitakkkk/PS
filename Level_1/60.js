function solution(X, Y) {
  let result = '';
  const x = X.split('');
  const y = Y.split('');
  for (let i = 0; i < 10; i++) {
    const tempX = x.filter((v) => Number(v) === i).length;
    const tempY = y.filter((v) => Number(v) === i).length;
    result += i.toString().repeat(Math.min(tempX, tempY));
  }
  if (result === '') return '-1';
  if (Number(result) === 0) return '0';
  return result
    .split('')
    .sort((a, b) => Number(b) - Number(a))
    .join('');
}
