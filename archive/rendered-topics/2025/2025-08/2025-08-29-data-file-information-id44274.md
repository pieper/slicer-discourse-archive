---
topic_id: 44274
title: "Data File Information"
date: 2025-08-29
url: https://discourse.slicer.org/t/44274
---

# Data file information

**Topic ID**: 44274
**Date**: 2025-08-29
**URL**: https://discourse.slicer.org/t/data-file-information/44274

---

## Post #1 by @michaelli (2025-08-29 21:46 UTC)

<p>I load a bunch of data files into Slicer 3D, including DICOM, STL and others, how can I get the file path and file name information? I cannot see the file information from data structure. I ask this because I have files with the same name from different folders. I’m confused and don’t remember if I loaded the file from the right folder. I want to double-check that.</p>

---

## Post #2 by @pieper (2025-08-29 21:49 UTC)

<p>If you bring up the save dialog the default save will be the directory you loaded from.</p>

---

## Post #3 by @michaelli (2025-08-29 21:55 UTC)

<p>Thanks for the tip. Yes, that will tell most of the file path, but I cannot see the DICOM file path. I’m wondering if there is other ways to view the file information easily.</p>

---

## Post #4 by @pieper (2025-08-30 16:39 UTC)

<p>You can get that using a little script, something like this: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-tag-of-a-scalar-volume-loaded-from-dicom">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-tag-of-a-scalar-volume-loaded-from-dicom</a></p>

---

## Post #5 by @michaelli (2025-08-30 17:10 UTC)

<pre><code class="lang-auto">&gt; def pathFromNode(node):
&gt;     storageNode = node.GetStorageNode()
&gt;     if storageNode is not None: # loaded via drag-drop
&gt;          filepath = storageNode.GetFullNameFromFileName()
&gt;     else: # Loaded via DICOM browser
&gt;          instanceUIDs = node.GetAttribute(“DICOM.instanceUIDs”).split()
&gt;          filepath = slicer.dicomDatabase.fileForInstance(instUids\[0\])
&gt;      return filepath
&gt; node = slicer.util.getNode(“2025data”)
&gt; path = self.pathFromNode(node)
&gt; print(“DICOM path=%s” % path)
</code></pre>
<p>NameError: name ‘self’ is not defined</p>
<p>Did I miss something?</p>

---

## Post #6 by @pieper (2025-08-30 17:46 UTC)

<aside class="quote no-group" data-username="michaelli" data-post="5" data-topic="44274">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/michaelli/48/67910_2.png" class="avatar"> michaelli:</div>
<blockquote>
<p><code>&gt; path = self.pathFromNode(node)</code></p>
</blockquote>
</aside>
<p>You only use <code>self</code> when you are in a class method.  Here you can just call <code>pathFromNode</code>.  Otherwise it looks reasonable.</p>

---

## Post #7 by @cpinter (2025-09-01 09:06 UTC)

<p>This may be a resonable piece of information to include in the subject hierarchy tooltip. I could add it in the base class (if a node has a storage node with a valid URL, add it to the tooltip). <a class="mention" href="/u/pieper">@pieper</a> what do you think?</p>

---

## Post #8 by @pieper (2025-09-01 13:31 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="44274">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>information to include in the subject hierarchy tooltip</p>
</blockquote>
</aside>
<p>I think that’s a great idea <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @cpinter (2025-09-02 13:43 UTC)

<p>I created a PR for this:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8690">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8690" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8690" target="_blank" rel="noopener">ENH: Show storage path for nodes loaded from file in SH</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>cpinter:storage-path-in-sh-tooltip</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-09-02" data-time="13:42:43" data-timezone="UTC">01:42PM - 02 Sep 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/cpinter" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
            cpinter
          </a>
        </div>

        <div class="lines" title="1 commits changed 10 files with 95 additions and 3 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8690/files" target="_blank" rel="noopener">
            <span class="added">+95</span>
            <span class="removed">-3</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Re https://discourse.slicer.org/t/data-file-information/44274/8

As discussed <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8690" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">in the above forum topic, I added a small feature that shows the file path each node is loaded from (if loaded from file and its storage node contains a path). These types of nodes support this feature for now:

Volume:
&lt;img width="416" height="83" alt="image" src="https://github.com/user-attachments/assets/86c03725-7b63-451c-9a13-503f0bc15e72" /&gt;

Model:
&lt;img width="516" height="77" alt="image" src="https://github.com/user-attachments/assets/74227078-100a-4796-905e-e716a6113fcd" /&gt;

Segmentation
&lt;img width="760" height="65" alt="image" src="https://github.com/user-attachments/assets/6ebb4637-800e-4f17-a31d-3fa507ab4c07" /&gt;

Table
&lt;img width="292" height="68" alt="image" src="https://github.com/user-attachments/assets/3ede3cec-b3c3-4271-a908-ab1b03e31e06" /&gt;

Markup
&lt;img width="216" height="69" alt="image" src="https://github.com/user-attachments/assets/0133b063-99e3-466c-8777-eeae9803f8a3" /&gt;

Transform
&lt;img width="465" height="142" alt="image" src="https://github.com/user-attachments/assets/1d1a98d6-8808-4291-bc88-7ca7e7be9d5c" /&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
