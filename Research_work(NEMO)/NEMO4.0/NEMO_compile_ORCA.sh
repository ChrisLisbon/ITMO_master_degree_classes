DIR=/home/julia/NEMO4.0/nemo4
export LD_LIBRARY_PATH=$DIR/nemo_i_libs/lib:$LD_LIBRARY_PATH

cd $DIR/nemo_i/r4.0.4
./makenemo -r ORCA2_ICE_PISCES -m icc17 -j 3