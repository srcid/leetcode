/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) {
        return []
    }

    let matrix = []
    
    for (let i = 0; i < rowsCount; i++) {
        matrix.push(Array(colsCount))
        for (let j = 0; j < colsCount; j++) {
            if (j % 2 == 0) {
                matrix[i][j] = this[(j * rowsCount) + i]
            }
            else {
                matrix[i][j] = this[((j + 1) * rowsCount) - i - 1]
            }
        }
    }
    
    return matrix
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */

let arr = [19, 10, 3, 7, 9, 8, 5, 2, 1, 17, 16, 14, 12, 18, 6, 13, 11, 20, 4, 15]
let rowsCount = 5
let colsCount = 4

console.log(arr.snail(rowsCount, colsCount))