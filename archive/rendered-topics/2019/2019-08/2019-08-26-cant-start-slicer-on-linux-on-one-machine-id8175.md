---
topic_id: 8175
title: "Cant Start Slicer On Linux On One Machine"
date: 2019-08-26
url: https://discourse.slicer.org/t/8175
---

# Can't start Slicer on Linux on one machine

**Topic ID**: 8175
**Date**: 2019-08-26
**URL**: https://discourse.slicer.org/t/cant-start-slicer-on-linux-on-one-machine/8175

---

## Post #1 by @chir.set (2019-08-26 07:12 UTC)

<p>I get the following message when launching Slicer :</p>
<blockquote>
<p>$ ./Slicer<br>
error: [/home/user/programs/Slicer-4.11.0-2019-08-22-linux-amd64/bin/SlicerApp-real] exit abnormally -<br>
Report the problem.</p>
</blockquote>
<p>This happens on my desktop machine only, it launches normally on my laptop. It happens with both home built Slicher unchanged and with packages from your repository.<br>
Unfortunately, there are no hints in the console message. This started after the major ITK/CTK updates.</p>
<p>I suspect a system library problem, but can’t get to it. But could be another root cause.</p>
<p>Using Qt 5.13.0 on both machines. I’ll provide other useful information you may need to resolve this. I fear it will be a lengthy process without error messages.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2019-08-26 12:49 UTC)

<p>Can you get a call stack?</p>
<p>If you build Slicer with debug information and run it in a debugger then you get detailed information about what goes wrong.</p>

---

## Post #3 by @pieper (2019-08-26 14:33 UTC)

<p>Another debugging approach (works with the binary download or local build):</p>
<p>First create a shell with Slicer’s environment:</p>
<pre><code class="lang-auto">./Slicer --launch xterm
</code></pre>
<p>Then in the new window:</p>
<pre><code class="lang-auto">strace ./bin/SlicerApp-real
</code></pre>
<p>This will give you a log of system calls and typically the last operations will indicate what was going on at the time of the crash (e.g. what file or library was being loaded).</p>

---

