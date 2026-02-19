---
topic_id: 14224
title: "Ubuntu 20 10 Cannot Run Previously Working Slicer Version"
date: 2020-10-24
url: https://discourse.slicer.org/t/14224
---

# Ubuntu 20.10 cannot run previously working Slicer version

**Topic ID**: 14224
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/ubuntu-20-10-cannot-run-previously-working-slicer-version/14224

---

## Post #1 by @Greydon_Gilmore (2020-10-24 15:21 UTC)

<p>Hello,</p>
<p>I have been using 3D Slicer v4.10.2 on Ubuntu 20.04 without issue. After upgrading to Ubuntu 20.10, 3D Slicer fails at the splash screen.</p>
<p>Are there critical libraries that might be missing between Ubuntu versions?</p>

---

## Post #2 by @pieper (2020-10-24 15:40 UTC)

<p>Do the extra installs listed here help? <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux</a></p>

---

## Post #3 by @Greydon_Gilmore (2020-10-24 15:43 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>I ran those dependency installs right after upgrading to 20.10 so it seems they are not the issue.</p>

---

## Post #4 by @lassoan (2020-10-24 16:09 UTC)

<p>Make sure xinerama is installed. That seems to be a common issue for recent Ubuntu and Qt versions.</p>

---

## Post #5 by @Greydon_Gilmore (2020-10-24 18:03 UTC)

<p>I have tried uninstalling and re-installing xinerama but v4.10.2 still does not load</p>

---

## Post #6 by @lassoan (2020-10-24 18:50 UTC)

<p>Please use the latest stable (currently Slicer-4.11.20200930) and let us knw if it works any better.</p>

---

## Post #7 by @Greydon_Gilmore (2020-10-24 19:01 UTC)

<p>yes the latest stable is working. I still require v4.10.2 to run as well (previous workflows rely on this backend). I’m not sure what Slicer v4.10.2 is missing between Ubuntu 20.04 and 20.10.</p>
<p>Should I try to build from  v4.10.2 source?</p>

---

## Post #8 by @lassoan (2020-10-24 19:39 UTC)

<p>I would not recommend spending time with trying to make the old stable version work. Latest stable version contains so many fixes and improvements that even if you could make the old version work, you would need to switch to the new version for various other reasons. Is there anything specific that is missing/does not work in the latest stable?</p>

---

## Post #9 by @lassoan (2020-10-25 00:34 UTC)

<p>10 posts were split to a new topic: <a href="/t/updating-modules-from-slicer-4-10-to-slicer-4-11/14230">Updating modules from Slicer-4.10 to Slicer-4.11</a></p>

---

## Post #12 by @pieper (2020-10-24 20:50 UTC)

<p>If you want to try debugging some more, try <code>Slicer --launch xterm</code> and then look at the output from running <code>SlicerApp-real</code> in that window.  You might also try <code>ldd $(which SlicerApp-real)</code> to see what libraries it might be missing.  Also <code>strace $(which SlicerApp-real)</code> will give an idea what it was doing when it died (may need to install <code>strace</code> first).</p>

---

## Post #13 by @Greydon_Gilmore (2020-10-24 22:17 UTC)

