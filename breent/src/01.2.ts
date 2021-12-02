import {readFile}  from 'fs/promises';

async function go() {
  const input = (await readFile('./data/01.txt')).toString()
    .split('\n')
    .filter(Boolean)
    .map((n: string) => parseInt(n, 10));

    const sum = input.reduce((sum: number, e: number, i: number) => {
        if (i < 3) return sum;
        const curr = e + input[i-1] + input[i-2];
        const prev = input[i-1] + input[i-2] + input[i-3];
        return curr > prev ? sum+1 : sum;
    }, 0);

   console.log(`sum: ${sum}`);
}

go()
  .then(() => console.log('DONE'))
  .catch(err => console.log(err));
