const fs = require('fs');

const dfs = (start, end) => {
  const ST = [[start, 0]];
  const visit = new Array(N + 1).fill(false);
  visit[start] = true;

  while (ST.length > 0) {
    const [curV, curW] = ST.pop();
    if (curV === end) return curW;

    for (const [neiV, neiW] of adj[curV]) {
      if (visit[neiV]) continue;
      ST.push([neiV, curW + neiW])
      visit[neiV] = true;
    }
  }
  return 0;
};

const stdin = fs.readFileSync(
  process.platform === 'linux' ? '/dev/stdin' : './00.txt'
).toString().trim().split('\n');

const [N, M] = stdin.shift().trim().split(' ').map(Number);
const input = (() => {
  let line = 0;
  return () => stdin[line++]
})();

const adj = new Array(N + 1).fill(0).map(() => []);

for (let i = 0; i < N - 1; i++) {
  const [v1, v2, w] = input().trim().split(' ').map(Number);
  adj[v1].push([v2, w]);
  adj[v2].push([v1, w]);
}

let ans = '';

for (let i = 0; i < M; i ++) {
  const [v1, v2] = input().trim().split(' ').map(Number);
  ans += `\n${dfs(v1, v2)}`;
}

console.log(ans.trim());