# Discourse post directly from error log

**Topic ID**: 124
**Date**: 2017-04-14
**URL**: https://discourse.slicer.org/t/discourse-post-directly-from-error-log/124

---

## Post #1 by @mrjeffs (2017-04-14 22:41 UTC)

<p>i like the idea of having links in slicer directly. may i suggest in the log messages panel adding an additional paste to forum button so when various errors are selected they can be placed directly in the text (or clipboard).<br>
another thought is to have the 1st log entry be a sys info  like the template on the new topic. that way its pre-captured in a structured way. just sayin’<br>
jeff</p>

---

## Post #2 by @lassoan (2017-04-15 02:22 UTC)

<p>I’ve updated links in the error report dialog in Slicer (menu: Help / Report a bug) to point to the Slicer forum.<br>
I’ve also implemented pre-populating the error report post with operating system and Slicer version:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a8422675ccb28afb602b5f819699b3267a2867e.png" data-download-href="/uploads/short-url/1v1S1o2BD4dq6e1tDqQJPnOJYmy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a8422675ccb28afb602b5f819699b3267a2867e.png" alt="image" data-base62-sha1="1v1S1o2BD4dq6e1tDqQJPnOJYmy" width="690" height="456" data-dominant-color="F2F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1233×816 20.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @jcfr (2017-04-15 04:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Well done <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=12" title=":thumbsup:" class="emoji" alt=":thumbsup:" loading="lazy" width="20" height="20"></p>
<p>Look like there are a small issue with new line (tested on Ubuntu 15.10).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8936d2333dab540614561841adbeea6acd438876.png" data-download-href="/uploads/short-url/jzQRL9hPaw47muQvwKWntPmgQe2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8936d2333dab540614561841adbeea6acd438876_2_690x153.png" alt="image" data-base62-sha1="jzQRL9hPaw47muQvwKWntPmgQe2" width="690" height="153" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8936d2333dab540614561841adbeea6acd438876_2_690x153.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8936d2333dab540614561841adbeea6acd438876_2_1035x229.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/8936d2333dab540614561841adbeea6acd438876_2_1380x306.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1577×350 20.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On the other hand, if I do right click and <code>Copy Link Location</code>, the link is this one:</p>
<p><code>https://discourse.slicer.org/new-topic?body=Platform:%20linux-amd64%0AApplication%20version:%204.7.0-2017-04-14%0A%0AExpected%20behavior:%20...%0A%0AActual%20behavior:%20...&amp;category=support</code></p>
<p>and it works as expected if I copy it in the address bar.</p>

---

## Post #4 by @lassoan (2017-04-15 04:22 UTC)

<p>This is very strange, because spaces are correctly resolved. Does it maybe work with %0D instead of %0A?</p>

---

## Post #5 by @lassoan (2017-04-15 20:55 UTC)

<p>I couldn’t find a way to pass multiline text through URL. I’ve changed the pre-populated text to be single-line.</p>

---

## Post #6 by @lassoan (2023-03-21 02:47 UTC)



---
