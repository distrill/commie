import {readFile}  from 'fs/promises';

async function go() {
  const input = (await readFile('./data/01.txt')).toString()
    .split('\n')
    .filter(Boolean)
    .map(n => parseInt(n, 10));

  const sum = input.reduce((sum, _, i) => {
    if (i < 1) return sum;
    return input[i] > input[i-1] ? sum+1 : sum;
  }, 0);

 console.log(`sum: ${sum}`);
}

go()
  .then(() => console.log('DONE'))
  .catch(err => console.log(err));
