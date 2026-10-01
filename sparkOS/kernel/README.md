# SparkOS bootable image foundation

SparkOS targets x86_64 Chromebooks. The image layout contains an EFI System Partition, SparkOS system partition, and separate recovery partition.

systemd-boot can load Linux EFI-stub kernels and UKIs from the ESP. UKIs combine the kernel and initrd into one EFI executable. citeturn0search0turn0search1

This repository now contains the image layout and staging scripts. A final hardware image still needs a kernel/configuration matched to the exact Chromebook board.