## Post #4 by @chir.set (2019-08-26 15:05 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>log of system calls and typically the last operations</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>what file or library was being loaded</p>
</blockquote>
</aside>
<blockquote>
<p>$ LC_ALL=C LANG=C strace ./bin/SlicerApp-real<br>
execve(“./bin/SlicerApp-real”, [“./bin/SlicerApp-real”], 0x7ffef0915fc0 /* 86 vars <em>/) = 0<br>
brk(NULL)                               = 0x5615e14c0000<br>
arch_prctl(0x3001 /</em> ARCH_??? */, 0x7fff7595d240) = -1 EINVAL (Invalid argument)<br>
access(“/etc/ld.so.preload”, R_OK)      = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/etc/ld.so.cache”, O_RDONLY|O_CLOEXEC) = 3<br>
fstat(3, {st_mode=S_IFREG|0644, st_size=336853, …}) = 0<br>
mmap(NULL, 336853, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7fb626511000<br>
close(3)                                = 0<br>
openat(AT_FDCWD, “/usr/lib/tls/x86_64/x86_64/libqSlicerApp.so”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
stat(“/usr/lib/tls/x86_64/x86_64”, 0x7fff7595c480) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/lib/tls/x86_64/libqSlicerApp.so”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
stat(“/usr/lib/tls/x86_64”, 0x7fff7595c480) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/lib/tls/x86_64/libqSlicerApp.so”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
stat(“/usr/lib/tls/x86_64”, 0x7fff7595c480) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/lib/tls/libqSlicerApp.so”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
stat(“/usr/lib/tls”, 0x7fff7595c480)    = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/lib/x86_64/x86_64/libqSlicerApp.so”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
stat(“/usr/lib/x86_64/x86_64”, 0x7fff7595c480) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/lib/x86_64/libqSlicerApp.so”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
stat(“/usr/lib/x86_64”, 0x7fff7595c480) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/lib/x86_64/libqSlicerApp.so”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
stat(“/usr/lib/x86_64”, 0x7fff7595c480) = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/lib/libqSlicerApp.so”, O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)<br>
stat(“/usr/lib”, {st_mode=S_IFDIR|0755, st_size=299008, …}) = 0<br>
writev(2, [{iov_base=“./bin/SlicerApp-real”, iov_len=20}, {iov_base=“: “, iov_len=2}, {iov_base=“error while loading shared libra”…, iov_len=36}, {iov_base=”: “, iov_len=2}, {iov_base<br>
=“libqSlicerApp.so”, iov_len=16}, {iov_base=”: “, iov_len=2}, {iov_base=“cannot open shared object file”, iov_len=30}, {iov_base=”: “, iov_len=2}, {iov_base=“No such file or directory”,<br>
iov_len=25}, {iov_base=”\n”, iov_len=1}], 10./bin/SlicerApp-real: error while loading shared libraries: libqSlicerApp.so: cannot open shared object file: No such file or directory<br>
) = 136<br>
exit_group(127)                         = ?<br>
+++ exited with 127 +++</p>
</blockquote>
<p>It seems it could not find libqSlicerApp.so, file that is present of course.</p>
<p>If I set LD_LIBRARY_PATH to ./lib/Slicer-4.11, it outputs similar results but for every library it tries to load.</p>
<p>Now I don’t have any kind of special setup on that particular machine.</p>
<p>I’m ready to try with a debug build, but won’t be able to do it before a few days.</p>
<p>Thanks.</p>

---

## Post #5 by @lassoan (2019-08-26 15:20 UTC)

<p>Have you executed <code>strace ./bin/SlicerApp-real</code> in a terminal created by <code>./Slicer --launch (your-terminal-executable-here)</code>?</p>

---

## Post #6 by @chir.set (2019-08-26 15:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Have you executed <code>strace ./bin/SlicerApp-real</code></p>
</blockquote>
</aside>
<p>Yes, the result is just <a href="https://discourse.slicer.org/t/cant-start-slicer-on-linux-on-one-machine/8175/4">one post above</a>.</p>

---

## Post #7 by @pieper (2019-08-26 16:50 UTC)

<p>It looks like something is interfering with Slicer’s paths.  Does your environment have any special variables set (e.g. <code>LD_PRELOAD</code>?)</p>

---

## Post #8 by @lassoan (2019-08-26 17:22 UTC)

<p>Could you copy-paste here the value of environment variables you have in the terminal where you attempted to run SlicerApp-real?</p>

---

## Post #9 by @chir.set (2019-08-26 18:27 UTC)

<p>I’ll post the env variables when I get back to work. Thanks.</p>

---

## Post #10 by @chir.set (2019-08-27 06:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>opy-paste here the value of environment variables</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>any special variables</p>
</blockquote>
</aside>
<p>Here are the environment variables in the relevant terminal. All variables are in this sorted list, though some values have been masked.</p>
<blockquote>
<p>_=/bin/env<br>
COLORFGBG=15;0<br>
COLORTERM=truecolor<br>
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1001/bus<br>
DESKTOP_SESSION=/usr/share/xsessions/plasma<br>
DISPLAY=:0<br>
EDITOR=/usr/bin/vim<br>
GS_LIB=/home/user/.fonts<br>
GTK2_RC_FILES=/etc/gtk-2.0/gtkrc:/home/user/.gtkrc-2.0:/home/user/.config/gtkrc-2.0<br>
GTK_MODULES=canberra-gtk-module<br>
GTK_RC_FILES=/etc/gtk/gtkrc:/home/user/.gtkrc:/home/user/.config/gtkrc<br>
HISTCONTROL=ignoreboth:erasedups<br>
HOME=/home/user<br>
KDE_FULL_SESSION=true<br>
KDE_SESSION_UID=1001<br>
KDE_SESSION_VERSION=5<br>
KONSOLE_DBUS_SERVICE=:1.31<br>
KONSOLE_DBUS_SESSION=/Sessions/7<br>
KONSOLE_PROFILE_NAME=Shell<br>
KONSOLE_VERSION=190403<br>
LANG=fr_FR.UTF-8<br>
LANGUAGE=fr<br>
LC_ADDRESS=fr_FR.UTF-8<br>
LC_COLLATE=fr_FR.UTF-8<br>
LC_CTYPE=fr_FR.UTF-8<br>
LC_IDENTIFICATION=fr_FR.UTF-8<br>
LC_MEASUREMENT=fr_FR.UTF-8<br>
LC_MESSAGES=fr_FR.UTF-8<br>
LC_MONETARY=fr_FR.UTF-8<br>
LC_NAME=fr_FR.UTF-8<br>
LC_NUMERIC=fr_FR.UTF-8<br>
LC_PAPER=fr_FR.UTF-8<br>
LC_TELEPHONE=fr_FR.UTF-8<br>
LC_TIME=fr_FR.UTF-8<br>
LL_HP=%eth0<br>
LL_SEC1L=%eth0<br>
LL_SEC1=%eth0<br>
LL_SEC2L=%eth0<br>
LL_SEC2=%eth0<br>
LL_U2=%eth0<br>
LL_U3=%eth0<br>
LL_VASC1=%eth0<br>
LL_VASC2=%eth0<br>
LL_Z2P=%eth0<br>
LOGNAME=user<br>
MAC_SEC1=<br>
MAC_SEC2=<br>
MAC_U2=<br>
MAC_U3=<br>
MAC_VASC1=<br>
MAC_VASC2=<br>
MAIL=/var/spool/mail/user<br>
MOZ_PLUGIN_PATH=/usr/lib/mozilla/plugins<br>
OLDPWD=/home/user<br>
PAM_KWALLET5_LOGIN=/run/user/1001/kwallet5.socket<br>
PATH=/home/user/.bin:/bin:/usr/bin:/usr/local/bin:/usr/local/sbin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl<br>
PROFILEHOME=<br>
PS1=#[\u@\h \W][\033[01;32m][${PIPESTATUS[@]}][\033[00m]$<br>
PWD=/home/user/programs/Slicer-4.11.0-2019-08-22-linux-amd64<br>
QT_AUTO_SCREEN_SCALE_FACTOR=0<br>
QT_SCREEN_SCALE_FACTORS=DisplayPort-0=1;DisplayPort-1=1;DisplayPort-2=1;HDMI-A-0=1;DVI-D-0=1;<br>
SESSION_MANAGER=local/vasc2.chirvasc-60.pro:@/tmp/.ICE-unix/819,unix/vasc2.chirvasc-60.pro:/tmp/.ICE-unix/819<br>
SHELL=/bin/bash<br>
SHELL_SESSION_ID=7659513d5ce046b9b392de66453524a6<br>
SHLVL=2<br>
SSH_AGENT_PID=707<br>
SSH_AUTH_SOCK=/tmp/ssh-vEy99OqlN3Qy/agent.706<br>
TERM=xterm-256color<br>
USER=user<br>
WINDOWID=50331655<br>
XAUTHORITY=/tmp/xauth-1001-_0<br>
XCURSOR_THEME=breeze_cursors<br>
XDG_CONFIG_HOME=/home/user/.config<br>
XDG_CURRENT_DESKTOP=KDE<br>
XDG_DATA_DIRS=/usr/share:/usr/share:/usr/local/share<br>
XDG_RUNTIME_DIR=/run/user/1001<br>
XDG_SEAT_PATH=/org/freedesktop/DisplayManager/Seat0<br>
XDG_SEAT=seat0<br>
XDG_SESSION_CLASS=user<br>
XDG_SESSION_DESKTOP=KDE<br>
XDG_SESSION_ID=c1<br>
XDG_SESSION_PATH=/org/freedesktop/DisplayManager/Session0<br>
XDG_SESSION_TYPE=x11<br>
XDG_VTNR=1<br>
XZ_DEFAULTS=-T0</p>
</blockquote>

---

## Post #11 by @pieper (2019-08-27 12:33 UTC)

<p>Is this the shell where you try to run Slicer?  You should be seeing a lot of Slicer-related environment variables when you start with the launcher.  Like custom PATH and LD_LIBRARY_PATH and APPLAUNCHER variables.</p>
<p>E.g. if you run this command:</p>
<pre><code class="lang-auto">./Downloads/Slicer-4.11.0-2019-08-22-linux-amd64/Slicer --launch env
</code></pre>
<p>Maybe there’s something resetting your environment.</p>
<p>If that’s not the issue you might compare <code>/etc/ld.so.conf</code> and <code>/etc/ld.so.conf.d</code> contents across systems.</p>

---

## Post #12 by @chir.set (2019-08-27 16:19 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>This will give you a log of system calls and typically the last operations will indicate what was going on at the time of the crash</p>
</blockquote>
</aside>
<p>Well, the program ‘xterm’ was not installed on my machine ! Hence all logs I posted above are irrelevant.</p>
<p>Please find the new log data <a href="https://yadi.sk/d/RyqvqQyZewFgZQ" rel="noopener nofollow ugc">here</a>.</p>
<p>Sorry for the inconvenience.</p>

---

## Post #13 by @lassoan (2019-08-27 17:12 UTC)

<p>Could you post strace output and environment that you get on the computer where Slicer starts correctly?</p>

---

## Post #14 by @chir.set (2019-08-27 19:47 UTC)

<p><a href="https://yadi.sk/d/RyqvqQyZewFgZQ" rel="nofollow noopener">Here</a> is the console output for strace and env, on my laptop, where the same Slicer build works fine.</p>
<p>Thanks.</p>

---

## Post #15 by @pieper (2019-08-27 20:00 UTC)

<p>Looks like the same zipfile link twice?</p>

---

## Post #16 by @chir.set (2019-08-27 20:43 UTC)

<p>Oops ! Here’s the right <a href="https://yadi.sk/d/6RaeOS9pcxce2A" rel="nofollow noopener">zip</a> file (tiresome day), sorry.</p>

---

## Post #17 by @pieper (2019-08-27 21:14 UTC)

<p>No worries <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>
<p>Unfortunately I don’t see anything definitive in the traces - maybe something to do with gnutls, which is being accessed right before the crash.  Could be some kind of incompatibility.  Unless you see something probably it makes sense to create a debug build.</p>

---

## Post #18 by @chir.set (2019-08-28 06:52 UTC)

<aside class="quote no-group" data-username="pieper" data-post="17" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>probably it makes sense to create a debug build</p>
</blockquote>
</aside>
<p>I’ll end up doing the debug build, ASAP. For now, I found this in dmesg, everytime I run the problematic build :</p>
<blockquote>
<p>[21639.829126] traps: SlicerApp-real[15453] trap invalid opcode ip:7f8aa07fa1c8 sp:7ffce616fca8 error:0 in libitkgdcmcharls-5.0.so.1[7f8aa07e4000+84000]</p>
</blockquote>
<p>It points out at least one library. ldd on this file does not reveal missing dependency.</p>

---

## Post #19 by @pieper (2019-08-28 18:51 UTC)

<p>Maybe the file is corrupted?  <code>invalid opcode</code> indicates something pretty low level is going on.</p>

---

## Post #20 by @chir.set (2019-09-01 15:40 UTC)

<p>Hi,</p>
<p>I built Slicer in debug mode and it does not crash surprisingly.</p>
<p>Then I built with RelWithDebInfo and this one does not start. I next ran</p>
<blockquote>
<p>./Slicer --launch xterm</p>
</blockquote>
<p>and in the new terminal</p>
<blockquote>
<p>gdb ./bin/SlicerApp-real<br>
Fatal Python error: initsite: Failed to import the site module<br>
Traceback (most recent call last):<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 553, in <br>
main()<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 539, in main<br>
known_paths = addusersitepackages(known_paths)<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 282, in addusersitepackages<br>
user_site = getusersitepackages()<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 258, in getusersitepackages<br>
user_base = getuserbase() # this will also set USER_BASE<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 248, in getuserbase<br>
USER_BASE = get_config_var(‘userbase’)<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/sysconfig.py”, line 601, in get_config_var<br>
return get_config_vars().get(name)<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/sysconfig.py”, line 550, in get_config_vars<br>
_init_posix(_CONFIG_VARS)<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/sysconfig.py”, line 421, in _init_posix<br>
_temp = <strong>import</strong>(name, globals(), locals(), [‘build_time_vars’], 0)<br>
ModuleNotFoundError: No module named ‘_sysconfigdata_m_linux_x86_64-linux-gnu’</p>
</blockquote>
<p>It seems that Python in the Slicer tree is looking for an unknown module in non-debug builds. On this single machine at least.</p>
<p>I’ll be using the debug build, and hope for a fix.</p>
<p>Regards.</p>

---

## Post #21 by @lassoan (2019-09-01 20:01 UTC)

<p>This information is very helpful. Have you tried to google for possible solutions?</p>
<p>For example, this one is interesting:</p>
<aside class="onebox stackexchange">
  <header class="source">
      <a href="https://stackoverflow.com/questions/49921336/sysconfigdata-error-when-trying-to-freeze-a-python-3-6-5-application" target="_blank" rel="nofollow noopener">stackoverflow.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://stackoverflow.com/users/9624420/benjamin-hammond" target="_blank" rel="nofollow noopener">
    <img alt="benjamin.hammond" src="https://www.gravatar.com/avatar/959c770bfc5a95f227d080b24df9d53e?s=128&amp;d=identicon&amp;r=PG&amp;f=1" class="thumbnail onebox-avatar" width="60" height="60">
  </a>
<h4>
  <a href="https://stackoverflow.com/questions/49921336/sysconfigdata-error-when-trying-to-freeze-a-python-3-6-5-application" target="_blank" rel="nofollow noopener">_sysconfigdata error when trying to Freeze a Python 3.6.5 application</a>
</h4>

<div class="tags">
  <strong>python, freeze</strong>
</div>

<div class="date">
  asked by
  
  <a href="https://stackoverflow.com/users/9624420/benjamin-hammond" target="_blank" rel="nofollow noopener">
    benjamin.hammond
  </a>
  on <a href="https://stackoverflow.com/questions/49921336/sysconfigdata-error-when-trying-to-freeze-a-python-3-6-5-application" target="_blank" rel="nofollow noopener">12:37PM - 19 Apr 18 UTC</a>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The problem is that user site packages are attempted to loaded (<code>...user_site = getusersitepackages()...</code>). They shouldn’t be loaded (see <a href="https://github.com/Slicer/Slicer/blob/cbf742277b5b96cb81f66088d2ab2242b15f4a13/Base/QTCore/qSlicerCorePythonManager.cxx#L48-L56" rel="nofollow noopener">here</a>).</p>
<p>Does any of the followings work?</p>
<ol>
<li><code>./PythonSlicer</code></li>
<li><code>./PythonSlicer -s</code></li>
<li><code>./PythonSlicer -S</code></li>
</ol>
<p>Does settings <code>PYTHONNOUSERSITE=1</code> environment variable make any difference?</p>
<p>Can you investigate why user site packages loading is not prevented (by reviewing content and adding print statements to the .py files listed in the call stack)?</p>

---

## Post #22 by @chir.set (2019-09-01 20:22 UTC)

<p>Well my Python knowledge is very scarce. In the --launch(ed) terminal, PythonSlicer {,-s,-S} works.</p>
<p>In that terminal, even launching ‘gdb’ without any argument generates the above mentioned Python errors.</p>
<p>PYTHONNOUSERSITE is already set to 1 in that terminal. Experimented with 0 to no avail.</p>
<p>Blindly, I unset PYTHONHOME, and then I could get a gdb prompt, with this console output :</p>
<details>
<summary>
Console output</summary>
<blockquote>
<p>Reading symbols from bin/SlicerApp-real…<br>
(gdb) r<br>
Starting program: /home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/SlicerApp-real<br>
[Thread debugging using libthread_db enabled]<br>
Using host libthread_db library “/usr/lib/libthread_db.so.1”.<br>
Traceback (most recent call last):<br>
File “/usr/share/gdb/auto-load/usr/lib/libstdc++.so.6.0.26-gdb.py”, line 18, in <br>
import gdb<br>
File “/usr/share/gdb/python/gdb/<strong>init</strong>.py”, line 16, in <br>
import traceback<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/traceback.py”, line 5, in <br>
import linecache<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/linecache.py”, line 11, in <br>
import tokenize<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/tokenize.py”, line 33, in <br>
import re<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/re.py”, line 123, in <br>
import sre_compile<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/sre_compile.py”, line 17, in <br>
assert _sre.MAGIC == MAGIC, “SRE module mismatch”<br>
AssertionError: SRE module mismatch<br>
Traceback (most recent call last):<br>
File “/usr/share/gdb/auto-load/usr/lib/libglib-2.0.so.0.6000.6-gdb.py”, line 2, in <br>
import gdb<br>
File “/usr/share/gdb/python/gdb/<strong>init</strong>.py”, line 16, in <br>
import traceback<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/traceback.py”, line 5, in <br>
import linecache<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/linecache.py”, line 11, in <br>
import tokenize<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/tokenize.py”, line 33, in <br>
import re<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/re.py”, line 123, in <br>
import sre_compile<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/sre_compile.py”, line 17, in <br>
assert _sre.MAGIC == MAGIC, “SRE module mismatch”<br>
AssertionError: SRE module mismatch</p>
<p>Program received signal SIGILL, Illegal instruction.<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
0x00007fffdf555ba5 in v3p_netlib_slamc2_ (Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
beta=beta@entry=0x7fffffffcc48, t=t@entry=0x7fffffffcc40, rnd=rnd@entry=0x7fffffffcc60,<br>
eps=eps@entry=0x7fffdf627884 , emin=emin@entry=0x7fffffffcc50, rmin=rmin@entry=0x7fffdf627880 , emax=0x7fffffffcc58,<br>
rmax=0x7fffdf62787c ) at /home/arc/src/Slicer-SuperBuild/ITK/Modules/ThirdParty/VNL/src/vxl/v3p/netlib/blas/slamch.c:719<br>
719     /home/arc/src/Slicer-SuperBuild/ITK/Modules/ThirdParty/VNL/src/vxl/v3p/netlib/blas/slamch.c: No such file or directory.<br>
(gdb) bt<br>
Python Exception &lt;class ‘AssertionError’&gt; SRE module mismatch:<br>
<span class="hashtag-raw">#0</span>  0x00007fffdf555ba5 in v3p_netlib_slamc2_ (beta=beta@entry=0x7fffffffcc48, t=t@entry=0x7fffffffcc40, rnd=rnd@entry=0x7fffffffcc60,<br>
eps=eps@entry=0x7fffdf627884 , emin=emin@entry=0x7fffffffcc50, rmin=rmin@entry=0x7fffdf627880 , emax=0x7fffffffcc58,<br>
rmax=0x7fffdf62787c ) at /home/arc/src/Slicer-SuperBuild/ITK/Modules/ThirdParty/VNL/src/vxl/v3p/netlib/blas/slamch.c:719<br>
<span class="hashtag-raw">#1</span>  0x00007fffdf5564b0 in v3p_netlib_slamch_ (cmach=cmach@entry=0x7fffdf612923 " ", cmach_len=cmach_len@entry=1)<br>
at /home/arc/src/Slicer-SuperBuild/ITK/Modules/ThirdParty/VNL/src/vxl/v3p/netlib/blas/slamch.c:165<br>
<span class="hashtag-raw">#2</span>  0x00007fffdf5568b1 in v3p_netlib_slamch_init ()<br>
at /home/arc/src/Slicer-SuperBuild/ITK/Modules/ThirdParty/VNL/src/vxl/v3p/netlib/blas/slamch.c:53<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
<span class="hashtag-raw">#3</span>  0x00007fffdf54c3f5 in v3p_netlib_initialize ()<br>
at /home/arc/src/Slicer-SuperBuild/ITK/Modules/ThirdParty/VNL/src/vxl/v3p/netlib/v3p_netlib_init.c:19<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
<span class="hashtag-raw">#4</span>  0x00007ffff7fe279a in call_init.part () from /lib64/ld-linux-x86-64.so.2<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
<span class="hashtag-raw">#5</span>  0x00007ffff7fe28a1 in _dl_init () from /lib64/ld-linux-x86-64.so.2<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
<span class="hashtag-raw">#6</span>  0x00007ffff7fd413a in _dl_start_user () from /lib64/ld-linux-x86-64.so.2<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
<span class="hashtag-raw">#7</span>  0x0000000000000001 in ?? ()<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
<span class="hashtag-raw">#8</span>  0x00007fffffffd28d in ?? ()<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
<span class="hashtag-raw">#9</span>  0x0000000000000000 in ?? ()<br>
Python Exception &lt;class ‘NameError’&gt; Installation error: gdb.execute_unwinders function is missing:<br>
(gdb)</p>
</blockquote>
</details>
<p>dmesg shows this error with libitkv3p_netlib :</p>
<blockquote>
<p>[ 7052.275896] traps: SlicerApp-real[4907] trap invalid opcode ip:7f5e91312ba5 sp:7ffe51239fa0 error:0 in libitkv3p_netlib-5.0.so.1[7f5e912fe000+e4000]</p>
</blockquote>
<p>I understand, perhaps wrongly, that the runtime error  first occurs at</p>
<blockquote>
<p>ITK/Modules/ThirdParty/VNL/src/vxl/v3p/netlib/blas/slamch.c:719</p>
</blockquote>
<p>or at</p>
<blockquote>
<p>ITK/Modules/ThirdParty/VNL/src/vxl/v3p/netlib/v3p_netlib_init.c:19</p>
</blockquote>
<p>Please note that Slicer built in Debug mode runs normally. Slicer crashes when built in Release or in RelWithDebInfo modes only.</p>
<p>Regards.</p>

