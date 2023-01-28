function solution(babbling) {
  const valiable = ['aya', 'ye', 'woo', 'ma'];
  let result = 0;
  for (let i = 0; i < babbling.length; i++) {
    for (let j = 0; j < valiable.length; j++) {
      if (babbling[i].includes(valiable[j].repeat(2))) {
        break;
      }
      babbling[i] = babbling[i].split(valiable[j]).join(' ');
    }
    if (babbling[i].split(' ').join('').length === 0) result++;
  }
  return result;
}
