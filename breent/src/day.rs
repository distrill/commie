use std::{
    fs::File,
    io::{prelude::*, BufReader},
};

pub trait Day<T: std::fmt::Display> {
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

    fn run(&self) {
        println!("{}.1 - {}", self.get_day_name(), self.run_01());
        println!("{}.2 - {}\n", self.get_day_name(), self.run_02());
    }

    fn run_01(&self) -> T;

    fn run_02(&self) -> T;
}
