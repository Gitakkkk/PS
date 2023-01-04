function solution(s, n) {
  // 65 A 90 Z 97 a 122 z
  let result = '';
  for (let i = 0; i < s.length; i++) {
    let ascii = s.charCodeAt(s.indexOf(s[i]));
    if (ascii === 32) {
      result += ' ';
      continue;
    }
    if (ascii <= 90) {
      ascii += n;
      ascii > 90 ? (ascii -= 26) : null;
    } else {
      ascii += n;
      ascii > 122 ? (ascii -= 26) : null;
    }
    result += String.fromCharCode(ascii);
  }
  return result;
}
