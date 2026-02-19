---
topic_id: 38564
title: "M3 Pro Catastrophic Crash In Volume Rendering"
date: 2024-09-27
url: https://discourse.slicer.org/t/38564
---

# M3 Pro catastrophic crash in volume rendering

**Topic ID**: 38564
**Date**: 2024-09-27
**URL**: https://discourse.slicer.org/t/m3-pro-catastrophic-crash-in-volume-rendering/38564

---

## Post #1 by @muratmaga (2024-09-27 01:03 UTC)

<p>I have this largish dataset (~3.8GB) that I loaded into the Slicer 5.6.2 on my M3 Pro mac. When I dragged the volume from data module to the 3D viewer, Slicer catastrophically crashed and actually caused my Mac to reboot (below is the crash log from MacOS, second log).</p>
<p>After the reboot, I tried one more time. This time Slicer briefly displayed the volume, then crashed again. However, it did not take the computer down. Below is the error from Slicer from that session.</p>
<p><strong>Update:</strong> Now that I tried a few times, I can reproduce the catastrophic crash when I set the volume rendering quality to adaptive. Sometimes the crash is immediate, the moment rendering is loaded, sometime a little delayed. Normal seems to work fine. I am going to upload the dataset and share the link shortly.</p>
<p>Slicer Error from the crash.</p>
<pre><code class="lang-auto">[CRITICAL][FD] 26.09.2024 17:44:34 [] (unknown:0) - 2024-09-26 17:44:34.519 Slicer[1179:18708] GLDRendererMetal command buffer completion error: Error Domain=MTLCommandBufferErrorDomain Code=2 "Caused GPU Hang Error (00000003:kIOGPUCommandBufferCallbackErrorHang)" UserInfo={NSLocalizedDescription=Caused GPU Hang Error (00000003:kIOGPUCommandBufferCallbackErrorHang), NSUnderlyingError=0x6000009d0ab0 {Error Domain=IOGPUCommandQueueErrorDomain Code=3 "(null)"}}
</code></pre>
<p>Crashlog from MacOS</p>
<pre><code class="lang-auto">Attempting to forcibly halt cpu 1
cpu 1 failed to halt with error -5: halt not supported for this configuration
Debugger synchronization timed out; waited 240000 nanoseconds
panic(cpu 0 caller 0xfffffe0011f15674): WDT timeout: CPU 1 failed to respond
Debugger message: panic
Memory ID: 0xff
OS release type: User
OS version: 23G93
Kernel version: Darwin Kernel Version 23.6.0: Mon Jul 29 21:14:30 PDT 2024; root:xnu-10063.141.2~1/RELEASE_ARM64_T6030
Fileset Kernelcache UUID: 7A75AB37BBCA71CC5E90FA0EC90FCB46
Kernel UUID: DF5E3A0A-B57A-3C8E-B38F-4262F03E4D1C
Boot session UUID: D1094E07-EC17-4CAB-ABC2-964162C2A70D
iBoot version: iBoot-10151.140.19
secure boot?: YES
roots installed: 0
Paniclog version: 14
KernelCache slide: 0x0000000008f6c000
KernelCache base:  0xfffffe000ff70000
Kernel slide:      0x0000000008f74000
Kernel text base:  0xfffffe000ff78000
Kernel text exec slide: 0x000000000a4c0000
Kernel text exec base:  0xfffffe00114c4000
mach_absolute_time: 0x1eff9a4d0eb3
Epoch Time:        sec       usec
  Boot    : 0x66dbb9c5 0x000bcc69
  Sleep   : 0x66f5fba3 0x000d8cc8
  Wake    : 0x66f5fbad 0x0007e1bf
  Calendar: 0x66f5fe15 0x000dc566

