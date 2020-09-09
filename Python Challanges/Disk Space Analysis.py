def segment(segment, space):
    # Write your code here

    if len(space) <= 1:
        return space[0]
    else:
        marker = 0

        max = min(space[marker: segment])
        while segment <= len(space):
            min_val_in_seg = min(space[marker: segment])
            if max < min_val_in_seg:
                max = min_val_in_seg
            marker += 1
            segment += 1

    return max

if __name__ == '__main__':
    x = 1

    space_count = 5

    space = [1, 2, 3, 1, 2]

    result = segment(x, space)

    print(result)

