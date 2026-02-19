---
topic_id: 13484
title: "How To Replace The Annotation Fiducial Placement Widget With"
date: 2020-09-14
url: https://discourse.slicer.org/t/13484
---

# How to replace the annotation fiducial placement widget with the plane fiducial widget in AIAA

**Topic ID**: 13484
**Date**: 2020-09-14
**URL**: https://discourse.slicer.org/t/how-to-replace-the-annotation-fiducial-placement-widget-with-the-plane-fiducial-widget-in-aiaa/13484

---

## Post #1 by @Yusuke (2020-09-14 19:39 UTC)

<p>Hi,</p>
<p>I would like to know how to replace the annotation fiducial placement widget with the plane fiducial widget in AIAA.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a6d4171f090876c7b4ff0eb3af0e963d984446a.png" data-download-href="/uploads/short-url/m27BNg2DPvcD8c6giUJUJobvaye.png?dl=1" title="aiaa_fiducial" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6d4171f090876c7b4ff0eb3af0e963d984446a_2_690x372.png" alt="aiaa_fiducial" data-base62-sha1="m27BNg2DPvcD8c6giUJUJobvaye" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6d4171f090876c7b4ff0eb3af0e963d984446a_2_690x372.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a6d4171f090876c7b4ff0eb3af0e963d984446a_2_1035x558.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a6d4171f090876c7b4ff0eb3af0e963d984446a.png 2x" data-dominant-color="3E3C3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">aiaa_fiducial</span><span class="informations">1168×631 96.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In qt windows, for some reasons, the widget is marked as ‘Break Layout’.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ab05753f295aa30afb8aeab59cce6b44977dba1.png" data-download-href="/uploads/short-url/jMTHoWW6tnUotntgsh11SnqsoCJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ab05753f295aa30afb8aeab59cce6b44977dba1_2_690x410.png" alt="image" data-base62-sha1="jMTHoWW6tnUotntgsh11SnqsoCJ" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ab05753f295aa30afb8aeab59cce6b44977dba1_2_690x410.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8ab05753f295aa30afb8aeab59cce6b44977dba1_2_1035x615.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ab05753f295aa30afb8aeab59cce6b44977dba1.png 2x" data-dominant-color="575758"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1076×640 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In .ui file, I believe row <span class="hashtag-raw">#151</span> - 160 represents the widget.</p>
<pre><code>                &lt;item row="1" column="1"&gt;
                    &lt;widget class="qSlicerMarkupsPlaceWidget" name="annotationFiducialPlacementWidget"&gt;
                        &lt;property name="buttonsVisible"&gt;
                            &lt;bool&gt;true&lt;/bool&gt;
                        &lt;/property&gt;
                        &lt;property name="placeMultipleMarkups"&gt;
                            &lt;enum&gt;qSlicerMarkupsPlaceWidget::ForcePlaceMultipleMarkups&lt;/enum&gt;
                        &lt;/property&gt;
                    &lt;/widget&gt;
                &lt;/item&gt;
</code></pre>
<p>so my questions are</p>
<ol>
<li>Why is the widget in qt window marked as ‘Break Layout’?</li>
<li>How can I replace the widget with plane fiducial?</li>
</ol>
<p>Thank you for your help in advance!</p>

---
