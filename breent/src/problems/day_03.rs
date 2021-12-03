use crate::day::Day;

pub struct Day03 {}

impl Day<i32> for Day03 {
    fn new() -> Day03 {
        Day03 {}
    }

    fn get_day_name(&self) -> String {
        "03".to_string()
    }

    fn run_01(&self) -> i32 {
        let data = &self.load_data();

        let mut common = String::new();
        let mut uncommon = String::new();

        // we assume every row has the same length
        for i in 0..data[0].len() {
            let mut zeros = 0;
            let mut ones = 0;
            for row in data {
                // we assume the only characters are 0 and 1
                if row.chars().nth(i).unwrap() == '0' {
                    zeros += 1;
                } else {
                    ones += 1;
                }
            }
            // we assume there will be no ties, because we have no information
            // about how to break them
            common.push(if zeros > ones { '0' } else { '1' });
            uncommon.push(if zeros > ones { '1' } else { '0' });
        }

        let gamma = i32::from_str_radix(common.as_str(), 2).unwrap();
        let epsilon = i32::from_str_radix(uncommon.as_str(), 2).unwrap();

        gamma * epsilon
    }

    fn run_02(&self) -> i32 {
        let data = &self.load_data();

        let mut oxygen_candidates: Vec<String> =
            data.iter().filter(|_| true).cloned().collect();
        let mut carbon_candidates: Vec<String> =
            data.iter().filter(|_| true).cloned().collect();

        // we assume every row has the same length
        for i in 0..data[0].len() {
            let mut oc = 0;
            let mut cc = 0;

            // we assume the only characters are 0 and 1
            for row in oxygen_candidates.iter() {
                if row.chars().nth(i).unwrap() == '0' {
                    oc -= 1;
                } else {
                    oc += 1;
                }
            }

            for row in carbon_candidates.iter() {
                if row.chars().nth(i).unwrap() == '0' {
                    cc -= 1;
                } else {
                    cc += 1;
                }
            }

            let oxygen_char = if oc < 0 { '0' } else { '1' };
            let carbon_char = if cc >= 0 { '0' } else { '1' };

            if oxygen_candidates.len() > 1 {
                oxygen_candidates = oxygen_candidates
                    .iter()
                    .filter(|c| c.chars().nth(i).unwrap() == oxygen_char)
                    .cloned()
                    .collect();
            }

            if carbon_candidates.len() > 1 {
                carbon_candidates = carbon_candidates
                    .iter()
                    .filter(|c| c.chars().nth(i).unwrap() == carbon_char)
                    .cloned()
                    .collect();
            }
        }

        if oxygen_candidates.len() != 1 {
            panic!("we expect to have a single valid oxygen candidate by this point")
        }
        if carbon_candidates.len() != 1 {
            panic!("we expect to have a single valid carbon candidate by this point");
        }

        let oxygen =
            i32::from_str_radix(oxygen_candidates[0].as_str(), 2).unwrap();
        let carbon =
            i32::from_str_radix(carbon_candidates[0].as_str(), 2).unwrap();

        oxygen * carbon
    }
}
