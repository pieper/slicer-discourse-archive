# SystemError when loading custom Python module path

**Topic ID**: 1207
**Date**: 2017-10-11
**URL**: https://discourse.slicer.org/t/systemerror-when-loading-custom-python-module-path/1207

---

## Post #1 by @rbrecheisen (2017-10-11 11:07 UTC)

<p>Hi there,</p>
<p>I’m working with Slicer 4.7.0 (see attached screenshot for full details) and I just set a custom Python module path in Edit &gt; Applicaition Settings &gt; Modules. After restarting Slicer I can import my custom module but as soon as the Python console opens I see the following error/warning message:</p>
<p>SystemError: /Users/kitware/Dashboards/Nightly/Slicer-0-build/Python-2.7.13/Objects/classobject.c:521: bad argument to internal function</p>
<p>My custom module script works so I’m not sure whether this is a big problem. Just thought you guys might know what’s going on. Loading a custom Python script seems pretty basic functionality so I was surprised that this error message appears <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Cheers!</p>
<p>Ralph</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6dd83fd761e5972c3cb0b968108be3f9cb4327be.png" alt="13" data-base62-sha1="fFJm69sWqr2FNdtqkrS7pmukQns" width="671" height="418"></p>

---

## Post #2 by @pieper (2017-10-11 12:47 UTC)

<p>Hi Ralph -</p>
<p>What does your scripted module use?  Any binary packages that aren’t built against the Slicer build of python can cause trouble for a binary download of Slicer.</p>
<p>Also a mix of “old style” and “new style” python classes can lead to this message (see the discussions linked below).</p>
<p>If it’s not that can you share the code for an example that leads to the issue?  The simplest code that leads to the message would be the most useful.</p>
<p>Best,<br>
Steve</p>
<p><a href="http://massmail.spl.harvard.edu/public-archives/slicer-devel/2014/016962.html" class="onebox" target="_blank">http://massmail.spl.harvard.edu/public-archives/slicer-devel/2014/016962.html</a></p>
<p><a href="http://slicer-devel-archive.65872.n3.nabble.com/Problems-when-trying-to-build-a-new-extension-td4036566.html" class="onebox" target="_blank">http://slicer-devel-archive.65872.n3.nabble.com/Problems-when-trying-to-build-a-new-extension-td4036566.html</a></p>

---

## Post #3 by @rbrecheisen (2017-10-11 21:39 UTC)

<p>Hi Steve,</p>
<p>My code is no secret. It’s just a file called test_me.py which contains a single method def test_me() that prints “test me”. Can’t get any simpler than that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:">.</p>
<p>By the way, the function works. It prints out “test me” like it’s supposed to. I was just wondering about the error message.</p>
<p>Cheers,</p>
<p>Ralph</p>

---

## Post #4 by @pieper (2017-10-11 22:55 UTC)

<p>Hi Ralph -</p>
<p>Ah, well, then maybe your code is ‘too simple’ to work that way  ; )</p>
<p>We use the term “module” in Slicer to refer to something pretty specific that implements GUI and Logic classes.  That’s what the Module Paths in the settings refers to.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Scripted_Modules" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Scripted_Modules</a></p>
<p>If what you want to do is set up the code like a test_me function to run every time Slicer starts, you can set up a .slicerrc.py file in your home directory as described here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F</a></p>
<p>Hope that helps!<br>
-Steve</p>

---

## Post #5 by @lassoan (2017-10-12 04:34 UTC)

<p>Ralph, you can put your custom (non-Slicer) Python packages in subdirectories within the folder that you specify in “Additional module paths”.</p>

---

## Post #6 by @rbrecheisen (2017-10-12 04:50 UTC)

<p>Hi Steve,</p>
<p>Ok, that was not clear from the what was written at the beginning of the documentation at <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a>. It mentioned "save the .py file to a directory and add the directory to the additional module paths in the Slicer application settings. No mention of a module being anymore than a regular Python module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ef261eaef4f12f5b3f46066411f309d4f002eac.png" data-download-href="/uploads/short-url/6HjgttyPTAUcBbnoF4Zr7tl2g6o.png?dl=1" title="41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef261eaef4f12f5b3f46066411f309d4f002eac_2_690x92.png" alt="41" data-base62-sha1="6HjgttyPTAUcBbnoF4Zr7tl2g6o" width="690" height="92" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef261eaef4f12f5b3f46066411f309d4f002eac_2_690x92.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef261eaef4f12f5b3f46066411f309d4f002eac_2_1035x138.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ef261eaef4f12f5b3f46066411f309d4f002eac_2_1380x184.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">41</span><span class="informations">1434×193 24.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Anyway, thanks for looking into this!</p>
<p>Ralph</p>

---

## Post #7 by @pieper (2017-10-12 11:45 UTC)

<p>Aha, I see - okay, I updated the wiki page to clarify:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Community-contributed_modules" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Community-contributed_modules</a></p>
<p>Let us know if other things aren’t clear.</p>
<p>Best,<br>
Steve</p>

---