---

## Post #23 by @lassoan (2019-09-01 21:05 UTC)

<p>There should be no need to change PYTHONHOME (it would just break everything). Instead, add print statements to show values of variables that control usage of user site packages to find out why <code>getusersitepackages</code> is called.</p>
<p>You may also try to clear out your user-specific site.py file (and parent folders) to confirm that it causes the Python startup failure.</p>
<p>Also check out <a href="https://bugs.launchpad.net/ubuntu/+source/python3.3/+bug/1192890" rel="nofollow noopener">this</a> and <a href="https://askubuntu.com/questions/765566/rhythmbox-crashes-due-failed-to-import-the-site-module" rel="nofollow noopener">this</a>.</p>

---

## Post #24 by @chir.set (2019-09-02 07:38 UTC)

<p>I’m quite lost with Python. If I call _main() in lib/Python/lib/python3.6/sysconfig.py at line 421 to get some information, the output is :</p>
<blockquote>
<p>$ gdb<br>
Platform: “linux-x86_64”<br>
Python version: “3.7”<br>
Current installation scheme: “posix_prefix”</p>
<p>Paths:<br>
data = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python”<br>
include = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/include/python3.7m”<br>
platinclude = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/include/python3.7m”<br>
platlib = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.7/site-packages”<br>
platstdlib = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.7”<br>
purelib = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.7/site-packages”<br>
scripts = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/bin”<br>
stdlib = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.7”</p>
<p>Variables:<br>
abiflags = “m”<br>
base = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python”<br>
exec_prefix = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python”<br>
installed_base = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python”<br>
installed_platbase = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python”<br>
platbase = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python”<br>
prefix = “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python”<br>
projectbase = “/usr/bin”<br>
py_version = “3.7.4”<br>
py_version_nodot = “37”<br>
py_version_short = “3.7”<br>
Fatal Python error: initsite: Failed to import the site module<br>
Traceback (most recent call last):<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 553, in <br>
main()<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 539, in main<br>
known_paths = addusersitepackages(known_paths)<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 282, in addusersitepackages<br>
user_site = getusersitepackages()<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 258, in getusersitepackages<br>
user_base = getuserbase() # this will also set USER_BASE<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site.py”, line 248, in getuserbase<br>
USER_BASE = get_config_var(‘userbase’)<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/sysconfig.py”, line 602, in get_config_var<br>
return get_config_vars().get(name)<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/sysconfig.py”, line 551, in get_config_vars<br>
_init_posix(_CONFIG_VARS)<br>
File “/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/lib/Python/lib/python3.6/sysconfig.py”, line 422, in _init_posix<br>
_temp = <strong>import</strong>(name, globals(), locals(), [‘build_time_vars’], 0)<br>
ModuleNotFoundError: No module named ‘_sysconfigdata_m_linux_x86_64-linux-gnu’</p>
</blockquote>
<p>Here system Python 3.7 is being called.</p>
<blockquote>
<p>$ env |grep PYTHON<br>
PYTHONNOUSERSITE=1<br>
PYTHONPATH=/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11:/home/user/programs/Test/Sli<br>
cer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11/qt-scripted-modules:/home/user/programs/Test/Slicer-4.11.0-2019-08-<br>
22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11/qt-loadable-modules:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelW<br>
ithDebInfo-O2/bin/…/lib/vtkTeem:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/bin/Python:/home/user/<br>
programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11/qt-loadable-modules/Python:/home/user/programs/Tes<br>
t/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-lin<br>
ux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/lib-dynload:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDe<br>
bInfo-O2/bin/…/lib/Python/lib/python3.6/site-packages:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/<br>
./lib/Slicer-4.11/python3.6/site-packages<br>
PYTHONHOME=/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python</p>
</blockquote>
<blockquote>
<p>$ env |grep python<br>
PYTHONPATH=/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11:/home/user/programs/Test/Sli<br>
cer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11/qt-scripted-modules:/home/user/programs/Test/Slicer-4.11.0-2019-08-<br>
22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11/qt-loadable-modules:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelW<br>
ithDebInfo-O2/bin/…/lib/vtkTeem:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/bin/Python:/home/user/<br>
programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11/qt-loadable-modules/Python:/home/user/programs/Tes<br>
t/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-lin<br>
ux-amd64-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/lib-dynload:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDe<br>
bInfo-O2/bin/…/lib/Python/lib/python3.6/site-packages:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/<br>
./lib/Slicer-4.11/python3.6/site-packages<br>
LD_LIBRARY_PATH=/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/bin:/home/user/programs/Test/Slicer-4.1<br>
1.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebIn<br>
fo-O2/bin/…/lib/Slicer-4.11/cli-modules:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.1<br>
1/qt-loadable-modules:…/lib/Slicer-4.11/qt-loadable-modules:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/b<br>
in/…/lib/Python/lib:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/Teem-1.12.0:/home/user/program<br>
s/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/lib/PythonQt:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd6<br>
4-RelWithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site-packages/numpy/core:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-Rel<br>
WithDebInfo-O2/bin/…/lib/Python/lib/python3.6/site-packages/numpy/lib</p>
</blockquote>
<blockquote>
<p>$ echo $PATH<br>
/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/…/bin:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-l<br>
inux-amd64-RelWithDebInfo-O2/bin/…/lib/Slicer-4.11/cli-modules:/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O<br>
2/bin/…/lib/Slicer-4.11/qt-loadable-modules:/home/user/.bin:/bin:/usr/bin:/usr/local/bin:/usr/local/sbin:/usr/lib/jvm/default/bin:/usr/bin/si<br>
te_perl:/usr/bin/vendor_perl:/usr/bin/core_perl</p>
</blockquote>
<p>Can’t know how to interpret all these.</p>
<p>Trying with lldb :</p>
<blockquote>
<p>$ lldb ./bin/SlicerApp-real<br>
(lldb) target create “./bin/SlicerApp-real”<br>
Current executable set to ‘./bin/SlicerApp-real’ (x86_64).<br>
(lldb) r<br>
Process 13686 launched: ‘/home/user/programs/Test/Slicer-4.11.0-2019-08-22-linux-amd64-RelWithDebInfo-O2/bin/SlicerApp-real’ (x86_64)<br>
Process 13686 stopped</p>
<ul>
<li>thread <span class="hashtag-raw">#1</span>, name = ‘SlicerApp-real’, stop reason = signal SIGILL: illegal instruction operand<br>
frame <span class="hashtag-raw">#0:</span> 0x00007fffdf555ba5 libitkv3p_netlib-5.0.so.1`v3p_netlib_slamc2_(beta=0x00007fffffffc0a8, t=0x00007fffffffc0a0, rnd=0x00007fffffffc0c0, eps=0x00007fffdf627884, emin=0x00007fffffffc0b0, rmin=0x00007fffdf627880, emax=0x00007fffffffc0b8, rmax=0x00007fffdf62787c) at slamch.c:719:11<br>
(lldb) bt</li>
<li>thread <span class="hashtag-raw">#1</span>, name = ‘SlicerApp-real’, stop reason = signal SIGILL: illegal instruction operand
<ul>
<li>frame <span class="hashtag-raw">#0:</span> 0x00007fffdf555ba5 libitkv3p_netlib-5.0.so.1<code>v3p_netlib_slamc2_(beta=0x00007fffffffc0a8, t=0x00007fffffffc0a0, rnd=0x00007fffffffc0c0, eps=0x00007fffdf627884, emin=0x00007fffffffc0b0, rmin=0x00007fffdf627880, emax=0x00007fffffffc0b8, rmax=0x00007fffdf62787c) at slamch.c:719:11 frame #1: 0x00007fffdf5564b0 libitkv3p_netlib-5.0.so.1</code>v3p_netlib_slamch_(cmach=" ", cmach_len=) at slamch.c:165:9<br>
frame <span class="hashtag-raw">#2:</span> 0x00007fffdf54c3f5 libitkv3p_netlib-5.0.so.1<code>v3p_netlib_initialize at v3p_netlib_init.c:19:5 frame #3: 0x00007ffff7fe279a ld-2.29.so</code>call_init.part.0 + 154<br>
frame <span class="hashtag-raw">#4:</span> 0x00007ffff7fe28a1 ld-2.29.so<code>_dl_init + 129 frame #5: 0x00007ffff7fd413a ld-2.29.so</code>_dl_start_user + 50</li>
</ul>
</li>
</ul>
</blockquote>

