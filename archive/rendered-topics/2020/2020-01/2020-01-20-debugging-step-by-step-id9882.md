# Debugging step by step

**Topic ID**: 9882
**Date**: 2020-01-20
**URL**: https://discourse.slicer.org/t/debugging-step-by-step/9882

---

## Post #1 by @rbahegne (2020-01-20 15:42 UTC)

<p>Hello,</p>
<p>I created a C++ extension, which works quite fine but i never managed to make to debugger work.</p>
<p>I tried with several IDE QtCreator, Kdevelop, Clion, I correctly set the CMAKE_BUILD_TYPE Flag to debug (for my extension and for 3D Slicer), and each time i can’t get breakpoints working. It seems that debug symbols are not generated.</p>
<p>Am I missing something ?</p>

---

## Post #2 by @jcfr (2020-01-20 16:03 UTC)

<p>Did you have a chance to read through the following page:  <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions</a></p>

---

## Post #3 by @rbahegne (2020-01-20 16:12 UTC)

<p>Yes quite a lot of times.</p>

---

## Post #4 by @jcfr (2020-01-20 16:26 UTC)

<p>Assuming you are using Linux, did you try to:</p>
<ul>
<li>start Slicer</li>
<li>start ddd and attach to the running process</li>
<li>set breakpoints</li>
</ul>

---

## Post #5 by @rbahegne (2020-01-20 16:44 UTC)

<p>I’m indeed on linux (ubuntu 18.04.3 , using Qt 5.11.0 GCC 64bit)</p>
<p>I tried this kind of thing using QtCreator when i attach to the process i get this :</p>
<blockquote>
<p>This does not seem to be a “Debug” build.<br>
Setting breakpoints by file name and line number may fail.<br>
Section .debug_info: Not found.<br>
Section .debug_abbrev: Not found.<br>
Section .debug_line: Not found.<br>
Section .debug_str: Not found.<br>
Section .debug_loc: Not found.<br>
Section .debug_range: Not found.<br>
Section .gdb_index: Not found.<br>
Section .note.gnu.build-id: Found.<br>
Section .gnu.hash: Found.<br>
Section .gnu_debuglink: Not found.</p>
</blockquote>
<p>After googling it i just got advice to set BuilType to Debug, which was the first thing i did.<br>
I though maybe the extension dependency to 3d slicer (which is also build in debug) was messing things up, but i did not found anything relevant.</p>

---

## Post #6 by @rbahegne (2020-03-13 15:30 UTC)

<p>For any futher user here how i fixed this :</p>
<p>The real process is not SlicerWith or Slicer but SlicerApp-real so you can’t debug at start, we need to attach to the process (ubuntu need some minor configuration to be able to do so, see below). From <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions</a></p>
<p>GDB debug by attaching to running process: Starting with Ubuntu 10.10, ptracing of non-child processes by non-root users as been disabled -ie. only a process which is a parent of another process can ptrace it for normal users. You can temporarily disable this restriction by: $ echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope</p>
<p>To permanently allow it to edit /etc/sysctl.d/10-ptrace.conf and change the line: kernel.yama.ptrace_scope = 1 to read: kernel.yama.ptrace_scope = 0</p>
<p>Run SlicerWith*NameOfYourExtension, then attach to process SlicerApp-real</p>

---
