use std::{
    fs::File,
    io::{prelude::*, BufReader},
};

pub trait Day {
    fn new() -> Self;

    fn get_day_name(&self) -> String;

    fn load_data(&self) -> Vec<String> {
        let filename = format!("data/{}.txt", self.get_day_name());
        let file = File::open(filename).expect("no such file");
        let buf = BufReader::new(file);
        buf.lines()
            .map(|l| l.expect("Could not parse line"))
            .collect()
    }

    fn run_01(&self);

    fn run_02(&self);

    fn log_01<T: std::fmt::Display>(&self, result: T) {
        println!("{}.1 - {}", self.get_day_name(), result);
    }

    fn log_02<T: std::fmt::Display>(&self, result: T) {
        println!("{}.2 - {}\n", self.get_day_name(), result);
    }
}
