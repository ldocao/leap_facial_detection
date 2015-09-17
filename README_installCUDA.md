I have tried several things, but I don't know which one finally did the trick:

# The problem

Following [this](https://github.com/wendykan/AWSGPU_DeepLearning) does not work out of the box

# Tutorials
1/ http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/

Use directly 

pip install -r https://raw.githubusercontent.com/dnouri/kfkd-tutorial/master/requirements.txt

2/ http://markus.com/install-theano-on-aws/


# Some fix to the tutorials

I have done both, and there was still some problem. To debug, you need to do the following checks:

- run /home/ubuntu/src/lasagne/examples/mnist.py
- run the code found at http://deeplearning.net/software/theano/tutorial/using_gpu.html

you might need to install additional libraries, following [this thread](https://github.com/wendykan/AWSGPU_DeepLearning/issues/5) :

sudo apt-get install libpng-dev
sudo apt-get install libfreetype6-dev


# In the end

Running setup.py in AWSGPU_DeepLearning still doesn't work, but at least the two tests are passed. Maybe by following Daniel Nour's link, line by line, we can find what's wrong with the code. Coding with GPU is tough !