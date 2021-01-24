def distance(strand_a, strand_b):
    hamming_distance = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("value error")

    if strand_a == strand_b and strand_a == "":
        return 0

    
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming_distance += 1           
    
    return hamming_distance
