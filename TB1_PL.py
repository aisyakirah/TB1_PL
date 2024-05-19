def decode_matrix(matrix):
    decoded_message = ""
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            decoded_message += matrix[i][j]
    return decoded_message.replace("#", "").replace("%", "").replace("$", "").replace("@", "").replace("&", "").replace("!", "").replace(" "," ")

def main():
    dimensions = input("Masukkan dimensi matriks (format: baris kolom): ").split()
    rows = int(dimensions[0])
    cols = int(dimensions[1])

    matrix = []
    print("Masukkan matriks:")
    for _ in range(rows):
        row = input()
        matrix.append(row)

    decoded_message = decode_matrix(matrix)
    print("Pesan terdekripsi:", decoded_message)

if __name__ == "__main__":
    main()