# Matlab Functions for Interacting with Slicer Data?

**Topic ID**: 786
**Date**: 2017-07-29
**URL**: https://discourse.slicer.org/t/matlab-functions-for-interacting-with-slicer-data/786

---

## Post #1 by @_jmichael (2017-07-29 22:32 UTC)

<p>Are there any existing collections of functions developed for Matlab that allow data saved from Slicer (e.g. markups fiducial, affine transforms, etc.) to be loaded in/out of Matlab?<br>
I’m aware of the Matlab Bridge extension of course, but rather something where the connection is not “live”. For instance, loading a .fcsv file created by Slicer into Matlab for analysis or writing points calculated in Matlab to a .fcsv file to be visualized using Slicer.</p>
<p>I found myself writing some <a href="https://github.com/jstnmchl/slicerUtils" rel="nofollow noopener">simple MATLAB code</a> to do this and thought I might check,</p>
<ol>
<li>Does something like this already exist? and</li>
<li>If it doesn’t and I made something like it, would others find it useful?</li>
</ol>
<p>Thanks in advance for your help!</p>

---

## Post #2 by @lassoan (2017-07-30 00:30 UTC)

<p>MatlabBridge has all the reader and writer functions for reading images, transforms, models, fiducials, etc. You can use them interactively through MatlabBridge in Slicer; or just use them independently from Slicer, in any Matlab project:</p>
<p><a href="https://subversion.assembla.com/svn/slicerrt/trunk/MatlabBridge/src/MatlabCommander/commandserver/" class="onebox" target="_blank">https://subversion.assembla.com/svn/slicerrt/trunk/MatlabBridge/src/MatlabCommander/commandserver/</a></p>
<p>Let me know if you developed any additional reader/writer that is not there yet, we can add them, too.</p>

---
