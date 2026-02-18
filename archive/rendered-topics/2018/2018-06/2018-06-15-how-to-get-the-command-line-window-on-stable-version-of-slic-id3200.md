# How to get the command line window on stable version of slicer

**Topic ID**: 3200
**Date**: 2018-06-15
**URL**: https://discourse.slicer.org/t/how-to-get-the-command-line-window-on-stable-version-of-slicer/3200

---

## Post #1 by @chaddy1004 (2018-06-15 18:36 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/246e8fdd4005b27ca5c823c9275123eb21e98473.png" data-download-href="/uploads/short-url/5ci491xvJRec8PgH9OphX12ZrYD.png?dl=1" title="slicerquestion" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246e8fdd4005b27ca5c823c9275123eb21e98473_2_690x418.png" alt="slicerquestion" data-base62-sha1="5ci491xvJRec8PgH9OphX12ZrYD" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246e8fdd4005b27ca5c823c9275123eb21e98473_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246e8fdd4005b27ca5c823c9275123eb21e98473_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/246e8fdd4005b27ca5c823c9275123eb21e98473_2_1380x836.png 2x" data-dominant-color="9B9CAB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerquestion</span><span class="informations">1433×870 74.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello</p>
<p>When I use nightly version of slicer, the command line window shows up when I open up the program.<br>
Is there an option/setting so that I can have the window pop up for the stable version of Slicer?</p>
<p>Thank you!</p>
<p>Chad Paik</p>

---

## Post #2 by @lassoan (2018-06-15 19:01 UTC)

<p>Unfortunately, the console cannot be hidden/shown dynamically (if you hide it dynamically then you would need to show again when exiting the application, which would look bad). Official builds (both nightly and stable) supposed to have the console disabled.</p>
<p>You can see approximately the same content in the log window (click the small x icon in the lower-right corner in the status bar), even more content application log file (you can see paths in menu: Help / Report a bug). If these don’t work for you then you need to build Slicer with console enabled.</p>

---
