# Installing a python package that is not supported by pip

**Topic ID**: 30125
**Date**: 2023-06-19
**URL**: https://discourse.slicer.org/t/installing-a-python-package-that-is-not-supported-by-pip/30125

---

## Post #1 by @bongo_kat (2023-06-19 17:15 UTC)

<p>Hello, I have a python script that uses Ezc3d library: <a href="https://github.com/pyomeca/ezc3d" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pyomeca/ezc3d: Easy to use C3D reader/writer for C++, Python and Matlab</a></p>
<p>I can’t use pip to install it on Slicer as it is not supported. I’ve installed it using Anaconda. Is it possible to make slicer use Anaconda interpreter ?</p>
<p>I tried to work around it by extending the search path to my anaconda environment but it doesn’t work.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afdd4ab1dca26d67a2ef78fa8d3ca9df1d9e9f25.png" alt="image" data-base62-sha1="p5LFI8EzkfhjMesHbU7UuzcSSl7" width="512" height="23"></p>
<p>Is there another way I can achieve this ?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78e5053335ea00f106099d254660c76bf174dfb3.png" alt="image" data-base62-sha1="hftY9uoMR37Sq5FMsWSZ9yXbyKL" width="187" height="105"></p>
<p>Thank you very much for your time.</p>

---

## Post #2 by @lassoan (2023-06-19 20:51 UTC)

<p>Anaconda is very opinionated, it makes many assumptions about how Python should work, so I don’t think anaconda packages would be compatible with Slicer’s Python environment. Also, Anaconda is a commercial product, so there could be licensing concerns about using packages in a completely free, restriction-free environment.</p>
<p>Since ezc3d is not a native Python package, it is not trivial to build it. I would suggest to submit an issue to the package’s GitHub repository asking for making it avaialble on PyPI. If you don’t get any response, then it could make sense to use a c3d package that is available on PyPI.</p>
<p>In general, if a Python package does not have wheels on PyPI then I would not recommend to rely on it, because most likely it has insufficient developer resources and/or community support for testing, troubleshooting, fixing bugs, etc. Also, such projects are usually maintained by a single person, and if that person loses interest, changes job, or hit by a bus, you need to switch to another package anyway. It is better to start with the right package in the first place.</p>

---

## Post #3 by @bongo_kat (2023-06-19 20:55 UTC)

<p>Thank you for your prompt response</p>

---

## Post #4 by @Pariterre (2024-12-20 19:56 UTC)

<p>For the future readers who searches how to install ezc3d without PyPI (I am the developer for ezc3d)</p>
<p>As of last week, ezc3d is on PyPI. So no need to compile by hand anymore (nor relying on conda). That said, what is <a class="mention" href="/u/lassoan">@lassoan</a> is saying is indeed true; I am the sole developer of the package, but as of now, I am still active, and hope I don’t get hit by a bus!</p>
<p>That said, since the c3d format does not evolve that much, it is unlikely that for the near or middle future, even if I was stopping the development of which, that it would stop working.</p>
<p>Hope this helps make you the best decision for your needs! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @jamesobutler (2024-12-20 20:27 UTC)

<p><a class="mention" href="/u/pariterre">@Pariterre</a> As of right now <code>ezc3d</code> will still be unavailable to Slicer users to install by PyPI provided whl as Slicer’s embedded Python version is 3.9. It appears <code>ez3cd</code> 1.5.16 and 1.5.17 on PyPI requires Python 3.10+.</p>

---

## Post #6 by @Pariterre (2024-12-20 21:29 UTC)

<p>That is correct as type hints that uses “|” are in the code.</p>

---
