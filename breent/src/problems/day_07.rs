use std::cell::RefCell;
use std::collections::HashMap;

use crate::day::Day;

pub struct Day07 {}

impl Day07 {
    fn init_data(&self) -> Vec<i32> {
        let data = &self.load_data();
        data[0]
            .split(",")
            .map(|x| x.parse::<i32>().unwrap())
            .collect()
    }

    fn align_crabs<F>(&self, f: F) -> i32
    where
        F: Fn(i32, i32) -> i32,
    {
        let data = self.init_data();
        let mut counts = HashMap::new();

        let mut max_sum = 0;
        for i in 0..*data.iter().max().unwrap() {
            if !counts.contains_key(&i) {
                let mut sum = 0;
                for j in data.iter() {
                    sum += f(i, *j);
                }
                if sum < max_sum || max_sum == 0 {
                    max_sum = sum;
                }
                counts.insert(i, sum);
            }
        }

        max_sum
    }
}

impl Day<i32> for Day07 {
    fn new() -> Day07 {
        Day07 {}
    }

    fn get_day_name(&self) -> String {
        "07".to_string()
    }

    fn run_01(&self) -> i32 {
        self.align_crabs(|x, y| (x - y).abs())
    }

    fn run_02(&self) -> i32 {
        let memo = RefCell::new(HashMap::new());
        self.align_crabs(|x, y| {
            let diff = (x - y).abs();
            let mut memo = memo.borrow_mut();
            if memo.contains_key(&diff) {
                return *memo.get(&diff).unwrap();
            }
            let mut sum = diff;
            for i in 0..diff {
                sum += i;
            }
            memo.insert(diff, sum);
            sum
        })
    }
}
