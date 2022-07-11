# Frog 0.1.0
## Decription
A beginning program language of me use python to compile to C++ to Unix Binary Exec.

## Recommend
Python3 or later.

## Support
Support UNIX (Linux,Darwin,...), no support windows now.

## Install
Run in terminal:

```chmod +x install.sh install.command```

In MacOS, run file install.command or run at terminal:

```./install.command```

In Linux distro, run at terminal:
```./install.sh```

## Usage
To show version:

```frog -v```

To clean up cache (optional because it'll be automatically cleanup up when you're compiling file):

```frog```

Compile file frog (file must be written with extension .frog):

```frog yourfile.frog your_output_file```

Or:

```frog -o your_output_file yourfile.frog```

If you don't give your_output_file, it will be named as the same as yourfile (of course without .frog).

## Documents
### Input/Output:
```#Input
variable=input("Your Prompt here.")
#Output
print("Hello World!")
```
### Import
```import your_other_file_without_extension_frog```

The library, I see it in /usr/local/lib/frog0.1/site-packages/, you can add library (with extension .frog) here.

### Creating and Assigning
```#char
char your_char
#String
string your_string
#int
int your_int
#float
float your_float
#array
array_type your_array[/*length*/]
#or (can't assign to any value while creating
array[/*length*]array_type your_array
```


Indeed, you can use C++ command or inluce header file of C++ in your code and it'll work.

## Thanks
Thank you so much for testing my language, although it hasn't been completed.

I'll create a version for Windows and after, I will develop it, hope it's good in offical version Frog 1.0.0.








