mod day;
mod day_01;
mod day_02;

use crate::day::Day;
use crate::day_01::Day01;
use crate::day_02::Day02;

fn main() {
    let day_01 = Day01::new();
    day_01.run_01();
    day_01.run_02();

    let day_02 = Day02::new();
    day_02.run_01();
    day_02.run_02();
}
