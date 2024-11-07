def countPairs(nomor: list[int],tujuan:int):
    hasil = 0
    a = set()
    b = set()
    for no in nomor:
        sisa = tujuan - no

        if sisa in a:
            pasangan = (min(no,sisa),max(no,sisa))

            if pasangan not in b:
                hasil += 1
                b.add(pasangan)
        
        a.add(no)
                

    # print(b)
    print(hasil)

countPairs([1, 3, 2, 2, 3, 4], 5)
countPairs([1, 1, 1, 1], 2)
countPairs([1, 2, 3, 4, 5], 7)
