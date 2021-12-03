use crate::day::Day;

pub struct Day01 {}

impl Day01 {
    pub fn init_data(&self) -> Vec<i16> {
        let data = &self.load_data();
        data.iter().map(|x| x.parse::<i16>().unwrap()).collect()
    }
}

impl Day<i32> for Day01 {
    fn new() -> Day01 {
        Day01 {}
    }

    fn get_day_name(&self) -> String {
        "01".to_string()
    }

    fn run_01(&self) -> i32 {
        let data = &self.init_data();

        let mut sum = 0;

        for i in 1..data.len() {
            if data[i] > data[i - 1] {
                sum += 1;
            }
        }

        sum
    }

    fn run_02(&self) -> i32 {
        let data = &self.init_data();

        let mut sum = 0;

        for i in 3..data.len() {
            let curr = data[i] + data[i - 1] + data[i - 2];
            let prev = data[i - 1] + data[i - 2] + data[i - 3];
            if curr > prev {
                sum += 1;
            }
        }

        sum
    }
}
