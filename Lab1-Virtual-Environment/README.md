# Lab 1: Virtual Environment Setup

## Objective
Set up a virtualized lab environment on macOS (Apple Silicon) using UTM to host Windows 11 and Ubuntu Linux VMs for IT administration practice.

## Tools Used
- UTM (virtualization for Apple Silicon)
- Windows 11 ARM
- Ubuntu 22.04 LTS ARM (pre built UTM image)

## Steps

### 1.1 - UTM Installation
- Downloaded and installed UTM on macOS (Apple Silicon M-series)
- Selected UTM over VirtualBox due to Apple Silicon ARM64 compatibility

### 1.2 - Windows 11 ARM VM
- Created new VM: Virtualize > Windows
- Specs: 4 GB RAM, 4 CPU cores, 64 GB storage
- Installed from Win11_25H2_English_Arm64.iso
- Resolved UEFI boot issue by navigating Boot Manager to select correct boot device
- Installed UTM Guest Tools for clipboard sharing and display improvements
- Created clean backup clone of VM before making changes

### 1.3 - Ubuntu ARM VM
- Imported pre built Ubuntu 22.04 ARM .utm image
- Specs: 4 GB RAM, 4 CPU cores, 32 GB storage
- Updated system packages via sudo apt update && sudo apt upgrade -y
- Resolved kernel version mismatch by rebooting after updates

### 1.4 - Network Configuration
- Both VMs configured with UTM Shared Network (virtio-net-pci)
- Verified internet connectivity on both VMs
- Windows 11 IP: DHCP assigned (192.168.64.x range)
- Ubuntu IP: 192.168.64.4

## Troubleshooting
- **UEFI Shell on boot:** Resolved by using Boot Manager to select correct boot device instead of defaulting to UEFI shell
- **Windows installer loading on reboot:** Cleared ISO from virtual CD/DVD drive to prevent 
re entering installer

## Skills Demonstrated
- Virtual machine creation and configuration on Apple Silicon
- Resource allocation (CPU, RAM, storage)
- VM cloning for backup/recovery
- Multi OS environment setup (Windows + Linux)
- Boot troubleshooting (UEFI)