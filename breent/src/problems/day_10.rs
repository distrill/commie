use crate::day::Day;

pub struct Day10 {}

impl Day10 {
    fn init_data(&self) -> Vec<Line> {
        let raw_data = self.load_data();
        let mut lines = Vec::new();
        for row in raw_data {
            lines.push(Line::from_string(&row));
        }
        lines
    }
}

impl Day<u64> for Day10 {
    fn new() -> Day10 {
        Day10 {}
    }

    fn get_day_name(&self) -> String {
        "10".to_string()
    }

    fn run_01(&self) -> u64 {
        let lines = self.init_data();
        let mut corruption_score = 0;
        for line in lines {
            if let Some(c) = line.get_corrupt() {
                let score = get_corruption_score(&c);
                corruption_score += score;
            }
        }
        corruption_score
    }

    fn run_02(&self) -> u64 {
        let lines = self.init_data();
        let mut completion_scores = Vec::new();
        for line in lines {
            if let None = line.get_corrupt() {
                if let Some(score) = line.get_completion_score() {
                    completion_scores.push(score);
                }
            }
        }
        completion_scores.sort();
        completion_scores[completion_scores.len() / 2]
    }
}

#[derive(Debug)]
struct Line(Vec<char>);

impl Line {
    fn from_string(s: &str) -> Line {
        Line(s.chars().collect())
    }

    fn get_corrupt(&self) -> Option<char> {
        let mut opened = Vec::new();
        for c in &self.0 {
            if is_open(&c) {
                opened.push(c);
            } else {
                if let Some(o) = opened.pop() {
                    if !is_matching_close(&o, &c) {
                        return Some(*c);
                    }
                }
            }
        }
        None
    }

    fn get_completion_score(&self) -> Option<u64> {
        let mut opened = Vec::new();
        for c in &self.0 {
            if is_open(&c) {
                opened.push(c);
            } else {
                if let Some(o) = opened.pop() {
                    if !is_matching_close(&o, &c) {
                        return None;
                    }
                }
            }
        }
        Some(get_closing_score(opened))
    }
}

fn get_corruption_score(c: &char) -> u64 {
    match c {
        ')' => 3,
        ']' => 57,
        '}' => 1197,
        '>' => 25137,
        _ => 0,
    }
}

fn get_completion_score(c: &char) -> u64 {
    match c {
        '(' => 1,
        '[' => 2,
        '{' => 3,
        '<' => 4,
        _ => 0,
    }
}

fn get_closing_score(mut opened: Vec<&char>) -> u64 {
    let mut score = 0;
    while let Some(o) = opened.pop() {
        score *= 5;
        score += get_completion_score(&o);
    }
    score
}

fn is_open(c: &char) -> bool {
    match c {
        '<' | '(' | '[' | '{' => true,
        _ => false,
    }
}

fn is_matching_close(open: &char, close: &char) -> bool {
    is_open(open)
        && match *open {
            '<' => *close == '>',
            '(' => *close == ')',
            '[' => *close == ']',
            '{' => *close == '}',
            _ => false,
        }
}
