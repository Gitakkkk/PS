function solution(array, commands) {
  const result = [];
  for (let i = 0; i < commands.length; i++) {
    const slice = array.slice(commands[i][0] - 1, commands[i][1]);
    const sorted = slice.sort((a, b) => a - b);
    result.push(sorted[commands[i][2] - 1]);
  }
  return result;
}