---

## Post #25 by @lassoan (2019-09-19 18:32 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="18" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>[21639.829126] traps: SlicerApp-real[15453] trap invalid opcode ip:7f8aa07fa1c8 sp:7ffce616fca8 error:0 in libitkgdcmcharls-5.0.so.1[7f8aa07e4000+84000]</p>
</blockquote>
</aside>
<p>I think we run into the same problem on a very old computer (with Intel Core i7-3770 CPU) running Windows 10.</p>
<p>Slicer does not start but instead this error is shown in a popup:</p>
<pre><code>The application was unable to start correctly (0xc0000142). Click OK to close the application
</code></pre>
<p>Windows application log tells that it is an exception 0xc000001d (Illegal instruction) in ITKIOGDCM-5.1.dll. Attaching a debugger and looking at the disassembly I found that indeed there was an <code>shlx</code> instruction where the exception was thrown, which is a <a href="https://en.wikipedia.org/wiki/Bit_Manipulation_Instruction_Sets#BMI2_(Bit_Manipulation_Instruction_Set_2)">BMI2 instruction</a> that is not supported in 3rd-generation (3xxx, Ivy Bridge) CPUs but only in 4th generation (4xxx, Haswell) and later.</p>
<p><a class="mention" href="/u/chir.set">@chir.set</a> Can you confirm that you had this problem on a 3rd-generation CPU?</p>
<p>We should either change build options to disable using BMI2 instruction set or check CPU type in the launcher and show a warning if non-compatible CPU is found. I’ve created an issue for this to make sure we follow up: <a href="https://issues.slicer.org/view.php?id=4712" class="inline-onebox">Slicer fails to start in Intel Ivy Bridge or older CPUs · Issue #4712 · Slicer/Slicer · GitHub</a></p>

