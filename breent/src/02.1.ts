import {readFile}  from 'fs/promises';

async function go() {
  let h = 0;
  let v = 0;
  (await readFile('./data/02.txt')).toString()
    .split('\n')
    .filter(Boolean)
    .forEach(row => {
      const [dir, mag] = row.split(' ');
      switch (dir) {
        // what do if already 0
        case 'up': {
          v -= parseInt(mag, 10);
          break;
        }
        case 'down': {
          v += parseInt(mag, 10);
          break;
        }
        case 'forward': {
          h += parseInt(mag, 10);
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
