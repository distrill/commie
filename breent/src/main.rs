mod day;
mod problems;

use crate::day::Day;
use crate::problems::day_01::Day01;
use crate::problems::day_02::Day02;

fn main() {
    Day01::new().run();
    Day02::new().run();
}
