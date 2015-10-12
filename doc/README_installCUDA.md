# References:

- https://github.com/wendykan/AWSGPU_DeepLearning
- http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/
- http://markus.com/install-theano-on-aws/
- http://deeplearning.net/software/theano/tutorial/using_gpu.html
- https://github.com/wendykan/AWSGPU_DeepLearning/issues/5
- https://www.kaggle.com/c/diabetic-retinopathy-detection/forums/t/15496/help-using-lasagne-in-ec2-theano-unable-to-detect-gpu


# Shell commands
Run one after the other, all the commands in installCUDA.sh

# Important notes
- Please note that if you kill your EC2 instance, you will lose all your setup, and need to re-do all over again. You should thus plan your time accordingly.
- Sometimes, your script can be very slow to run. This may be due to very fast Interrupt Request (IRQ). You can check that with the top command, and notice that ksoftirqd/0 is eating up all your CPU. I'm not expert enough to fix this properly, but I did notice that by rebooting the EC2 server, the problem goes away. Anybody else has this problem ?
