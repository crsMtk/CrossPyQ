def chunk(target, size):
    if len(target) == 0 or size == 0:
        return []
        
    chunk_data = []
    temp_data = target
    while size < len(temp_data):
        chunk_data.append(temp_data[:size])
        temp_data = temp_data[size:]
    chunk_data.append(temp_data)
    return chunk_data


def main():
    target = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    size = 15
    print(chunk(target, size))
    

if __name__ == '__main__':
    main()