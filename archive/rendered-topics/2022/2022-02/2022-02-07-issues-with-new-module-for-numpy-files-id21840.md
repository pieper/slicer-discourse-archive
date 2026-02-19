---
topic_id: 21840
title: "Issues With New Module For Numpy Files"
date: 2022-02-07
url: https://discourse.slicer.org/t/21840
---

# Issues with New Module for Numpy Files

**Topic ID**: 21840
**Date**: 2022-02-07
**URL**: https://discourse.slicer.org/t/issues-with-new-module-for-numpy-files/21840

---

## Post #1 by @stevenagl12 (2022-02-07 16:06 UTC)

<p>Hi, I am trying to work out a new extension that is capable of going into a directory and pulling out all npy or npz files and importing them into 3D slicer as a volume. I am positive that the radio button logic on my code needs work, but I am not sure how to continue. I have looked through multiple instances of other codes using these radiobuttons and have tried their syntax only for it to break my script (obviously this is a problem caused by a lack of knowledge about UI code and connecting the logic up right). Attached is my gist if there is anyone willing to take  a look.<br>
<a href="https://gist.github.com/stevenagl12/2f933f8fb5e3a823ce506d55582583d4" rel="noopener nofollow ugc">https://gist.github.com/stevenagl12/2f933f8fb5e3a823ce506d55582583d4</a></p>

---

## Post #2 by @lassoan (2022-02-08 20:44 UTC)

<p>If you don’t want to immediately act on your radiobutton clicks then there is no need to connect any signals to them. In the <code>onApply</code> method you can get the state of the radiobutton like this:</p>
<pre><code>isFormatNpy = self.FileTypeNPY.checked</code></pre>

---

## Post #3 by @jcfr (2022-02-10 02:59 UTC)

<p>Thanks for working on adding support for importing <code>npy</code> or <code>npz</code> files.</p>
<p>For convenience and to have it one-click away, the format is documented here: <a href="https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format" class="inline-onebox">numpy.lib.format — NumPy v1.22 Manual</a></p>

---

## Post #4 by @stevenagl12 (2022-02-10 09:56 UTC)

<p>Thank you for your help. I have updated the script and it is working with numpy files as well as npz files. The last thing I wanted to do was to make it where the script was capable of creating a listing of all of the files that met a certain search parameter. In my code I used a list comprehension for this with a parameter called FileConstraints, but for some reason, when I run the script with a constraint, it is not capable of creating the desired list of filenames. Here is my gist again if there is anyone who can take a look. <a href="https://gist.github.com/stevenagl12/2f933f8fb5e3a823ce506d55582583d4" rel="noopener nofollow ugc">https://gist.github.com/stevenagl12/2f933f8fb5e3a823ce506d55582583d4</a></p>

---

## Post #5 by @stevenagl12 (2022-02-10 09:57 UTC)

<p>So, by the looks of the information you provided to me, do you think I should expand my script to be capable of using pickled array information in npy file format as well? My script is currently able to import npy file formats, but I don’t know how regularly people pickle npy files, as the only instance I have of this was with the npz files that do it natively as arr_0.</p>

---
