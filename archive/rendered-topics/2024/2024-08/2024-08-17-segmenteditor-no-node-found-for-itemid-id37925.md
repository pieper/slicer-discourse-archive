# SegmentEditor: No node found for itemID

**Topic ID**: 37925
**Date**: 2024-08-17
**URL**: https://discourse.slicer.org/t/segmenteditor-no-node-found-for-itemid/37925

---

## Post #1 by @chir.set (2024-08-17 11:45 UTC)

<p>Whenever a new segment is created in ‘Segment editor’, this message appears in the python console:</p>
<blockquote>
<p>No node found for itemID {19…??}</p>
</blockquote>
<p>It is unknown in which release it started, it is noted in factory release 5.7.0-2024-08-05 r32964 / 52af5a2.</p>
<p>Just reporting as it floods the console and can cast doubts about user code.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2024-08-17 14:39 UTC)

<p>Tha ks for reporting. Could you please describe how to reproduce it?</p>

---

## Post #3 by @chir.set (2024-08-17 15:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="37925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>describe how to reproduce it</p>
</blockquote>
</aside>
<p>Start slicer.<br>
Load a scalar volume.<br>
Go to ‘Segment editor’.<br>
Click ‘Add’ a new segment.</p>
<p>The messages appear in the Python console, even with no ‘.slicerrc.py’ loaded. I agree it’s certainly harmless.</p>

---

## Post #4 by @lassoan (2024-08-17 20:02 UTC)

<p>I cannot reproduce this on Windows, using the latest Slicer Preview Release. Could you please upload the full application log somewhere (dropbox, onedrive, …) and post the link here? Thank you.</p>

---

## Post #5 by @chir.set (2024-08-17 20:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="37925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the full application log</p>
</blockquote>
</aside>
<p>Thank you for considering this.</p>
<p>The log file is <a href="https://disk.yandex.com/d/7zRwkztytPXq_Q" rel="noopener nofollow ugc">here</a>.</p>
<p>After further testing, it is related to SlicerEditor since the lines do not appear if SlicerEditor is not installed. I’ll use Slicer without this module as I’ve got <a href="https://github.com/SlicerMorph/SlicerEditor/issues/40" rel="noopener nofollow ugc">another</a> issue with it.</p>
<p>Sorry to have bothered you.</p>
<p>Ping <a class="mention" href="/u/muratmaga">@muratmaga</a> .</p>

---

## Post #6 by @oothomas (2024-08-19 20:30 UTC)

<p>Hi,</p>
<p>Thanks for reporting this issue. I think I found its source. This can quickly be resolved by removing the else statement in the method below, but I should investigate why this is being triggered when you are working in SegmentEditor.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b83e372ae9207c32e58e17a1802d6ea6da65d6bc.jpeg" data-download-href="/uploads/short-url/qhT9l6VP2npT2RqOMPbMKG2wVis.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b83e372ae9207c32e58e17a1802d6ea6da65d6bc_2_690x279.jpeg" alt="image" data-base62-sha1="qhT9l6VP2npT2RqOMPbMKG2wVis" width="690" height="279" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b83e372ae9207c32e58e17a1802d6ea6da65d6bc_2_690x279.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b83e372ae9207c32e58e17a1802d6ea6da65d6bc_2_1035x418.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b83e372ae9207c32e58e17a1802d6ea6da65d6bc_2_1380x558.jpeg 2x" data-dominant-color="232529"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×779 59.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ll remove this statement for now and push an update to the repo.</p>
<p>Oshane</p>

---

## Post #7 by @chir.set (2024-08-19 20:44 UTC)

<aside class="quote no-group" data-username="oothomas" data-post="6" data-topic="37925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oothomas/48/68743_2.png" class="avatar"> oothomas:</div>
<blockquote>
<p>I’ll remove this statement for now and push an update to the repo.</p>
</blockquote>
</aside>
<p>Ok, thanks, I’ll keep you informed after my next build this weekend.</p>

---

## Post #8 by @chir.set (2024-08-24 12:48 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="7" data-topic="37925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I’ll keep you informed</p>
</blockquote>
</aside>
<p>These messages no longer appear in the Python console.</p>
<p>The code completion combobox appears nicely. However, every time it appears, the following is printed in the terminal where Slicer is launched (not Python console):</p>
<p><code>Running  "json.dumps(list(globals().keys()))"  result is  "[\"__name__\", \"__doc__\", ... very loooooong list... \"json\"]"</code></p>
<p>There is code completion though.</p>

---

## Post #9 by @chir.set (2024-08-25 14:16 UTC)

<p>Hello <a class="mention" href="/u/oothomas">@oothomas</a> ,</p>
<p>This message also appears many many times in the terminal:</p>
<p><code>In "PyFileFileWriter" class, function 'canWriteObject'  is expected to return a boolean !</code></p>
<p>I don’t mean to bother you, it’s just that I sometimes look for expected messages in the terminal and have to scroll much to find them.</p>
<p>Regards.</p>

---

## Post #10 by @pieper (2024-08-25 17:37 UTC)

<p>These will be good things to sort out - can you file issues on the repository?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerMorph/SlicerEditor/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerEditor/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/9ac95408ba56c8d29e7b4d04453a151a40a39d3aa4c37c8861d9ca05105caf35/SlicerMorph/SlicerEditor" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerMorph/SlicerEditor/issues" target="_blank" rel="noopener">Issues · SlicerMorph/SlicerEditor</a></h3>

  <p>a simple programming editor for Slicer based on monaco - Issues · SlicerMorph/SlicerEditor</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @chir.set (2024-08-25 20:28 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="37925">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>can you file issues on the repository?</p>
</blockquote>
</aside>
<p><a href="https://github.com/SlicerMorph/SlicerEditor/issues/43" rel="noopener nofollow ugc">Here</a> you go.</p>

---
