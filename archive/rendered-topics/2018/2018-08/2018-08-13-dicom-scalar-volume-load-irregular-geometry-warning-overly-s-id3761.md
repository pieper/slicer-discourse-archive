# DICOM scalar volume load: irregular geometry warning overly stringent?

**Topic ID**: 3761
**Date**: 2018-08-13
**URL**: https://discourse.slicer.org/t/dicom-scalar-volume-load-irregular-geometry-warning-overly-stringent/3761

---

## Post #1 by @fedorov (2018-08-13 15:30 UTC)

<p>I noticed that geometry mismatch reporting is overly stringent in reporting errors:</p>
<pre><code class="lang-auto">Irregular volume geometry detected, but maximum error is within 
   tolerance (maximum error of 5.17578e-08 mm, tolerance 
   threshold is 0.001 mm).
</code></pre>
<p>I suggest that if the error is less than the limit, there should be no notification at all.</p>

---

## Post #2 by @pieper (2018-08-13 16:57 UTC)

<p>I think it’s helpful to know if there’s a nonzero geometry issue, even when it is below the threshold.  It could make sense to define an epsilon to account for numerical issues, but it can be hard to pick a valid value for that so letting the user look at the value and, as in this case, ignore it because it’s small.</p>
<p>To put it another way, the Examine step should probably generate some kind of “report” or “assessment” data structure that would describe how well the data matches the requirements of the reader.  The user could choose to look at this or not.</p>
<p>Currently it’s true that the 0.001 mm threshold is very arbitrary and not exposed to the user.</p>

---

## Post #3 by @fedorov (2018-08-13 17:24 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="3761">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I think it’s helpful to know if there’s a nonzero geometry issue</p>
</blockquote>
</aside>
<p>There will always be a nonzero (ie, machine precision) geometry issue, which means there will always be that warning/error message. If we report warning/error every time, chances are it will be ignored, and important issues may be un-noticed. I am not sure it is helpful to know that there is an error of 5e-08. That is not an error.</p>

---

## Post #4 by @pieper (2018-08-13 17:41 UTC)

<p>What I’m saying is that there are really two thresholds of interest - one is the tolerance for “effectively zero” and once is the tolerance for non-zero but not significant.  Would you want to ignore all values less than 1e-6?  Perhaps we should add preference settings for both values.</p>

---

## Post #5 by @fedorov (2018-08-13 17:50 UTC)

<p>Yes, I agree, it makes sense to have 2 thresholds. I guess the difference between the 2 would be warning in the console, or warning in the loadables list?</p>

---

## Post #6 by @pieper (2018-08-13 18:08 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="3761">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I guess the difference between the 2 would be warning in the console, or warning in the loadables list?</p>
</blockquote>
</aside>
<p>Yes, that’s what I would think.  I guess the only question is the best default values for these, since most people wouldn’t be expected to change them in normal practice.</p>

---

## Post #7 by @fedorov (2018-08-13 18:21 UTC)

<p>I think adding the second threshold and setting it to 1e-6 should be harmless, even if it is not exposed in the preferences. All it will do is reduce the amount of red in the python console.</p>

---

## Post #8 by @pieper (2018-08-13 18:41 UTC)

<p>Okay - I’ll add that.</p>

---

## Post #9 by @pieper (2018-08-13 19:00 UTC)

<p>Committed:</p>
<p><a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27350" class="onebox" target="_blank">http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27350</a></p>

---

## Post #10 by @lassoan (2018-08-14 06:56 UTC)

<p>Are these tolerances exposed in the application settings GUI? Tolerances may be different for a microCT or pre-clinical data sets, so it would be better if the user had control over it. We already expose some DICOM settings in the application settings, it should not be difficult to add some more parameters.</p>

---

## Post #11 by @pieper (2018-08-14 13:50 UTC)

<p>It could make sense to add them to the settings under the choice of applying the regularization or not.  In reality the setting is more dataset-specific than global.  We might think about expanding the concept of the DICOMPlugins to include a small user interface to select interpretation options as an alternative to generating a long list of loadables to select among.</p>

---

## Post #12 by @pieper (2018-08-14 13:51 UTC)

<p>For now the tolerances are optional at the python class level, so maybe it’s enough to provide an example of how to use it from the scripting level.</p>

---

## Post #13 by @fedorov (2018-11-01 14:40 UTC)

<p>Not a huge deal, but I just noticed that somehow the tolerance warning is also reported as CRITICAL in the log:</p>
<pre><code class="lang-auto">[WARNING][Python] 01.11.2018 10:19:02 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.9/qt-scripted-modules/DICOMScalarVolumePlugin.py:681) - Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 0.000165356 mm, tolerance threshold is 0.001 mm).
[CRITICAL][Stream] 01.11.2018 10:19:02 [] (unknown:0) - Irregular volume geometry detected, but maximum error non-zero but is within tolerance (maximum error of 0.000165356 mm, tolerance threshold is 0.001 mm).
</code></pre>

---

## Post #14 by @pieper (2018-11-02 01:32 UTC)

<p>Looks to me like it’s calling logging.warning - why is it coming up as critical?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Slicer/Slicer/search?q=Irregular%2Bvolume%2Bgeometry%2Bdetected&amp;unscoped_q=Irregular%2Bvolume%2Bgeometry%2Bdetected">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/search?q=Irregular%2Bvolume%2Bgeometry%2Bdetected&amp;unscoped_q=Irregular%2Bvolume%2Bgeometry%2Bdetected" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/260b51cea87582cb4a1284d84aa26d7d76c757b01131b5c8f7aa1b2fca0e65fd/Slicer/Slicer" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Slicer/Slicer/search?q=Irregular%2Bvolume%2Bgeometry%2Bdetected&amp;unscoped_q=Irregular%2Bvolume%2Bgeometry%2Bdetected" target="_blank" rel="noopener">Search · Irregular volume geometry detected · Slicer/Slicer</a></h3>

  <p>Multi-platform, free open source software for visualization and image computing. - Search · Irregular volume geometry detected · Slicer/Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://github.com/Slicer/Slicer/blob/b0443c748cb51904dfd82fa603b4353a335e3364/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L669-L681" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/b0443c748cb51904dfd82fa603b4353a335e3364/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L669-L681</a></p>

---

## Post #15 by @lassoan (2018-11-02 15:20 UTC)

<aside class="quote no-group" data-username="pieper" data-post="14" data-topic="3761">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Looks to me like it’s calling logging.warning - why is it coming up as critical?</p>
</blockquote>
</aside>
<p>logging.warning messages are stored in the application log correctly as a warning.</p>
<p>However, the warning message is also printed on the console as standard error. Anything that is printed as standard error is stored in the application log as critical error (we have no way of knowing what kind of error was that or it was just a warning).</p>

---

## Post #16 by @pieper (2018-11-02 15:45 UTC)

<p>Okay - makes sense - maybe the dicom loadables should have the option to return both warnings and errors, and then they would be printed to stdout and stderr respectively.</p>

---
