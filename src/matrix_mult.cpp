// matrix_mult.cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <iomanip>
#include <cstdlib>

// A simple CPU-bound matrix multiplication (C = A * B)
void matrix_multiply(int size) {
    // 1. Allocate memory
    std::vector<double> A(size * size);
    std::vector<double> B(size * size);
    std::vector<double> C(size * size);

    // 2. Initialize with random numbers
    std::mt19937 gen(42);
    std::uniform_real_distribution<> dis(0.0, 1.0);
    for (int i = 0; i < size * size; i++) {
        A[i] = dis(gen);
        B[i] = dis(gen);
    }

    std::cout << "[INFO] Starting " << size << "x" << size << " matrix multiplication..." << std::endl;

    // 3. The Computation Loop (The "Work")
    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            double sum = 0.0;
            for (int k = 0; k < size; k++) {
                sum += A[i * size + k] * B[k * size + j];
            }
            C[i * size + j] = sum;
        }
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    // 4. Calculate Performance
    double ops = 2.0 * size * size * size; // 2 ops (multiply + add) per element
    double gflops = (ops / duration.count()) / 1e9;

    std::cout << "[INFO] Time: " << duration.count() << " seconds" << std::endl;
    // This is the "Magic String" our Regex looks for:
    std::cout << "Performance = " << std::fixed << std::setprecision(2) << gflops << " GFlops" << std::endl;
    std::cout << "SUCCESS: Benchmark Finished" << std::endl;
}

int main(int argc, char* argv[]) {
    int size = 512; // Default small size for testing
    if (argc > 1) {
        size = std::atoi(argv[1]);
    }
    matrix_multiply(size);
    return 0;
}