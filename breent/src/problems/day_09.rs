use std::collections::{HashMap, HashSet};

use crate::day::Day;

pub struct Day09 {}

impl Day09 {
    fn init_data(&self) -> Vec<Vec<u32>> {
        let raw_data = self.load_data();
        let mut data = Vec::new();
        for line in raw_data {
            let row = line.chars().map(|n| n.to_digit(10).unwrap()).collect();
            data.push(row);
        }
        data
    }
}

impl Day<u32> for Day09 {
    fn new() -> Day09 {
        Day09 {}
    }

    fn get_day_name(&self) -> String {
        "09".to_string()
    }

    fn run_01(&self) -> u32 {
        let data = self.init_data();
        let height = data.len();
        let width = data[0].len();
        let mut low_points = Vec::new();
        for i in 0..height {
            for j in 0..width {
                let mut is_low_point = true;
                // above
                if i > 0 && data[i][j] >= data[i - 1][j] {
                    is_low_point = false;
                }
                // right
                if j < width - 1 && data[i][j] >= data[i][j + 1] {
                    is_low_point = false;
                }
                // below
                if i < height - 1 && data[i][j] >= data[i + 1][j] {
                    is_low_point = false;
                }
                // left
                if j > 0 && data[i][j] >= data[i][j - 1] {
                    is_low_point = false;
                }
                if is_low_point {
                    low_points.push(data[i][j]);
                }
            }
        }

        let mut risk = 0u32;
        for lp in low_points.iter() {
            risk += *lp as u32 + 1u32;
        }
        // println!("low_points.len() {}", low_points.len());
        risk
    }

    fn run_02(&self) -> u32 {
        let data = self.init_data();
        let height = data.len();
        let width = data[0].len();

        let mut low_points = Vec::new();
        for i in 0..height {
            for j in 0..width {
                let mut is_low_point = true;
                // above
                if i > 0 && data[i][j] >= data[i - 1][j] {
                    is_low_point = false;
                }
                // right
                if j < width - 1 && data[i][j] >= data[i][j + 1] {
                    is_low_point = false;
                }
                // below
                if i < height - 1 && data[i][j] >= data[i + 1][j] {
                    is_low_point = false;
                }
                // left
                if j > 0 && data[i][j] >= data[i][j - 1] {
                    is_low_point = false;
                }
                if is_low_point {
                    low_points.push((i, j));
                }
            }
        }

        let mut counts = Vec::new();
        for lp in low_points {
            let thing = do_thing(&data, lp.0, lp.1, HashSet::new());
            counts.push(thing.len());
            println!("{:?}", thing);
        }

        counts.sort();
        counts.reverse();
        println!("{:?}", counts);

        (counts[0] * counts[1] * counts[2]) as u32
    }
}

fn do_thing(
    map: &Vec<Vec<u32>>,
    i: usize,
    j: usize,
    mut visited: HashSet<String>,
) -> HashSet<String> {
    if map[i][j] == 9 {
        return visited;
    }
    visited.insert(format!("{}-{}", i, j));

    // up
    if i > 0 {
        let up_key = format!("{}-{}", i - 1, j);
        if i > 0 && map[i - 1][j] != 9 && !visited.contains(&up_key) {
            visited = do_thing(map, i - 1, j, visited);
        }
    }

    // right
    let right_key = format!("{}-{}", i, j + 1);
    if (j + 1) < map[0].len()
        && map[i][j + 1] != 9
        && !visited.contains(&right_key)
    {
        visited = do_thing(map, i, j + 1, visited);
    }

    // down
    let down_key = format!("{}-{}", i + 1, j);
    if (i + 1) < map.len() && map[i + 1][j] != 9 && !visited.contains(&down_key)
    {
        visited = do_thing(map, i + 1, j, visited);
    }

    // left
    if j > 0 {
        let left_key = format!("{}-{}", i, j - 1);
        if j > 0 && map[i][j - 1] != 9 && !visited.contains(&left_key) {
            visited = do_thing(map, i, j - 1, visited);
        }
    }

    visited
}
