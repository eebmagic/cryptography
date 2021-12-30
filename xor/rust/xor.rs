use std::fs;

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

fn xor_str(s: &String, key: u8) -> String {
    let mut result = String::from("");
    for c in s.chars() {
        let new = ((c as u8)^key) as char;
        result.push(new);
        // println!("{}, {} -> {}", i, c, new);
    }

    // println!("result: {}", result);
    return result;
}

fn main() {
    // Set key value
    let key: u8 = 123;

    // Load file content
    let filename = "source.txt";
    println!("filename: {}", filename);
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    println!("Found text:\n{}", contents);
    print_type_of(&contents);


    // Iterate over content
    let result = xor_str(&contents, key);
    let decrypt = xor_str(&result, key);
    println!("\n---------\nENCRYPTING\n---------\n");
    println!("out of encrypt:\n{}", result);

    println!("\n---------\nDECRYPTING\n---------\n");
    println!("out of decrypt:\n{}", decrypt);

    // Write to file
    fs::write("output.txt", result).expect("Unable to write file");
}