---

## Post #26 by @muratmaga (2019-09-19 19:22 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I wonder if this the same/similar issue I have been encountering our old Sandy Bridge (Xeon E5-1620) computers that were recently updated to Windows 10 from Windows 7? Slicer preview versions used to work fine, and now getting and error message</p><aside class="quote" data-post="4" data-topic="8410">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/application-unable-to-start-correctly-0xc0000142-error/8410/4">Application unable to start correctly (0xc0000142) error</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This was a windows 7 computer with a working Slicer that was recently migrated to Windows 10. It must be some sort of a corporate user policy change that probably broke the functionality. I managed to install other new programs (e.g., TurboVNC etc) that all seem to work. 
It will be hard to chase, so I will just have them do a fresh reinstall of OS.
  </blockquote>
</aside>

<p>Is there a work around? We really don’t toss them out as they are fairly usable computers.</p>

---

## Post #27 by @lassoan (2019-09-19 19:26 UTC)

<p>Yes, it’s exactly the same error.</p>
<p>I would tend towards dropping support for these 6-8 years old computers. It’s not just the CPU instruction set but graphics card features are very limited, too (VTK’s OpenGL2 backend is not compatible with these old systems anyway).</p>

---

## Post #28 by @muratmaga (2019-09-19 19:27 UTC)

