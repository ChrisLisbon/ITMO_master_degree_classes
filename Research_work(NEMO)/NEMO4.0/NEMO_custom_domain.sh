DIR=/home/julia/NEMO4.0/nemo4
export LD_LIBRARY_PATH=$DIR/nemo_i_libs/lib:$LD_LIBRARY_PATH

cd $DIR/nemo_i/r4.0.4/tools/DOMAINcfg
mpiexec -np 1 ./make_domain_cfg.exe