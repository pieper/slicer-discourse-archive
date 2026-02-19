---
topic_id: 25241
title: "Installing Slicer Extension From Script"
date: 2022-09-13
url: https://discourse.slicer.org/t/25241
---

# Installing Slicer extension from script

**Topic ID**: 25241
**Date**: 2022-09-13
**URL**: https://discourse.slicer.org/t/installing-slicer-extension-from-script/25241

---

## Post #1 by @Nadya_Shusharina (2022-09-13 16:13 UTC)

<p>Hello,<br>
I would like to build a Docker container with Slicer 5.0.2 r30822 linux-amd64, and with Slicer extensions installed. To do that, I am trying to have Slicer install extensions from a python script:</p>
<pre><code class="lang-auto">emm = slicer.app.extensionsManagerModel()
md = emm.retrieveExtensionMetadataByName("DCMQI")
x = emm.downloadAndInstallExtension(md['extension_id'])
if x:
    print('emm completed ok')
else:
    print('emm error', x)
</code></pre>
<p>and then run <code>Slicer --python-script "myscript.py" --no-splash --no-main-window</code><br>
This does download and install the extension but the script does not exit. If I add <code>sys.exit(0)</code> to the script as suggested <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">here</a>, Slicer exits after downloading the extension, but before installing it. Could you please advise what is the correct way to install Slicer extensions from script?</p>
<p>Thank you,<br>
Nadya</p>

---

## Post #2 by @pieper (2022-09-13 17:14 UTC)

<p>Here’s an example of installing extensions in a dockerfile with a python script:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/pieper/SlicerDockers/tree/master/slicer-plus">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerDockers/tree/master/slicer-plus" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/pieper/SlicerDockers/tree/master/slicer-plus" target="_blank" rel="noopener">SlicerDockers/slicer-plus at master · pieper/SlicerDockers</a></h3>

  <p><a href="https://github.com/pieper/SlicerDockers/tree/master/slicer-plus" target="_blank" rel="noopener">master/slicer-plus</a></p>

  <p><span class="label1">docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Nadya_Shusharina (2022-09-13 19:06 UTC)

<p>Thank you, it works, I also used parts of your Dockerfile (xfvb-run Slicer).</p>

---

## Post #4 by @Piyush_Khurana (2023-12-27 16:58 UTC)

<p>Hi Steve,<br>
Thank you for the script.<br>
I am trying to find the docs, I wanted to change the extensions path.</p>
<p>I found this: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.app" class="inline-onebox" rel="noopener nofollow ugc">slicer — 3D Slicer documentation</a></p>
<p>But, the docs does not have any slicer.app.extensionsManager</p>

---

## Post #5 by @pieper (2023-12-27 18:14 UTC)

<aside class="quote no-group" data-username="Piyush_Khurana" data-post="4" data-topic="25241">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/piyush_khurana/48/68815_2.png" class="avatar"> Piyush_Khurana:</div>
<blockquote>
<p>But, the docs does not have any slicer.app.extensionsManager</p>
</blockquote>
</aside>
<p>The documentation is not always the best way to learn.  Since Slicer is open source, reviewing the code directly using IDE tools or <a href="https://github.com/search?q=repo%3ASlicer%2FSlicer%20qSlicerExtensionsManagerModel&amp;type=code">directly in github</a> is a good way to learn.</p>

---

## Post #6 by @Piyush_Khurana (2023-12-28 08:22 UTC)

<p>Hmm, thanks for the tip!</p>

---
