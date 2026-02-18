# SlicerApp-real: error while loading shared libraries: * : cannot open shared object file: No such file or directory

**Topic ID**: 33738
**Date**: 2024-01-11
**URL**: https://discourse.slicer.org/t/slicerapp-real-error-while-loading-shared-libraries-cannot-open-shared-object-file-no-such-file-or-directory/33738

---

## Post #1 by @tbillah (2024-01-11 17:21 UTC)

<p>We are testing Slicer on CentOS 9. We downloaded both 4.10.2 and 5.2.2 but ran into libraries deficit:</p>
<blockquote>
<p>Slicer-4.10.2-linux-amd64/bin/SlicerApp-real: error while loading shared libraries: libnsl.so.1: cannot open shared object file: No such file or directory</p>
</blockquote>
<blockquote>
<p>Slicer-5.2.2-linux-amd64/bin/SlicerApp-real: error while loading shared libraries: libGLU.so.1: cannot open shared object file: No such file or directory</p>
</blockquote>
<p>We thought Slicer works off the shelf. Do you no longer ship necessary libraries in <code>Slicer-*-linux-amd64/lib</code> directory? Or is it that we need to set <code>LD_LIBRARY_PATH</code> to this directory before launching Slicer?</p>
<p>If neither is the case, should we <code>yum install mesa-libGL</code> etc.?</p>

---

## Post #2 by @muratmaga (2024-01-11 18:28 UTC)

<p>These are fairly old versions of the slicer. I am not sure if anyone has tested them with Centos9. As per instructions for Fedora, you need to install libglu1.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#fedora" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#fedora</a></p>

---

## Post #3 by @tbillah (2024-01-11 18:39 UTC)

<p>Thanks. What is the newest version that we should use?</p>

---

## Post #4 by @muratmaga (2024-01-11 18:41 UTC)

<p>5.6.1 has been released two months ago. I would start with that.</p>

---

## Post #5 by @tbillah (2024-01-11 21:32 UTC)

<p>It was not a Slicer version issue. It appears that Slicer does not ship <code>libGLU</code> and <code>libsnl</code>. So we had to do:</p>
<blockquote>
<p>yum install -y mesa-libGLU libnsl</p>
</blockquote>

---

## Post #6 by @muratmaga (2024-01-11 21:49 UTC)

<p>Yes, I think it is expected given the Fedora instructions I shared.</p>

---
