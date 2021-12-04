use std::collections::HashMap;
use std::convert::TryInto;

use crate::day::Day;

#[derive(Debug)]
struct Board {
    numbers: [[u16; 5]; 5],
}

impl Board {
    fn from_strings(rows: &[String]) -> Board {
        let mut numbers: [[u16; 5]; 5] = [[0; 5]; 5];

        for i in 0..5 {
            let row: Vec<u16> = rows[i]
                .split(' ')
                .map(|n| n.trim())
                .filter(|s| !s.is_empty())
                .map(|n| n.parse().unwrap())
                .collect();
            numbers[i] = row[0..5].try_into().expect("should work");
        }

        Board { numbers }
    }

    fn is_winner(&self, called_numbers: &HashMap<u16, bool>) -> bool {
        for i in 0..5 {
            let mut col_sum = 0;
            let mut row_sum = 0;
            for j in 0..5 {
                if called_numbers.contains_key(&self.numbers[i][j]) {
                    row_sum += 1;
                }
                if called_numbers.contains_key(&self.numbers[j][i]) {
                    col_sum += 1;
                }
            }
            if row_sum == 5 || col_sum == 5 {
                return true;
            }
        }
        return false;
    }

    fn get_unmarked_sum(&self, called_numbers: &HashMap<u16, bool>) -> u32 {
        let mut sum: u32 = 0;
        for row in &self.numbers {
            for n in row {
                if !called_numbers.contains_key(n) {
                    sum += *n as u32;
                }
            }
        }
        return sum;
    }
}

#[derive(Debug)]
struct Game {
    uncalled_numbers: Vec<u16>,
    called_numbers: HashMap<u16, bool>,
    boards: Vec<Board>,
}

impl Game {
    fn new(numbers: Vec<u16>, boards: Vec<Board>) -> Game {
        Game {
            uncalled_numbers: numbers,
            called_numbers: HashMap::new(),
            boards,
        }
    }
}

pub struct Day04 {}

impl Day04 {
    fn init_data(&self) -> Game {
        let data = &self.load_data();

        let numbers: Vec<u16> = data[0]
            .split(",")
            .map(|n| n.trim().parse().unwrap())
            .collect();

        let mut game = Game::new(numbers, Vec::new());
        for i in (2..data.len() - 1).step_by(6) {
            let board = Board::from_strings(&data[i..i + 5]);
            game.boards.push(board);
        }

        game
    }
}

impl Day<u32> for Day04 {
    fn new() -> Day04 {
        Day04 {}
    }

    fn get_day_name(&self) -> String {
        "04".to_string()
    }

    fn run_01(&self) -> u32 {
        let mut game = self.init_data();
        let mut score: u32 = 0;
        for x in game.uncalled_numbers {
            game.called_numbers.insert(x, true);
            for b in &game.boards {
                if b.is_winner(&game.called_numbers) {
                    score +=
                        x as u32 * b.get_unmarked_sum(&game.called_numbers);
                    break;
                }
            }
            if score > 0 {
                break;
            }
        }
        score
    }

    fn run_02(&self) -> u32 {
        let mut game = self.init_data();
        let mut score: u32 = 0;
        let mut last_removed = None;

        for x in game.uncalled_numbers {
            game.called_numbers.insert(x, true);

            let mut num_removed = 0;
            for board_num in 0..game.boards.len() {
                let i = board_num - num_removed;
                if game.boards[i].is_winner(&game.called_numbers) {
                    last_removed = Some(game.boards.remove(i));
                    num_removed += 1;
                }
            }

            if game.boards.len() == 0 {
                if let Some(b) = last_removed {
                    score = x as u32 * b.get_unmarked_sum(&game.called_numbers);
                }
                break;
            }
        }
        score
    }
}
