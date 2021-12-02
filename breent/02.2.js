const {readFile}  = require('fs/promises');

async function go() {
  let h = 0;
  let v = 0;
  let aim = 0;
  (await readFile('./data/02.txt')).toString()
    .split('\n')
    .filter(Boolean)
    .forEach(row => {
      const [dir, mag] = row.split(' ');
      const x = parseInt(mag, 10);
      switch (dir) {
        // what do if already 0
        case 'up': {
          aim -= x;
          break;
        }
        case 'down': {
          aim += x;
          break;
        }
        case 'forward': {
          h += x;
          v += aim * x;
          break;
        }
        default: {
          throw new Error(`Unexpected dir: ${dir}`);
          break;
        }
      }
      console.log({dir, mag, h, v});
    });
  console.log({h, v, m: h*v});
}

go()
  .then(() => console.log('DONE'))
  .catch(err => console.log(err));
