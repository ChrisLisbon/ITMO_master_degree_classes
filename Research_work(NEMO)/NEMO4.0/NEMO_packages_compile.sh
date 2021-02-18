DIR=/home/julia/NEMO4.0/nemo4

mkdir -p -v  $DIR

# Create directory for sources of packages
mkdir -p -v  $DIR/build

# Create directory for built packages
mkdir -p -v  $DIR/nemo_req_intel

# Go to sources directory
cd $DIR/build

# Download required packages
wget -c -v http://zlib.net/zlib-1.2.11.tar.gz
wget -c -v https://support.hdfgroup.org/ftp/lib-external/szip/2.1.1/src/szip-2.1.1.tar.gz
wget -c -v https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.20/src/hdf5-1.8.20.tar.gz
wget -c -v ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.0.tar.gz
wget -c -v ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-fortran-4.4.4.tar.gz
wget -c -v ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-cxx-4.2.tar.gz
wget --no-check-certificate -c -v https://curl.haxx.se/download/curl-7.56.1.tar.gz

# Export environment variables for packages building
export CC=mpicc
export CXX=mpicxx
export FC=mpiifort
export F77=mpiifort
export CFLAGS='-O2 -DBOOST_DISABLE_ASSERTS'
export CXXFLAGS='-O2 -DBOOST_DISABLE_ASSERTS'
export FCFLAGS='-O2'
export FFLAGS='-O2'

# Build szip package
tar xf szip-2.1.1.tar.gz
cd szip-2.1.1
./configure --prefix=$DIR/nemo_req_intel/szip-2.1 --enable-encoding --enable-production --enable-shared --enable-static
make -j16
make check
make install
export LD_LIBRARY_PATH=$DIR/nemo_req_intel/szip-2.1/lib:$LD_LIBRARY_PATH
cd $DIR/build

# Build zlib package
tar xf zlib-1.2.11.tar.gz
cd zlib-1.2.11
./configure --prefix=$DIR/nemo_req_intel/zlib-1.2.8 --enable-shared
make -j16
make check
make install
export zlib=$DIR/nemo_req_intel/zlib-1.2.8
export LD_LIBRARY_PATH=$DIR/nemo_req_intel/zlib-1.2.8/lib:$LD_LIBRARY_PATH
cd $DIR/build

# Export environment variables for building packages with MPI support
export CC=mpicc
export FC=mpiifort
export CXX=mpicxx
export CFLAGS='-O2 -DBOOST_DISABLE_ASSERTS'
export CXXFLAGS='-O2 -DBOOST_DISABLE_ASSERTS'
export FCFLAGS='-O2'

# Build hdf5 package
tar xf hdf5-1.8.20.tar.gz
cd hdf5-1.8.20
#mkdir $DIR/nemo_req_intel/hdf5-1.8.20


./configure --prefix=/$DIR/nemo_req_intel/hdf5-1.8.20 --enable-parallel --enable-fortran --enable-fortran2003 --enable-hl --enable-shared --enable-static --enable-production --enable-build-all --with-zlib=$DIR/nemo_req_intel/zlib-1.2.8 --with-szlib=$DIR/nemo_req_intel/szip-2.1
make 
mkdir -p -v  -p ~/test_mpi
HDF5_PARAPREFIX=~/test_mpi
export HDF5_PARAPREFIX
#make check
make install 
export PATH=$DIR/nemo_req_intel/hdf5-1.8.20/bin:$PATH
export LD_LIBRARY_PATH=$DIR/nemo_req_intel/hdf5-1.8.20/lib:$LD_LIBRARY_PATH
export HDF5=$DIR/nemo_req_intel/hdf5-1.8.20
cd $DIR/build

# Build curl package
export CC=mpiicc
export CFLAGS='-O2 -DBOOST_DISABLE_ASSERTS'
export CPP='icc -E'
tar xf curl-7.56.1.tar.gz
cd curl-7.56.1
./configure --prefix=$DIR/nemo_req_intel/curl-7.50.0 --disable-ipv6 --enable-crypto-auth --with-zlib=$DIR/nemo_req_intel/zlib-1.2.8 --with-ssl
make
make check
make install
export PATH=$DIR/nemo_req_intel/curl-7.50.0/bin:$PATH
export LD_LIBRARY_PATH=$DIR/nemo_req_intel/curl-7.50.0/lib:$LD_LIBRARY_PATH
cd $DIR/build


