# How to compile and run ~~MODEL FROM HELL~~ NEMO 4.0
## 1. Installing Intel compilers (Fortran, C++) 
1. Download **Intel® oneAPI Base Toolkit** from [here](https://software.intel.com/content/www/us/en/develop/tools/oneapi/hpc-toolkit/download.html#operatingsystem=Linux&#distributions=Web%20&%20Local%20(recommended)&#options=Online).
2. Default software install with:

        wget https://registrationcenter-download.intel.com/akdlm/irc_nas/17427/l_HPCKit_p_2021.1.0.2684.sh

        sudo bash l_HPCKit_p_2021.1.0.2684.sh
3. Configure the system ([source](https://software.intel.com/content/www/us/en/develop/documentation/get-started-with-intel-oneapi-hpc-linux/top/before-you-begin.html)).

        sudo apt -y install cmake pkg-config build-essential

    Set environmental variables (for root or sudo):

        . /opt/intel/oneapi/setvars.sh
        source /opt/intel/oneapi/setvars.sh

    or (for normal user):

        . ~/intel/oneapi/setvars.sh
        source ~/intel/oneapi/setvars.sh
## 2. Installing and compile required packages
1. Download and compile libraries (szip, zlib, hdf5, curl, netcdf, C++ netcdf, Fortran netcdf)

        bash ./NEMO_packages_compile.sh

2. Download and compile XIOS 2.5

        sudo apt-get install subversion
        bash ./NEMO_XIOS_compile.sh

## 3. Installing and compile NEMO 4.0

1. Download NEMO 4.0 and configure

        bash ./NEMO_model_configure.sh

2. Compile SPITZ12

        bash ./NEMO_compile_SPITZ.sh

2. Compile ORCA2_ICE_PISCES

        bash ./NEMO_compile_ORCA.sh

3. Run model calculations

    Before running model input data should be downloaded from [here](https://zenodo.org/record/3386310#.YCw6DHUzaZE). Names of archives are in [documentation](https://forge.ipsl.jussieu.fr/nemo/chrome/site/doc/NEMO/guide/html/cfgs.html).

    Then files (input archives) are comfortable to put in *~/NEMO4.0/nemo4/nemo_i/r4.0.4/cfgs/\<config name>\/MY_SRC*. 
    
    And unpack files in *~/NEMO4.0/nemo4/nemo_i/r4.0.4/cfgs/\<config name>\/EXP00* 

    To start model calculations run:

        bash ./NEMO_SPITZ_run.sh
        bash ./NEMO_ORCA_run.sh

***
# Model customization
## 1. Copy default model
 Run bush  but change name of configuration

    bash ./NEMO_custom_conf.sh

## 2. Custom changes
Before custom model compilation input archives must be prepared as in default but the main detail is *domain_cfg.nc* file. 

To generate it the  [*DOMAINcfg* tool](https://forge.ipsl.jussieu.fr/nemo/chrome/site/doc/NEMO/guide/html/tools.html#domaincfg) should be compiled and run. 

Compilation:

    bush ./DOMAINcfg_compile.sh

Then in folder *~/NEMO4.0/nemo4/nemo_i/r4.0.4/tools/DOMAINcfg* where *make_domain_cfg.exe* was created, resourses and *namelist_cfg* should be changed on the same from default configuration (more info in ~/DOMAINcfg/README).

To create custom *domain_cfg.nc* file:

    bush ./NEMO_custom_domain.sh

>*Вот тут у меня все и сломалось, файл создается, но он кривой какой-то, на нем модель падает. Скорее всего потому что неправильно внесла новые параметры. Нужно попробовать взять namelist из уже скомпиленной дефолтной модели и подумать, что такое ресурсы и куда их правильно положить.*