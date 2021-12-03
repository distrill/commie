mod day;
mod problems;

use crate::day::Day;
use crate::problems::day_01::Day01;
use crate::problems::day_02::Day02;
use crate::problems::day_03::Day03;

fn main() {
    println!("!! AOC 2021 !!");
    Day01::new().run();
    Day02::new().run();
    Day03::new().run();
}
