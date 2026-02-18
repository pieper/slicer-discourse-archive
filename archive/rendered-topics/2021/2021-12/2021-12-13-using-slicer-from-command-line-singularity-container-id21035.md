# Using Slicer from Command-Line - Singularity container

**Topic ID**: 21035
**Date**: 2021-12-13
**URL**: https://discourse.slicer.org/t/using-slicer-from-command-line-singularity-container/21035

---

## Post #1 by @Hayabusa (2021-12-13 16:02 UTC)

<p>Operating system: linux  ubuntu 20.04.3 (Focal Fossa)<br>
Slicer version: <a href="https://download.slicer.org/bitstream/60add706ae4540bf6a89bf98" rel="noopener nofollow ugc">4.11.20210226</a><br>
Expected behavior:<br>
Running slicer from a singularity container in our cluster with command xvfb-run -a --no-splash should resolve without problems</p>
<p>Actual behavior: Slicer crashes after producing the following error:</p>
<p>QStandardPaths: error creating runtime directory /run/user/3115426 (No such file or directory)</p>
<p>/Slicer/lib/Slicer-4.11/qt-loadable-modules/vtkSlicerCropVolumeModuleLogicPython.so: failed to map segment from shared object</p>
<p>/Slicer/lib/Slicer-4.11/qt-loadable-modules/vtkSlicerDICOMLibModuleLogicPython.so: failed to map segment from shared object</p>
<p>(xvfb-run : we would like to run slicer without invoking GUI or X11_. Please advice. Thanks</p>

---

## Post #2 by @pieper (2021-12-13 18:25 UTC)

<p>I have no problem running Slicer on ubuntu 20.04 with xvfb-run (not using singularity).  Looks like you have a problem with the Slicer paths because those libraries should be in the distribution and in the paths set by the launcher.</p>

---

## Post #3 by @Hayabusa (2021-12-13 20:38 UTC)

<p>Thanks Steve, for bringing this up to me.<br>
I am setting my library path in a definition files as:<br>
LD_LIBRARY_PATH=/home/user/Slicer/lib:/home/user/Slicer/share/<br>
but I am still getting the same error from the command line.<br>
Interestingly, on my local laptop Slicer does not crash, instead it prompts:<br>
Qt: Session management error: None of the authentication protocols specified are supported<br>
QStandardPaths: error creating runtime directory /run/user/1000 (No such file or directory)</p>
<p>and eventually :<br>
Switch to module:  “Welcome”</p>
<p>Could be an issue with permissions? the tmp folder for slicer seems right (drwxrwxr-x)?</p>

---

## Post #4 by @pieper (2021-12-13 21:57 UTC)

<p>We would definitely suggest using the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Launcher">launcher</a> rather than setting paths by hand.</p>
<p>The errors reported at startup can probably be ignored, at least for now.  Once it says “Switch to module: “Welcome”" slicer should be running fine (maybe use vnc if you want to interact with it) or use the command line arguments to give slicer code to run.</p>

---

## Post #5 by @Hayabusa (2021-12-14 02:18 UTC)

<p>Thanks Steve<br>
running Slicer with the launcher : xvfb-run -a ${SINGULARITY_ROOTFS}/Slicer/Slicer --launcher-verbose<br>
goes a step further before crashing and prompts: terminate called after throwing an instance of ‘St9bad_alloc’<br>
what():  std::bad_alloc<br>
error: [/Slicer/bin/SlicerApp-real] exit abnormally - Report the problem.</p>

---

## Post #6 by @Hayabusa (2021-12-14 13:39 UTC)

<p>Using launcher and: xvfb-run -a ${SINGULARITY_ROOTFS}/Slicer/Slicer --disable-scripted-loadable-module seem to work. we get switch to module ‘welcome’</p>

---

## Post #7 by @Hayabusa (2021-12-14 13:59 UTC)

<p>xvfb-run -a ${SINGULARITY_ROOTFS}/Slicer/Slicer --disable-builtinscripted-loadable-module fails with the same error as above: [/Slicer/bin/SlicerApp-real] exit abnormally</p>

---

## Post #8 by @Hayabusa (2021-12-18 18:15 UTC)

<p>I did a strace using --launch xterm, with the output below, in the hopes it might shed some light. With X11 enabled the main gui appears twice before ultimately crashing.</p>

---

## Post #9 by @Hayabusa (2021-12-18 18:16 UTC)

<p>stat("/Slicer/bin/Slicer-SplashScreen.png", {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
openat(AT_FDCWD, “/Slicer/bin/Slicer-SplashScreen.png”, O_RDONLY) = 10<br>
fcntl(10, F_SETFD, FD_CLOEXEC)          = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
read(10, “\211PNG\r\n\32\n\0\0\0\rIHDR\0\0\2=\0\0\1x\10\2\0\0\0000\216\337”…, 16384) = 16384<br>
mmap(NULL, 864256, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x2b564ef42000<br>
brk(0x1c18000)                          = 0x1c18000<br>
read(10, “\261X,]\323\273\f\32&lt;d\364\350\321\244\343Q\233\33\255\361\330\261c\237\177\376\271\370\365\316;\357”…, 159) = 159<br>
read(10, “\277\350+\273x\1\0000\27\364v\200XK\371\245\313\202\333u\345\307\37\1778\377c\367^)\322\354”…, 16384) = 16384<br>
read(10, “\376\235\f\330\0\0;\273IDAT\241\267\226cP\355d6%b(g)N+R\316\nUI”…, 16384) = 15417<br>
read(10, “”, 967)                       = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=48344, …}) = 0<br>
brk(0x1c10000)                          = 0x1c10000<br>
brk(0x1c0c000)                          = 0x1c0c000<br>
close(10)                               = 0<br>
brk(0x1c08000)                          = 0x1c08000<br>
uname({sysname=“Linux”, nodename=“beluga2.int.ets1.calculquebec.ca”, …}) = 0<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\2\0\4\0\304\7\0\0\20\0\0\0\1\0\0\0\2\0\4\0\304\7\0\0\0\10\0\0000@@\0"…, iov_len=492}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 492<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1\0\241\0\0\0\0\0\\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 32<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\22\0\7\0\2\0\0\3\\1\0\0\37\0\0\0\10\0\4\0\1\0\0\0C\10\0\0\f@\5\0"…, iov_len=100}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 100<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1\0\245\0\0\0\0\0]\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 32<br>
getpid()                                = 52860<br>
futex(0x2b564e3da0c8, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/SlicerDMRI/lib/Slicer-4.11/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/SlicerDMRI/lib/Slicer-4.11/cli-modules/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/SlicerDMRI/lib/Slicer-4.11/qt-loadable-modules/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/UKFTractography/lib/Slicer-4.11/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/UKFTractography/lib/Slicer-4.11/cli-modules/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/UKFTractography/lib/Slicer-4.11/qt-loadable-modules/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/bin/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Slicer-4.11/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Slicer-4.11/cli-modules/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Slicer-4.11/qt-loadable-modules/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Python/lib/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Teem-1.12.0/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Python/lib/python3.6/site-packages/numpy/core/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Python/lib/python3.6/site-packages/numpy/lib/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/.singularity.d/libs/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/etc/ld.so.cache”, O_RDONLY|O_CLOEXEC) = 10<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=32924, …}) = 0<br>
mmap(NULL, 32924, PROT_READ, MAP_PRIVATE, 10, 0) = 0x2b564ed23000<br>
close(10)                               = 0<br>
openat(AT_FDCWD, “/usr/lib/x86_64-linux-gnu/libXcursor.so.1”, O_RDONLY|O_CLOEXEC) = 10<br>
read(10, “\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0&gt;\0\1\0\0\0\3605\0\0\0\0\0\0”…, 832) = 832<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=47768, …}) = 0<br>
mmap(NULL, 49944, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 10, 0) = 0x2b564f015000<br>
mmap(0x2b564f018000, 24576, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 10, 0x3000) = 0x2b564f018000<br>
mmap(0x2b564f01e000, 8192, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 10, 0x9000) = 0x2b564f01e000<br>
mmap(0x2b564f020000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 10, 0xa000) = 0x2b564f020000<br>
close(10)                               = 0<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/SlicerDMRI/lib/Slicer-4.11/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/SlicerDMRI/lib/Slicer-4.11/cli-modules/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/SlicerDMRI/lib/Slicer-4.11/qt-loadable-modules/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/UKFTractography/lib/Slicer-4.11/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/UKFTractography/lib/Slicer-4.11/cli-modules/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/NA-MIC/Extensions-29738/UKFTractography/lib/Slicer-4.11/qt-loadable-modules/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/bin/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Slicer-4.11/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Slicer-4.11/cli-modules/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Slicer-4.11/qt-loadable-modules/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Python/lib/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Teem-1.12.0/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Python/lib/python3.6/site-packages/numpy/core/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/Slicer/bin/…/lib/Python/lib/python3.6/site-packages/numpy/lib/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/.singularity.d/libs/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/lib/x86_64-linux-gnu/libXfixes.so.3”, O_RDONLY|O_CLOEXEC) = 10<br>
read(10, “\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0&gt;\0\1\0\0\0\220\25\0\0\0\0\0\0”…, 832) = 832<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=22656, …}) = 0<br>
mmap(NULL, 2117912, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 10, 0) = 0x2b564f022000<br>
mprotect(0x2b564f027000, 2093056, PROT_NONE) = 0<br>
mmap(0x2b564f226000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 10, 0x4000) = 0x2b564f226000<br>
close(10)                               = 0<br>
mprotect(0x2b564f226000, 4096, PROT_READ) = 0<br>
mprotect(0x2b564f020000, 4096, PROT_READ) = 0<br>
munmap(0x2b564ed23000, 32924)           = 0<br>
openat(AT_FDCWD, “/usr/share/X11/locale/locale.alias”, O_RDONLY) = 10<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=82746, …}) = 0<br>
read(10, “\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n”…, 1024) = 1024<br>
read(10, “A.ISO-8859-6\t\t\t\tar_AA.ISO8859-6\n”…, 1024) = 1024<br>
read(10, “.ISO-8859-6\t\t\t\tar_LB.ISO8859-6\na”…, 1024) = 1024<br>
read(10, “8859-6\nar_TN.utf8\t\t\t\t\tar_TN.UTF-”…, 1024) = 1024<br>
read(10, “UTF-8\nbo_IN.utf8\t\t\t\t\tbo_IN.UTF-8”…, 1024) = 1024<br>
read(10, “9-1\nca_ES.iso885915\t\t\t\tca_ES.ISO”…, 1024) = 1024<br>
read(10, “s_CZ.ISO8859-2\ncs_CZ.ISO_8859-2\t”…, 1024) = 1024<br>
read(10, “de_DE.ISO8859-15\nde_AT\t\t\t\t\t\tde_A”…, 1024) = 1024<br>
read(10, “\t\t\tde_DE.ISO8859-15\nde_DE.88591\t”…, 1024) = 1024<br>
read(10, “l_GR.ISO8859-7\nel_GR\t\t\t\t\t\tel_GR.”…, 1024) = 1024<br>
read(10, “591\t\t\t\t\ten_GB.ISO8859-1\nen_GB.88”…, 1024) = 1024<br>
read(10, “.UTF-8\nen_PH.iso88591\t\t\t\t\ten_PH.”…, 1024) = 1024<br>
read(10, “\t\ten_ZA.ISO8859-1\nen_ZA.88591.en”…, 1024) = 1024<br>
read(10, “O.ISO-8859-1\t\t\t\tes_CO.ISO8859-1\n”…, 1024) = 1024<br>
read(10, “859-1\nes_HN.ISO-8859-1\t\t\t\tes_HN.”…, 1024) = 1024<br>
read(10, “\nes_SV.iso885915\t\t\t\tes_SV.ISO885”…, 1024) = 1024<br>
read(10, “\t\t\t\teu_ES.ISO8859-1\neu_ES.iso885”…, 1024) = 1024<br>
read(10, “\t\t\tfo_FO.ISO8859-15\nfo_FO.utf8\t\t”…, 1024) = 1024<br>
read(10, “15\t\t\t\tfr_CH.ISO8859-15\nfr_CH.utf”…, 1024) = 1024<br>
read(10, “IE.ISO-8859-1\t\t\t\tga_IE.ISO8859-1”…, 1024) = 1024<br>
read(10, “o88591\t\t\t\t\tgv_GB.ISO8859-1\ngv_GB”…, 1024) = 1024<br>
read(10, “\thu_HU.ISO8859-2\nhu_HU.iso88592\t”…, 1024) = 1024<br>
read(10, “\tit_IT.ISO8859-15\nit_IT.ISO-8859”…, 1024) = 1024<br>
read(10, “IS\nja_JP.SJIS\t\t\t\t\tja_JP.SJIS\nja_”…, 1024) = 1024<br>
read(10, “kw\t\t\t\t\t\tkw_GB.ISO8859-1\nkw_GB\t\t\t”…, 1024) = 1024<br>
read(10, “9-13\nlv_LV.ISO_8859-13\t\t\t\tlv_LV.”…, 1024) = 1024<br>
read(10, “859-1\nnb_NO.iso885915\t\t\t\tnb_NO.I”…, 1024) = 1024<br>
read(10, “_NL.UTF-8\nnn\t\t\t\t\t\tnn_NO.ISO8859-”…, 1024) = 1024<br>
read(10, “59-15\nno@nynorsk\t\t\t\t\tny_NO.ISO88”…, 1024) = 1024<br>
read(10, “1\npt\t\t\t\t\t\tpt_PT.ISO8859-1\npt.ISO”…, 1024) = 1024<br>
read(10, “ru_RU.ISO8859-5\nru_RU.koi8r\t\t\t\t\t”…, 1024) = 1024<br>
read(10, “tenegro (now separate RS and ME)”…, 1024) = 1024<br>
read(10, “\nsr_YU@cyrillic\t\t\t\t\tsr_RS.UTF-8\n”…, 1024) = 1024<br>
read(10, “I.ISO8859-15\nsv_FI.UTF-8@euro\t\t\t”…, 1024) = 1024<br>
read(10, “\t\ttn_ZA.ISO8859-15\ntn_ZA.iso8859”…, 1024) = 1024<br>
read(10, “ROSOFT-CP1256\t\t\t\tur_PK.CP1256\nuz”…, 1024) = 1024<br>
read(10, “\tyi_US.CP1255\nyi_US.MICROSOFT-CP”…, 1024) = 1024<br>
read(10, “UTF-8\nZH_TW.UTF-8\t\t\t\t\tzh_TW.UTF-”…, 1024) = 1024<br>
read(10, “\t\t\t\t\t\tet_EE.ISO8859-1\nenglish.is”…, 1024) = 1024<br>
read(10, “\tro_RO.ISO8859-2\nrumanian\t\t\t\t\tro”…, 1024) = 1024<br>
read(10, “rd is full locale name.\n#\n#\n\nPOS”…, 1024) = 1024<br>
read(10, “59-6\nar_BH.iso88596:\t\t\t\t\tar_BH.I”…, 1024) = 1024<br>
read(10, “SO8859-6\nar_LY.utf8:\t\t\t\t\tar_LY.U”…, 1024) = 1024<br>
read(10, “\tar_YE.ISO8859-6\nar_YE.iso88596:”…, 1024) = 1024<br>
read(10, “1\nbr_FR.iso88591:\t\t\t\t\tbr_FR.ISO8”…, 1024) = 1024<br>
read(10, “\t\t\tca_ES.UTF-8\nca_ES.ISO-8859-15”…, 1024) = 1024<br>
read(10, “<em>8859-2:\t\t\t\tcs_CZ.ISO8859-2\ncs_C"…, 1024) = 1024<br>
read(10, “:\t\t\t\t\tde_DE.ISO8859-15\nde_AT:\t\t\t”…, 1024) = 1024<br>
read(10, “:\t\t\t\t\t\tde_DE.ISO8859-1\nde_DE@eur”…, 1024) = 1024<br>
read(10, “\t\t\t\tee_EE.ISO8859-4\nee_EE.iso885”…, 1024) = 1024<br>
read(10, “59-15\nen_DK.utf8:\t\t\t\t\ten_DK.UTF-”…, 1024) = 1024<br>
read(10, “en_NZ.ISO8859-1\nen_NZ.ISO-8859-1”…, 1024) = 1024<br>
read(10, “\ten_US.ISO8859-15\nen_US.ISO8859-”…, 1024) = 1024<br>
read(10, “L:\t\t\t\t\t\tes_CL.ISO8859-1\nes_CL.is”…, 1024) = 1024<br>
read(10, “<em>ES.UTF-8\nes_ES.utf8:\t\t\t\t\tes_ES."…, 1024) = 1024<br>
read(10, “\t\t\tes_PY.ISO8859-1\nes_PY.iso8859”…, 1024) = 1024<br>
read(10, “t_EE.iso88594:\t\t\t\t\tet_EE.ISO8859”…, 1024) = 1024<br>
read(10, “I.ISO-8859-15@euro:\t\t\t\tfi_FI.ISO”…, 1024) = 1024<br>
read(10, “\t\t\tfr_CA.ISO8859-1\nfr_CA.iso8859”…, 1024) = 1024<br>
read(10, “1\nfr_LU.iso885915:\t\t\t\tfr_LU.ISO8”…, 1024) = 1024<br>
read(10, “O8859-1\ngl_ES.iso88591:\t\t\t\t\tgl_E”…, 1024) = 1024<br>
read(10, “i_IN.ISCII-DEV\nHI_IN:\t\t\t\t\t\thi_IN”…, 1024) = 1024<br>
read(10, “t_IT.ISO8859-15\nit.UTF-8:\t\t\t\t\tit”…, 1024) = 1024<br>
read(10, “iw_IL.iso88598:\t\t\t\t\the_IL.ISO885”…, 1024) = 1024<br>
read(10, “-8\nkm_KH.utf8:\t\t\t\t\tkm_KH.UTF-8\nk”…, 1024) = 1024<br>
read(10, “lo_LA.IBM-CP1133\nlo_LA.mulelao1:”…, 1024) = 1024<br>
read(10, “1:\t\t\t\tmk_MK.CP1251\nmk_MK.MICROSO”…, 1024) = 1024<br>
read(10, “O8859-1\nnl_BE.iso885915:\t\t\t\tnl_B”…, 1024) = 1024<br>
read(10, “59-1\nno_NO.iso88591:\t\t\t\t\tno_NO.I”…, 1024) = 1024<br>
read(10, “\t\t\t\tor_IN.UTF-8\npa:\t\t\t\t\t\tpa_IN.U”…, 1024) = 1024<br>
read(10, “1\npt_PT.88591:\t\t\t\t\tpt_PT.ISO8859”…, 1024) = 1024<br>
read(10, “UA.microsoftcp1251:\t\t\t\tru_UA.CP1”…, 1024) = 1024<br>
read(10, "                       sid_ET.UT"…, 1024) = 1024<br>
read(10, “TF-8@latin\nsr_RS:\t\t\t\t\t\tsr_RS.UTF”…, 1024) = 1024<br>
read(10, “<em>SE.ISO-8859-1:\t\t\t\tsv_SE.ISO8859"…, 1024) = 1024<br>
read(10, “599:\t\t\t\t\ttr_TR.ISO8859-9\ntr_TR.I”…, 1024) = 1024<br>
read(10, “TF-8\nuz_UZ.UTF-8@cyrillic:\t\t\t\tuz”…, 1024) = 1024<br>
read(10, "5\nzh_CN.EUC:\t\t\t\t\tzh_CN.eucCN\nzh</em>”…, 1024) = 1024<br>
read(10, “\t\t\tzu_ZA.ISO8859-1\nzu_ZA.iso8859”…, 1024) = 1024<br>
read(10, “\t\t\ten_US.ISO8859-1\nestonian:\t\t\t\t”…, 1024) = 1024<br>
read(10, “ISO8859-2\nrumanian:\t\t\t\t\tro_RO.IS”…, 1024) = 826<br>
read(10, “”, 1024)                      = 0<br>
close(10)                               = 0<br>
openat(AT_FDCWD, “/usr/share/X11/locale/locale.dir”, O_RDONLY) = 10<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=40625, …}) = 0<br>
read(10, “\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n”…, 1024) = 1024<br>
read(10, “E.ISO8859-6\niso8859-6/XLC_LOCALE”…, 1024) = 1024<br>
read(10, “<em>DK.ISO8859-1\niso8859-15/XLC_LOC"…, 1024) = 1024<br>
read(10, “OCALE\t\t\ten_GB.ISO8859-1\niso8859-”…, 1024) = 1024<br>
read(10, “8859-1/XLC_LOCALE\t\t\tes_CR.ISO885”…, 1024) = 1024<br>
read(10, "9-13\niso8859-15/XLC_LOCALE\t\t\tet</em>”…, 1024) = 1024<br>
read(10, “OCALE\t\t\tgd_GB.ISO8859-15\niso8859”…, 1024) = 1024<br>
read(10, "OCALE\t\t\tkl_GL.ISO8859-15\nko/XLC</em>”…, 1024) = 1024<br>
read(10, “LC_LOCALE\t\t\tno_NO.ISO8859-15\niso”…, 1024) = 1024<br>
read(10, " \t\tru_RU.CP1251\nkoi8-r/XLC_LOCAL"…, 1024) = 1024<br>
read(10, “20\niso8859-1/XLC_LOCALE \t\t\ttl_PH”…, 1024) = 1024<br>
read(10, “<em>LOCALE\t\t\tzu_ZA.ISO8859-1\n# Note"…, 1024) = 1024<br>
read(10, “s_IN.UTF-8\nen_US.UTF-8/XLC_LOCAL”…, 1024) = 1024<br>
read(10, “.UTF-8\nen_US.UTF-8/XLC_LOCALE\t\t\t”…, 1024) = 1024<br>
read(10, “UTF-8/XLC_LOCALE\t\t\tes_EC.UTF-8\ne”…, 1024) = 1024<br>
read(10, "   gez_ER.UTF-8\nen_US.UTF-8/XLC</em>”…, 1024) = 1024<br>
read(10, “ALE\t\t\tku_TR.UTF-8\nen_US.UTF-8/XL”…, 1024) = 1024<br>
read(10, “XLC_LOCALE\t\t\toc_FR.UTF-8\nen_US.U”…, 1024) = 1024<br>
read(10, “.UTF-8\nen_US.UTF-8/XLC_LOCALE\t\t\t”…, 1024) = 1024<br>
read(10, “.UTF-8\nen_US.UTF-8/XLC_LOCALE\t\t\t”…, 1024) = 1024<br>
close(10)                               = 0<br>
access("/usr/share/X11/locale/C/XLC_LOCALE", R_OK) = 0<br>
openat(AT_FDCWD, “/usr/share/X11/locale/C/XLC_LOCALE”, O_RDONLY) = 10<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=693, …}) = 0<br>
read(10, “\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n”…, 1024) = 693<br>
read(10, “”, 1024)                      = 0<br>
close(10)                               = 0<br>
openat(AT_FDCWD, “/usr/share/X11/locale/locale.alias”, O_RDONLY) = 10<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=82746, …}) = 0<br>
read(10, “\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n”…, 1024) = 1024<br>
read(10, “A.ISO-8859-6\t\t\t\tar_AA.ISO8859-6\n”…, 1024) = 1024<br>
read(10, “.ISO-8859-6\t\t\t\tar_LB.ISO8859-6\na”…, 1024) = 1024<br>
read(10, “8859-6\nar_TN.utf8\t\t\t\t\tar_TN.UTF-”…, 1024) = 1024<br>
read(10, “UTF-8\nbo_IN.utf8\t\t\t\t\tbo_IN.UTF-8”…, 1024) = 1024<br>
read(10, “9-1\nca_ES.iso885915\t\t\t\tca_ES.ISO”…, 1024) = 1024<br>
read(10, “s_CZ.ISO8859-2\ncs_CZ.ISO_8859-2\t”…, 1024) = 1024<br>
read(10, “de_DE.ISO8859-15\nde_AT\t\t\t\t\t\tde_A”…, 1024) = 1024<br>
read(10, “\t\t\tde_DE.ISO8859-15\nde_DE.88591\t”…, 1024) = 1024<br>
read(10, “l_GR.ISO8859-7\nel_GR\t\t\t\t\t\tel_GR.”…, 1024) = 1024<br>
read(10, “591\t\t\t\t\ten_GB.ISO8859-1\nen_GB.88”…, 1024) = 1024<br>
read(10, “.UTF-8\nen_PH.iso88591\t\t\t\t\ten_PH.”…, 1024) = 1024<br>
read(10, “\t\ten_ZA.ISO8859-1\nen_ZA.88591.en”…, 1024) = 1024<br>
read(10, “O.ISO-8859-1\t\t\t\tes_CO.ISO8859-1\n”…, 1024) = 1024<br>
read(10, “859-1\nes_HN.ISO-8859-1\t\t\t\tes_HN.”…, 1024) = 1024<br>
read(10, “\nes_SV.iso885915\t\t\t\tes_SV.ISO885”…, 1024) = 1024<br>
read(10, “\t\t\t\teu_ES.ISO8859-1\neu_ES.iso885”…, 1024) = 1024<br>
read(10, “\t\t\tfo_FO.ISO8859-15\nfo_FO.utf8\t\t”…, 1024) = 1024<br>
read(10, “15\t\t\t\tfr_CH.ISO8859-15\nfr_CH.utf”…, 1024) = 1024<br>
read(10, “IE.ISO-8859-1\t\t\t\tga_IE.ISO8859-1”…, 1024) = 1024<br>
read(10, “o88591\t\t\t\t\tgv_GB.ISO8859-1\ngv_GB”…, 1024) = 1024<br>
read(10, “\thu_HU.ISO8859-2\nhu_HU.iso88592\t”…, 1024) = 1024<br>
read(10, “\tit_IT.ISO8859-15\nit_IT.ISO-8859”…, 1024) = 1024<br>
read(10, "IS\nja_JP.SJIS\t\t\t\t\tja_JP.SJIS\nja</em>”…, 1024) = 1024<br>
read(10, “kw\t\t\t\t\t\tkw_GB.ISO8859-1\nkw_GB\t\t\t”…, 1024) = 1024<br>
read(10, “9-13\nlv_LV.ISO_8859-13\t\t\t\tlv_LV.”…, 1024) = 1024<br>
read(10, “859-1\nnb_NO.iso885915\t\t\t\tnb_NO.I”…, 1024) = 1024<br>
read(10, “_NL.UTF-8\nnn\t\t\t\t\t\tnn_NO.ISO8859-”…, 1024) = 1024<br>
read(10, “59-15\nno@nynorsk\t\t\t\t\tny_NO.ISO88”…, 1024) = 1024<br>
read(10, “1\npt\t\t\t\t\t\tpt_PT.ISO8859-1\npt.ISO”…, 1024) = 1024<br>
read(10, “ru_RU.ISO8859-5\nru_RU.koi8r\t\t\t\t\t”…, 1024) = 1024<br>
read(10, “tenegro (now separate RS and ME)”…, 1024) = 1024<br>
read(10, “\nsr_YU@cyrillic\t\t\t\t\tsr_RS.UTF-8\n”…, 1024) = 1024<br>
read(10, “I.ISO8859-15\nsv_FI.UTF-8@euro\t\t\t”…, 1024) = 1024<br>
read(10, “\t\ttn_ZA.ISO8859-15\ntn_ZA.iso8859”…, 1024) = 1024<br>
read(10, “ROSOFT-CP1256\t\t\t\tur_PK.CP1256\nuz”…, 1024) = 1024<br>
read(10, “\tyi_US.CP1255\nyi_US.MICROSOFT-CP”…, 1024) = 1024<br>
read(10, “UTF-8\nZH_TW.UTF-8\t\t\t\t\tzh_TW.UTF-”…, 1024) = 1024<br>
read(10, “\t\t\t\t\t\tet_EE.ISO8859-1\nenglish.is”…, 1024) = 1024<br>
read(10, “\tro_RO.ISO8859-2\nrumanian\t\t\t\t\tro”…, 1024) = 1024<br>
read(10, “rd is full locale name.\n#\n#\n\nPOS”…, 1024) = 1024<br>
read(10, “59-6\nar_BH.iso88596:\t\t\t\t\tar_BH.I”…, 1024) = 1024<br>
read(10, “SO8859-6\nar_LY.utf8:\t\t\t\t\tar_LY.U”…, 1024) = 1024<br>
read(10, “\tar_YE.ISO8859-6\nar_YE.iso88596:”…, 1024) = 1024<br>
read(10, “1\nbr_FR.iso88591:\t\t\t\t\tbr_FR.ISO8”…, 1024) = 1024<br>
read(10, “\t\t\tca_ES.UTF-8\nca_ES.ISO-8859-15”…, 1024) = 1024<br>
read(10, “_8859-2:\t\t\t\tcs_CZ.ISO8859-2\ncs_C”…, 1024) = 1024<br>
read(10, “:\t\t\t\t\tde_DE.ISO8859-15\nde_AT:\t\t\t”…, 1024) = 1024<br>
read(10, “:\t\t\t\t\t\tde_DE.ISO8859-1\nde_DE@eur”…, 1024) = 1024<br>
read(10, “\t\t\t\tee_EE.ISO8859-4\nee_EE.iso885”…, 1024) = 1024<br>
read(10, “59-15\nen_DK.utf8:\t\t\t\t\ten_DK.UTF-”…, 1024) = 1024<br>
read(10, “en_NZ.ISO8859-1\nen_NZ.ISO-8859-1”…, 1024) = 1024<br>
read(10, “\ten_US.ISO8859-15\nen_US.ISO8859-”…, 1024) = 1024<br>
read(10, “L:\t\t\t\t\t\tes_CL.ISO8859-1\nes_CL.is”…, 1024) = 1024<br>
read(10, “<em>ES.UTF-8\nes_ES.utf8:\t\t\t\t\tes_ES."…, 1024) = 1024<br>
read(10, “\t\t\tes_PY.ISO8859-1\nes_PY.iso8859”…, 1024) = 1024<br>
read(10, “t_EE.iso88594:\t\t\t\t\tet_EE.ISO8859”…, 1024) = 1024<br>
read(10, “I.ISO-8859-15@euro:\t\t\t\tfi_FI.ISO”…, 1024) = 1024<br>
read(10, “\t\t\tfr_CA.ISO8859-1\nfr_CA.iso8859”…, 1024) = 1024<br>
read(10, “1\nfr_LU.iso885915:\t\t\t\tfr_LU.ISO8”…, 1024) = 1024<br>
read(10, “O8859-1\ngl_ES.iso88591:\t\t\t\t\tgl_E”…, 1024) = 1024<br>
read(10, “i_IN.ISCII-DEV\nHI_IN:\t\t\t\t\t\thi_IN”…, 1024) = 1024<br>
read(10, “t_IT.ISO8859-15\nit.UTF-8:\t\t\t\t\tit”…, 1024) = 1024<br>
read(10, “iw_IL.iso88598:\t\t\t\t\the_IL.ISO885”…, 1024) = 1024<br>
read(10, “-8\nkm_KH.utf8:\t\t\t\t\tkm_KH.UTF-8\nk”…, 1024) = 1024<br>
read(10, “lo_LA.IBM-CP1133\nlo_LA.mulelao1:”…, 1024) = 1024<br>
read(10, “1:\t\t\t\tmk_MK.CP1251\nmk_MK.MICROSO”…, 1024) = 1024<br>
read(10, “O8859-1\nnl_BE.iso885915:\t\t\t\tnl_B”…, 1024) = 1024<br>
read(10, “59-1\nno_NO.iso88591:\t\t\t\t\tno_NO.I”…, 1024) = 1024<br>
read(10, “\t\t\t\tor_IN.UTF-8\npa:\t\t\t\t\t\tpa_IN.U”…, 1024) = 1024<br>
read(10, “1\npt_PT.88591:\t\t\t\t\tpt_PT.ISO8859”…, 1024) = 1024<br>
read(10, “UA.microsoftcp1251:\t\t\t\tru_UA.CP1”…, 1024) = 1024<br>
read(10, "                       sid_ET.UT"…, 1024) = 1024<br>
read(10, “TF-8@latin\nsr_RS:\t\t\t\t\t\tsr_RS.UTF”…, 1024) = 1024<br>
read(10, “<em>SE.ISO-8859-1:\t\t\t\tsv_SE.ISO8859"…, 1024) = 1024<br>
read(10, “599:\t\t\t\t\ttr_TR.ISO8859-9\ntr_TR.I”…, 1024) = 1024<br>
read(10, “TF-8\nuz_UZ.UTF-8@cyrillic:\t\t\t\tuz”…, 1024) = 1024<br>
read(10, "5\nzh_CN.EUC:\t\t\t\t\tzh_CN.eucCN\nzh</em>”…, 1024) = 1024<br>
read(10, “\t\t\tzu_ZA.ISO8859-1\nzu_ZA.iso8859”…, 1024) = 1024<br>
read(10, “\t\t\ten_US.ISO8859-1\nestonian:\t\t\t\t”…, 1024) = 1024<br>
read(10, “ISO8859-2\nrumanian:\t\t\t\t\tro_RO.IS”…, 1024) = 826<br>
read(10, “”, 1024)                      = 0<br>
close(10)                               = 0<br>
openat(AT_FDCWD, “/usr/share/X11/locale/locale.dir”, O_RDONLY) = 10<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=40625, …}) = 0<br>
read(10, “\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n”…, 1024) = 1024<br>
read(10, “E.ISO8859-6\niso8859-6/XLC_LOCALE”…, 1024) = 1024<br>
read(10, “<em>DK.ISO8859-1\niso8859-15/XLC_LOC"…, 1024) = 1024<br>
read(10, “OCALE\t\t\ten_GB.ISO8859-1\niso8859-”…, 1024) = 1024<br>
read(10, “8859-1/XLC_LOCALE\t\t\tes_CR.ISO885”…, 1024) = 1024<br>
read(10, "9-13\niso8859-15/XLC_LOCALE\t\t\tet</em>”…, 1024) = 1024<br>
read(10, “OCALE\t\t\tgd_GB.ISO8859-15\niso8859”…, 1024) = 1024<br>
read(10, "OCALE\t\t\tkl_GL.ISO8859-15\nko/XLC</em>”…, 1024) = 1024<br>
read(10, “LC_LOCALE\t\t\tno_NO.ISO8859-15\niso”…, 1024) = 1024<br>
read(10, " \t\tru_RU.CP1251\nkoi8-r/XLC_LOCAL"…, 1024) = 1024<br>
read(10, “20\niso8859-1/XLC_LOCALE \t\t\ttl_PH”…, 1024) = 1024<br>
read(10, “<em>LOCALE\t\t\tzu_ZA.ISO8859-1\n# Note"…, 1024) = 1024<br>
read(10, “s_IN.UTF-8\nen_US.UTF-8/XLC_LOCAL”…, 1024) = 1024<br>
read(10, “.UTF-8\nen_US.UTF-8/XLC_LOCALE\t\t\t”…, 1024) = 1024<br>
read(10, “UTF-8/XLC_LOCALE\t\t\tes_EC.UTF-8\ne”…, 1024) = 1024<br>
read(10, "   gez_ER.UTF-8\nen_US.UTF-8/XLC</em>”…, 1024) = 1024<br>
read(10, “ALE\t\t\tku_TR.UTF-8\nen_US.UTF-8/XL”…, 1024) = 1024<br>
read(10, “XLC_LOCALE\t\t\toc_FR.UTF-8\nen_US.U”…, 1024) = 1024<br>
read(10, “.UTF-8\nen_US.UTF-8/XLC_LOCALE\t\t\t”…, 1024) = 1024<br>
read(10, “.UTF-8\nen_US.UTF-8/XLC_LOCALE\t\t\t”…, 1024) = 1024<br>
close(10)                               = 0<br>
access("/usr/share/X11/locale/C/XLC_LOCALE", R_OK) = 0<br>
openat(AT_FDCWD, “/usr/share/X11/locale/C/XLC_LOCALE”, O_RDONLY) = 10<br>
fstat(10, {st_mode=S_IFREG|0644, st_size=693, …}) = 0<br>
read(10, “\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n”…, 1024) = 693<br>
read(10, “”, 1024)                      = 0<br>
close(10)                               = 0<br>
uname({sysname=“Linux”, nodename=“beluga2.int.ets1.calculquebec.ca”, …}) = 0<br>
openat(AT_FDCWD, “/home/hayabusa/.Xdefaults-beluga2.int.ets1.calculquebec.ca”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/home/hayabusa/.icons/Yaru/cursors/left_ptr”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/home/hayabusa/.icons/Yaru/index.theme”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/share/icons/Yaru/cursors/left_ptr”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/share/icons/Yaru/index.theme”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/share/pixmaps/Yaru/cursors/left_ptr”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/share/pixmaps/Yaru/index.theme”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/home/hayabusa/.icons/default/cursors/left_ptr”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/home/hayabusa/.icons/default/index.theme”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/share/icons/default/cursors/left_ptr”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/share/icons/default/index.theme”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/share/pixmaps/default/cursors/left_ptr”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/share/pixmaps/default/index.theme”, O_RDONLY) = -1 ENOENT (No such file or directory)<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\22\0\n\0\2\0\0\3]\1\0\0\4\0\0\0 \0\4\0\4\0\0\0[\1\0\0^\1\0\0"…, iov_len=380}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 380<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\260\0\2\0\0\3\366\2\0\0\305\235m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 132<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\22\0\17\0\2\0\0\3#\0\0\0#\0\0\0 \0\4\0\t\0\0\0C\0\0\0\1\0\0\0"…, iov_len=84}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 84<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\266\0\2\0\0\3#\0\0\0\322\235m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 100<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\22\0\17\0\2\0\0\3#\0\0\0#\0\0\0 \0\4\0\t\0\0\0C\0\0\0\1\0\0\0"…, iov_len=208}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 208<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\270\0\2\0\0\3#\0\0\0\336\235m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 128<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\23\0\3\0\2\0\0\3\252\1\0\0\24\0\6\0\2\0\0\3k\1\0\0\4\0\0\0\0\0\0\0"…, iov_len=36}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 36<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1\0\275\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 32<br>
ioctl(16, FIONREAD, [0])                = 0<br>
close(16)                               = 0<br>
ioctl(14, FIONREAD, [0])                = 0<br>
close(14)                               = 0<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\22\0\10\0\2\0\0\3k\1\0\0\4\0\0\0 \0\0\3\2\0\0\0l\1\0\0\357\2\0\0"…, iov_len=84}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 84<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
select(21, [5 9 20], [], [], {tv_sec=2, tv_usec=999740}) = 1 (in [5], left {tv_sec=2, tv_usec=999738})<br>
read(5, “\0”, 16)                       = 1<br>
read(5, 0x7fff7060d190, 16)             = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
select(21, [5 9 20], [], [], {tv_sec=2, tv_usec=999608}) = 1 (in [9], left {tv_sec=2, tv_usec=983855})<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\276\0\2\0\0\3k\1\0\0\371\235m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 64<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\24\0\6\0\2\0\0\3k\1\0\0\4\0\0\0\0\0\0\0\0\4\0\0", iov_len=24}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 24<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\301\0\2\0\0\3\313\1\0\0\373\235m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 64<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\301\0\2\0\0\3\337\1\0\0\4\236m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 224<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\301\0\2\0\0\3\251\1\0\0\7\236m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 492<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\24\0\6\0\2\0\0\3k\1\0\0\4\0\0\0\0\0\0\0\0\4\0\0", iov_len=24}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 24<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1 \303\0\3\0\0\0\4\0\0\0\0\0\0\0\3\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 44<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="+\0\1\0", iov_len=4}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 4<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1\1\304\0\0\0\0\0\17\0\340\2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 32<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\24\0\6\0\2\0\0\3\251\1\0\0\251\1\0\0\0\0\0\0\2\0\0\0", iov_len=24}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 24<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1 \305\0\2\0\0\0\251\1\0\0\0\0\0\0\2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 40<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\24\0\6\0\2\0\0\3k\1\0\0\4\0\0\0\0\0\0\0\0\4\0\0", iov_len=24}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 24<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1 \306\0\3\0\0\0\4\0\0\0\0\0\0\0\3\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 44<br>
select(21, [5 9 20], [], [], {tv_sec=0, tv_usec=0}) = 0 (Timeout)<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\24\0\6\0\2\0\0\3k\1\0\0\4\0\0\0\0\0\0\0\0\4\0\0", iov_len=24}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 24<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1 \307\0\3\0\0\0\4\0\0\0\0\0\0\0\3\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 44<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
mmap(NULL, 864256, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x2b564f228000<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base=“H\0020\377\2\0\0\3\7\0\0\3=\2r\0\0\0\0\0\0\30\0\0”, iov_len=24}, {iov_base="\232\232\232\377\232\232\232\377\232\232\232\377\232\232\232\377\232\232\232\377\232\232\232\377\232\232\232\377\232\232\232\377"…, iov_len=261288}, {iov_base="", iov_len=0}], 3) = 261312<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base=“H\0020\377\2\0\0\3\7\0\0\3=\2r\0\0\0r\0\0\30\0\0”, iov_len=24}, {iov_base="\232\232\232\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377"…, iov_len=261288}, {iov_base="", iov_len=0}], 3) = 261312<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base=“H\0020\377\2\0\0\3\7\0\0\3=\2r\0\0\0\344\0\0\30\0\0”, iov_len=24}, {iov_base="\232\232\232\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377"…, iov_len=261288}, {iov_base="", iov_len=0}], 3) = 261312<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base=“H\2 L\2\0\0\3\7\0\0\3=\2”\0\0\0V\1\0\30\0\0", iov_len=24}, {iov_base="\232\232\232\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377\377"…, iov_len=77928}, {iov_base="", iov_len=0}], 3) = 77952<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
select(21, [5 9 20], [], [], {tv_sec=2, tv_usec=898078}QStandardPaths: error creating runtime directory /run/user/3115426 (No such file or directory)<br>
) = 0 (Timeout)<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\n\2\2\0\2\0\0\3\31\0\v\0\304\7\0\0\0\0\30\0\22\0\0\0\304\7\0\0\2\0\0\3"…, iov_len=52}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 52<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
select(21, [5 9 20], [], [], {tv_sec=26, tv_usec=906420}) = 1 (in [9], left {tv_sec=26, tv_usec=880003})<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\22\0\314\0\2\0\0\3\2\0\0\3\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 192<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\24\0\6\0\2\0\0\3\251\1\0\0\251\1\0\0\0\0\0\0\2\0\0\0", iov_len=24}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 24<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1 \316\0\2\0\0\0\251\1\0\0\0\0\0\0\2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 40<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base="\23\0\3\0\2\0\0\3\251\1\0\0", iov_len=12}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 12<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
select(21, [5 9 20], [], [], {tv_sec=26, tv_usec=863445}) = 1 (in [9], left {tv_sec=26, tv_usec=836072})<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\317\0\2\0\0\3\251\1\0\0\332\251m\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 32<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
select(21, [5 9 20], [], [], {tv_sec=26, tv_usec=835938}) = 1 (in [9], left {tv_sec=24, tv_usec=452303})<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\317\0\304\7\0\0\326\1\0\08\263m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 64<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
select(21, [5 9 20], [], [], {tv_sec=24, tv_usec=452113}) = 1 (in [9], left {tv_sec=24, tv_usec=444994})<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\317\0\304\7\0\0\300\1\0\0:\263m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 96<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
recvmsg(9, {msg_namelen=0}, 0)          = -1 EAGAIN (Resource temporarily unavailable)<br>
select(21, [5 9 20], [], [], {tv_sec=24, tv_usec=444870}QThread::start: Thread creation error (Resource temporarily unavailable)<br>
QThread::start: Thread creation error (Resource temporarily unavailable)<br>
QThread::start: Thread creation error (Resource temporarily unavailable)</p>
<p>) = ? ERESTARTNOHAND (To be restarted if no handler)<br>
— SIGCHLD {si_signo=SIGCHLD, si_code=CLD_KILLED, si_pid=52872, si_uid=3115426, si_status=SIGABRT, si_utime=526, si_stime=261} —<br>
write(8, “\0”, 1)                       = 1<br>
rt_sigreturn({mask=[]})                 = -1 EINTR (Interrupted system call)<br>
select(21, [5 9 20], [], [], {tv_sec=21, tv_usec=257509}) = 1 (in [20], left {tv_sec=21, tv_usec=257507})<br>
read(20, “\0”, 1)                       = 1<br>
wait4(52872, [{WIFSIGNALED(s) &amp;&amp; WTERMSIG(s) == SIGABRT}], WNOHANG, NULL) = 52872<br>
ioctl(-1, FIONREAD, 0x7fff7060cc6c)     = -1 EBADF (Bad file descriptor)<br>
ioctl(-1, FIONREAD, 0x7fff7060cc6c)     = -1 EBADF (Bad file descriptor)<br>
close(11)                               = 0<br>
close(21)                               = 0<br>
close(20)                               = 0<br>
write(2, “error: “, 7error: )                  = 7<br>
write(2, “[/Slicer/bin/SlicerApp-real] exi”…, 66[/Slicer/bin/SlicerApp-real] exit abnormally - Report the problem.) = 66<br>
write(2, “\n”, 1<br>
)                       = 1<br>
write(6, “\0”, 1)                       = 1<br>
munmap(0x2b564f228000, 864256)          = 0<br>
munmap(0x2b564ef42000, 864256)          = 0<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base=”\213\7\2\0\3\0\0\3\22\0\n\0\2\0\0\3\366\2\0\0\366\2\0\0\10\7\0\0\20\0\0\0”…, iov_len=84}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 84<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\321\0\2\0\0\3\366\2\0\0\366\277m\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 224<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\34\0\322\0\2\0\0\3\372\1\0\0\366\277m\0\1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"…, iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 512<br>
poll([{fd=9, events=POLLIN|POLLOUT}], 1, -1) = 1 ([{fd=9, revents=POLLOUT}])<br>
writev(9, [{iov_base=“O\7\2\0\1\0\0\3&lt;\0\2\0\0\0\0\3.\2\2\0\5\0\0\3+\7\1\0”, iov_len=28}, {iov_base=NULL, iov_len=0}, {iov_base="", iov_len=0}], 3) = 28<br>
poll([{fd=9, events=POLLIN}], 1, -1)    = 1 ([{fd=9, revents=POLLIN}])<br>
recvmsg(9, {msg_name=NULL, msg_namelen=0, msg_iov=[{iov_base="\1\1\332\0\0\0\0\0\17\0\340\2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", iov_len=4096}], msg_iovlen=1, msg_controllen=0, msg_flags=0}, 0) = 32<br>
shutdown(9, SHUT_RDWR)                  = 0<br>
close(9)                                = 0<br>
openat(AT_FDCWD, “/sys/devices/system/cpu/online”, O_RDONLY|O_CLOEXEC) = 9<br>
read(9, “0-39\n”, 8192)                 = 5<br>
close(9)                                = 0<br>
close(5)                                = 0<br>
close(6)                                = 0<br>
write(8, “@”, 1)                        = 1<br>
close(8)                                = 0<br>
futex(0x1b5b070, FUTEX_WAIT_PRIVATE, 0, NULL) = 0<br>
futex(0x1b5b020, FUTEX_WAKE_PRIVATE, 1) = 0<br>
close(7)                                = 0<br>
rt_sigaction(SIGCHLD, NULL, {sa_handler=0xa7ff60, sa_mask=[], sa_flags=SA_RESTORER|SA_SIGINFO|SA_NOCLDSTOP, sa_restorer=0x2b564e3c7730}, 8) = 0<br>
rt_sigaction(SIGCHLD, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x2b564e3c7730}, NULL, 8) = 0<br>
exit_group(1)                           = ?<br>
+++ exited with 1 +++</p>

