

def mergeSort(lt):
    l = len(lt)
    if l == 1:
        return lt

    def _sort(begin, end):
        l = end - begin
        if l == 1:
            return
        _sort(0, m)
        _sort(m, end)

        j = m
        i = begin
        # print lt[begin:end], '--->',
        while i < m:
            while j < end:
                # print lt[i], lt[j],'#',
                if lt[i] > lt[j]:
                    lt[i], lt[j] = lt[j], lt[i]
                j += 1
            i += 1
        # print lt[begin:end]

    _sort(0, l)

    return lt

print '\\n'

# print mergeSort([3,9,4,8,5,6,7])

#eof
