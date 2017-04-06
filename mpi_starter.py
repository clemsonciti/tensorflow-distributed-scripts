from mpi4py import MPI
import subprocess
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
p = subprocess.Popen(['/software/singularity/2.2.1-ext4/bin/singularity', 'exec', '-B', '/software:/software', '-B', '/scratch2:/scratch2', '-B', '/local_scratch:/local_scratch', '/software/singularity-containers/ubuntu_dl_gpu.img', '/usr/bin/python', 'start_worker.py', 'nodes.txt', str(rank)], stdout=subprocess.PIPE)
