import reframe as rfm
import reframe.utility.sanity as sn
# 1. EXPLICIT IMPORT: We import the build system class directly
from reframe.core.buildsystems import SingleSource

@rfm.simple_test
class MatrixBenchmark(rfm.RegressionTest):
    def __init__(self):
        super().__init__()
        
        # 2. System Setup
        self.valid_systems = ['*']
        self.valid_prog_environs = ['*']
        
        # 3. Build System (The "Hardcoded" Fix)
        # We create a real SingleSource object instead of using a string.
        # This allows us to manually set the compiler to 'g++' immediately.
        self.build_system = SingleSource()
        self.build_system.cxx = 'g++'  # Explicitly force g++
        
        # 4. Source and Executable
        self.sourcepath = 'matrix_mult.cpp'
        self.executable_opts = ['512']
        
        # 5. Sanity Patterns
        self.sanity_patterns = sn.assert_found(
            r'SUCCESS: Benchmark Finished', self.stdout
        )

        # 6. Performance Patterns
        self.perf_patterns = {
            'GFlops': sn.extractsingle(
                r'Performance = (\S+) GFlops', self.stdout, 1, float
            )
        }

        # 7. Reference
        self.reference = {
            '*': {'GFlops': (0, None, None, 'GFlops')}
        }
        