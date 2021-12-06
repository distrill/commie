use std::collections::HashMap;

use crate::day::Day;

#[derive(Debug)]
struct School {
    fish: HashMap<u64, u64>,
}

impl School {
    fn from_string(data: &str) -> School {
        let mut fish = HashMap::new();
        for f in data
            .split(',')
            .map(|x| x.parse::<u64>().unwrap())
            .collect::<Vec<u64>>()
        {
            let count = fish.entry(f).or_insert(0);
            *count += 1;
        }
        School { fish }
    }

    fn iter_day(&mut self) {
        let mut fish = HashMap::new();
        let mut soon_6 = 0;
        for (f, count) in self.fish.iter() {
            match f {
                0u64 => {
                    // each fish has a bb fish plus they reset
                    fish.insert(8, *count);
                    soon_6 += *count;
                }
                7u64 => {
                    soon_6 += *count;
                }
                1u64 | 2u64 | 3u64 | 4u64 | 5u64 | 6u64 | 8u64 => {
                    fish.insert(f - 1u64, *count);
                }
                _ => {
                    panic!("unexpected fish expectancy!");
                }
            }
        }
        if soon_6 > 0 {
            fish.insert(6, soon_6);
        }
        self.fish = fish;
    }

    fn iter_days(&mut self, n: u64) {
        for _ in 0..n {
            self.iter_day();
        }
    }

    fn count(&self) -> u64 {
        let mut count = 0;
        for (_, c) in self.fish.iter() {
            count += c;
        }
        count
    }
}

pub struct Day06 {}

impl Day06 {
    fn init_data(&self) -> School {
        let data = self.load_data();
        School::from_string(data[0].as_str())
    }
}

impl Day<u64> for Day06 {
    fn new() -> Day06 {
        Day06 {}
    }

    fn get_day_name(&self) -> String {
        "06".to_string()
    }

    fn run_01(&self) -> u64 {
        let mut school = self.init_data();
        school.iter_days(80);
        school.count()
    }

    fn run_02(&self) -> u64 {
        let mut school = self.init_data();
        school.iter_days(256);
        school.count()
    }
}
