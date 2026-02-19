---
topic_id: 33528
title: "Problem With Debugging On Windows"
date: 2023-12-27
url: https://discourse.slicer.org/t/33528
---

# Problem with debugging on Windows

**Topic ID**: 33528
**Date**: 2023-12-27
**URL**: https://discourse.slicer.org/t/problem-with-debugging-on-windows/33528

---

## Post #1 by @nnzzll (2023-12-27 07:30 UTC)

<p>I followed the debug instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html#debugging-using-visual-studio" rel="noopener nofollow ugc">here</a> and trying to debug my C++ extensions. However, I can never start it.</p>
<p>It says cannot find python36.dll, but I’m using Slicer5.6.0 of which python version is 3.9, so there is no python36.dll.</p>
<p>Remaining error messages are shown below:</p>
<blockquote>
<p>Exception thrown at 0x00007FFF1CC524F6 (ntdll.dll) in SlicerApp-real.exe: 0xC0000139: Entry Point Not Found.<br>
Exception thrown at 0x00007FFF1CC524F6 (ntdll.dll) in SlicerApp-real.exe: 0xC0000139: Entry Point Not Found.<br>
The thread 1280 has exited with code 3221225785 (0xc0000139).<br>
The thread 13340 has exited with code 3221225785 (0xc0000139).<br>
The thread 30636 has exited with code 3221225785 (0xc0000139).<br>
The program ‘[31248] SlicerApp-real.exe’ has exited with code 3221225785 (0xc0000139) ‘Entry Point Not Found’.</p>
</blockquote>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c43603310f2c7e9dd37576c000abaec78cf0aff.png" alt="屏幕截图 2023-12-27 152719" data-base62-sha1="421IHXByJaLChxVWn2TVwYmg1xt" width="563" height="222"><br>
Cannot find python36.dll</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fe606e07f9ba967ee5bd98b8e1bd346e614ff18.png" alt="屏幕截图 2023-12-27 152742" data-base62-sha1="boOy7URrPwrncGfOvo0xJ5Nw63m" width="552" height="272"><br>
Cannot find Entry Point.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47e3149552e1789e8437c6661348addf9b0f36eb.png" alt="屏幕截图 2023-12-27 152809" data-base62-sha1="afWpUuEyhYiuYqI2Gjdriwfscjh" width="547" height="253"><br>
Cannot find Entry Point.</p>

---

## Post #2 by @cpinter (2024-01-02 10:45 UTC)

<p>I don’t understand any of the Chinese error messages, but they remind me of errors I get when the environment is not properly set up. Please try following the instructions again, double and triple checking that you do not miss any step.</p>

---
