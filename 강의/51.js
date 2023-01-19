function solution(n, arr) {
  const sumArr = [];
  let result = 0;
  let temp = 0;
  for (let i = 0; i < arr.length; i++) {
    let sum = 0;
    const tempArr = arr[i].toString().split('');
    tempArr.map((e) => (sum += Number(e)));
    sumArr.push(sum);
  }
  for (let i = 0; i < sumArr.length; i++) {
    if (sumArr[i] > temp) {
      result = arr[i];
      temp = sumArr[i];
    } else if (temp === sumArr[i]) {
      if (arr[i] > result) result = arr[i];
    }
  }
  return result;
}

let arr = [128, 460, 603, 40, 521, 137, 123];
console.log(solution(7, arr));
