#!/bin/bash

sudo apt-get -y install libpng-dev
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

#check1 on theano
scp -i "keyname.pem" check1.py ubuntu@[DNS]:./ #first upload check1.py onto EC2 with something like:
ssh -i "keyname.pem" ubuntu@[DNS] #log back
python check1.py #you should get something like below:
# Using gpu device 0: GRID K520 (CNMeM is disabled)
# [GpuElemwise{exp,no_inplace}(<CudaNdarrayType(float32, vector)>), HostFromGpu(GpuElemwise{exp,no_inplace}.0)]
# Looping 1000 times took 0.654080 seconds
# Result is [ 1.23178029  1.61879349  1.52278066 ...,  2.20771813  2.29967761
#   1.62323296]
# Used the gpu



#check2 on theano
#do the same than above with the file check2.py, you should get:
# ubuntu@ip-172-31-12-21:~$ python check2.py 
# Using gpu device 0: GRID K520 (CNMeM is disabled)
# [GpuElemwise{exp,no_inplace}(<CudaNdarrayType(float32, vector)>)]
# Looping 1000 times took 0.193634 seconds
# Result is <CudaNdarray object at 0x7fd2995aceb0>
# Numpy result is [ 1.23178029  1.61879349  1.52278066 ...,  2.20771813  2.29967761
#   1.62323296]
# Used the gpu
