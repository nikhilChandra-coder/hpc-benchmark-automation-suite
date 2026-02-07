import json
import sqlite3
import sys
import os
from datetime import datetime

DB_NAME = "hpc_metrics.db"

def ingest_report(json_file):
    print(f"--- FINAL PRODUCTION RUN: {json_file} ---")
    
    with open(json_file, 'r') as f:
        data = json.load(f)

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    # Create a fresh 5-column table
    c.execute('''CREATE TABLE IF NOT EXISTS benchmark_runs 
                 (timestamp DATETIME, test_name TEXT, metric_name TEXT, metric_value REAL, unit TEXT)''')
    
    count = 0
    runs = data.get('runs', [])
    
    for run in runs:
        testcases = run.get('testcases', [])
        for test in testcases:
            test_name = test.get('name')
            perf_data = test.get('perfvalues', {})
            
            # Iterate through the dictionary
            for key, val in perf_data.items():
                # The key looks like "generic:default:GFlops", so we split it to get "GFlops"
                m_name = key.split(':')[-1]
                
                # The val is a list: [0.37, 0, None, None, 'GFlops', 'pass']
                # We want index 0 (Value) and index 4 (Unit)
                if isinstance(val, list) and len(val) > 0:
                    m_value = val[0]
                    m_unit = val[4] if len(val) > 4 else "generic"
                    
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"[SUCCESS] Ingesting: {test_name} -> {m_name} = {m_value} {m_unit}")
                    
                    c.execute("INSERT INTO benchmark_runs VALUES (?, ?, ?, ?, ?)", 
                              (timestamp, test_name, m_name, m_value, m_unit))
                    count += 1

    conn.commit()
    conn.close()
    print(f"--- DONE. Total metrics ingested: {count} ---")

if __name__ == "__main__":
    ingest_report(sys.argv[1])
