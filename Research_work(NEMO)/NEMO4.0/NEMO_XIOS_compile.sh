DIR=/home/julia/NEMO4.0/nemo4

mkdir -p -v  $DIR

mkdir $DIR/nemo_i
cd $DIR/nemo_i

# Download XIOS

svn co https://forge.ipsl.jussieu.fr/ioserver/svn/XIOS/branchs/xios-2.5 xios
cd $DIR/nemo_i/xios/arch

# Configure build options XIOS for blades
cp arch-GCC_LINUX.env arch-GCC_local.env
cp arch-GCC_LINUX.fcm arch-GCC_local.fcm
cp arch-GCC_LINUX.path arch-GCC_local.path

cat <<EOF > arch-GCC_local.env
export HDF5_INC_DIR=$DIR/nemo_i_libs/include
export HDF5_LIB_DIR=$DIR/nemo_i_libs/lib

export NETCDF_INC_DIR=$DIR/nemo_i_libs/include
export NETCDF_LIB_DIR=$DIR/nemo_i_libs/lib

EOF
cat <<EOF > arch-GCC_local.fcm
################################################################################
###################                Projet XIOS               ###################
################################################################################

%CCOMPILER      mpicc
%FCOMPILER      mpiifort
%LINKER         mpiifort

%BASE_CFLAGS    -ansi -w
%PROD_CFLAGS    -O3 -DBOOST_DISABLE_ASSERTS
%DEV_CFLAGS     -g 
%DEBUG_CFLAGS   -g

%BASE_FFLAGS    -D__NONE__ 
%PROD_FFLAGS    -O3
%DEV_FFLAGS     -g -O2
%DEBUG_FFLAGS   -g

%BASE_INC       -D__NONE__
%BASE_LD        -lstdc++

%CPP            mpicc
%FPP            cpp -P
%MAKE           make

EOF

cat <<EOF > arch-GCC_local.path
NETCDF_INCDIR="-I$DIR/nemo_i_libs/include"
NETCDF_LIBDIR=" -L$DIR/nemo_i_libs/lib"
NETCDF_LIB="-lnetcdff -lnetcdf"

MPI_INCDIR=""
MPI_LIBDIR=""
MPI_LIB="-lmpi"

HDF5_INCDIR="-I$DIR/nemo_i_libs/include"
HDF5_LIBDIR="-L$DIR/nemo_i_libs/lib"
HDF5_LIB="-lhdf5_hl -lhdf5 -lhdf5 -lz -lsz -lmpi -lmpifort -lmpicxx"

EOF

cd $DIR/nemo_i/xios
sed -i 's+bld::tool::cflags    %CFLAGS %CBASE_INC -I${PWD}/extern/src_netcdf -I${PWD}/extern/boost/include -I${PWD}/extern/rapidxml/include -I${PWD}/extern/blitz/include+bld::tool::cflags    %CFLAGS %CBASE_INC -I${PWD}/extern/src_netcdf4 -I${PWD}/extern/boost/include -I${PWD}/extern/rapidxml/include -I${PWD}/extern/blitz/include+g' bld.cfg

# Build XIOS package

./make_xios --full --prod --arch GCC_local -j2