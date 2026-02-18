# An unhandled win32 exception occured in Slicer App-real.exe

**Topic ID**: 14288
**Date**: 2020-10-28
**URL**: https://discourse.slicer.org/t/an-unhandled-win32-exception-occured-in-slicer-app-real-exe/14288

---

## Post #1 by @marianaslicer (2020-10-28 13:36 UTC)

<p>Operating system: windows 7 professional<br>
Slicer version: 4.11.20200930</p>
<p>Hello everyone,</p>
<p>Everytime that I try to run my own python module the 3D Slicer shows this message and it stops working.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd52f2a5c7fb8577aef8f6df4e623f98d7869d35.png" alt="image" data-base62-sha1="tinAYsFlCyGBlBiXbqlymBMf0jP" width="376" height="195"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c608c7933a30819e7ef0c47e7ab87911879446b.png" alt="image" data-base62-sha1="1LuAeb0ytZQBjxsyVxxyJ3M2hdN" width="416" height="454"></p>
<p>Anyone can help me?<br>
Thank you in advance.</p>

---

## Post #2 by @cpinter (2020-10-28 13:55 UTC)

<p>It seems that your Python module does something that makes Slicer crash. Since debugging crashes coming from Python is not trivial (even if you build Slicer and debug the crash that happens in the C++ core, you won’t exactly see the Python line that caused it), I suggest commenting out parts of your code and see which one is the culprit.</p>

---
