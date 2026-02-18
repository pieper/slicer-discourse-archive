# DWIConvert and libITKFactoryRegistration.so error

**Topic ID**: 2395
**Date**: 2018-03-22
**URL**: https://discourse.slicer.org/t/dwiconvert-and-libitkfactoryregistration-so-error/2395

---

## Post #1 by @micaceous (2018-03-22 03:35 UTC)

<p>Hello Slicer team,</p>
<p>I’m running Ubuntu 16.04 on Bash on Windows. I’m using the nightly build, Slicer-4.9.0-2018-02-08-linux</p>
<p>DWIConvert is not working…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93a9ec3143e7cf43106103f664a4437307707260.png" data-download-href="/uploads/short-url/l4ifeuk60zJAEquUiVZmA3ARpYY.png?dl=1" title="Slicer_dwiconvert_error2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93a9ec3143e7cf43106103f664a4437307707260.png" alt="Slicer_dwiconvert_error2" data-base62-sha1="l4ifeuk60zJAEquUiVZmA3ARpYY" width="690" height="113" data-dominant-color="131416"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_dwiconvert_error2</span><span class="informations">883×145 8.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It appears the problem is due to “libITKFactoryRegistration.so” not being found, but it does indeed exist (in /Slicer-4.9.0-2018-02-08-linux-amd64/lib/Slicer-4.9).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84b77bd09c250090da858aaaabe2245290100c8f.png" data-download-href="/uploads/short-url/iW48yvKqsM7TFYjckYG3IgoFTVJ.png?dl=1" title="Slicer_dwiconvert_error3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84b77bd09c250090da858aaaabe2245290100c8f.png" alt="Slicer_dwiconvert_error3" data-base62-sha1="iW48yvKqsM7TFYjckYG3IgoFTVJ" width="690" height="90" data-dominant-color="111315"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_dwiconvert_error3</span><span class="informations">865×113 6.29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Both problems also exist when I try using the stable 4.8 version.<br>
This used to work with previous version Slicer 4.6 (is it a problem that I deleted that older version, but the path to that now-deleted version is still in my $PATH, from setup in my ~/.profile?)</p>
<p>I also <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings" rel="noopener nofollow ugc">saw</a> that there is a way to delete previous settings involving this file (~/.config/NA-MIC/) but I’m scared to do this without knowing exactly what to do (if it’s required, can you guide me how to?)</p>
<p>Any other info you need?</p>
<p>Many thanks,<br>
Micah</p>

---