# Export additional environment variables for netcdf package
export CC=mpiicc
export CXX=mpicxx
export CFLAGS='-O2'
export CXXFLAGS='-O2'
export F77=mpiifort
export F90=mpiifort
export FFLAGS='-O2'
export CPP='mpiicc -E'
export CXXCPP='mpicxx -E'

export CPPFLAGS="-I$DIR/nemo_req_intel/zlib-1.2.8/include -I$DIR/nemo_req_intel/szip-2.1/include -I$DIR/nemo_req_intel/hdf5-1.8.20/include -I$DIR/nemo_req_intel/netcdf-4.4.0/include -I$DIR/nemo_req_intel/curl-7.50.0/include"
export LDFLAGS="-L$DIR/nemo_req_intel/zlib-1.2.8/lib -L$DIR/nemo_req_intel/szip-2.1/lib -L$DIR/nemo_req_intel/hdf5-1.8.20/lib -L$DIR/nemo_req_intel/netcdf-4.4.0/lib -L$DIR/nemo_req_intel/curl-7.50.0/lib"
export LD_LIBRARY_PATH="$DIR/nemo_req_intel/zlib-1.2.8/lib:$DIR/nemo_req_intel/szip-2.1/lib:$DIR/nemo_req_intel/hdf5-1.8.20/lib:$DIR/nemo_req_intel/netcdf-4.4.0/lib:$DIR/nemo_req_intel/curl-7.50.0/lib:$LD_LIBRARY_PATH"

# Build netcdf package
tar xf netcdf-4.4.0.tar.gz
cd netcdf-4.4.0
./configure --prefix=/$DIR/nemo_req_intel/netcdf-4.4.0  --enable-shared --enable-static --enable-parallel4 --enable-dap --enable-jna --enable-mmap --enable-diskless
make -j16
make check
make install
export PATH=$DIR/nemo_req_intel/netcdf-4.4.0/bin:$PATH
export NETCDF=$DIR/nemo_req_intel/netcdf-4.4.0
export NETCDF_LIB=$DIR/nemo_req_intel/netcdf-4.4.0/lib
export NETCDF_INC=$DIR/nemo_req_intel/netcdf-4.4.0/include
cd $DIR/build


# Build Fortran netcdf package
tar xf netcdf-fortran-4.4.4.tar.gz
cd netcdf-fortran-4.4.4
./configure --prefix=/$DIR/nemo_req_intel/netcdf-4.4.0 --enable-shared --enable-static --enable-f03
make -j16                                                                         
make check                                                                        
make install                                                                      
cd $DIR/build

# Build C++ netcdf package
tar xf netcdf-cxx-4.2.tar.gz                                                      
cd netcdf-cxx-4.2                                                                 
./configure --prefix=/$DIR/nemo_req_intel/netcdf-4.4.0 --enable-shared --enable-static
make -j16
make check
make install
cd $DIR/build


mkdir $DIR/nemo_i_libs

mkdir $DIR/nemo_i_libs/lib
mkdir $DIR/nemo_i_libs/include

cp -r -a $DIR/nemo_req_intel/szip-2.1/lib/* $DIR/nemo_i_libs/lib
cp -r -a $DIR/nemo_req_intel/zlib-1.2.8/lib/* $DIR/nemo_i_libs/lib
cp -r -a $DIR/nemo_req_intel/curl-7.50.0/lib/* $DIR/nemo_i_libs/lib
cp -r -a $DIR/nemo_req_intel/hdf5-1.8.20/lib/* $DIR/nemo_i_libs/lib
cp -r -a $DIR/nemo_req_intel/netcdf-4.4.0/lib/* $DIR/nemo_i_libs/lib

cp -r -a $DIR/nemo_req_intel/szip-2.1/include/* $DIR/nemo_i_libs/include
cp -r -a $DIR/nemo_req_intel/zlib-1.2.8/include/* $DIR/nemo_i_libs/include
cp -r -a $DIR/nemo_req_intel/curl-7.50.0/include/* $DIR/nemo_i_libs/include
cp -r -a $DIR/nemo_req_intel/hdf5-1.8.20/include/* $DIR/nemo_i_libs/include
cp -r -a $DIR/nemo_req_intel/netcdf-4.4.0/include/* $DIR/nemo_i_libs/include