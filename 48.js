// 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
// 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
function solution(N, stages) {
  const result = [];
  const percent = [];
  for (let i = 1; i <= N; i++) {
    let den = 0;
    let mol = 0;
    stages.map((e) => {
      if (e >= i) den++;
      if (e === i) mol++;
    });
    if (mol === 0) {
      percent.push(0);
      continue;
    }
    percent.push(mol / den);
  }
  for (let i = 0; i < percent.length; i++) {
    result.push(percent.indexOf(Math.max(...percent)) + 1);
    percent[percent.indexOf(Math.max(...percent))] = -1;
  }
  return result;
}
