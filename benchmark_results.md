# SIMDString Benchmark Results

- Number of iterations : 1000000

| Functions                             |     Default String |        SIMDString |
| :------------------------------------ | -----------------: | ----------------: |
| Append Operation - Char (+=)          |  0.086109599971678 | 1.844931100029498 |
| Append Operation - Str Length 10 (+=) |  3.887853199965321 | 1.908019600028638 |
| Append Operation - Str Length 25 (+=) | 23.338599999959115 | 1.964293700002600 |
| Append Function - Char                |  0.091276100021787 | 2.337395099981222 |
| Append Function - Str Length 10       |  3.953721199999563 | 2.439930799999274 |
| Append Function - Str Length 25       | 24.786470199993346 | 2.437047699990217 |
 


| Functions                           |    Default String |        SIMDString |
| :---------------------------------- | ----------------: | ----------------: |
| Assign Function - Char              | 0.016810300003272 | 2.565124999964610 |
| Assign Operation - Char             | 0.017197099979967 | 0.017251099983696 |
| Assign Function - String Length 10  | 0.067326299962588 | 2.579731800011359 |
| Assign Operation - String Length 10 | 0.056008699990343 | 0.055630100017879 |
| Assign Function - String Length 25  | 0.055120100034401 | 2.558700499997940 |
| Assign Operation - String Length 25 | 0.053441700001713 | 0.055950000009034 |
 


| Functions                      |     Default String |         SIMDString |
| :----------------------------- | -----------------: | -----------------: |
| Insert At The Beginning - Char | 15.349451299989596 | 14.877794500032905 |
| Insert At The End - Char       |  0.086191500013229 |  2.798107200011145 |
| Insert In The Middle - Char    | 48.530026799999177 |  8.850002799998038 |
 


