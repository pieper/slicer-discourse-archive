# Python interactor showing message when turned on

**Topic ID**: 22701
**Date**: 2022-03-26
**URL**: https://discourse.slicer.org/t/python-interactor-showing-message-when-turned-on/22701

---

## Post #1 by @hourglassnam (2022-03-26 17:03 UTC)

<p>Hello!<br>
I have been getting this message when I load the 3d slicer and I wanted to know if this is something I should be worried about.<br>
I thought this was a default message, but as I go through the forum I have been realizing this is should not happen…<br>
As a python beginner, I don’t fully understand the message.<br>
Can someone please help me to understand what this means and what kind of action I should take?<br>
From what I could understand, the only parts with problems are print command?<br>
If so, is this something I should not be worried about?<br>
Thank you always for your help.<br>
Greatly appreciated.</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\njy95\AppData\Local\NA-MIC\Slicer 4.13.0-2022-02-25\lib\Python\Lib\imp.py”, line 169, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 613, in _exec<br>
File “”, line 846, in exec_module<br>
File “”, line 983, in get_code<br>
File “”, line 913, in source_to_code<br>
File “”, line 228, in _call_with_frames_removed<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 4.13.0-2022-02-25/NA-MIC/Extensions-30657/DatabaseInteractor/lib/Slicer-4.13/qt-scripted-modules/DatabaseInteractor.py”, line 1252<br>
print filesDifference<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(filesDifference)?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\njy95\AppData\Local\NA-MIC\Slicer 4.13.0-2022-02-25\lib\Python\Lib\imp.py”, line 169, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 613, in _exec<br>
File “”, line 846, in exec_module<br>
File “”, line 983, in get_code<br>
File “”, line 913, in source_to_code<br>
File “”, line 228, in _call_with_frames_removed<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 4.13.0-2022-02-25/NA-MIC/Extensions-30657/ShapeQuantifier/lib/Slicer-4.13/qt-scripted-modules/ShapeQuantifier.py”, line 89<br>
print “----- Shape Quantifier widget setup -----”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“----- Shape Quantifier widget setup -----”)?<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\njy95\AppData\Local\NA-MIC\Slicer 4.13.0-2022-02-25\lib\Python\Lib\imp.py”, line 169, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 613, in _exec<br>
File “”, line 846, in exec_module<br>
File “”, line 983, in get_code<br>
File “”, line 913, in source_to_code<br>
File “”, line 228, in _call_with_frames_removed<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 4.13.0-2022-02-25/NA-MIC/Extensions-30657/ShapeQuantifier/lib/Slicer-4.13/qt-scripted-modules/ShapeQuantifierCore.py”, line 43<br>
print “UpdateThreeDView”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“UpdateThreeDView”)?<br>
TODO: implement cloud fingerprint store<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\njy95\AppData\Local\NA-MIC\Slicer 4.13.0-2022-02-25\lib\Python\Lib\imp.py”, line 169, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 613, in _exec<br>
File “”, line 846, in exec_module<br>
File “”, line 983, in get_code<br>
File “”, line 913, in source_to_code<br>
File “”, line 228, in _call_with_frames_removed<br>
File “C:/Users/njy95/AppData/Local/NA-MIC/Slicer 4.13.0-2022-02-25/NA-MIC/Extensions-30657/Slicer-Wasp/lib/Slicer-4.13/qt-scripted-modules/Wasp.py”, line 98<br>
print “progress callback not an int”<br>
^<br>
SyntaxError: Missing parentheses in call to ‘print’. Did you mean print(“progress callback not an int”)?</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/010c91890820c181caf70832e22eeca2b2ab3e80.png" data-download-href="/uploads/short-url/9hp8aBKmGX2uJ5b9wFjES9O4YE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/010c91890820c181caf70832e22eeca2b2ab3e80_2_690x370.png" alt="image" data-base62-sha1="9hp8aBKmGX2uJ5b9wFjES9O4YE" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/010c91890820c181caf70832e22eeca2b2ab3e80_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/010c91890820c181caf70832e22eeca2b2ab3e80_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/010c91890820c181caf70832e22eeca2b2ab3e80_2_1380x740.png 2x" data-dominant-color="BDB9B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×2060 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2022-03-26 20:03 UTC)

<p>That extension hasn’t been updated to work with current Slicer.  You may be able to use it with an older release.</p>

---

## Post #3 by @lassoan (2022-03-27 00:18 UTC)

<p>Watershed segmentation is now available in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/#watershed">Segment Editor in <code>Watershed</code> effect</a>. It is provided by SegmentEditorExtraEffects extension. For many cases <code>Grow from seeds</code> effect work better, so I would recommend to try that, too.</p>

---

## Post #4 by @hourglassnam (2022-03-27 02:22 UTC)

<p>Thank you so much!<br>
My curitosity has been satisfied and I am so glad to know what the message is trying to say!</p>

---

## Post #5 by @hourglassnam (2022-03-27 02:23 UTC)

<p>Thank you lassoan! I will definitely try that!</p>

---
