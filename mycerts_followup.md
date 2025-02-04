# My IT Certifications and its paths


## My Certifications List:

 - Linux Professional Institute Certification 1 - LPIC1 (DESIRED)



## My Certifications Paths:

 - My path for the LPIC1 Certification:
    1. System Architecturei (==Exam 101==):
        1.1. [ ] **Determine and configure hardware settings** (==Weight: 2==): /sys/, /proc/, /dev/, modprobe, lsmod, lspci, lsusb...
            **Candidates should be able to determine and configure fundamental system hardware.**
            - [ ] Enable and disable integrated peripherals.
            - [ ] Differentiate between the various types of mass storage devices.
            - [ ] Determine hardware resources for devices.
            - [ ] Tools and utilities to list various hardware information (e.g. lsusb, lspci, etc.).
            - [ ] Tools and utilities to manipulate USB devices.
            - [ ] Conceptual understanding of sysfs, udev and dbus.
        1.2. [ ] **Boot the system** (==Weight:3==): dmesg, journalctl, BIOS, UEFI, bootloader, kernel, initramfs, init, SysVinit, systemd...
            **Candidates should be able to guide the system through the booting process.** 
            - [ ] Provide common commands to the boot loader and options to the kernel at boot time.
            - [ ] Demonstrate knowledge of the boot sequence from BIOS/UEFI to boot completion.
            - [ ] Understanding of SysVinit and systemd.
            - [ ] Awareness of Upstart.
            - [ ] Check boot events in the log files. 
        1.3. [ ] **Change runlevels / boot targets and shutdown or reboot system** (==Weight3==): /etc/inittab, shutdown, init, /etc/init.d, telinit, systemd, systemctl, /etc/systemd/, /usr/lib/systemd/, wall...
            **Candidates should be able to manage the SysVinit runlevel or systemd boot target of the system. This objective includes changing to single user mode, shutdown or rebooting the system. Candidates should be able to alert users before switching runlevels / boot targets and properly terminate processes. This objective also includes setting the default SysVinit runlevel or systemd boot target. It also includes awareness of Upstart as an alternative to SysVinit or systemd.**
            - [ ] Set the default runlevel or boot target.
            - [ ] Change between runlevels / boot targets including single user mode.
            - [ ] Shutdown and reboot from the command line.
            - [ ] Alert users before switching runlevels / boot targets or other major system events.
            - [ ] Properly terminate processes.
            - [ ] Awareness of acpid. 
    2. Linux Installation and Package Management:
        2.1. [ ] **Design hard disk layout** (==Weight:2==): /(root) filesystem, /var filesystem, /home filesyste, /boot filesystem, EFI System Partition (ESP), swap space, mount points, partitions...
            **Candidates should be able to design a disk partitioning scheme for a Linux system.** 
            - [ ] Allocate filesystems and swap space to separate partitions or disks.
            - [ ] Tailor the design to the intended use of the system.
            - [ ] Ensure the /boot partition conforms to the hardware architecture requirements for booting.
            - [ ] Knowledge of basic features of LVM.
        2.2. [ ] **Install a boot manager** (==Weight:2==): menu.lst, grub.cfg and grub.conf, grub-install, grub-mkconfig, MBR...
            **Candidates should be able to select, install and configure a boot manager.** 
            - [ ] Providing alternative boot locations and backup boot options.
            - [ ] Install and configure a boot loader such as GRUB Legacy.
            - [ ] Perform basic configuration changes for GRUB 2.
            - [ ] Interact with the boot loader. 
        2.3. [ ] **Manage shared libraries** (==Weight:1==): ldd, ldconfig, /etc/ld.so.conf, LS_LIBRARY_PATH...
            **Candidates should be able to determine the shared libraries that executable programs depend on and install them when necessary.** 
            - [ ] Identify shared libraries.
            - [ ] Identify the typical locations of system libraries.
            - [ ] Load shared libraries. 
        2.4. [ ] **Use Debian package management** (==Weight:3==): /etc/apt/sources.list, dpkg, dpkg-reconfigure, apt-get, apt-cache...
            **Candidates should be able to perform package management using the Debian package tools.** 
            - [ ] Install, upgrade and uninstall Debian binary packages.
            - [ ] Find packages containing specific files or libraries which may or may not be installed.
            - [ ] Obtain package information like version, content, dependencies, package integrity and installation status (whether or not the package is installed).
            - [ ] Awareness of apt.
        2.5. [ ] **Use RPM and YUM package management** (==Weight:3==): rpm, rpm2cpio, /etc/yum.conf, /etc/yum.repos.d/, yum, zypper...
            **Candidates should be able to perform package management using RPM, YUM and Zypper.** 
            - [ ] Install, re-install, upgrade and remove packages using RPM, YUM and Zypper.
            - [ ] Obtain information on RPM packages such as version, status, dependencies, integrity and signatures.
            - [ ] Determine what files a package provides, as well as find which package a specific file comes from.
            - [ ] Awareness of dnf.
        2.6. [ ] **Linux as a virtualization guest** (==Weight:1==): Virtual machine, Linux container, Application container, Guest drivers, SSH host keys, D-Bus machine id...
            **Candidates should understand the implications of virtualization and cloud computing on a Linux guest system.** 
            - [ ] Understand the general concept of virtual machines and containers
            - [ ] Understand common elements virtual machines in an IaaS cloud, such as computing instances, block storage and networking
            - [ ] Understand unique properties of a Linux system which have to changed when a system is cloned or used as a template
            - [ ] Understand how system images are used to deploy virtual machines, cloud instances and containers
            - [ ] Understand Linux extensions which integrate Linux with a virtualization product
            - [ ] Awareness of cloud-init
    3. GNU and Unix Commands:
        3.1. [ ] Work on the command line (==Weight:4==): bash, echo, env, export, pwd, set, unset, type, which, man uname, history, .bash_history, Quoting...
            **Candidates should be able to interact with shells and commands using the command line. The objective assumes the Bash shell.** 
            - [ ] Use single shell commands and one line command sequences to perform basic tasks on the command line.
            - [ ] Use and modify the shell environment including defining, referencing and exporting environment variables.
            - [ ] Use and edit command history.
            - [ ] Invoke commands inside and outside the defined path. 
        3.2. [ ] ***Process text streams using filters** (==Weight:2==): bzcat, cat, cut, head, less, md5sum, nl, od, paste, sed, sha256sum, sha512sum, sort, split, tail, tr, uniq, wc, xzcat, zcat...
            **Candidates should should be able to apply filters to text streams.** 
            - [ ] Send text files and output streams through text utility filters to modify the output using standard UNIX commands found in the GNU textutils package. 
        3.3. [ ] **Perform basic file management** (==Weight:4==): cp, find, mkdir, mv, ls, rm, rmdir, touch, tar, cpio, dd, file, gzip, gunzip, bzip2, bunzip2, xz, unxz, file globbing...
            **Candidates should be able to use the basic Linux commands to manage files and directories.** 
            - [ ] Copy, move and remove files and directories individually.
            - [ ] Copy multiple files and directories recursively.
            - [ ] Remove files and directories recursively.
            - [ ] Use simple and advanced wildcard specifications in commands.
            - [ ] Using find to locate and act on files based on type, size, or time.
            - [ ] Usage of tar, cpio and dd. 
        3.4. [ ] **Use streams, pipes and redirects** (==Weight:4==): tee, xargs...
            **Candidates should be able to redirect streams and connect them in order to efficiently process textual data. Tasks include redirecting standard input, standard output and standard error, piping the output of one command to the input of another command, using the output of one command as arguments to another command and sending output to both stdout and a file.**
            - [ ] Redirecting standard input, standard output and standard error.
            - [ ] Pipe the output of one command to the input of another command.
            - [ ] Use the output of one command as arguments to another command.
            - [ ] Send output to both stdout and a file. 
        3.5. [ ] **Create, monitor and kill processes** (==Weight:4==): &, bg, fg, jobs, kill, nohup, ps, top, free, uptime, pgrep, pkill, killall, watch, screen, tmux...
            **Candidates should be able to perform basic process management.** 
            - [ ] Run jobs in the foreground and background.
            - [ ] Signal a program to continue running after logout.
            - [ ] Monitor active processes.
            - [ ] Select and sort processes for display.
            - [ ] Send signals to processes. 
        3.6. [ ] **Modify process execution priorities** (==Weight:2==): nice, ps, renice, top...
            **Candidates should should be able to manage process execution priorities.** 
            - [ ] Know the default priority of a job that is created.
            - [ ] Run a program with higher or lower priority than the default.
            - [ ] Change the priority of a running process. 
        3.7. [ ] **Search text files using regular expressions** (==Weight:3==): grep, egrep, fgrep, sed, regex(7)...
            **Candidates should be able to manipulate files and text data using regular expressions. This objective includes creating simple regular expressions containing several notational elements as well as understanding the differences between basic and extended regular expressions. It also includes using regular expression tools to perform searches through a filesystem or file content.**
            - [ ] Create simple regular expressions containing several notational elements.
            - [ ] Understand the differences between basic and extended regular expressions.
            - [ ] Understand the concepts of special characters, character classes, quantifiers and anchors.
            - [ ] Use regular expression tools to perform searches through a filesystem or file content.
            - [ ] Use regular expressions to delete, change and substitute text.
        3.8. [ ] **Basic file editing** (==Weight:3==): vi, /, ?, h, j, k, l, i, o, a, d, p, y, dd, yy, ZZ, :w!, :q!, EDITOR...
            **Candidates should be able to edit text files using vi. This objective includes vi navigation, vi modes, inserting, editing, deleting, copying and finding text. It also includes awareness of other common editors and setting the default editor.** 
            - [ ] Navigate a document using vi.
            - [ ] Understand and use vi modes.
            - [ ] Insert, edit, delete, copy and find text in vi.
            - [ ] Awareness of Emacs, nano and vim.
            - [ ] Configure the standard editor.
    4. Devices, Linux Filesystems, Filesystem Hierarchy Standard:
        4.1. [ ] **Create partitions and filesystems** (==Weight:2==): fdisk, gdisk, parted, mkfs, mkswap...
            **Candidates should be able to configure disk partitions and then create filesystems on media such as hard disks. This includes the handling of swap partitions.**
            - [ ] Manage MBR and GPT partition tables
            - [ ] Use various mkfs commands to create various filesystems such as: ext2/ext3/ext4, XFS, VFAT, exFAT. 
            - [ ] Basic feature knowledge of Btrfs, including multi-device filesystems, compression and subvolumes.
        4.2. [ ] **Maintain the integrity of filesystems** (==Weight:2==): du, df, fsck, e2fsck, mke2fs, tune2fs, xfs_repair, xfs_fsr, xfs_db...
            **Candidates should be able to maintain a standard filesystem, as well as the extra data associated with a journaling filesystem.** 
            - [ ] Verify the integrity of filesystems.
            - [ ] Monitor free space and inodes.
            - [ ] Repair simple filesystem problems. 
        4.3. [ ] **Control mounting and unmounting of filesystems** (==Weight:3==): /etc/fstab, /media/, mount, umount, blkid, lsblk...
            **Candidates should be able to configure the mounting of a filesystem.** 
            - [ ] Manually mount and unmount filesystems.
            - [ ] Configure filesystem mounting on bootup.
            - [ ] Configure user mountable removable filesystems.
            - [ ] Use of labels and UUIDs for identifying and mounting file systems.
            - [ ] Awareness of systemd mount units.
        4.4. [ ] **~~REMOVED~~**
        4.5. [ ] **Manage file permissions and ownership** (==Weight:3==): chmod, umask, chown, chgrp...
            **Candidates should be able to control file access through the proper use of permissions and ownerships.** 
            - [ ] Manage access permissions on regular and special files as well as directories.
            - [ ] Use access modes such as suid, sgid and the sticky bit to maintain security.
            - [ ] Know how to change the file creation mask.
            - [ ] Use the group field to grant file access to group members. 
        4.6. [ ] **Create and change hard and symbolic links** (==Weight:2==): ln, ls...
            **Candidates should be able to create and manage hard and symbolic links to a file.** 
            - [ ] Create links.
            - [ ] Identify hard and/or soft links.
            - [ ] Copying versus linking files.
            - [ ] Use links to support system administration tasks.
        4.7. [ ] **Find system files and place files in the correct location** (==Weight:2==): find, locate, updatedb, whereis, which, type, /etc/updatedb.conf...
            **Candidates should be thoroughly familiar with the Filesystem Hierarchy Standard (FHS), including typical file locations and directory classifications.** 
            - [ ] Understand the correct locations of files under the FHS.
            - [ ] Find files and commands on a Linux system.
            - [ ] Know the location and purpose of important file and directories as defined in the FHS. 
    5. Shells and Shell Scripting (==Exam 102==):
        5.1. [ ] **Customize and use the shell environment** (==Weight:4==): ., source, /etc/bash.bashrc, /etc/profile, env, export, set, unset, ~/.bash_profile, ~/.bash_login, ~/.profile, ~/lbashrc, ~/.bash_logout, function, alias...
            **Candidates should be able to customize shell environments to meet users' needs. Candidates should be able to modify global and user profiles.** 
            - [ ] Set environment variables (e.g. PATH) at login or when spawning a new shell.
            - [ ] Write Bash functions for frequently used sequences of commands.
            - [ ] Maintain skeleton directories for new user accounts.
            - [ ] Set command search path with the proper directory. 
        5.2. [ ] **Customize or write simple scripts** (Weight:4): for, while, test, if, read, seq, exec, ||, &&...
            **Candidates should be able to customize existing scripts, or write simple new Bash scripts.** 
            - [ ] Use standard sh syntax (loops, tests).
            - [ ] Use command substitution.
            - [ ] Test return values for success or failure or other information provided by a command.
            - [ ] Execute chained commands.
            - [ ] Perform conditional mailing to the superuser.
            - [ ] Correctly select the script interpreter through the shebang (#!) line.
            - [ ] Manage the location, ownership, execution and suid-rights of scripts. 
    6. Interfaces and Desktops:
        6.1 [ ] **Install and configure X11** (==Weight:2==): /etc/X11/xorg.conf, /etc/X11/xorg.conf.d/, ~/.xsession-errors, xhost...
            **Candidates should be able to install and configure X11.** 
             - [ ] Understanding of the X11 architecture.
             - [ ] Basic understanding and knowledge of the X Window configuration file.
             - [ ] Overwrite specific aspects of Xorg configuration, such as keyboard layout.
             - [ ] Understand the components of desktop environments, such as display managers and window managers.
             - [ ] Manage access to the X server and display applications on remote X servers.
             - [ ] Awareness of Wayland.
        6.2. [ ] **Graphical Desktops** (==Weight:1==): KDE, Gnome, Xfce, X11, xdmcp, vnc, Spice, RDP...
            **Candidates should be aware of major Linux desktops. Furthermore, candidates should be aware of protocols used to access remote desktop sessions.** 
             - [ ] Awareness of major desktop environments
             - [ ] Awareness of protocols to access remote desktop sessions.
        6.3. [ ] **Accessibility** (==Weight:1==): High Contrast/ Large Print Desktop Themes, Screen Reader, Braille Magnifier, Screen Manifier, On-Screen Keyboard, Stichy/Repeat Keys, Slow/Bounce/Toggle Keys, Mouse Keys, Gestures, Voice recognition...
            **Demonstrate knowledge and awareness of accessibility technologies.**
             - [ ] Basic knowledge of visual settings and themes.
             - [ ] Basic knowledge of assistive technology.
    7. Administrative Tasks:
        7.1. [ ] **Manage user and group accounts and related system files** (==Weight:5==) /etc/passwd, /etc/shadow, /etc/group /etc/skel/, chage, getent, groupadd, groupdel, groupmod, passwd, useradd, userdel, usermod...
            **Candidates should be able to add, remove, suspend and change user accounts.** 
             - [ ] Add, modify and remove users and groups.
             - [ ] Manage user/group info in password/group databases.
             - [ ] Create and manage special purpose and limited accounts. 
        7.2. [ ] **Automate system administration tasks by scheduling jobs** (==Weight: 4==): /etc/cron.{d,daily, hourly,monthly,weekly}/, /etc/at.deny, /etc/at.allow, /etc/crontab, /etc/cron.allow, /etc/cron.deny, /var/spool/cron/, crontab, at ,atq, atrm, systemctl, systemd-run...
            **Candidates should be able to use cron and systemd timers to run jobs at regular intervals and to use at to run jobs at a specific time.** 
              - [ ] Manage cron and at jobs.
              - [ ] Configure user access to cron and at services.
              - [ ] Understand systemd timer units.
        7.3. [ ] **Localisation and internationalisation** (==Weight: 3==): /etc/timezone, /etc/localtime, /usr/share/zoneinfo/, LC_*, LC_ALL, LANG, TZ, /usr/bin/locale, tzselect, timectl, date, iconv, UTF-8, ISO-8859, ASCII, Unicode...
            **Candidates should be able to localize a system in a different language than English. As well, an understanding of why LANG=C is useful when scripting.**
              - [ ] Configure locale settings and environment variables.
              - [ ] Configure timezone settings and environment variables.
    8. Essential System Services:
        8.1. [ ] **Maintain system time** (==Weight: 3==): /usr/share/zoneinfo/, /etc/timezone, /etc/localtime, /etc/ntp.conf, /etc/chrony.conf, date, hwclock, timedatectl, ntpd, ntpdate, chronyc, pool.ntp.org...
            **Candidates should be able to properly maintain the system time and synchronize the clock via NTP.** 
              - [ ]  Set the system date and time.
              - [ ] Set the hardware clock to the correct time in UTC.
              - [ ] Configure the correct timezone.
              - [ ] Basic NTP configuration using ntpd and chrony.
              - [ ] Knowledge of using the pool.ntp.org service.
              - [ ] Awareness of the ntpq command.
        8.2. [ ] **System logging** (==Weight: 4==): /etc/rsyslog.conf, /var/log/, logger, logrotate, /etc/logrotate.conf, /etc/logrotate.d/, journalctl, systemd-cat, /etc/systemd/journald.conf, /var/log/journal...
            **Candidates should be able to configure rsyslog. This objective also includes configuring the logging daemon to send log output to a central log server or accept log output as a central log server. Use of the systemd journal subsystem is covered. Also, awareness of syslog and syslog-ng as alternative logging systems is included.** 
              - [ ] Basic configuration of rsyslog.
              - [ ] Understanding of standard facilities, priorities and actions.
              - [ ] Query the systemd journal.
              - [ ] Filter systemd journal data by criteria such as date, service or priority
              - [ ] Configure persistent systemd journal storage and journal size
              - [ ] Delete old systemd journal data
              - [ ] Retrieve systemd journal data from a rescue system or file system copy
              - [ ] Understand interaction of rsyslog with systemd-journald
              - [ ] Configuration of logrotate.
              - [ ] Awareness of syslog and syslog-ng.
        8.3. [ ] **Mail Transfer Agent (MTA) basics** (==Weight: 3==): ~/.forward, sendmail emulation layer commands, newaliases, mail, mailq, postfix, sendmail, exim...
            **Candidates should be aware of the commonly available MTA programs and be able to perform basic forward and alias configuration on a client host. Other configuration files are not covered.**  
               - [ ] Create e-mail aliases.
               - [ ] Configure e-mail forwarding.
               - [ ] Knowledge of commonly available MTA programs (postfix, sendmail, exim) (no configuration). 
        8.4. [ ] **Manage printers and printing** (==Weight: 2==): CUPS configuration files, tools and utilities, /etc/cups/, lpd legacy interface (lpr, lprm, lpq)...
            **Candidates should be able to manage print queues and user print jobs using CUPS and the LPD compatibility interface.** 
              - [ ] Basic CUPS configuration (for local and remote printers).
              - [ ] Manage user print queues.
              - [ ] Troubleshoot general printing problems.
              - [ ] Add and remove jobs from configured printer queues. 
    9. Networking Fundamentals:
        9.1. [ ] **Fundamentals of internet protocols** (==Weight: 4==): /etc/services/, IPv4, IPv6, Subnetting, TCP, UDP, ICMP...
            **Candidates should demonstrate a proper understanding of TCP/IP network fundamentals.** 
               - [ ] Demonstrate an understanding of network masks and CIDR notation.
               - [ ] Knowledge of the differences between private and public "dotted quad" IP addresses.
               - [ ] Knowledge about common TCP and UDP ports and services (20, 21, 22, 23, 25, 53, 80, 110, 123, 139, 143, 161, 162, 389, 443, 465, 514, 636, 993, 995).
               - [ ] Knowledge about the differences and major features of UDP, TCP and ICMP.
               - [ ] Knowledge of the major differences between IPv4 and IPv6.
               - [ ] Knowledge of the basic features of IPv6.
        9.2. [ ] **Persistent network configuration** (==Weight: 4==): /etc/hostname, /etc/hosts, /etc/nsswitch.conf, /etc/resolv.conf, nmcli, hostnamectl, ifup, ifdown...
            **Candidates should be able to manage the persistent network configuration of a Linux host.**
               - [ ] Understand basic TCP/IP host configuration
               - [ ] Configure ethernet and wi-fi network configuration using NetworkManager
               - [ ] Awareness of systemd-networkd.
        9.3. [ ] **Basic network troubleshooting** (==Weight: 4==): ip, hostname, ss, ,ping, ping6, traceroute, traceroute6, tracepath, tracepath6, netcat, ifconfig, netstat, route...
            **Candidates should be able to troubleshoot networking issues on client hosts.** 
               - [ ] Manually configure network interfaces, including viewing and changing the configuration of network interfaces using iproute2.
               - [ ] Manually configure routing, including viewing and changing routing tables and setting the default route using iproute2.
               - [ ] Debug problems associated with the network configuration.
               - [ ] Awareness of legacy net-tools commands.
        9.4. [ ] **Configure client side DNS** (==Weiht: 2==): /etc/hosts, /etc/resolv.conf, /etc/nsswitch.conf, host, dig, getent...
            **Candidates should be able to configure DNS on a client host.** 
               - [ ] Query remote DNS servers.
               - [ ] Configure local name resolution and use remote DNS servers.
               - [ ] Modify the order in which name resolution is done.
               - [ ] Debug errors related to name resolution.
               - [ ] Awareness of systemd-resolved.
    10. Security:
        10.1. [ ] **Perform security administration tasks** (==Weight: 3==): find, passwd, fuser, lsof, nmap, chage, netstat, sudo, /etc/sudoers/, su, usermod, ulimit, who, w, last...
            **Candidates should know how to review system configuration to ensure host security in accordance with local security policies.** 
                - [ ] Audit a system to find files with the suid/sgid bit set.
                - [ ] Set or change user passwords and password aging information.
                - [ ] Being able to use nmap and netstat to discover open ports on a system.
                - [ ] Set up limits on user logins, processes and memory usage.
                - [ ] Determine which users have logged in to the system or are currently logged in.
                - [ ] Basic sudo configuration and usage. 
        10.2. [ ] **Setup host security** (==Weight: 3==): /etc/nologin, /etc/passwd, /etc/shadow, /etc/xinetd.d/, /etc/xinetd.conf, systemd.socket, /etc/inittab, /etc/init.d/, /etc/hosts.allow, /etc/hosts.deny... 
            **Candidates should know how to set up a basic level of host security.** 
                - [ ] Awareness of shadow passwords and how they work.
                - [ ] Turn off network services not in use.
                - [ ] Understand the role of TCP wrappers. 
        10.3. [ ] **Securing data with encryption** (==Weight: 4==): ssh, ssh-keygen, ssh-agent, ssh-add, ~/.ssh/id_rsa and id_rsa.pub, ~/.ssh/id_dsa and id_dsa.pub, ~/.ssh/id-ecdsa and id_ecdsa.pub, ~/.ssh/id_ed25519 and id_ed25519.pub, ~/.ssh/authorized_keys, ssh_know_hosts, gpg, gpg-agent, ~/.gnupg/...
            **The candidate should be able to use public key techniques to secure data and communication.** 
                - [ ] Perform basic OpenSSH 2 client configuration and usage.
                - [ ] Understand the role of OpenSSH 2 server host keys.
                - [ ] Perform basic GnuPG configuration, usage and revocation.
                - [ ] Use GPG to encrypt, decrypt, sign and verify files.
                - [ ] Understand SSH port tunnels (including X11 tunnels).
    - [LPIC-1 Exam 101 and 102 Objectives](https://www.lpi.org/our-certifications/exam-101-102-objectives/) 















