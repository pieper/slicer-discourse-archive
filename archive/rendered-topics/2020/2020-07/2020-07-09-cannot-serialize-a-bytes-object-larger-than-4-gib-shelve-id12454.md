---
topic_id: 12454
title: "Cannot Serialize A Bytes Object Larger Than 4 Gib Shelve"
date: 2020-07-09
url: https://discourse.slicer.org/t/12454
---

# Cannot serialize a bytes object larger than 4 GiB - shelve

**Topic ID**: 12454
**Date**: 2020-07-09
**URL**: https://discourse.slicer.org/t/cannot-serialize-a-bytes-object-larger-than-4-gib-shelve/12454

---

## Post #1 by @siaeleni (2020-07-09 02:20 UTC)

<p>Hello,<br>
I am trying to run partial incremental PCA with the following</p>
<blockquote>
<p>decomposer.partial_fit</p>
</blockquote>
<p>But I get the following error when I trying this:</p>
<blockquote>
<p>file[‘eigenModes’] = decomposer.components_<br>
OverflowError: cannot serialize a bytes object larger than 4 GiB</p>
</blockquote>
<p>I found that link <a href="https://stackoverflow.com/questions/29704139/pickle-in-python3-doesnt-work-for-large-data-saving" class="inline-onebox" rel="noopener nofollow ugc">python - _pickle in python3 doesn't work for large data saving - Stack Overflow</a> where it says that I need to point protocol 4 for pickle. I checked that the protocol you are using is 3, and I am wondering if there is any way to use protocol 4 through shelve or if you have any other idea?</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #2 by @lassoan (2020-07-09 02:28 UTC)

<p>The solution is described at the link - you need to specify the pickle protocol:</p>
<pre><code>pickle.dump(d, open("file", 'w'), protocol=4)</code></pre>

---

## Post #3 by @siaeleni (2020-07-09 17:04 UTC)

<p>Yes, true, I was thinking more if there is a way to use pickle protocol 4 from shelve lib, but I will use it directly.<br>
Thanks!</p>

---

## Post #4 by @lassoan (2020-07-09 17:21 UTC)

<p>I don’t think shelve library is bundled with Slicer, so you can install any version and configure it any way you want.</p>
<p>For example, you can specify protocol in <code>shelve.open</code> (<a href="https://docs.python.org/3/library/shelve.html">https://docs.python.org/3/library/shelve.html</a>).</p>

---