Zone info:
  Zone map: 0xfffffe100d01c000 - 0xfffffe300d01c000
  . VM    : 0xfffffe100d01c000 - 0xfffffe14d9ce8000
  . RO    : 0xfffffe14d9ce8000 - 0xfffffe1673680000
  . GEN0  : 0xfffffe1673680000 - 0xfffffe1b4034c000
  . GEN1  : 0xfffffe1b4034c000 - 0xfffffe200d018000
  . GEN2  : 0xfffffe200d018000 - 0xfffffe24d9ce4000
  . GEN3  : 0xfffffe24d9ce4000 - 0xfffffe29a69b0000
  . DATA  : 0xfffffe29a69b0000 - 0xfffffe300d01c000
  Metadata: 0xfffffe39f06ec000 - 0xfffffe39f86ec000
  Bitmaps : 0xfffffe39f86ec000 - 0xfffffe39feffc000
  Extra   : 0 - 0

CORE 0 recently retired instr at 0xfffffe001166dbf8
CORE 1 recently retired instr at 0xfffffe0011d62328
CORE 2 recently retired instr at 0xfffffe001166f32c
CORE 3 recently retired instr at 0xfffffe001166f32c
CORE 4 recently retired instr at 0xfffffe001166f32c
CORE 5 recently retired instr at 0xfffffe001166f32c
CORE 6 recently retired instr at 0xfffffe001166f32c
CORE 7 recently retired instr at 0xfffffe001166f32c
CORE 8 recently retired instr at 0xfffffe001166f32c
CORE 9 recently retired instr at 0xfffffe001166f32c
CORE 10 recently retired instr at 0xfffffe001166f32c
CORE 11 recently retired instr at 0xfffffe001166f32c
TPIDRx_ELy = {1: 0xfffffe200cf9cfd0  0: 0x0000000000000000  0ro: 0x0000000000000000 }
CORE 0 PVH locks held: None
CORE 1 PVH locks held: None
CORE 2 PVH locks held: None
CORE 3 PVH locks held: None
CORE 4 PVH locks held: None
CORE 5 PVH locks held: None
CORE 6 PVH locks held: None
CORE 7 PVH locks held: None
CORE 8 PVH locks held: None
CORE 9 PVH locks held: None
CORE 10 PVH locks held: None
CORE 11 PVH locks held: None
CORE 0 is the one that panicked. Check the full backtrace for details.
CORE 1: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b7fe63ef0
CORE 2: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b7f677ef0
CORE 3: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b7f443ef0
CORE 4: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b7f36bef0
CORE 5: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b804e7ef0
CORE 6: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b7f95fef0
CORE 7: PC=0xfffffe00115561bc, LR=0xfffffe00115561b8, FP=0xfffffe8b7f527ef0
CORE 8: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b80743ef0
CORE 9: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b7f7ebef0
CORE 10: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b8008fef0
CORE 11: PC=0xfffffe00115561b8, LR=0xfffffe00115561b8, FP=0xfffffe8b7ffb3ef0
Compressor Info: 2% of compressed pages limit (OK) and 3% of segments limit (OK) with 2 swapfiles and OK swap space
Total cpu_usage: 52298211
Thread task pri cpu_usage
0xfffffe200ad3a7a8 kernel_task 81 463
0xfffffe200cf9cfd0 kernel_task 0 4926273
0xfffffe200cd807c8 kernel_task 0 0
0xfffffe200cd827e8 kernel_task 0 5065505
0xfffffe200cd7cf90 kernel_task 0 5500025