---

## Post #10 by @Hayabusa (2021-12-21 01:32 UTC)

<p>And using gdb on /bin/SlicerApp-real<br>
${SINGULARITY_ROOTFS}/Slicer/Slicer --launch gdb ${SINGULARITY_ROOTFS}/Slicer/bin/SlicerApp-real</p>

---

## Post #11 by @Hayabusa (2021-12-21 01:32 UTC)

<p>Traceback (most recent call last):<br>
File “/Slicer/bin/…/lib/Python/lib/python3.6/site.py”, line 553, in <br>
main()<br>
File “/Slicer/bin/…/lib/Python/lib/python3.6/site.py”, line 539, in main<br>
known_paths = addusersitepackages(known_paths)<br>
File “/Slicer/bin/…/lib/Python/lib/python3.6/site.py”, line 282, in addusersitepackages<br>
user_site = getusersitepackages()<br>
File “/Slicer/bin/…/lib/Python/lib/python3.6/site.py”, line 258, in getusersitepackages<br>
user_base = getuserbase() # this will also set USER_BASE<br>
File “/Slicer/bin/…/lib/Python/lib/python3.6/site.py”, line 248, in getuserbase<br>
USER_BASE = get_config_var(‘userbase’)<br>
File “/Slicer/lib/Python/lib/python3.6/sysconfig.py”, line 601, in get_config_var<br>
return get_config_vars().get(name)<br>
File “/Slicer/lib/Python/lib/python3.6/sysconfig.py”, line 550, in get_config_vars<br>
_init_posix(_CONFIG_VARS)<br>
File “/Slicer/lib/Python/lib/python3.6/sysconfig.py”, line 421, in _init_posix<br>
_temp = <strong>import</strong>(name, globals(), locals(), [‘build_time_vars’], 0)<br>
ModuleNotFoundError: No module named ‘_sysconfigdata__linux_x86_64-linux-gnu’</p>

---

## Post #12 by @Hayabusa (2021-12-21 01:33 UTC)

<p>ModuleNotFoundError: No module named ‘_sysconfigdata__linux_x86_64-linux-gnu’</p>
<p>I have no clue…</p>

---

## Post #13 by @lassoan (2021-12-28 17:40 UTC)

<p>This GDB problem is due to GDB depending on Python and GDB developers thinking that only system Python exists. See workaround here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/linuxcpp.html#analyze-a-segmentation-fault" class="inline-onebox">C++ debugging on GNU/Linux systems — 3D Slicer documentation</a></p>

---
