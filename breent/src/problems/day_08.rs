use std::collections::{HashMap, HashSet};
use std::iter::FromIterator;

use crate::day::Day;

pub struct Day08 {}

impl Day08 {
    fn build_digits(&self, line: &String) -> HashMap<String, i32> {
        let input = line.split(" | ").collect::<Vec<&str>>()[0]
            .split(" ")
            .map(|s| alphabetize(s))
            .collect::<Vec<String>>();

        let mut digits: [&str; 10] = [""; 10];

        // unique bois first
        for word in input.iter() {
            if word.len() == 2 {
                digits[1] = word;
            }
            if word.len() == 4 {
                digits[4] = word;
            }
            if word.len() == 3 {
                digits[7] = word;
            }
            if word.len() == 7 {
                digits[8] = word;
            }
        }

        let one = HashSet::<char>::from_iter(digits[1].chars());
        let four = HashSet::<char>::from_iter(digits[4].chars());

        // 0, 6, 9 = have length 6
        for word in input.iter() {
            if word.len() == 6 {
                let maybe_zero = HashSet::<char>::from_iter(word.chars());
                if one.intersection(&maybe_zero).count() == 2
                    && four.intersection(&maybe_zero).count() == 3
                {
                    digits[0] = word;
                }

                let maybe_six = HashSet::<char>::from_iter(word.chars());
                if one.intersection(&maybe_six).count() == 1 {
                    digits[6] = word;
                }

                let maybe_nine = HashSet::<char>::from_iter(word.chars());
                if four.intersection(&maybe_nine).count() == 4 {
                    digits[9] = word;
                }
            }
        }

        let six = HashSet::<char>::from_iter(digits[6].chars());

        // 2, 3, 5 have length 5
        for word in input.iter() {
            if word.len() == 5 {
                let maybe_two = HashSet::<char>::from_iter(word.chars());
                if six.intersection(&maybe_two).count() == 4
                    && one.intersection(&maybe_two).count() == 1
                {
                    digits[2] = word;
                }

                let maybe_three = HashSet::<char>::from_iter(word.chars());
                if one.intersection(&maybe_three).count() == 2 {
                    digits[3] = word;
                }

                let maybe_five = HashSet::<char>::from_iter(word.chars());
                if six.intersection(&maybe_five).count() == 5 {
                    digits[5] = word;
                }
            }
        }

        // hash it up
        let mut digit_values = HashMap::new();
        for (i, digit) in digits.iter().enumerate() {
            digit_values.insert(digit.to_string(), i as i32);
        }

        digit_values
    }
}

impl Day<i32> for Day08 {
    fn new() -> Day08 {
        Day08 {}
    }

    fn get_day_name(&self) -> String {
        "08".to_string()
    }

    fn run_01(&self) -> i32 {
        let data = self.load_data();

        let mut count = 0;

        for line in data {
            let digit_values = self.build_digits(&line);

            let output = line.split(" | ").collect::<Vec<&str>>()[1]
                .split(" ")
                .map(|s| alphabetize(s))
                .collect::<Vec<String>>();

            for digit in output.iter() {
                let n = *digit_values.get(digit.as_str()).unwrap();
                if n == 1 || n == 4 || n == 7 || n == 8 {
                    count += 1;
                }
            }
        }
        count
    }

    fn run_02(&self) -> i32 {
        let data = self.load_data();
        let mut sum = 0;
        for line in data {
            let digit_values = self.build_digits(&line);

            let output = line.split(" | ").collect::<Vec<&str>>()[1]
                .split(" ")
                .map(|s| alphabetize(s))
                .collect::<Vec<String>>();

            let mut num = 0i32;
            let mut tens = 1000i32;
            for digit in output.iter() {
                num += *digit_values.get(digit.as_str()).unwrap() * tens;
                tens /= 10;
            }

            sum += num;
        }
        sum
    }
}

fn alphabetize(s: &str) -> String {
    let mut chars: Vec<char> = s.chars().collect();
    chars.sort_by(|a, b| b.cmp(a));
    String::from_iter(chars)
}