Panicked task 0xfffffe24d9dec9e0: 0 pages, 589 threads: pid 0: kernel_task
Panicked thread: 0xfffffe200cf9cfd0, backtrace: 0xfffffe39cc6c38d0, tid: 596
		  lr: 0xfffffe001151c124  fp: 0xfffffe39cc6c3960
		  lr: 0xfffffe0011666358  fp: 0xfffffe39cc6c39d0
		  lr: 0xfffffe001166476c  fp: 0xfffffe39cc6c3a90
		  lr: 0xfffffe00114cb8cc  fp: 0xfffffe39cc6c3aa0
		  lr: 0xfffffe001151ba18  fp: 0xfffffe39cc6c3e50
		  lr: 0xfffffe0011d204cc  fp: 0xfffffe39cc6c3e70
		  lr: 0xfffffe0011f15674  fp: 0xfffffe39cc6c3e90
		  lr: 0xfffffe0011f11e20  fp: 0xfffffe39cc6c3f00
		  lr: 0xfffffe0011f119e4  fp: 0xfffffe39cc6c3f20
		  lr: 0xfffffe00128c57b8  fp: 0xfffffe39cc6c3fc0
		  lr: 0xfffffe0011667ca0  fp: 0xfffffe39cc6c3fe0
		  lr: 0xfffffe00114cb940  fp: 0xfffffe39cc6c3ff0
		  lr: 0xfffffe00115561b8  fp: 0xfffffe8b80083ef0
		  lr: 0xfffffe00115563d0  fp: 0xfffffe8b80083f20
		  lr: 0xfffffe00114d58a4  fp: 0x0000000000000000
      Kernel Extensions in backtrace:
         com.apple.driver.AppleInterruptControllerV3(1.0d1)[34C105A1-89B4-36D5-9981-25302EFBF1FC]@0xfffffe00128c2880-&gt;0xfffffe00128c6a57
            dependency: com.apple.driver.AppleARMPlatform(1.0.2)[44EAEE3D-751F-3A0B-9AE3-99173AA796CC]@0xfffffe0011ebbf60-&gt;0xfffffe0011f10103
         com.apple.driver.AppleARMWatchdogTimer(1.0)[1C56DCEF-1A8F-3617-B865-D1AE918AB892]@0xfffffe0011f10110-&gt;0xfffffe0011f158b3
            dependency: com.apple.driver.AppleARMPlatform(1.0.2)[44EAEE3D-751F-3A0B-9AE3-99173AA796CC]@0xfffffe0011ebbf60-&gt;0xfffffe0011f10103