<p>I ran xterm.<br>
running <code>SlicerApp-real</code> returned:</p>
<pre><code class="lang-auto">[1]    2227884 abort (core dumped)  ./bin/SlicerApp-real
</code></pre>
<p>running <code>ldd $(which SlicerApp-real)</code> did not return any missing libraries.</p>
<p>running <code>strace $(which SlicerApp-real)</code> I wasn’t sure how to interpret the output. The last bit of output returned:</p>
<pre><code class="lang-auto">openat(AT_FDCWD, "/proc/self/status", O_RDONLY) = 42
fstat(42, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(42, "Name:\tSlicerApp-real\nUmask:\t0002"..., 1024) = 1024
read(42, "t:\t0-7\nMems_allowed:\t00000000,00"..., 1024) = 393
read(42, "", 1024)                      = 0
close(42)                               = 0
statfs("/selinux", 0x7ffed2edbb10)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/proc/mounts", O_RDONLY) = 42
fstat(42, {st_mode=S_IFREG|0444, st_size=0, ...}) = 0
read(42, "sysfs /sys sysfs rw,nosuid,nodev"..., 1024) = 1024
read(42, "f rw,nosuid,nodev,noexec,relatim"..., 1024) = 1024
read(42, "=0,minproto=5,maxproto=5,direct,"..., 1024) = 1024
read(42, "nn-vulkan/86 squashfs ro,nodev,r"..., 1024) = 1024
read(42, "/1880 squashfs ro,nodev,relatime"..., 1024) = 1024
read(42, "uid,nodev,relatime,user_id=1000,"..., 1024) = 1024
read(42, "ypt_aux_mnt1 fuse.veracrypt rw,n"..., 1024) = 226
read(42, "", 1024)                      = 0
close(42)                               = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7efeac000000
rt_sigprocmask(SIG_UNBLOCK, [ABRT], NULL, 8) = 0
rt_sigprocmask(SIG_BLOCK, ~[RTMIN RT_1], [], 8) = 0
getpid()                                = 2229838
gettid()                                = 2229838
tgkill(2229838, 2229838, SIGABRT)       = 0
rt_sigprocmask(SIG_SETMASK, [], NULL, 8) = 0
--- SIGABRT {si_signo=SIGABRT, si_code=SI_TKILL, si_pid=2229838, si_uid=1000} ---
+++ killed by SIGABRT (core dumped) +++
[1]    2229835 abort (core dumped)  strace $(which SlicerApp-real)
</code></pre>

---

## Post #14 by @lassoan (2020-10-25 01:02 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/updating-modules-from-slicer-4-10-to-slicer-4-11/14230/11">Updating modules from Slicer-4.10 to Slicer-4.11</a></p>

---

## Post #15 by @surajpaib (2021-01-21 00:04 UTC)

<p>I’m having similar troubles with the latest (stable) version of Slicer. I’m on PopOS 20.10.</p>
<p>Tried running xterm and strace as mentioned earlier on this post with similar-looking output. I can however run Slicer normally if I disable python. I do need python on my Slicer install so I’m wondering if you managed to find a fix for the issue you had.</p>
<p>I’m not familiar enough with the slicer build to debug this python-related issue better. Any guidance on that front would be much appreciated as well</p>

---

## Post #16 by @lassoan (2021-01-21 00:22 UTC)

<p>SlicerApp-real must be run using the <code>./Slicer</code> launcher, which sets up the runtime environment (similarly to other virtual Python environments) before it starts the application.</p>
<p>All other tools must be run using <code>./Slicer --launch ...</code>.</p>
<p>Could you get the stack trace (backtrace) of the crash? (strace prints a list of system calls, which is not that useful for investigating crashes)</p>

---

## Post #17 by @surajpaib (2021-01-21 00:44 UTC)

<p>Thanks for the super quick response! I have indeed been running Slicer as you’ve pointed out. Here is a snippet of the backtrace I obtained by running -<br>
<code>./Slicer --launch gdb ./bin/SlicerApp-real</code> as mentioned in debug instructions.</p>
<pre><code class="lang-auto">Fatal Python error: init_import_size: Failed to import the site module
Python runtime state: initialized
Traceback (most recent call last):
  File "/home/suraj/Repositories/tools/Slicer-4.11.20200930-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 553, in &lt;module&gt;
    main()
  File "/home/suraj/Repositories/tools/Slicer-4.11.20200930-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 539, in main
    known_paths = addusersitepackages(known_paths)
  File "/home/suraj/Repositories/tools/Slicer-4.11.20200930-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 282, in addusersitepackages
    user_site = getusersitepackages()
  File "/home/suraj/Repositories/tools/Slicer-4.11.20200930-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 258, in getusersitepackages
    user_base = getuserbase() # this will also set USER_BASE
  File "/home/suraj/Repositories/tools/Slicer-4.11.20200930-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 248, in getuserbase
    USER_BASE = get_config_var('userbase')
  File "/home/suraj/Repositories/tools/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/sysconfig.py", line 601, in get_config_var
    return get_config_vars().get(name)
  File "/home/suraj/Repositories/tools/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/sysconfig.py", line 550, in get_config_vars
    _init_posix(_CONFIG_VARS)
  File "/home/suraj/Repositories/tools/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/sysconfig.py", line 421, in _init_posix
    _temp = __import__(name, globals(), locals(), ['build_time_vars'], 0)
ModuleNotFoundError: No module named '_sysconfigdata__linux_x86_64-linux-gnu'
</code></pre>
<p>Tried checking out a bit on this but it seems to be a bit of a dead search (with my knowledge)</p>

---

## Post #18 by @lassoan (2021-01-21 01:09 UTC)

<aside class="quote no-group" data-username="surajpaib" data-post="17" data-topic="14224">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/surajpaib/48/8719_2.png" class="avatar"> surajpaib:</div>
<blockquote>
<p><code>ModuleNotFoundError: No module named '_sysconfigdata__linux_x86_64-linux-gnu'</code></p>
</blockquote>
</aside>
<p>We’ve seen this error a couple of times.</p>
<p>Do you have anaconda installed? (see <a href="https://discourse.slicer.org/t/im-getting-not-a-useful-error-when-i-try-to-start-slicer-jupyter-kernel-how-to-debug/13530/12">here</a> and <a href="https://github.com/conda/conda/issues/6836">here</a> and error reports at many other places)</p>

---

## Post #19 by @RafaelPalomar (2021-01-21 09:14 UTC)

<p><a class="mention" href="/u/greydon_gilmore">@Greydon_Gilmore</a> have a look at this post <a href="https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029/19">https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029/19</a></p>
<p>Common causes for Slicer crashing on linux are:</p>
<ul>
<li>Mismatch between the OS OpenSSL version and 3D Slicer version. Check that OpenSSL 1.1.1g is available in the CMake options when you build it (it was added at some point, but not sure it was at 4.10.2)</li>
<li>Incompatibility with libffi (see indicated post).</li>
</ul>
<p>I hope it helps. But as <a class="mention" href="/u/lassoan">@lassoan</a> mentioned, building old releases of Slicer in new OSs can be challenging. You would be better off migrating to recent OS and Slicer versions.</p>

---

## Post #20 by @surajpaib (2021-01-21 16:02 UTC)

<p>I did check for a conda environment issue but the issue still persisted. ( Removed conda set environment variables and tried as well. PythonSlicer works perfectly.)</p>
<p>Ended up spending a considerable amount of time, followed by giving up and reverting to PopOS! 20.04</p>
<p>Works without an issue now. (Incase it helps someone in my exact position)</p>
<p>Thanks for your help <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
