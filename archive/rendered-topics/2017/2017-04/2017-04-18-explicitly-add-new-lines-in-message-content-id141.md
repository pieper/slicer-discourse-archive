---
topic_id: 141
title: "Explicitly Add New Lines In Message Content"
date: 2017-04-18
url: https://discourse.slicer.org/t/141
---

# Explicitly add new lines in message content

**Topic ID**: 141
**Date**: 2017-04-18
**URL**: https://discourse.slicer.org/t/explicitly-add-new-lines-in-message-content/141

---

## Post #1 by @jcfr (2017-04-18 19:08 UTC)

<p>To facilitate reading of history using either <code>git log</code>, <code>gitk</code>, … I suggest we consistently format commit messages by explicitly adding newlines.</p>
<h3><a name="p-350-without-newlines-1" class="anchor" href="#p-350-without-newlines-1" aria-label="Heading link"></a>without newlines:</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/700c6685e325e1fbe226d4a0a28a8b16949a137c.png" data-download-href="/uploads/short-url/fZe2LqKp4D2Forcx13yBXoghz52.png?dl=1" title="without-newline.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/700c6685e325e1fbe226d4a0a28a8b16949a137c_2_690x138.png" data-base62-sha1="fZe2LqKp4D2Forcx13yBXoghz52" width="690" height="138" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/700c6685e325e1fbe226d4a0a28a8b16949a137c_2_690x138.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/700c6685e325e1fbe226d4a0a28a8b16949a137c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/700c6685e325e1fbe226d4a0a28a8b16949a137c.png 2x" data-dominant-color="DFE2DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">without-newline.png</span><span class="informations">836×168 23.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-350-with-newlines-2" class="anchor" href="#p-350-with-newlines-2" aria-label="Heading link"></a>with newlines</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a73e6abca92394e2ad78c633b5d46c1ff452b5.png" data-download-href="/uploads/short-url/gmgKuroxNI717DJ0fwWFurrCtcV.png?dl=1" title="with-newline-1.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72a73e6abca92394e2ad78c633b5d46c1ff452b5.png" data-base62-sha1="gmgKuroxNI717DJ0fwWFurrCtcV" width="690" height="255" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">with-newline-1.png</span><span class="informations">796×295 36.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329312df04a106a526debe9415085105c7f6be03.png" data-download-href="/uploads/short-url/7doYBwIXwHBgbJqFRgc5UboKnPt.png?dl=1" title="with-newline-2.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/329312df04a106a526debe9415085105c7f6be03_2_690x159.png" data-base62-sha1="7doYBwIXwHBgbJqFRgc5UboKnPt" width="690" height="159" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/329312df04a106a526debe9415085105c7f6be03_2_690x159.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329312df04a106a526debe9415085105c7f6be03.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329312df04a106a526debe9415085105c7f6be03.png 2x" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">with-newline-2.png</span><span class="informations">915×212 27.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2017-04-18 21:28 UTC)

<p>Is there a commit hook that can do that?</p>

---

## Post #3 by @jcfr (2017-04-18 21:33 UTC)

<p>Not that I am aware.</p>
<p>Using <code>git gui</code> (or any git frontend) should allow to easily format the message before running <code>git svn dcommit</code>.</p>
<p>Text editor like vim, emacs can also be configured to wrap lines while editing.</p>

---

## Post #4 by @lassoan (2017-04-18 22:24 UTC)

<p>I like that I can take advantage of whatever screen size I have (if I make my window wider I see longer lines) and adding line breaks manually is a chore, but if everybody prefers short lines then I’m OK with it.</p>
<p>We have some hooks for checking commit message format (starts with ENH: …) but maybe that’s only for SVN?</p>

---

## Post #5 by @cpinter (2017-04-18 22:34 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="3" data-topic="141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>(or any git frontend) should allow to easily format the message</p>
</blockquote>
</aside>
<p>Not true for TortoiseGit, which is the one I use (and most of the Windows people I know).</p>
<p>In general I find these limitations about line length unreasonable, especially introducing new ones. That said I can hit enter once in a while if that’s what the community requires.</p>

---

## Post #6 by @cpinter (2017-04-19 12:34 UTC)

<p>Just one more note here. I think the deficiency of the Git GUI application is not that it doesn’t hard-break the lines, but that it doesn’t wrap them when displaying. For example this is how I see it:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3420223ca34f11fe265c042eb8c27dcaae9b8faf.png" data-download-href="/uploads/short-url/7r7FPsTqTO0P5M2xx5sP1ne9uft.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3420223ca34f11fe265c042eb8c27dcaae9b8faf.png" alt="image" data-base62-sha1="7r7FPsTqTO0P5M2xx5sP1ne9uft" width="690" height="177" data-dominant-color="E5E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">741×191 11.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
