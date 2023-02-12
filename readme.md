# Jumping

python port of : [https://github.com/jinyus/jumpr](https://github.com/jinyus/jumpr)

Assign custom aliases to directories and quickly jump to them
from anywhere.

1. clone this repo
2. put the following in your `~/.bashrc` or `~/.zshrc` file:

```sh
alias jumpr='python3 /path/to/jumpr.py'
alias jset='jumpr --set'
j(){
	local dir
	dir="$(jumpr --get "$1")"
	[[ -d "$dir" ]] && cd "$dir"
}
```

## Usage

```sh
jset <alias> # defines an alias at the current working directory
j <alias> # jumps to the directory associated with an alias
jumpr -l # lists all aliases
```

## Guide

When you're in a directory and you realize you might want to
access it later, just run `jset <alias>`. For example, if I'm in
`~/Desktop/repositories/fuzzyhome`, I might make an alias `rf`:

```sh
jset rf
```

Later, when I want to change to the
`~/Desktop/repositories/jumping` directory, I can jump to it from
anywhere with

```sh
j rf
```

## FAQ

#### Why do I have to edit my `~/.bashrc` or `~/.zshrc`?

Programs cannot change the directory of the underlying shell. I'd
love to be wrong about that, but as far as I know if you want
this functionality you _have_ to use a bash/zsh function in your
`rc` file. So we just use `jumping` to set and get our aliases,
while our bash function does the actual directory changing.