last started kext at 33860548825735: com.apple.driver.usb.AppleUSBHostBillboardDevice	1.0 (addr 0xfffffe001086b830, size 2576)
loaded kexts:
com.apple.driver.usb.AppleUSBHostBillboardDevice	1.0
com.apple.filesystems.smbfs	5.1
com.apple.filesystems.autofs	3.0
com.apple.UVCService	1
com.apple.iokit.SCSITaskUserClient	495
com.apple.driver.AppleUSBMassStorageInterfaceNub	556
com.apple.driver.AppleTopCaseHIDEventDriver	7440.8
com.apple.driver.AppleBiometricServices	1
com.apple.driver.CoreKDL	1
com.apple.driver.AppleALSColorSensor	1.0.0d1
com.apple.driver.AppleAOPVoiceTrigger	340.42
com.apple.driver.BCMWLANFirmware4388.Hashstore	1
com.apple.driver.BCMWLANFirmware4387.Hashstore	1
com.apple.driver.BCMWLANFirmware4378.Hashstore	1
com.apple.driver.DiskImages.ReadWriteDiskImage	493.0.0
com.apple.driver.DiskImages.UDIFDiskImage	493.0.0
com.apple.driver.DiskImages.RAMBackingStore	493.0.0
com.apple.driver.DiskImages.FileBackingStore	493.0.0
com.apple.driver.AppleFileSystemDriver	3.0.1
com.apple.driver.AppleThunderboltIP	4.0.3
com.apple.driver.AppleUSBDeviceNCM	5.0.0
com.apple.nke.l2tp	1.9
com.apple.filesystems.tmpfs	1
com.apple.filesystems.nfs	1
com.apple.filesystems.lifs	1
com.apple.filesystems.apfs	2236.141.1
com.apple.IOTextEncryptionFamily	1.0.0
com.apple.filesystems.hfs.kext	650.140.2
com.apple.security.BootPolicy	1
com.apple.BootCache	40
com.apple.AppleFSCompression.AppleFSCompressionTypeZlib	1.0.0
com.apple.AppleFSCompression.AppleFSCompressionTypeDataless	1.0.0d1
com.apple.driver.AppleProResHW	350.47.0
com.apple.driver.AppleAVE2	760.31.1
com.apple.driver.AudioDMAController-T6030	350.2
com.apple.driver.AppleSmartIO2	1
com.apple.driver.AppleSmartBatteryManager	161.0.0
com.apple.AppleEmbeddedSimpleSPINORFlasher	1
com.apple.driver.AppleCS42L84Audio	740.41
com.apple.driver.AppleJPEGDriver	6.6.2
com.apple.driver.SEPHibernation	1
com.apple.driver.AppleMobileDispT603S-DCP	140.0
com.apple.driver.AppleAVD	743
com.apple.driver.AppleTypeCRetimer	1.0.0
com.apple.driver.ApplePMP	1
com.apple.driver.AppleSN012776Amp	740.41
com.apple.driver.AppleT6030SOCTuner	1
com.apple.driver.AppleT6030CLPC	1
com.apple.AGXG15S	282.14
com.apple.driver.AppleSerialShim	1
com.apple.driver.usb.AppleSynopsysUSB40XHCI	1
com.apple.driver.ApplePMPFirmware	1
com.apple.driver.AppleDPDisplayTCON	1
com.apple.driver.AppleEventLogHandler	1
com.apple.driver.AppleS5L8960XNCO	1
com.apple.driver.AppleT6030PMGR	1
com.apple.driver.AppleS8000AES	1
com.apple.driver.AppleS8000DWI	1.0.0d1
com.apple.driver.AppleInterruptControllerV3	1.0.0d1
com.apple.driver.AppleBluetoothModule	1
com.apple.driver.AppleSamsungSerial	1.0.0d1
com.apple.driver.AppleBCMWLANBusInterfacePCIe	1
com.apple.driver.AppleT8110DART	1
com.apple.driver.AppleS5L8920XPWM	1.0.0d1
com.apple.driver.AppleS5L8940XI2C	1.0.0d2
com.apple.driver.AppleSPIMC	1
com.apple.driver.AppleT6030	1
com.apple.driver.AppleSDXC	3.5.2
com.apple.driver.AppleM68Buttons	1.0.0d1
com.apple.iokit.IOUserEthernet	1.0.1
com.apple.driver.usb.AppleUSBUserHCI	1
com.apple.iokit.IOKitRegistryCompatibility	1
com.apple.iokit.EndpointSecurity	1
com.apple.driver.AppleUIO	1
com.apple.driver.AppleDiskImages2	276.120.7
com.apple.AppleSystemPolicy	2.0.0
com.apple.nke.applicationfirewall	405
com.apple.kec.InvalidateHmac	1
com.apple.kec.AppleEncryptedArchive	1
com.apple.driver.AppleUVDMDriver	1.0.0
com.apple.driver.AppleUVDM	1.0.0
com.apple.driver.driverkit.serial	6.0.0
com.apple.iokit.IOAVBFamily	1220.1
com.apple.driver.usb.IOUSBHostHIDDevice	1.2
com.apple.driver.usb.cdc	5.0.0
com.apple.driver.AppleUSBAudio	640.12
com.apple.iokit.IOAudioFamily	540.3
com.apple.vecLib.kext	1.2.0
com.apple.driver.AppleHSBluetoothDriver	7440.8
com.apple.driver.IOBluetoothHIDDriver	9.0.0
com.apple.driver.AppleHIDKeyboard	7440.3
com.apple.driver.AppleActuatorDriver	7440.9
com.apple.driver.AppleMultitouchDriver	7440.9
com.apple.driver.AppleMesaSEPDriver	100.99
com.apple.iokit.IOBiometricFamily	1
com.apple.driver.AppleAOPAudio	340.4
com.apple.driver.DiskImages.KernelBacked	493.0.0
com.apple.driver.AppleXsanScheme	3
com.apple.driver.usb.networking	5.0.0
com.apple.driver.AppleThunderboltUSBDownAdapter	1.0.4
com.apple.driver.AppleThunderboltPCIDownAdapter	4.1.1
com.apple.driver.AppleThunderboltDPInAdapter	8.5.1
com.apple.driver.AppleThunderboltDPAdapterFamily	8.5.1
com.apple.nke.ppp	1.9
com.apple.driver.AppleBSDKextStarter	3
com.apple.kext.triggers	1.0
com.apple.filesystems.hfs.encodings.kext	1
com.apple.driver.AppleSyntheticGameController	11.6.1
com.apple.AGXFirmwareKextG15SRTBuddy	1
com.apple.AGXFirmwareKextRTBuddy64	282.14
com.apple.plugin.IOgPTPPlugin	1240.15
com.apple.driver.AppleConvergedIPCOLYBTControl	1
com.apple.driver.AppleConvergedPCI	1
com.apple.driver.AppleBluetoothDebug	1
com.apple.driver.AppleBTM	1.0.1
com.apple.driver.IOHIDPowerSource	1
com.apple.driver.AppleCallbackPowerSource	1
com.apple.driver.AppleHPM	3.4.4
com.apple.driver.AppleDCPDPTXProxy	1.0.0
com.apple.driver.DCPDPFamilyProxy	1
com.apple.driver.AppleDiagnosticDataAccessReadOnly	1.0.0
com.apple.driver.AppleCSEmbeddedAudio	740.41
com.apple.driver.AppleStockholmControl	1.0.0
com.apple.driver.AppleTrustedAccessory	1
com.apple.iokit.AppleSEPGenericTransfer	1
com.apple.iokit.IOMobileGraphicsFamily-DCP	343.0.0
com.apple.iokit.IOMobileGraphicsFamily	343.0.0
com.apple.driver.AppleM2ScalerCSCDriver	265.0.0
com.apple.driver.AppleH13CameraInterface	8.701.0
com.apple.driver.AppleSEPHDCPManager	1.0.1
com.apple.driver.AppleH11ANEInterface	7.453.0
com.apple.driver.AppleDCP	1
com.apple.driver.DCPAVFamilyProxy	1
com.apple.driver.AppleEmbeddedAudio	740.41
com.apple.iokit.AppleARMIISAudio	340.16
com.apple.driver.IISAudioIsolatedStreamECProxy	340.16
com.apple.driver.ExclavesAudioKext	1
com.apple.driver.ApplePassthroughPPM	3.0
com.apple.iokit.IOGPUFamily	93.40.3
com.apple.driver.AppleUSBXDCIARM	1.0
com.apple.driver.AppleUSBXDCI	1.0
com.apple.iokit.IOUSBDeviceFamily	2.0.0
com.apple.driver.usb.AppleSynopsysUSBXHCI	1
com.apple.driver.usb.AppleUSBXHCI	1.2
com.apple.driver.AppleEmbeddedUSBHost	1
com.apple.driver.usb.AppleUSBHub	1.2
com.apple.driver.usb.AppleUSBHostCompositeDevice	1.2
com.apple.driver.AppleT8122TypeCPhy	1
com.apple.driver.AppleSPMIPMU	1.0.1
com.apple.driver.AppleDialogPMU	1.0.1
com.apple.driver.AppleSPMI	1.0.1
com.apple.driver.AppleFirmwareKit	1
com.apple.iokit.IONVMeFamily	2.1.0
com.apple.driver.AppleNANDConfigAccess	1.0.0
com.apple.driver.AppleHIDTransportFIFO	7440.1
com.apple.driver.AppleHIDTransport	7440.1
com.apple.driver.AppleSPU	1
com.apple.driver.AppleInputDeviceSupport	7440.1
com.apple.driver.AppleDockChannel	1
com.apple.driver.AppleSART	1
com.apple.driver.ApplePMGR	1
com.apple.driver.AppleA7IOP-ASCWrap-v6	1.0.2
com.apple.driver.AppleARMWatchdogTimer	1
com.apple.driver.AppleMobileApNonce	1
com.apple.driver.AppleDisplayCrossbar	1.0.0
com.apple.iokit.IODisplayPortFamily	1.0.0
com.apple.driver.AppleTypeCPhy	1
com.apple.driver.AppleThunderboltNHI	7.2.81
com.apple.driver.AppleT8122PCIeC	1
com.apple.iokit.IOThunderboltFamily	9.3.3
com.apple.iokit.IOPortFamily	1.0
com.apple.driver.ApplePIODMA	1
com.apple.driver.AppleA7IOP-MXWrap-v1	1.0.2
com.apple.driver.AppleT6030PCIe	1
com.apple.driver.AppleMultiFunctionManager	1
com.apple.driver.AppleBluetoothDebugService	1
com.apple.driver.AppleBCMWLANCore	1.0.0
com.apple.iokit.IO80211Family	1200.13.0
com.apple.driver.IOImageLoader	1.0.0
com.apple.driver.AppleOLYHAL	1
com.apple.driver.corecapture	1.0.4
com.apple.driver.AppleMCA2-T6030	840.3
com.apple.driver.AppleEmbeddedAudioLibs	340.8
com.apple.driver.AppleFirmwareUpdateKext	1
com.apple.driver.AppleGPIOICController	1.0.2
com.apple.driver.AppleEverestErrorHandler	1
com.apple.driver.AppleEmbeddedPCIE	1
com.apple.driver.usb.AppleUSBHostPacketFilter	1.0
com.apple.iokit.IOTimeSyncFamily	1240.15
com.apple.driver.DiskImages	493.0.0
com.apple.iokit.IOGraphicsFamily	598
com.apple.iokit.IOBluetoothFamily	9.0.0
com.apple.driver.AppleT6030ANEHAL	7.453.0
com.apple.driver.AppleSSE	1.0
com.apple.driver.AppleSEPKeyStore	2
com.apple.driver.AppleUSBTDM	556
com.apple.iokit.IOUSBMassStorageDriver	245
com.apple.iokit.IOPCIFamily	2.9
com.apple.iokit.IOUSBHostFamily	1.2
com.apple.driver.AppleUSBHostMergeProperties	1.2
com.apple.driver.usb.AppleUSBCommon	1.0
com.apple.driver.AppleSMC	3.1.9
com.apple.driver.RTBuddy	1.0.0
com.apple.driver.AppleEmbeddedTempSensor	1.0.0
com.apple.driver.AppleARMPMU	1.0
com.apple.iokit.IOAccessoryManager	1.0.0
com.apple.driver.AppleOnboardSerial	1.0
com.apple.iokit.IOSerialFamily	11
com.apple.iokit.IOSCSIBlockCommandsDevice	495
com.apple.iokit.IOSCSIArchitectureModelFamily	495
com.apple.driver.AppleRSMChannel	1
com.apple.iokit.IORSMFamily	1
com.apple.driver.AppleLockdownMode	1
com.apple.driver.AppleIPAppender	1.0
com.apple.iokit.IOSkywalkFamily	1.0
com.apple.driver.mDNSOffloadUserClient	1.0.1b8
com.apple.iokit.IONetworkingFamily	3.4
com.apple.driver.AppleFDEKeyStore	28.30
com.apple.driver.AppleEffaceableStorage	1.0
com.apple.driver.AppleCredentialManager	1.0
com.apple.driver.AppleSEPManager	1.0.1
com.apple.driver.IODARTFamily	1
com.apple.driver.AppleA7IOP	1.0.2
com.apple.driver.IOSlaveProcessor	1
com.apple.driver.AppleBiometricSensor	2
com.apple.iokit.IOHIDFamily	2.0.0
com.apple.AUC	1.0
com.apple.iokit.IOSurface	352.50.1
com.apple.iokit.IOAVFamily	1.0.0
com.apple.iokit.IOHDCPFamily	1.0.0
com.apple.iokit.IOCECFamily	1
com.apple.iokit.IOAudio2Family	1.0
com.apple.driver.AppleIISController	340.1
com.apple.driver.AppleAudioClockLibs	340.8
com.apple.driver.FairPlayIOKit	71.10.0
com.apple.driver.AppleARMPlatform	1.0.2
com.apple.iokit.IOSlowAdaptiveClockingFamily	1.0.0
com.apple.iokit.IOReportFamily	47
com.apple.security.quarantine	4
com.apple.security.sandbox	300.0
com.apple.iokit.IOStorageFamily	2.1
com.apple.kext.AppleMatch	1.0.0d1
com.apple.driver.AppleMobileFileIntegrity	1.0.5
com.apple.iokit.CoreAnalyticsFamily	1
com.apple.security.AppleImage4	6.3.0
com.apple.kext.CoreTrust	1
com.apple.iokit.IOCryptoAcceleratorFamily	1.0.1
com.apple.kec.pthread	1
com.apple.kec.Libm	1
com.apple.kec.Compression	1.0
com.apple.kec.corecrypto	14.0


