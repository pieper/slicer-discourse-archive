# Bad defines in archive_pack_dev.c

**Topic ID**: 5902
**Date**: 2019-02-24
**URL**: https://discourse.slicer.org/t/bad-defines-in-archive-pack-dev-c/5902

---

## Post #1 by @wvxvw (2019-02-24 13:49 UTC)

<p>Operating system: Xubuntu 18 LTS<br>
Slicer version: 4.10.1<br>
Expected behavior: Slicer compiles<br>
Actual behavior: Slicer doesn’t compile</p>
<p>/home/wvxvw/src/Slicer/Slicer-SuperBuild-Debug/LibArchive/libarchive/archive_pack_dev.c:114:13: error: In the GNU C Library, “minor” is defined<br>
by &lt;sys/sysmacros.h&gt;. For historical compatibility, it is<br>
currently defined by &lt;sys/types.h&gt; as well, but we plan to<br>
remove this soon. To use “minor”, include &lt;sys/sysmacros.h&gt;<br>
directly. If you did not intend to use a system-defined macro<br>
“minor”, you should undefine it after including &lt;sys/types.h&gt;. [-Werror]<br>
else if ((unsigned long)minor(dev) != numbers[1])<br>
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>
<p>This error comes from generated code, and I’m not familiar enough with CMake / the project’s structure to be able to fix it. Any pointers?</p>
<p>gcc version is 7.3.0, Qt version is 5.11.3, CMake version is 3.8.2, installed, as per instruction from a tarball rather than using the one from distro packages.</p>
<p>As an aside, it is impossible to create an account in Slicer bug tracker, I’m being told that “Your account may be disabled or blocked or the username/password you entered is incorrect.”, while there could hardly be any reason to block me (I’ve not done anything yet <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=6" title=":wink:" class="emoji" alt=":wink:"> and I’m certain that my username / password are correct.</p>

---

## Post #2 by @pieper (2019-02-25 12:39 UTC)

<p>Hi <a class="mention" href="/u/wvxvw">@wvxvw</a> -</p>
<p>libarchive causes problems from time to time but usually gets fixed.  I haven’t tried that particular combination myself but maybe someone has suggestions.</p>
<p>Regarding mantis, I assume you have the same account name there and the account looks fine from the admin panel.  I sent you a password reset so let’s see if that clears things up.  Thanks for your help.</p>

---
