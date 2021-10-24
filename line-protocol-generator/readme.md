# Line Protocol Generator

This line protocol generator was made with the intention of generating sample data to play in InfluxDB Cloud.

To start to use it, you need to change the measurements, tag_key, tag, fields and values to match with the schema that you want to replicate or generate.

Once you going to paste o import the data generated in the file data.txt, you need to select seconds when you specify the precision. 

![screenshot](screenshot.png)

```
cpu_load_short,host=server01 load=3 1635047466
cpu_load_short,host=server01 load=79 1635047476
cpu_load_short,host=server01 load=33 1635047486
cpu_load_short,host=server01 load=38 1635047496
cpu_load_short,host=server01 load=49 1635047506
cpu_load_short,host=server01 load=36 1635047516
cpu_load_short,host=server01 load=59 1635047526
cpu_load_short,host=server01 load=37 1635047536
cpu_load_short,host=server01 load=4 1635047546
cpu_load_short,host=server01 load=85 1635047556
cpu_load_short,host=server01 load=62 1635047566
cpu_load_short,host=server01 load=94 1635047576
cpu_load_short,host=server01 load=1 1635047586
cpu_load_short,host=server01 load=74 1635047596
cpu_load_short,host=server01 load=88 1635047606
cpu_load_short,host=server01 load=77 1635047616
cpu_load_short,host=server01 load=27 1635047626
cpu_load_short,host=server01 load=45 1635047636
cpu_load_short,host=server01 load=61 1635047646
cpu_load_short,host=server01 load=82 1635047656
cpu_load_short,host=server01 load=87 1635047666
```

## Next cool thing

Write directly this sample data to InfluxDB Cloud directly.
