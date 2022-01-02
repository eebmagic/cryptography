use std::io;
use std::io::Read;
use std::io::BufReader;
use std::io::BufWriter;
use std::io::Write;
use std::fs::File;
use std::env;

fn main() -> io::Result<()> {
    /*
        Load args in format:
            xor [input file] [key] [output filename]
    */

    // Load args
    let args: Vec<String> = env::args().collect();

    // Set key values
    let key: u8 = args[2].parse::<u8>().unwrap();
    let filename: &String = &args[1];
    let out_name: &String = &args[3];

    // Setup file readers
    let f = File::open(filename)?;
    let mut reader = BufReader::new(f);
    let mut buffer = Vec::new();
    
    // Read file into vector.
    reader.read_to_end(&mut buffer)?;
    
    // Read
    let mut vec = Vec::new();
    for value in buffer {
        let newvalue = value ^ key;
        // println!("BYTE: {}, {} -> {}", value, value as char, newvalue as char);
        vec.push(newvalue);
    }

    println!("\nsource file: {}\noutput file: {}", filename, out_name);
    let c: &[u8] = &vec;
    let mut result_buffer = BufWriter::new(File::create(out_name)?);
    result_buffer.write(c)?;
    result_buffer.flush()?;

    Ok(())
}