!! debugger synchronization failed, no stackshot !!
</code></pre>

---

## Post #2 by @muratmaga (2024-09-27 01:16 UTC)

<p>Here is the link to the NRRD:<br>
<a href="https://js2.jetstream-cloud.org:8001/swift/v1/SampleData/Crash/turbinates__rec00000012.nrrd" class="onebox" target="_blank" rel="noopener nofollow ugc">https://js2.jetstream-cloud.org:8001/swift/v1/SampleData/Crash/turbinates__rec00000012.nrrd</a></p>
<p>if the catastrophic crash replicates for others, perhaps we may need to disable Adaptive setting in MacOS with apple silicon (given how serious it is).</p>

---

## Post #3 by @lassoan (2024-09-27 12:16 UTC)

<p>This sounds like a driver/operating system/rosetta bug. There should be no way an application could ever be able to bring down the operating system. If an application reaches resource limits or violates some rules then worst case the operating system may close the process. Probably Apple is already aware of this issue and working on a solution, but to make sure that they know the frequency and impact, it could be nice if you reported this issue to them.</p>
<p>There is a good chance that native ARM builds will be more robust, so I would not spend too much time investigating this, but rather work towards creating an ARM build of Slicer and see if the problem is still reproducible.</p>
<p>Until then, if you have any simple workaround then we can implement it. For example, if it looks like a widespread universal problem on macOS on ARM that volume rendering crashes with adaptive option enabled then we could disable it. It would be nice to test it on several systems, with different settings (shadows enabled/disabled, different volume sizes, on latest Slicer Preview Release) to make sure we minimize the scope of the workaround.</p>
<details>
<summary>
C++ code for detecting if running on ARM</summary>
<p>Non-tested code for detecting the executable is running on macOS on ARM:</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">#include &lt;iostream&gt;
#include &lt;sys/sysctl.h&gt;

