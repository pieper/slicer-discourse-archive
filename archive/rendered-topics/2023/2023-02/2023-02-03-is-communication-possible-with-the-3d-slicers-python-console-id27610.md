---
topic_id: 27610
title: "Is Communication Possible With The 3D Slicers Python Console"
date: 2023-02-03
url: https://discourse.slicer.org/t/27610
---

# Is communication possible with the 3D slicer's python console?

**Topic ID**: 27610
**Date**: 2023-02-03
**URL**: https://discourse.slicer.org/t/is-communication-possible-with-the-3d-slicers-python-console/27610

---

## Post #1 by @dsa934 (2023-02-03 07:22 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Hello , 3D slicer users<br>
With your help, my project has been successfully completed.<br>
The second project is communication.</p>
<p>I’m going to create a Python module that communicates between admin-client.</p>
<ul>
<li>admin: Distribute tasks to clients</li>
<li>client : Sends the task to the admin when the task is complete</li>
</ul>
<p>The question is, I want to configure this module as a slicer extension module so that it works on the python console within the 3D slicer. Is this possible?<br>
Does 3d slicer have support for communication module?</p>

---

## Post #2 by @pieper (2023-02-03 07:59 UTC)

<p>Yes, there are many ways to do this.  It will help people understand your goals better if you clarify what type of communication you have in mind (raw tcp, http, other?).  And what exactly is the admin program and what is the client (are they both Slicer instances?  are they other programs?).</p>
<p>It might help if you look at the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">WebServer module</a>, which can allow other programs, perhaps your admin program, to control the operation of a Slicer instance, perhaps your client.</p>

---

## Post #3 by @dsa934 (2023-02-03 08:14 UTC)

<p>Thank you for quick response.</p>
<p>Nothing has been decided yet, but I first wondered if communication was possible in the Python console of the 3D slicer.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="27610">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>are they both Slicer instances? are they other programs?</p>
</blockquote>
</aside>
<p>Yes. Both work only in slicer.</p>
<p>If I deduce my boss’ thoughts, it seems to create a Python module that works with a 3D slicer, and<br>
the client that has finished the work sends the completed slicer task to the admin.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="27610">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It might help if you look at the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html" rel="noopener nofollow ugc">WebServer module</a>, which can allow other programs, perhaps your admin program, to control the operation of a Slicer instance, perhaps your client.</p>
</blockquote>
</aside>
<p>After reading the article you recommended and understanding the concept as much as possible, I will try to ask more detailed questions. thanks for the quick reply</p>

---

## Post #4 by @pieper (2023-02-03 08:18 UTC)

<p>Then yes, using something like the <code>requests</code> module from the admin Slicer instance can allow you to connect to an arbitrary number of client Slicer instances (assign unique tcp ports to each) via the WebServer and the <code>exec</code> API to run python code in the client.  Let us know how it works for you.</p>

---

## Post #5 by @dsa934 (2023-02-03 08:19 UTC)

<p>Okay I’ll try it , see you later !</p>

---

## Post #6 by @dsa934 (2023-02-03 08:31 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="27610">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>ype of communication you have in mind (raw tcp, http, other?).</p>
</blockquote>
</aside>
<p>Is the ‘https’ protocol possible?</p>

---

## Post #7 by @pieper (2023-02-03 08:44 UTC)

<p>Yes, when you instantiate the server you can <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/WebServer/WebServer.py#L275">supply a certificate</a>.  If you are in a controlled network or the same machine this is really optional.  If you are using multiple machines on an open network I suggest creating ssh tunnels instead for security rather than relying on network traffic even if it is encrypted.  Web server security is a big topic, so be thoughtful about what you expose.</p>

---

## Post #8 by @dsa934 (2023-02-03 09:28 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Hi again</p>
<p>I want to make a toy project before making a communication module.<br>
What should I refer to to do the task below?</p>
<ul>
<li>Transfer slicer tasks (add markups, etc…) from your computer to your colleague’s computer</li>
<li>When you open the transferred file on your colleague’s computer, check if it is the same as the file you worked on on your computer.</li>
</ul>
<p>Would it be good to refer to ‘OpenIGTLink Python package’ ?</p>

---

## Post #9 by @pieper (2023-02-03 09:53 UTC)

<p>Hard to say, but if your goal is to transfer this task to a human being who will use slicer to do something like segmentation and then give you back the result it may be easier to use .mrb files with a shared network directory or a system like dropbox.  You can make some small scripts if you want to automate this and check that the results are in the right format.</p>
<p>OpenIGTLink is for continuous real-time data like video or 3D tracker data.</p>
<p>The WebServer would allow real-time control of one Slicer instance from another, but maybe not as logical to use when there are human beings involved on the client computer.</p>

---

## Post #10 by @jamesobutler (2023-02-03 12:40 UTC)

<p>If the task is AI related, you may consider the MONAILabelReviewer module.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer/MONAILabelReviewer">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer/MONAILabelReviewer" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer/MONAILabelReviewer" target="_blank" rel="noopener nofollow ugc">MONAILabel/plugins/slicer/MONAILabelReviewer at main · Project-MONAI/MONAILabel</a></h3>

  <p><a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer/MONAILabelReviewer" target="_blank" rel="noopener nofollow ugc">main/plugins/slicer/MONAILabelReviewer</a></p>

  <p><span class="label1">MONAI Label is an intelligent open source image labeling and learning tool.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @dsa934 (2023-02-04 17:00 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="27610">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It might help if you look at the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html" rel="noopener nofollow ugc">WebServer module </a>,</p>
</blockquote>
</aside>
<p>Honestly, I’ve never done anything other than data engineering and AI model building, so even looking at the network documentation you linked to, I don’t quite understand.</p>
<p>Q1. The basic framework of the server is already built, and am I adding various options with a command?</p>
<pre><code class="lang-auto">some_slicer_server_build_command( security_protocol_params, etc, .. ) 
</code></pre>
<p>Can you give me a code example of building a server and sending and receiving simple data?</p>
<p>If I know the command to turn on the server and send and receive data in the Slicer’s Python console, I think I can do something based on this, but I don’t know how.</p>

---
