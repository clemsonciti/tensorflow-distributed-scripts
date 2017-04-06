module add gcc/4.8.1 openmpi/1.8.1
module add anaconda/4.3.0
uniq $PBS_NODEFILE > nodes.txt
mpirun python mpi_starter.py