bool isRunningUnderRosetta() {
    int isTranslated = 0;
    size_t size = sizeof(isTranslated);
    int result = sysctlbyname("sysctl.proc_translated", &amp;isTranslated, &amp;size, nullptr, 0);
    return result == 0 &amp;&amp; isTranslated != 0;
}

int main() {
    if (isRunningUnderRosetta()) {
        // Change behavior for Rosetta
        std::cout &lt;&lt; "Running under Rosetta" &lt;&lt; std::endl;
    } else {
        // Normal behavior
        std::cout &lt;&lt; "Running natively" &lt;&lt; std::endl;
    }
    return 0;
}
</code></pre>
</details>

---

## Post #4 by @muratmaga (2024-09-27 14:35 UTC)

<p>I only have one arm Mac, and it does reproduce fairly consistently. if others can give it a try with the sample data, we might understand whether it is unique to my mac OS (Sonoma) and driver, or maybe more widespread.</p>

---

## Post #5 by @muratmaga (2024-09-28 02:31 UTC)

<p>Did anyone has a chance to try?</p>

---

## Post #6 by @chir.set (2024-09-28 06:31 UTC)

<p>I loaded the volume on a desktop PC with AMD Radeon 6700 XT, and on a laptop with a discrete AMD Radeon RX 7600M XT card; ‘Volume rendering’ could not produce a 3D view in both cases, with this message :</p>
<blockquote>
<p>[VTK] Capabilities check via proxy texture 3D allocation failed!</p>
</blockquote>
<p>The Linux boxes did not crash, Slicer neither.</p>

