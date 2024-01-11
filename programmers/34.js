function solution(sizes) {
  const max = [];
  const wid_arr = [];
  const len_arr = [];

  for (let i = 0; i < sizes.length; i++) {
    sizes[i][0] > sizes[i][1] ? max.push([sizes[i][0], sizes[i][1]]) : max.push([sizes[i][1], sizes[i][0]]);
  }

  for (let i = 0; i < sizes.length; i++) {
    wid_arr.push(max[i][0]);
    len_arr.push(max[i][1]);
  }

  const wid_max = Math.max(...wid_arr);
  const len_max = Math.max(...len_arr);

  return wid_max * len_max;
}
