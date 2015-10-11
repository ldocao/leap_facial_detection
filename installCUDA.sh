#!/bin/bash

##for convenience
sudo apt-get install emacs

##install CUDA
sudo apt-get update
sudo apt-get -y dist-upgrade  
sudo apt-get install python-pip
sudo apt-get install -y gcc g++ gfortran build-essential git wget linux-image-generic libopenblas-dev python-dev python-pip python-nose python-numpy python-scipy 
sudo pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
sudo wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.0-28_amd64.deb  
sudo dpkg -i cuda-repo-ubuntu1404_7.0-28_amd64.deb 
sudo apt-get update
sudo apt-get install -y cuda  
echo -e "\nexport PATH=/usr/local/cuda/bin:$PATH\n\nexport LD_LIBRARY_PATH=/usr/local/cuda/lib64" >> .bashrc 
sudo reboot  #this will log you out. wait for couple of minutes, then log back with ssh


sudo apt-get install libpng-dev 
sudo apt-get install libfreetype6-dev
sudo ldconfig /usr/local/cuda-7.5/lib64
sudo pip install -r https://raw.githubusercontent.com/dnouri/kfkd-tutorial/master/requirements.txt

#some test on CUDA
python /home/ubuntu/src/lasagne/examples/mnist.py #the command above should output something like this below. Note that it enters an infinite loop and you need to hit "Ctrl-C" to break it, and get back the terminal.

# Loading data...
# Downloading MNIST dataset
# Building model and compiling functions...
# /home/ubuntu/src/lasagne/lasagne/init.py:86: UserWarning: The uniform initializer no longer uses Glorot et al.'s approach to determine the bounds, but defaults to the range (-0.01, 0.01) instead. Please use the new GlorotUniform initializer to get the old behavior. GlorotUniform is now the default for all layers.
#   warnings.warn("The uniform initializer no longer uses Glorot et al.'s "
# /home/ubuntu/src/lasagne/lasagne/layers/helper.py:52: UserWarning: get_all_layers() has been changed to return layers in topological order. The former implementation is still available as get_all_layers_old(), but will be removed before the first release of Lasagne. To ignore this warning, use `warnings.filterwarnings('ignore', '.*topo.*')`.
#   warnings.warn("get_all_layers() has been changed to return layers in "
# Starting training...
# Epoch 1 of 500 took 5.624s
#   training loss:        1.318171
#   validation loss:      0.456231
#   validation accuracy:      87.68 %%
# Epoch 2 of 500 took 5.616s
#   training loss:        0.591208
#   validation loss:      0.328247
#   validation accuracy:      90.68 %%
# Epoch 3 of 500 took 5.605s
#   training loss:        0.465466
#   validation loss:      0.278153
#   validation accuracy:      91.85 %%
# Epoch 4 of 500 took 5.605s
#   training loss:        0.400180
#   validation loss:      0.246367
#   validation accuracy:      92.89 %%
# Epoch 5 of 500 took 5.606s
#   training loss:        0.363664
#   validation loss:      0.225049
#   validation accuracy:      93.50 %%
# Epoch 6 of 500 took 5.607s
#   training loss:        0.332929
#   validation loss:      0.207362
#   validation accuracy:      93.98 %%



## install Theano
echo -e "\n[global]\nfloatX=float32\ndevice=gpu\n[mode]=FAST_RUN\n\n[nvcc]\nfastmath=True\n\n[cuda]\nroot=/usr/local/cuda" >> ~/.theanorc 

#some test on theano
scp -i "keyname.pem" check1.py ubuntu@[DNS]:./ #first upload check1.py onto EC2 with something like:
ssh -i "keyname.pem" ubuntu@[DNS] #log back
python check1.py #you should get something like below:
# Using gpu device 0: GRID K520 (CNMeM is disabled)
# [GpuElemwise{exp,no_inplace}(<CudaNdarrayType(float32, vector)>), HostFromGpu(GpuElemwise{exp,no_inplace}.0)]
# Looping 1000 times took 0.654080 seconds
# Result is [ 1.23178029  1.61879349  1.52278066 ...,  2.20771813  2.29967761
#   1.62323296]
# Used the gpu

