# Central line infection data

Data cleanup and file rendering for a story on vox.com. Messy but reproducible.

It uses shell scripts, [csvkit](//csvkit.readthedocs.org), and a couple Python 
scripts because the shell stuff got too out of hand. It's not at all optimized 
for performance. It's only been tested on an early 2015 MacBook Pro. But it's 
heavily commented. Although I did a lot of the early work in MySQL, I used csvkit 
for these scripts because I think it's more accessible than MySQL.

Inspired by [NPR's visual team](//github.com/nprapps/leso).


## How to run

```bash
$ ./process.sh
```

The process script creates a timestamped directory, clones scripts into it, and 
runs the scripts. (Cloning allowed me to test edits before making adjustments to 
the master scripts.) 

There are some other commands in the individual scripts themselves that you can 
comment or un-comment based on what you want. You can read the scripts to find 
out what they do.


## Contact

Email me at [soo@vox.com](mailto:soo@vox.com).