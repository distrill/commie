use crate::day::Day;

pub struct Day02 {}

impl Day for Day02 {
    fn new() -> Day02 {
        Day02 {}
    }

    fn get_day_name(&self) -> String {
        "02".to_string()
    }

    fn run_01(&self) {
        let data = &self.load_data();

        let mut v: i32 = 0;
        let mut h: i32 = 0;

        for row in data {
            let row: Vec<&str> = row.split(" ").collect();
            let dir = row[0];
            let mag = row[1].parse::<i32>().unwrap();
            match dir {
                "up" => {
                    v -= mag;
                }
                "down" => {
                    v += mag;
                }
                "forward" => {
                    h += mag;
                }
                _ => {
                    panic!("Unexpected dir");
                }
            }
        }

        self.log_01(h * v);
    }

    fn run_02(&self) {
        let data = &self.load_data();

        let mut v: i32 = 0;
        let mut h: i32 = 0;
        let mut aim: i32 = 0;

        for row in data {
            let row: Vec<&str> = row.split(" ").collect();
            let dir = row[0];
            let mag = row[1].parse::<i32>().unwrap();
            match dir {
                "up" => {
                    aim -= mag;
                }
                "down" => {
                    aim += mag;
                }
                "forward" => {
                    h += mag;
                    v += mag * aim;
                }
                _ => {
                    panic!("Unexpected dir");
                }
            }
        }

        self.log_02(h * v);
    }
}
