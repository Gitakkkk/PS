function solution(num) {
  const result = [];
  num.map((e) => {
    const number = Number(e.toString().split('').reverse().join(''));
    if (number !== 1 && isPrime(number)) result.push(number);
  });
  return result;
}

function isPrime(n) {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

let arr = [32, 55, 62, 20, 250, 370, 200, 30, 100];
console.log(solution(arr));