<p>himm. Actually they have all 1080Ti on them, as they have discrete GPUs that we can upgrade (as the power supply permitting).</p>

---

## Post #29 by @chir.set (2019-09-19 21:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you confirm that you had this problem on a 3rd-generation CPU?</p>
</blockquote>
</aside>
<p>It’s an old AMD Phenom II X6 1100T CPU. It has 20+ instruction sets missing compared to recent CPUs.</p>
<p>However, Slicer build and runs with the following tuning :</p>
<blockquote>
<p>-march=amdfam10 -mtune=amdfam10 -mno-sse4.1 -mno-sse4.2 (CFLAGS, CXXFLAGS, ADDITIONAL_CXX_FLAGS)</p>
</blockquote>
<p>The funny part is that when built with GCC 9.1, it crashes when reading the first DICOM file. I can get the backtrace later on if it’s of importance.</p>
<p>But Slicer just behaves normally when built with clang 8, using the same options. I gave it a blast today and it was rock solid. For how long ? I can also just change my work machine or the CPU, but that’s not scheduled for now.</p>
<p>Regards.</p>

---

## Post #30 by @chir.set (2019-09-19 21:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="27" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would tend towards dropping support for these 6-8 years old computers.</p>
</blockquote>
</aside>
<p>But the build itself can be tuned ! Dropping support won’t help anyone downloading binaries from your repository. The rationale of doing the extra work to drop support for old CPUs is not that clear.</p>

---

## Post #31 by @lassoan (2019-09-19 23:03 UTC)

<p>We have a few options:</p>
<ul>
<li>A: Tune the build options to not take advantage of new instruction sets and so potentially lose some performance/power optimization possibilities in current CPUs.</li>
<li>B. Improve CPU/GPU checks at startup to detect incompatible hardware and advise users to upgrade. This might not be very simple when a library crashes in its automatic initialization step (execution of the main application does not even start).</li>
<li>C. Do nothing. This may discourage some potential users.</li>
</ul>
<p>C is the easiest to do (we are already doing it), but A or B would be of course better.</p>
<p>Probably disabling recent instruction sets would not cause significant performance degradation, so if someone prepared a pull request with the necessary compilation flag changes then we would integrate them.</p>

---

## Post #32 by @muratmaga (2019-09-19 23:27 UTC)

<p>These are my observations with today’s nightly :</p>
<p>Win 10 + E5-1620 gives the stated error.<br>
Centos 7.6 + E5-2690 works fine.<br>
(I will report on the Centos 7.6 + E5-1620 combination tomorrow).</p>
<p>These two CPUs are from the same generation. Are optimization flags OS specific?</p>

---

## Post #33 by @lassoan (2019-09-20 00:27 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="32" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Are optimization flags OS specific?</p>
</blockquote>
</aside>
<p>Even worse, they are compiler-specific. It should be possible to find the right set of options for each toolchain but it may require a lot of iterations. By the time we get everything right (safely work on most systems but not to degrade performance on current systems), most of the old computers may be decommissioned.</p>
<p>I’ve checked recent ITK changes and maybe they messed up something there that can be reverted without too much pain. I’ve <a href="https://discourse.itk.org/t/itk5-crashes-in-gdcm-on-older-cpus/2250/2?u=lassoan">reported the issue to their forum</a>.</p>

---

## Post #34 by @muratmaga (2019-09-23 17:19 UTC)

<p>Did the discussion on ITK forum conclude for a course of action?</p>

---

## Post #35 by @lassoan (2019-09-23 18:29 UTC)

<p>I’m testing a solution (setting ITK_*_OPTIMIZATION_FLAGS to empty in Slicer superbuild). Once I confirm that it works, I’ll send a pull request. Probably tomorrow.</p>

---

## Post #36 by @lassoan (2019-09-24 03:16 UTC)

