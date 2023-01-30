function solution(A, B) {
  let arrA = A.sort((a, b) => a - b);
  let arrB = B.sort((a, b) => b - a);
  let result = 0;
  for (let i = 0; i < arrA.length; i++) {
    result += arrA[i] * arrB[i];
  }
  return result;
}
