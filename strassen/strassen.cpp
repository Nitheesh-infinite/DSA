#include "common.h"

Matrix add(const Matrix &A, const Matrix &B) {
    int n = A.size();
    Matrix C(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            C[i][j] = A[i][j] + B[i][j];
    return C;
}

Matrix subtract(const Matrix &A, const Matrix &B) {
    int n = A.size();
    Matrix C(n, vector<int>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            C[i][j] = A[i][j] - B[i][j];
    return C;
}

Matrix naiveMultiply(const Matrix &A, const Matrix &B) {
    int n = A.size();
    Matrix C(n, vector<int>(n, 0));
    for (int i = 0; i < n; ++i)
        for (int k = 0; k < n; ++k)
            for (int j = 0; j < n; ++j)
                C[i][j] += A[i][k] * B[k][j];
    return C;
}

Matrix strassenMultiply(const Matrix &A, const Matrix &B, int threshold) {
    int n = A.size();

    if (n <= threshold)
        return naiveMultiply(A, B);

    int mid = n / 2;
    Matrix A11(mid, vector<int>(mid)), A12(mid, vector<int>(mid));
    Matrix A21(mid, vector<int>(mid)), A22(mid, vector<int>(mid));
    Matrix B11(mid, vector<int>(mid)), B12(mid, vector<int>(mid));
    Matrix B21(mid, vector<int>(mid)), B22(mid, vector<int>(mid));

    for (int i = 0; i < mid; ++i)
        for (int j = 0; j < mid; ++j) {
            A11[i][j] = A[i][j];
            A12[i][j] = A[i][j + mid];
            A21[i][j] = A[i + mid][j];
            A22[i][j] = A[i + mid][j + mid];

            B11[i][j] = B[i][j];
            B12[i][j] = B[i][j + mid];
            B21[i][j] = B[i + mid][j];
            B22[i][j] = B[i + mid][j + mid];
        }

    Matrix M1 = strassenMultiply(add(A11, A22), add(B11, B22), threshold);
    Matrix M2 = strassenMultiply(add(A21, A22), B11, threshold);
    Matrix M3 = strassenMultiply(A11, subtract(B12, B22), threshold);
    Matrix M4 = strassenMultiply(A22, subtract(B21, B11), threshold);
    Matrix M5 = strassenMultiply(add(A11, A12), B22, threshold);
    Matrix M6 = strassenMultiply(subtract(A21, A11), add(B11, B12), threshold);
    Matrix M7 = strassenMultiply(subtract(A12, A22), add(B21, B22), threshold);

    Matrix C(n, vector<int>(n));
    for (int i = 0; i < mid; ++i)
        for (int j = 0; j < mid; ++j) {
            C[i][j] = M1[i][j] + M4[i][j] - M5[i][j] + M7[i][j];
            C[i][j + mid] = M3[i][j] + M5[i][j];
            C[i + mid][j] = M2[i][j] + M4[i][j];
            C[i + mid][j + mid] = M1[i][j] - M2[i][j] + M3[i][j] + M6[i][j];
        }

    return C;
}


bool equal(const Matrix &A, const Matrix &B) {
    int n = A.size();
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (A[i][j] != B[i][j])
                return false;
    return true;
}

