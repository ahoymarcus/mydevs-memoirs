# My IT Certifications and its paths


## My Certifications List:

 - Linux Professional Institute Certification 1 - LPIC1 (desired)



## My Certifications Paths:

 - My path for the LPIC1 Certification:
    - System Architecture:
        - [ ] Determine and configure hardware settings: /sys/, /proc/, /dev/, modprobe, lsmod, lspci, lsusb...
            - Candidates should be able to determine and configure fundamental system hardware. 
            - [ ] Enable and disable integrated peripherals.
            - [ ] Differentiate between the various types of mass storage devices.
            - [ ] Determine hardware resources for devices.
            - [ ] Tools and utilities to list various hardware information (e.g. lsusb, lspci, etc.).
            - [ ] Tools and utilities to manipulate USB devices.
            - [ ] Conceptual understanding of sysfs, udev and dbus.
        - [ ] Boot the system: dmesg, journalctl, BIOS, UEFI, bootloader, kernel, initramfs, init, SysVinit, systemd...
            - Candidates should be able to guide the system through the booting process. 
            - [ ] Provide common commands to the boot loader and options to the kernel at boot time.
            - [ ] Demonstrate knowledge of the boot sequence from BIOS/UEFI to boot completion.
            - [ ] Understanding of SysVinit and systemd.
            - [ ] Awareness of Upstart.
            - [ ] Check boot events in the log files. 
        - [ ] Change runlevels / boot targets and shutdown or reboot system: /etc/inittab, shutdown, init, /etc/init.d, telinit, systemd, systemctl, /etc/systemd/, /usr/lib/systemd/, wall...
            - Candidates should be able to manage the SysVinit runlevel or systemd boot target of the system. This objective includes changing to single user mode, shutdown or rebooting the system. Candidates should be able to alert users before switching runlevels / boot targets and properly terminate processes. This objective also includes setting the default SysVinit runlevel or systemd boot target. It also includes awareness of Upstart as an alternative to SysVinit or systemd. 
            - [ ] Set the default runlevel or boot target.
            - [ ] Change between runlevels / boot targets including single user mode.
            - [ ] Shutdown and reboot from the command line.
            - [ ] Alert users before switching runlevels / boot targets or other major system events.
            - [ ] Properly terminate processes.
            - [ ] Awareness of acpid. 
    - Linux Installation and Package Management:
        - [ ] Design hard disk layout: /(root) filesystem, /var filesystem, /home filesyste, /boot filesystem, EFI System Partition (ESP), swap space, mount points, partitions...
            - Candidates should be able to design a disk partitioning scheme for a Linux system. 
            - [ ] Allocate filesystems and swap space to separate partitions or disks.
            - [ ] Tailor the design to the intended use of the system.
            - [ ] Ensure the /boot partition conforms to the hardware architecture requirements for booting.
            - [ ] Knowledge of basic features of LVM.
        - [ ] Install a boot manager: menu.lst, grub.cfg and grub.conf, grub-install, grub-mkconfig, MBR...
            - Candidates should be able to select, install and configure a boot manager. 
            - [ ] Providing alternative boot locations and backup boot options.
            - [ ] Install and configure a boot loader such as GRUB Legacy.
            - [ ] Perform basic configuration changes for GRUB 2.
            - [ ] Interact with the boot loader. 
        - [ ] Manage shared libraries: ldd, ldconfig, /etc/ld.so.conf, LS_LIBRARY_PATH...
            - Candidates should be able to determine the shared libraries that executable programs depend on and install them when necessary. 
            - [ ] Identify shared libraries.
            - [ ] Identify the typical locations of system libraries.
            - [ ] Load shared libraries. 
        - [ ] Use Debian package management: /etc/apt/sources.list, dpkg, dpkg-reconfigure, apt-get, apt-cache...
            - Candidates should be able to perform package management using the Debian package tools. 
            - [ ] Install, upgrade and uninstall Debian binary packages.
            - [ ] Find packages containing specific files or libraries which may or may not be installed.
            - [ ] Obtain package information like version, content, dependencies, package integrity and installation status (whether or not the package is installed).
            - [ ] Awareness of apt.
        - [ ] Use RPM and YUM package management: rpm, rpm2cpio, /etc/yum.conf, /etc/yum.repos.d/, yum, zypper...
            - Candidates should be able to perform package management using RPM, YUM and Zypper. 
            - [ ] Install, re-install, upgrade and remove packages using RPM, YUM and Zypper.
            - [ ] Obtain information on RPM packages such as version, status, dependencies, integrity and signatures.
            - [ ] Determine what files a package provides, as well as find which package a specific file comes from.
            - [ ] Awareness of dnf.
        - [ ] Linux as a virtualization guest: Virtual machine, Linux container, Application container, Guest drivers, SSH host keys, D-Bus machine id...
            - Candidates should understand the implications of virtualization and cloud computing on a Linux guest system. 
            - [ ] Understand the general concept of virtual machines and containers
            - [ ] Understand common elements virtual machines in an IaaS cloud, such as computing instances, block storage and networking
            - [ ] Understand unique properties of a Linux system which have to changed when a system is cloned or used as a template
            - [ ] Understand how system images are used to deploy virtual machines, cloud instances and containers
            - [ ] Understand Linux extensions which integrate Linux with a virtualization product
            - [ ] Awareness of cloud-init
    - GNU and Unix Commands:
        - [ ] Work on the command line: bash, echo, env, export, pwd, set, unset, type, which, man uname, history, .bash_history, Quoting...
            - Candidates should be able to interact with shells and commands using the command line. The objective assumes the Bash shell. 
            - [ ] Use single shell commands and one line command sequences to perform basic tasks on the command line.
            - [ ] Use and modify the shell environment including defining, referencing and exporting environment variables.
            - [ ] Use and edit command history.
            - [ ] Invoke commands inside and outside the defined path. 
        - [ ] Process text streams using filters: bzcat, cat, cut, head, less, md5sum, nl, od, paste, sed, sha256sum, sha512sum, sort, split, tail, tr, uniq, wc, xzcat, zcat...
            - Candidates should should be able to apply filters to text streams. 
            - [ ] Send text files and output streams through text utility filters to modify the output using standard UNIX commands found in the GNU textutils package. 
        - [ ] Perform basic file management: cp, find, mkdir, mv, ls, rm, rmdir, touch, tar, cpio, dd, file, gzip, gunzip, bzip2, bunzip2, xz, unxz, file globbing...
            - Candidates should be able to use the basic Linux commands to manage files and directories. 
            - [ ] Copy, move and remove files and directories individually.
            - [ ] Copy multiple files and directories recursively.
            - [ ] Remove files and directories recursively.
            - [ ] Use simple and advanced wildcard specifications in commands.
            - [ ] Using find to locate and act on files based on type, size, or time.
            - [ ] Usage of tar, cpio and dd. 
        - [ ] Use streams, pipes and redirects: tee, xargs...
            - Candidates should be able to redirect streams and connect them in order to efficiently process textual data. Tasks include redirecting standard input, standard output and standard error, piping the output of one command to the input of another command, using the output of one command as arguments to another command and sending output to both stdout and a file. 
            - [ ] Redirecting standard input, standard output and standard error.
            - [ ] Pipe the output of one command to the input of another command.
            - [ ] Use the output of one command as arguments to another command.
            - [ ] Send output to both stdout and a file. 
        - [ ] Create, monitor and kill processes: &, bg, fg, jobs, kill, nohup, ps, top, free, uptime, pgrep, pkill, killall, watch, screen, tmux...
            - Candidates should be able to perform basic process management. 
            - [ ] Run jobs in the foreground and background.
            - [ ] Signal a program to continue running after logout.
            - [ ] Monitor active processes.
            - [ ] Select and sort processes for display.
            - [ ] Send signals to processes. 
        - [ ] Modify process execution priorities: nice, ps, renice, top...
            - Candidates should should be able to manage process execution priorities. 
            - [ ] Know the default priority of a job that is created.
            - [ ] Run a program with higher or lower priority than the default.
            - [ ] Change the priority of a running process. 
        - [ ] Search text files using regular expressions: grep, egrep, fgrep, sed, regex(7)...
            - Candidates should be able to manipulate files and text data using regular expressions. This objective includes creating simple regular expressions containing several notational elements as well as understanding the differences between basic and extended regular expressions. It also includes using regular expression tools to perform searches through a filesystem or file content. 
            - [ ] Create simple regular expressions containing several notational elements.
            - [ ] Understand the differences between basic and extended regular expressions.
            - [ ] Understand the concepts of special characters, character classes, quantifiers and anchors.
            - [ ] Use regular expression tools to perform searches through a filesystem or file content.
            - [ ] Use regular expressions to delete, change and substitute text.
        - [ ] Basic file editing: vi, /, ?, h, j, k, l, i, o, a, d, p, y, dd, yy, ZZ, :w!, :q!, EDITOR...
            - Candidates should be able to edit text files using vi. This objective includes vi navigation, vi modes, inserting, editing, deleting, copying and finding text. It also includes awareness of other common editors and setting the default editor. 
            - [ ] Navigate a document using vi.
            - [ ] Understand and use vi modes.
            - [ ] Insert, edit, delete, copy and find text in vi.
            - [ ] Awareness of Emacs, nano and vim.
            - [ ] Configure the standard editor.
    - Devices, Linux Filesystems, Filesystem Hierarchy Standard:
        - [ ] Create partitions and filesystems: fdisk, gdisk, parted, mkfs, mkswap...
            - Candidates should be able to configure disk partitions and then create filesystems on media such as hard disks. This includes the handling of swap partitions. 
            - [ ] Manage MBR and GPT partition tables
            - [ ] Use various mkfs commands to create various filesystems such as: ext2/ext3/ext4, XFS, VFAT, exFAT. 
            - [ ] Basic feature knowledge of Btrfs, including multi-device filesystems, compression and subvolumes.
        - [ ] Maintain the integrity of filesystems: du, df, fsck, e2fsck, mke2fs, tune2fs, xfs_repair, xfs_fsr, xfs_db...
            - Candidates should be able to maintain a standard filesystem, as well as the extra data associated with a journaling filesystem. 
            - [ ] Verify the integrity of filesystems.
            - [ ] Monitor free space and inodes.
            - [ ] Repair simple filesystem problems. 
        - [ ] Control mounting and unmounting of filesystems: /etc/fstab, /media/, mount, umount, blkid, lsblk...
            - Candidates should be able to configure the mounting of a filesystem. 
            - [ ] Manually mount and unmount filesystems.
            - [ ] Configure filesystem mounting on bootup.
            - [ ] Configure user mountable removable filesystems.
            - [ ] Use of labels and UUIDs for identifying and mounting file systems.
            - [ ] Awareness of systemd mount units.
        - [ ] REMOVED
        - [ ] Manage file permissions and ownership: chmod, umask, chown, chgrp...
            - Candidates should be able to control file access through the proper use of permissions and ownerships. 
            - [ ] Manage access permissions on regular and special files as well as directories.
            - [ ] Use access modes such as suid, sgid and the sticky bit to maintain security.
            - [ ] Know how to change the file creation mask.
            - [ ] Use the group field to grant file access to group members. 
        - [ ] Create and change hard and symbolic links: ln, ls...
            - Candidates should be able to create and manage hard and symbolic links to a file. 
            - [ ] Create links.
            - [ ] Identify hard and/or soft links.
            - [ ] Copying versus linking files.
            - [ ] Use links to support system administration tasks.
        - [ ] Find system files and place files in the correct location: find, locate, updatedb, whereis, which, type, /etc/updatedb.conf...
            - Candidates should be thoroughly familiar with the Filesystem Hierarchy Standard (FHS), including typical file locations and directory classifications. 
            - [ ] Understand the correct locations of files under the FHS.
            - [ ] Find files and commands on a Linux system.
            - [ ] Know the location and purpose of important file and directories as defined in the FHS. 
    - Shells and Shell Scripting:
        - [ ] Customize and use the shell environment: ., source, /etc/bash.bashrc, /etc/profile, env, export, set, unset, ~/.bash_profile, ~/.bash_login, ~/.profile, ~/lbashrc, ~/.bash_logout, function, alias...
            - Candidates should be able to customize shell environments to meet users' needs. Candidates should be able to modify global and user profiles. 
            - [ ] Set environment variables (e.g. PATH) at login or when spawning a new shell.
            - [ ] Write Bash functions for frequently used sequences of commands.
            - [ ] Maintain skeleton directories for new user accounts.
            - [ ] Set command search path with the proper directory. 
        - [ ] Customize or write simple scripts: for, while, test, if, read, seq, exec, ||, &&...
            - Candidates should be able to customize existing scripts, or write simple new Bash scripts. 
            - [ ] Use standard sh syntax (loops, tests).
            - [ ] Use command substitution.
            - [ ] Test return values for success or failure or other information provided by a command.
            - [ ] Execute chained commands.
            - [ ] Perform conditional mailing to the superuser.
            - [ ] Correctly select the script interpreter through the shebang (#!) line.
            - [ ] Manage the location, ownership, execution and suid-rights of scripts. 
    - Interfaces and Desktops:
        - [ ] Install and configure X11:

        - [ ] Graphical Desktops:

        - [ ] Accessibility:

    - Administrative Tasks:
        - [ ] Manage user and group accounts and related system files:

        - [ ] Automate system administration tasks by scheduling jobs:

        - [ ] Localisation and internationalisation:

    - Essential System Services:
        - [ ] Maintain system time:

        - [ ] System logging:

        - [ ] Mail Transfer Agent (MTA) basics:

        - [ ] Manage printers and printing:

    - Networking Fundamentals:
        - [ ] Fundamentals of internet protocols:

        - [ ] Persistent network configuration:

        - [ ] Basic network troubleshooting:

        - [ ] Configure client side DNS:

    - Security:
        - [ ] Perform security administration tasks:

        - [ ] Setup host security:

        - [ ] Securing data with encryption:

    - [LPIC-1 Exam 101 and 102 Objectives](https://www.lpi.org/our-certifications/exam-101-102-objectives/) 















