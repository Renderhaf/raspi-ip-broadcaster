# raspi-ip-broadcaster
To activate for the first time, run RasbIP.py and write your Email address.
To make it send its ip to your Email do this:

```bash
$ sudo nano /etc/rc.local

```

And add This:

python3 /home/pi/raspi-ip-broadcaster/RasbIP.py

To change the Email configuration, do:

```bash
$ nano mail.config

```

the program only works with Gmail
