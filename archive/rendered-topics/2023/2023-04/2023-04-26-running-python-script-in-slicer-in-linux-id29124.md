# Running python script in slicer in linux

**Topic ID**: 29124
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/running-python-script-in-slicer-in-linux/29124

---

## Post #1 by @exngan (2023-04-26 00:59 UTC)

<p>Hi I tried to run python script or code in slicer in linux and windows (linux mainly). I followed this guideline, but none of the methods worked. I received syntax error everytime.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html</a></p>
<p>I used ‘/’ in linux and ‘\’ in windows for file path.<br>
I installed slicer in a folder ‘home\user\Software\Slicer-5.2.2-linux-amd64’<br>
The python script is installed in another folder like ‘home\user\project\mice\test.py’</p>
<p>inside test.py, it is just <code>print(1+2)</code></p>
<pre><code class="lang-auto">import os
homepath = ''home\user\Software\Slicer-5.2.2-linux-amd64"
os,chdir(homepath)  # this one worked
</code></pre>
<p>these all failed</p>
<pre><code class="lang-auto">start Slicer home\user\project\mice\test.py
</code></pre>
<pre><code class="lang-auto">Slicer.exe --python-script "'home\user\project\mice\test.py" 
</code></pre>
<p>Syntaxx.Error: invalid syntax</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2023-04-26 02:10 UTC)

<aside class="quote no-group" data-username="exngan" data-post="1" data-topic="29124">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/exngan/48/65770_2.png" class="avatar"> exngan:</div>
<blockquote>
<p><code>homepath = ''home\user\Software\Slicer-5.2.2-linux-amd64"</code></p>
</blockquote>
</aside>
<p>There are multiple typos:</p>
<ol>
<li>user either apostrophe or double quotes.</li>
</ol>
<p>Try<br>
<code>homepath = 'home\user\Software\Slicer-5.2.2-linux-amd64'</code></p>
<p>or</p>
<p><code>homepath = "home\user\Software\Slicer-5.2.2-linux-amd64"</code></p>
<ol start="2">
<li>Linux paths start with / not backslash (<code>\</code>) like:</li>
</ol>
<p><code>homepath = '/home/user/Software/Slicer-5.2.2-linux-amd64'</code></p>

---

## Post #3 by @exngan (2023-04-26 05:25 UTC)

<p>some typos in the post, i dont know how to edit it. let me rephrase my question</p>
<p>I tested all the following codes in linux and windows. If in linux, I changed the separator to forward slash (/). In windows, I tested the codes with double blackslash “\\” and single blackslash “\” respectively . (For some reasons, I have to enter two blackslashes in order to show a single blackslash in this forum.)</p>
<p>import os<br>
homepath = ‘home\user\Software\Slicer-5.2.2-linux-amd64’   # / if in linux<br>
os.chdir(homepath)</p>
<p>(above 3 lines worked, no issues with them)</p>
<p>below all failed, even if I changed the separator for different operating systems</p>
<p>start Slicer home\\user\\project\\mice\\test.py<br>
Slicer.exe --python-script “home\\user\\project\\mice\\test.py”</p>
<p>or<br>
start Slicer home/user/project/mice/test.py<br>
Slicer.exe --python-script “home/user/project/mice/test.py”</p>

---

## Post #4 by @rbumm (2023-04-26 08:33 UTC)

<p>In the Slicer Python console you can</p>
<pre><code class="lang-auto"># run Python script
exec(open(r"C:\Users\Yourname\Documents\MySlicerExtensions\Python\test.py").read())
</code></pre>

---
