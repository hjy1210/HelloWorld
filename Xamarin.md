# Visual Studio 2015 + Xamarin

In Visual Studio 2015, Xamarin.Forms portable template can generate .Android, .Ios and .UMP projects.

Hyper-V is Microsoft’s virtualisation solution that can be installed with Windows. 
Visual Studio device emulators for Windows 10 Mobile rely on Hyper-V for the guest system. 
While this may work in most cases, it has the major disadvantage that Hyper-V is running permanently when installed, 
unlike application hypervisors like VMware or VirtualBox.

So we have:
* .Ios project need Mac machine
* .Android project with Android emulator need Hyper-V deactivated.
* .UMP project with Windows Phone emulator need Hyper-V activated.
* .UMP project with local machine always work in any status of Hyper-V.

## HyperVSwitch
We can execute [HyperVSwitch.exe](https://unclassified.software/en/apps/hypervswitch) as administrator to switch Hyper-V on/off.

Note: It need reboot computer after switching Hyper-V.

## bcdedit command
* Use command `bcdedit /set hypervisorlaunchtype off` to turn off Hyper-V
* Use `bcdedit /set hypervisorlaunchtype auto` to turn on Hyper-V

Note: HyperVSwitch is better than bcdedit, because we can first see current status of Hyper-V then decide is it need change.

## With Hyper-V Activated
We can execute in
* .UMP project with local machine.
* .UMP project with Mobile emulator 10.0.14393 series.

Can **NOT** execute in
* .UMP project with Windows Mobile emulator 10.0.15063 series(why?)
* .Android project with Android emulators

## With Hyper-V Dectivated
We can execute in
* .UMP project with local machine
* .Android project Android emulators

Can **NOT** execute in
* .UMP project with Windows Mobile emulators