<p>Confirmed the fix works on Windows. Commited in rev28520.</p>

---

## Post #37 by @gaoyi.cn (2019-10-31 01:57 UTC)

<p>I have the same issue recently:<br>
Under Linux Mint 19.2 (Ubuntu 18.04), with Slicer trunk on 20191031<br>
Here are what I trid:</p>
<ol>
<li>i tried both gcc 7.4 and gcc-6</li>
<li>I tried release, debug, relwithdebinfo, all have the same result</li>
<li>i changed the libarchive/archive_pack_dev.c suggested by Steve in <a href="https://issues.slicer.org/view.php?id=4616" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4616</a>
</li>
<li>The CPU is Intel® Core™ i7-7700HQ CPU so I also comment out ITK_*_OPTIMIZATION_FLAGS suggested by Andras</li>
</ol>
<p>But with no luck…</p>
<p>I ran:<br>
./Slicer --launch mate-terminal<br>
then in the term:<br>
strace SlicerApp-real<br>
I got ( the last part):</p>
<p>close(18)                               = 0<br>
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)<br>
openat(AT_FDCWD, “/usr/lib/x86_64-linux-gnu/libssl.so.1.1”, O_RDONLY|O_CLOEXEC) = 18<br>
read(18, “\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0&gt;\0\1\0\0\0\220\325\1\0\0\0\0\0”…, 832) = 832<br>
fstat(18, {st_mode=S_IFREG|0644, st_size=577312, …}) = 0<br>
mmap(NULL, 2673024, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 18, 0) = 0x7fc2856d1000<br>
mprotect(0x7fc285751000, 2097152, PROT_NONE) = 0<br>
mmap(0x7fc285951000, 53248, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 18, 0x80000) = 0x7fc285951000<br>
close(18)                               = 0<br>
mprotect(0x7fc285951000, 36864, PROT_READ) = 0<br>
munmap(0x7fc285e29000, 109229)          = 0<br>
futex(0x7fc285e27810, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e27804, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e278d8, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e277f0, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e277e8, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e25c7c, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e276c4, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e2765c, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e27650, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e277fc, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e277b8, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
futex(0x7fc285e277b0, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
openat(AT_FDCWD, “/usr/lib/ssl/openssl.cnf”, O_RDONLY) = 18<br>
fstat(18, {st_mode=S_IFREG|0644, st_size=10998, …}) = 0<br>
read(18, “#\n# OpenSSL example configuratio”…, 4096) = 4096<br>
read(18, “tableString, T61String (no BMPSt”…, 4096) = 4096<br>
read(18, “eting an end user certificate as”…, 4096) = 2806<br>
read(18, “”, 4096)                      = 0<br>
close(18)                               = 0<br>
futex(0x7fc285e277e0, FUTEX_WAKE_PRIVATE, 2147483647) = 0<br>
— SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=NULL} —<br>
+++ killed by SIGSEGV (core dumped) +++<br>
Segmentation fault (core dumped)</p>
<p>Could I have some direction to try on?</p>
<p>Thanks!</p>

---

## Post #38 by @gaoyi.cn (2019-10-31 04:00 UTC)

<p>Solved using ssl:</p><aside class="quote quote-modified" data-post="10" data-topic="5627">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bcef8e/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/building-slicer-on-a-freshly-installed-ubuntu-18-04/5627/10">Building Slicer on a freshly installed Ubuntu 18.04</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Here is what I am getting when I execute gdb with bin/SlicerApp-real: 
(gdb) exec-file SlicerApp-real 
(gdb) run 
Starting program: /home/satya/wrk/Slicer/build/Slicer-build/bin/SlicerApp-real 
[Thread debugging using libthread_db enabled] 
Using host libthread_db library “/lib/x86_64-linux-gnu/libthread_db.so.1”. 
[New Thread 0x7fffad95a700 (LWP 8620)] 
qt5ct: using qt5ct plugin 
[New Thread 0x7fffa59e1700 (LWP 8621)] 
[New Thread 0x7fffa5127700 (LWP 8622)] 
Thread 1 “SlicerApp-real” received s…
  </blockquote>
</aside>


---

## Post #39 by @gaoyi.cn (2019-10-31 07:32 UTC)

<p>with the very same ( i think) environment, i tried to repeat the success in an adjacent folder, just to make sure I really got it right. But this time the building stopped in the middle due to the python site module problem.</p>
<p>And i just realized that even for the “success build” i have, it actually is not so right: the numpy is not loaded:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/media/pv/data/pv/usr/work/namic/rls20191029/Slicer-sb/python-install/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/media/pv/data/pv/usr/work/namic/rls20191029/Slicer-sb/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 1, in <br>
import numpy<br>
ModuleNotFoundError: No module named ‘numpy’<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/media/pv/data/pv/usr/work/namic/rls20191029/Slicer-sb/python-install/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/media/pv/data/pv/usr/work/namic/rls20191029/Slicer-sb/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/Editor.py”, line 4, in <br>
import EditorLib<br>
File “/media/pv/data/pv/usr/work/namic/rls20191029/Slicer-sb/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/EditorLib/<strong>init</strong>.py”, line 37, in <br>
exec(“from .{0} import {0}Options, {0}Tool, {0}Logic, {0}”.format(effectName))<br>
File “”, line 1, in <br>
File “/media/pv/data/pv/usr/work/namic/rls20191029/Slicer-sb/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/EditorLib/PaintEffect.py”, line 10, in <br>
import numpy<br>
ModuleNotFoundError: No module named ‘numpy’<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “/media/pv/data/pv/usr/work/namic/rls20191029/Slicer-sb/python-install/lib/python3.6/imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “/media/pv/data/pv/usr/work/namic/rls20191029/Slicer-sb/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 5, in <br>
import vtk.util.numpy_support<br>
File “/media/pv/data/pv/usr/work/namic/rls20191029/Slicer-sb/VTK-build/lib/python3.6/site-packages/vtkmodules/util/numpy_support.py”, line 31, in <br>
import numpy<br>
ModuleNotFoundError: No module named ‘numpy’<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘numpy’ is not defined</p>
<p>I’m investigating and will report back</p>

---

## Post #40 by @Leon (2019-10-31 11:50 UTC)

<p>I quickly run through this topic and I see that people build Slicer on their linux computer.<br>
My question is ‘Why?’</p>
<p>I also run Slicer on a linux machine (LinuxMint 19.1) and I have <strong>never</strong> build it on that!<br>
Just downloaded the linux package from the site, unpacked it in a folder called ‘Slicer’ and then run the  executable ‘slicer’.<br>
That’s it!</p>

---

## Post #41 by @chir.set (2019-10-31 12:44 UTC)

<aside class="quote no-group" data-username="Leon" data-post="40" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>then run the executable ‘slicer’.<br>
That’s it!</p>
</blockquote>
</aside>
<p>You have probably not used it long enough to say ‘Ooops! what’s happening ? Where is Slicer ?’. That happened twice to me, building it was the only way in these situations.</p>

---

## Post #42 by @lassoan (2019-10-31 12:54 UTC)

<p>It is quite likely that the same Slicer binaries don’t work correctly on all Linux flavours and configurations, but I guess most Linux users chose the platform because they prefer to have more control over their systems and got used to building components on their own.</p>

---

## Post #43 by @pieper (2019-10-31 13:54 UTC)

<p>Yes, and those same Linux systems tend to have variability in compiler versions and directory layouts, so some build issues can be expected from time to time.  It’s actually kind of remarkable that some much works well most of the time.</p>

---

## Post #44 by @Leon (2019-10-31 13:57 UTC)

<p>Ever thought about distributing Slicer as a Flatpak? <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"><br>
<a href="https://flatpak.org/" class="onebox" target="_blank" rel="nofollow noopener">https://flatpak.org/</a></p>
<p>Other software packages also use this (check it out for yourself).</p>

---

## Post #45 by @gaoyi.cn (2019-10-31 14:40 UTC)

<p>coz i’m developing based on Slicer. that needs building from source.</p>

---

## Post #46 by @pieper (2019-10-31 18:07 UTC)

<aside class="quote no-group" data-username="Leon" data-post="44" data-topic="8175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>Ever thought about distributing Slicer as a Flatpak?</p>
</blockquote>
</aside>
<p>Yes, and there’s also <a href="https://snapcraft.io/">https://snapcraft.io/</a>.  Could be handy if anyone wants to take it on.</p>
<p>But realistically it hasn’t come up that often - the linux binaries we build seem to be pretty compatible with the distributions I use anyway.</p>

---

## Post #47 by @gaoyi.cn (2019-11-02 02:19 UTC)

<p>by usnig strace SlicerApp-real, it seems that slicer is searching for libssl.so.1.1 in many places, with no luck.</p>
<p>However, in the entire superbuilld dir, i found ssl lib in:<br>
./OpenSSL/libssl.so.1.0.0</p>
<p>Also in cmake, the default ssl version is 1.0.2n</p>
<p>I’m trying to see where in the process the 1.1 is requested…</p>

---

## Post #48 by @gaoyi.cn (2019-11-02 06:56 UTC)

<p>Hi Steve, Hi Andras,  <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I believed the problem on my machine was that python needs openssl 1.1.0 and up. I then upgraded openssl super build version to 1.1.1d. It then requires curl to be upgraded to 7.66, which I did, and it worked.</p>
<p>I believe this may be related with several recent issues:</p>
<ul>
<li>
<a href="https://discourse.slicer.org/t/building-slicer-on-a-freshly-installed-ubuntu-18-04/5627/10" class="inline-onebox">Building Slicer on a freshly installed Ubuntu 18.04</a><br>
Initially I though this solves the problem (using both system ssl and curl). But though Slicer built, it doesn’t work properly: numpy can’t be imported.</li>
<li><a href="https://issues.slicer.org/view.php?id=4617" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4617</a></li>
<li>
<a href="https://discourse.slicer.org/t/slicer-crash-on-fresh-build/351" class="inline-onebox">Slicer crash on fresh build</a><br>
I had the same problem. I though it was a python problem. But latter found the problem is ssl</li>
</ul>
<p>Now I have a freshly built Slicer…</p>

---

## Post #49 by @lassoan (2019-11-03 02:11 UTC)

<p>It is great that you were able to figure out all these and thank you very much for sharing the results.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Can you make the necessary changes in Slicer’s build system?</p>

---

## Post #50 by @pieper (2019-11-03 18:13 UTC)

<p><a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> Yes, nice work Yi!  Is there a chance you could make a pull request with the needed changes?</p>

---

## Post #51 by @pieper (2019-11-03 18:20 UTC)

<p>Oops, I see you already made a PR  <a href="https://github.com/Slicer/Slicer/pull/1245/files">https://github.com/Slicer/Slicer/pull/1245/files</a></p>
<p><a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> are these the right fixes?  I’m curious why you closed it.</p>

---

## Post #53 by @gaoyi.cn (2019-11-14 11:12 UTC)

<p>Hi Steve,</p>
<p>I recently did many test builds on different machines under different internet connection conditions. I believe the proposed changes does solve my problem. So I put them together and create a new pull request. Please advice.</p>
<p>Thanks!<br>
yi</p>

---

## Post #54 by @pieper (2019-11-19 21:10 UTC)

<p>Hi Yi -</p>
<p>Were you doing a debug build or a release build?  For me (debug build on mac), with the new curl the library had an extra <code>-d</code> in the filename and I could only link if I renamed the file.</p>
<p>See: <a href="https://github.com/Slicer/Slicer/pull/1260">https://github.com/Slicer/Slicer/pull/1260</a></p>
<p>-Steve</p>

---

## Post #55 by @gaoyi.cn (2019-11-20 08:50 UTC)

<p>HI Steve,</p>
<p>I did release build before. Let me try a Debug build on linux.</p>
<p>Previously, the configuration for building a static curl was by "      -DCURL_STATICLIB:BOOL=ON" in the SuperBuild/External_curl.cmake file.</p>
<p>After changing to the newer version, this flag was not recognized. Changing to<br>
-DBUILD_SHARED_LIBS:BOOL=OFF<br>
solved my problem in release build on LInux.</p>
<p>Let me try debug and report back.</p>
<p>yi</p>

---

## Post #56 by @gaoyi.cn (2019-11-21 08:22 UTC)

<p>Hi Steve,</p>
<p>Yes I reproduced your building error in Debug mode.</p>
<p>Moreover, in the debug mode, the libArchive has to be changed following your suggestion in<br>
<a href="https://issues.slicer.org/view.php?id=4616" class="onebox" target="_blank" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4616</a></p>
<p>I’m investigating the libcurl-d.a the “-d” problem and will report back.</p>
<p>–yi</p>

---

## Post #57 by @lassoan (2019-11-21 12:39 UTC)

<p>I’ve updated Slicer’s LibArchive version a few days ago. Manual patching should not be necessary anymore.</p>

---

## Post #58 by @gaoyi.cn (2019-11-24 10:51 UTC)

<p>Hi Steve,</p>
<p>The curl lib is modified (slightly) so the debug build does not post-fix the “-d”. I’ll create another pull request.</p>
<p>Now it builds on both debug and release modes.</p>
<p>Best,<br>
yi</p>

---

## Post #59 by @bpycinski (2020-01-21 12:33 UTC)

<p>Hello, I faced the same errors as <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a>, on Linux Mint 19, latest git commit, Debug version. But my problem resulted from using system Qt libraries (5.9.5). Change to 5.11.3 from <a href="https://download.qt.io/archive/qt/" rel="nofollow noopener">https://download.qt.io/archive/qt/</a> solved the problem.</p>
<p>I just mention it, if anyone else would fall into this issue.</p>

---
