extern crate cc;

fn main() {
    cc::Build::new()
        .flag("-c")
        .file("src/syscall.S")
        .compile("libsyscall.a");
}
