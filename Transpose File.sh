#!/bin/sh
FILE=$1
awk '
{
    if (max_nf < NF)
        max_nf = NF
    max_nr = NR
    for ( f=1; f <= NF; f++ ) {
        lines[f, NR] = $f
    }
}
END {

    for (f = 1; f <= max_nf; f++) {
        for (r = 1; r <= max_nr; r++) {
            printf("%s", lines[f, r])
            if (r != max_nr)
                printf("-")
        }
        print ""
    }
}
' /root/test/${FILE}.txt