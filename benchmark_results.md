# SIMDString Benchmark Results

- Number of iterations : 1000000

| Functions                             |     Default String |        SIMDString |
| :------------------------------------ | -----------------: | ----------------: |
| Append Operation - Char (+=)          |  0.088059099973179 | 1.848876700038090 |
| Append Operation - Str Length 10 (+=) |  3.824022199958563 | 1.865448499971535 |
| Append Operation - Str Length 25 (+=) | 23.915154799993616 | 1.978215800016187 |
| Append Function - Char                |  0.093803199997637 | 2.297245600027964 |
| Append Function - Str Length 10       |  3.980126300011761 | 2.352189900004305 |
| Append Function - Str Length 25       | 23.158148700022139 | 2.465692400000989 |
| Assign Function - Char                |  0.017153799999505 | 2.501999399974011 |
| Assign Operation - Char               |  0.017328299989458 | 0.017469200014602 |
| Assign Function - String Length 10    |  0.058008199965116 | 2.536571599950548 |
| Assign Operation - String Length 10   |  0.061088799964637 | 0.063508799998090 |
| Assign Function - String Length 25    |  0.056277900002897 | 2.541052599961404 |
| Assign Operation - String Length 25   |  0.053381099947728 | 0.054724699992221 |
