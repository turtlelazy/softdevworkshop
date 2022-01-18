# Creating a Droplet With Digital Ocean

## Creating the Droplet

You are presented with a simple, neat UI by Digital Ocean, and only need to select the desired configurations. After selecting on create droplet, it's pretty straightforward.


Step 1: Creating the droplet
* Select Ubuntu for the distribution
* Choose whatever CPU and block storage plan that is desired (block storage is entirely optionally)
* Choose your region desired for the datacenter
* You can select ssh key or password for now. We will change this in the config file later.
* Select any additional features desired
* Name your project and droplet!
* Create!

Step 2: Configuring Accounts
Here, we utilize the resource https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04, Digital Ocean provides very helpful guides for what we want to do.

* Login to root@{ipaddressofyourdroplet} and with the password (or automatic if using ssh key)
* Create a new account by using the command ```adduser {username}```
