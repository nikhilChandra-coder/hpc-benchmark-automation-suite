# matrix_bench.py
import time
import random
import sys

def mock_computation(size):
    print(f"[INFO] Initializing matrix size {size}x{size}...")
    # Simulate work
    time.sleep(random.uniform(0.5, 2.0))
    
    # Generate a fake performance number based on "random" variance
    base_flops = 450.0
    variance = random.uniform(-15.0, 15.0)
    gflops = base_flops + variance
    
    print("[INFO] Computation complete.")
    print(f"RESULT: Performance = {gflops:.2f} GFlops")
    print("SUCCESS: Benchmark Finished")

if __name__ == "__main__":
    try:
        size = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
        mock_computation(size)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)