---

## Post #7 by @muratmaga (2024-09-28 18:39 UTC)

<p>Thanks <a class="mention" href="/u/chir.set">@chir.set</a>. I am fairly certain this is unique to Apple silicon. It doesn’t even replicate on my intel mac.</p>

---

## Post #8 by @hherhold (2024-09-29 13:09 UTC)

<p>Maybe 3D texture dimension limits in the (deprecated) OpenGL implementation for Apple silicon are too small for this volume? Shouldn’t panic the kernel, though, as <a class="mention" href="/u/lassoan">@lassoan</a> mentioned.</p>

---

## Post #9 by @muratmaga (2024-09-29 16:08 UTC)

<p>Maximum dimension is only 1900 voxels. Everything works fine with (rendering, interactivity) Normal quality setting.</p>

---

## Post #10 by @hherhold (2024-09-29 16:21 UTC)

<p>Oops, yeah, I probably should have downloaded the data and looked at it before posting… that’s what I get for my first post in a long time, and before coffee.</p>

---

## Post #11 by @pieper (2024-10-01 22:20 UTC)

<p>I tried this on a MacBook Air M2 with 8GB memory.  I was able to volume render with the GPU renderer in Adaptive and Normal modes.  In Maximum mode it crashed Slicer after printing the message below.  The Activity Monitor showed it was using all 8GB and swap.  My machine did not crash, just Slicer crashed and everything else is normal.</p>
<pre><code class="lang-auto">2024-10-01 16:00:50.497 Slicer[16088:44830565] GLDRendererMetal command buffer completion error: Error Domain=MTLCommandBufferErrorDomain Code=2 "Caused GPU Hang Error (00000003:kIOGPUCommandBufferCallbackErrorHang)" UserInfo={NSLocalizedDescription=Caused GPU Hang Error (00000003:kIOGPUCommandBufferCallbackErrorHang), NSUnderlyingError=0x60000240ea00 {Error Domain=IOGPUCommandQueueErrorDomain Code=3 "(null)"}}
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e346b45fbdf222871345f006a3ced47e512f063f.jpeg" data-download-href="/uploads/short-url/wqzRV0nuSKOhNUPCRWsTev8rZmL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e346b45fbdf222871345f006a3ced47e512f063f_2_289x500.jpeg" alt="image" data-base62-sha1="wqzRV0nuSKOhNUPCRWsTev8rZmL" width="289" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e346b45fbdf222871345f006a3ced47e512f063f_2_289x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e346b45fbdf222871345f006a3ced47e512f063f_2_433x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e346b45fbdf222871345f006a3ced47e512f063f.jpeg 2x" data-dominant-color="8E959D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">562×972 49.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @muratmaga (2024-10-01 23:09 UTC)

<p>Thanks Steve. I am glad it is not a widespread issue. Seems specific to combination of os, driver and H/W…</p>

---

## Post #13 by @lassoan (2024-10-02 02:25 UTC)

<p>The error <a class="mention" href="/u/pieper">@pieper</a> got seems to be similar to TDR crash on Windows: if the GPU is not responsive for a few seconds due to some heavy computation then the operating system “recovers” by restarting the graphics driver. It may be avoided by increasing the TDR delay on Windows, and enabling partitioning in the GPU volume mapper may solve it, too.</p>

---
