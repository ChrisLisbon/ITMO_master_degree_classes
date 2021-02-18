DIR=/home/julia/NEMO4.0/nemo4
cd $DIR/nemo_i
svn co https://forge.ipsl.jussieu.fr/nemo/svn/NEMO/releases/r4.0/r4.0.4

cd $DIR/nemo_i/r4.0.4/arch/

# Configure NEMO package

cat <<EOF > arch-icc17.fcm
# Intel 2017 Update 4 and Intel MPI
%NCDF_HOME           $DIR/nemo_i_libs
%XIOS_HOME           $DIR/nemo_i/xios
%HDF5_HOME           $DIR/nemo_i_libs

%XIOS_LIB            -L%XIOS_HOME/lib -lxios
%XIOS_INC            -I%XIOS_HOME/inc

%NCDF_INC            -I%NCDF_HOME/include
%NCDF_LIB            -L%NCDF_HOME/lib -lnetcdf -lnetcdff



%FC                  mpiifort
%FCFLAGS             -O3 -xHost -g -heap-arrays -fp-model fast -r8 
%CFLAGS              -O3 -xHost -g -heap-arrays -fp-model fast  
%FFLAGS              -O3 -xHost -g -heap-arrays -fp-model fast -r8 
%LD                  %FC
%FPPFLAGS            -P -C -traditional
%LDFLAGS             %XIOS_LIB %NCDF_LIB -lstdc++ -lnetcdff -lnetcdf -lhdf5_hl -lhdf5 -lhdf5 -lz -lsz -lmpi -lmpifort -lmpicxx
%AR                  ar
%ARFLAGS             -r
%MK                  make
%CPP                 icpc -traditional -E -x c
%USER_INC            %XIOS_INC %NCDF_INC
%USER_LIB            %XIOS_LIB %NCDF_LIB
%CC                  mpiicc

EOF