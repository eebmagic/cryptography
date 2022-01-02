use std::io;
use std::io::Read;
use std::io::BufReader;
use std::io::BufWriter;
use std::io::Write;
use std::fs::File;

fn main() -> io::Result<()> {
    // Set key values
    let key: u8 = 123;
    let filename = "source.txt";

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
        println!("BYTE: {}, {} -> {}", value, value as char, newvalue as char);
        vec.push(newvalue);
    }

    let c: &[u8] = &vec;
    let mut result_buffer = BufWriter::new(File::create("output.txt")?);
    result_buffer.write(c)?;
    result_buffer.flush()?;

    Ok(())
}
