---
topic_id: 736
title: "Fsl Through Slicer"
date: 2017-07-21
url: https://discourse.slicer.org/t/736
---

# FSL through Slicer

**Topic ID**: 736
**Date**: 2017-07-21
**URL**: https://discourse.slicer.org/t/fsl-through-slicer/736

---

## Post #1 by @marlene (2017-07-21 13:56 UTC)

<p>Hello everybody,</p>
<p>I am trying to use an external library (fsl) in my module. My problem is exactly this : <a href="http://massmail.spl.harvard.edu/public-archives/slicer-users/2016/010173.html" rel="nofollow noopener">http://massmail.spl.harvard.edu/public-archives/slicer-users/2016/010173.html</a> . I am wondering weather in the meanwhile a more straightforward solution has been implemented.</p>
<p>I was thinking a (not really elegant) way to do it :</p>
<ol>
<li>creating a function in matlab which call ‘fsl’ using a shell command</li>
<li>call the function through the matlab bridge extension.</li>
</ol>
<p>Does it make sense?  if yes, how can I call the function from the python script of my module?</p>
<p>thank you very much</p>

---

## Post #2 by @ihnorton (2017-07-21 14:16 UTC)

<p>If you are on Linux or Mac, I would suggest to first try installing nipype with Slicer’s pip (it probably won’t work on Windows). See <a href="https://discourse.slicer.org/t/pyzmq-in-slicer-python/587/4?u=ihnorton">this post</a> for instructions. Slicer compatibility with the rest of the Python world is still in limbo. Hopefully once we move to Python3 and Visual Studio 2015, we can consider building against miniconda by default.</p>
<p>If you are willing to write your own shell-out routine, there’s no need to introduce a Matlab dependency, Python can do it directly: <a href="https://docs.python.org/2/library/subprocess.html">https://docs.python.org/2/library/subprocess.html</a></p>

---

## Post #3 by @marlene (2017-07-24 15:01 UTC)

<p>thank you for your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
