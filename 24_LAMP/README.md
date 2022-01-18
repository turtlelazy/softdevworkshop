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
* Add user to sudo group ```usermod -aG sudo sammy```
* We need to use ufw, to manage the connections our server has. Use ```ufw allow OpenSSH``` to allow OpenSSH
* Enable a firewall with ```ufw enable```
* Login into the user you created, and add your ssh key. For a guide on how to create and add keys, check https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
* Now we need to disable root, and make sure only ssh is the option we want enabled. Let's ```su {user}````
* Check this resource out: https://phoenixnap.com/kb/ssh-permission-denied-publickey
* We will need to change our config file. Let's edit ```~/etc/ssh/sshd_config``` with nano:
* ```sudo nano ~/etc/ssh/sshd_config```
* Inside this config file, look for ```password authentication {yes/no}``` and set the boolean to ```no```
* Look for ```PermitRootLogin {yes/no}``` and set that to ```no```
* Look for ```PubKeyAuthentication {yes/no}``` and set it to ```yes```
* Now, use ```sudo systemctl restart sshd``` to restart the ssh service.

Step 3: Installing Apache 2.0 (alternatively, follow this better guide https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04)

* Let's ```sudo apt update``` and ```sudo apt install apache2```
* Now, we use ufw again, and do ```sudo ufw allow 'Apache'```
* If you use, ```sudo ufw status```, you should see Apache be on the list and allowed
* Now, you should be all set up! You can type ```sudo systemctl status apache2``` to double check the status of your server. Navigate to your server's IP, to now see the results of your Apache setup in its full glory.