import os
import sys

k_0 = 30
k_1 = 125
n_runs = 50
n_simultaneous = 40
n_iterations = int(sys.argv[1])
output_directory = sys.argv[2]

for t in range(n_simultaneous):
    output_log_file = str(t) + ".txt"
    os.system("bsub -M 1 -R \"rusage[mem=1]\" " +
              "-o /home/blpercha/output-logs/" + output_log_file + ".out " +
              "-e /home/blpercha/output-logs/" + output_log_file + ".err " +
              "python /home/blpercha/ebc/clusters-repeat.py " +
              "/home/blpercha/ebc/resources/matrix-ebc-paper-dense.tsv " +
              "0,2,4 " +
              "%d,%d " % (k_0, k_1) +
              "%d " % n_runs +
              "%s/repeat-%d.txt " % (output_directory, t) +
              "1e-10 " +
              "%d 0" % n_iterations)
