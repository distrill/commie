use std::collections::HashMap;

use crate::day::Day;

#[derive(Debug)]
struct Point {
    x: i32,
    y: i32,
}

impl Point {
    fn from_string(s: &str) -> Point {
        let ns: Vec<i32> = s.split(',').map(|n| n.parse().unwrap()).collect();
        Point { x: ns[0], y: ns[1] }
    }
}

#[derive(Debug)]
struct Line {
    start: Point,
    end: Point,
}

impl Line {
    fn from_string(s: &str) -> Line {
        let ns: Vec<&str> = s.split(" -> ").collect();
        Line {
            start: Point::from_string(ns[0]),
            end: Point::from_string(ns[1]),
        }
    }
}

pub struct Day05 {}

impl Day05 {
    fn init_data(&self) -> Vec<Line> {
        self.load_data()
            .iter()
            .map(|line| Line::from_string(line.as_str()))
            .collect()
    }

    fn get_next(curr: i32, end: i32) -> i32 {
        if curr == end {
            return curr;
        }
        if curr > end {
            return curr - 1;
        }
        return curr + 1;
    }

    fn get_dangers(lines: Vec<Line>) -> i32 {
        let mut lookup = HashMap::new();

        for line in lines {
            let steps = std::cmp::max(
                (line.start.x - line.end.x).abs(),
                (line.start.y - line.end.y).abs(),
            ) + 1;

            let mut x = line.start.x;
            let mut y = line.start.y;
            for _ in 0..steps {
                let key = format!("{}-{}", x, y);
                let n = if lookup.contains_key(key.as_str()) {
                    *lookup.get(key.as_str()).unwrap()
                } else {
                    0
                };
                lookup.insert(key, n + 1);
                x = Day05::get_next(x, line.end.x);
                y = Day05::get_next(y, line.end.y);
            }
        }

        let mut dangers = 0;
        for (_, count) in lookup {
            if count > 1 {
                dangers += 1;
            }
        }

        dangers
    }
}

impl Day<i32> for Day05 {
    fn new() -> Day05 {
        Day05 {}
    }

    fn get_day_name(&self) -> String {
        "05".to_string()
    }

    fn run_01(&self) -> i32 {
        let lines = self
            .init_data()
            .into_iter()
            .filter(|line| {
                line.start.x == line.end.x || line.start.y == line.end.y
            })
            .collect();

        Day05::get_dangers(lines)
    }

    fn run_02(&self) -> i32 {
        let lines = self.init_data();
        Day05::get_dangers(lines)
    }
}
