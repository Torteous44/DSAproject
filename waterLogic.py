def waterPath(matrix, startingRow, startingCol):
    Rows = len(matrix)
    Cols = len(matrix[0])

    pathArray = []
    visited = set()

    def movement(row, cols):
        visited.add((row, cols))

        # Top
        if row - 1 >= 0:
            if cols - 1 >= 0 and (row - 1, cols - 1) not in visited:
                if matrix[row - 1][cols - 1] <= matrix[row][cols]:
                    pathArray.append(f"{row - 1},{cols - 1}")
                    movement(row - 1, cols - 1)
            if (row - 1, cols) not in visited and matrix[row - 1][cols] <= matrix[row][cols]:
                pathArray.append(f"{row - 1},{cols}")
                movement(row - 1, cols)
            if cols + 1 < Cols and (row - 1, cols + 1) not in visited:
                if matrix[row - 1][cols + 1] <= matrix[row][cols]:
                    pathArray.append(f"{row - 1},{cols + 1}")
                    movement(row - 1, cols + 1)

        # Bottom
        if row + 1 < Rows:
            if cols - 1 >= 0 and (row + 1, cols - 1) not in visited:
                if matrix[row + 1][cols - 1] <= matrix[row][cols]:
                    pathArray.append(f"{row + 1},{cols - 1}")
                    movement(row + 1, cols - 1)
            if (row + 1, cols) not in visited and matrix[row + 1][cols] <= matrix[row][cols]:
                pathArray.append(f"{row + 1},{cols}")
                movement(row + 1, cols)
            if cols + 1 < Cols and (row + 1, cols + 1) not in visited:
                if matrix[row + 1][cols + 1] <= matrix[row][cols]:
                    pathArray.append(f"{row + 1},{cols + 1}")
                    movement(row + 1, cols + 1)

        # Sides (left and right)
        if cols - 1 >= 0 and (row, cols - 1) not in visited:
            if matrix[row][cols - 1] <= matrix[row][cols]:
                pathArray.append(f"{row},{cols - 1}")
                movement(row, cols - 1)
        if cols + 1 < Cols and (row, cols + 1) not in visited:
            if matrix[row][cols + 1] <= matrix[row][cols]:
                pathArray.append(f"{row},{cols + 1}")
                movement(row, cols + 1)

        return

    movement(startingRow, startingCol)
    return pathArray







