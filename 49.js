function solution(food) {
  let result = '';
  for (let i = 1; i < food.length; i++) {
    if (food[i] % 2 === 1) food[i] -= 1;
    result += `${i}`.repeat(food[i] / 2);
  }
  result += '0';
  for (let i = food.length; i >= 1; i--) {
    if (food[i] % 2 === 1) food[i] -= 1;
    result += `${i}`.repeat(food[i] / 2);
  }
  return result;
}
