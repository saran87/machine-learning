#!/bin/bash

#
#
# Hadoop setup script
# Authour: Saravana Kumar
#

#****************************************************************************
# 1. Install java version7
#*****************************************************************************
echo "================================================================================"
echo "Installing Java...."
echo "================================================================================"
sudo apt-get install openjdk-7-jre

#****************************************************************************
# 2. Create a dedicated group for
#    Hadoop system  users will help in
#    separating Hadoop installation
#*****************************************************************************
echo "================================================================================"
echo "Creating hadoop group..."
echo "================================================================================"
sudo addgroup hadoop

#***************************************************************************
# 3. Create Hadoop user (hduser) and add it the Hadoop user group
#    Create a password and profile for the user.
#
#*****************************************************************************
echo "================================================================================"
echo "Creating hadoop user and adding it to the group..."
sudo adduser --ingroup hadoop hduser
echo "================================================================================"
#==============================================================================
#				  CONFIGURING SSH FOR HADOOP USER
#==============================================================================
 
#***************************************************************************
# 4. Change user to Hadoop User
#
#*****************************************************************************
#su - hduser
 
#***************************************************************************
# 5. Create RSA Key pair with empty password
#
#*****************************************************************************
echo "================================================================================"
echo "Generate public key for allowing ssh access"
echo "================================================================================"
ssh-keygen -t rsa -P ""

#***************************************************************************
# 6. Now enable access ssh access to local machine with newly created RSA key pairs.
#
#*****************************************************************************
echo "================================================================================"
echo "Copy the public key to the hadoop user folder"
echo "================================================================================"
cat $HOME/.ssh/id_rsa.pub >> /home/hduser/.ssh/authorized_keys

#================================================================================
#
#  Disable ipv6 manually 
#  You can check whether IPv6 is enabled on your machine with the following command:
#  $ cat /proc/sys/net/ipv6/conf/all/disable_ipv6
#  A return value of 0 means IPv6 is enabled, a value of 1 means disabled (that’s what we want).
#
#  To disable IPv6 on Ubuntu 12.04 LTS, open /etc/sysctl.conf in the editor of your choice 
#  and add the following lines to the end of the file:
#  disable ipv6
#  net.ipv6.conf.all.disable_ipv6 = 1
#  net.ipv6.conf.default.disable_ipv6 = 1
#  net.ipv6.conf.lo.disable_ipv6 = 1
#
#  You have to reboot your machine in order to make the changes take effect.
#================================================================================";

#================================================================================
#				  INSTALLING  HADOOP 
#================================================================================

#***************************************************************************
# 7. Get the latest version of Hadoop
#
#*****************************************************************************
echo "================================================================================"
echo "Downloading Hadoop..."
echo "================================================================================"

wget http://apache.mirrors.lucidnetworks.net/hadoop/core/stable/hadoop-1.0.4-bin.tar.gz

#***************************************************************************
# 8. UnPack the Hadoop package and move Hadoop to /usr/local location
#
#*****************************************************************************
echo "================================================================================"
echo "Expanding Hadoop..."
sudo tar xzf hadoop-1.0.4-bin.tar.gz
echo "Moving Hadoop to  /usr/local/  location..."
sudo mv hadoop-1.0.4 hadoop
echo "================================================================================"

sudo mv hadoop /usr/local/hadoop

#***************************************************************************
# 9. Give file permission to the hadoop user to the hadoop folder under
#     /usr/local/hadoop
#*****************************************************************************
echo "================================================================================"
echo "Giving permission to hadoop user (hduser) for hadoop folder"
echo "================================================================================"
cd /usr/local
sudo chown -R hduser:hadoop hadoop



