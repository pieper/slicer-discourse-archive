# Single Slicer application on Linux

**Topic ID**: 17624
**Date**: 2021-05-14
**URL**: https://discourse.slicer.org/t/single-slicer-application-on-linux/17624

---

## Post #1 by @muratmaga (2021-05-14 20:41 UTC)

<p>I would like to have Slicer installed as a shared application, but people should be able to install extensions to their own home directories.<br>
How can I do that?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3e4de9cb222d267e822c19ba746f167e1f65c78.png" data-download-href="/uploads/short-url/nnSb481UElnspaXKmFY1CgCMIVq.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3e4de9cb222d267e822c19ba746f167e1f65c78_2_345x239.png" alt="image" data-base62-sha1="nnSb481UElnspaXKmFY1CgCMIVq" width="345" height="239" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3e4de9cb222d267e822c19ba746f167e1f65c78_2_345x239.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3e4de9cb222d267e822c19ba746f167e1f65c78_2_517x358.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3e4de9cb222d267e822c19ba746f167e1f65c78_2_690x478.png 2x" data-dominant-color="F5F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">839×583 79.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>[Edit: I need to be able to do this without people manually going to do Application Settings-&gt;Extensions and specifying the correct path. Possibly via script, or if there is a launcher setting something like that…]</p>

---

## Post #2 by @pieper (2021-05-14 21:02 UTC)

<p>I’m not sure what’s best in general, but if this is in the SlicerMorphCloud context where there’s only one user on each instance of the container you could probably put a symbolic link in the image that points to a directory in the user’s file space.</p>

---

## Post #3 by @muratmaga (2021-05-14 21:07 UTC)

<p>This is not just for SlicerMorphCloud docker instance, but in general for any multi-user Linux system, with people that has separate accounts.</p>

---

## Post #4 by @pieper (2021-05-14 21:12 UTC)

<p>How common is that use case these days?  For windows the Slicer default is now to install the user’s home directory which makes it more compatible with shared machines.  I personally don’t use multi-user linux systems, or at least haven’t for years, but I would think that disks are big enough now that each user having their own customized installation of Slicer isn’t a huge burden.  But maybe educational environments are different from my experience.</p>

---

## Post #5 by @lassoan (2021-05-15 00:51 UTC)

<p>Several extensions now rely on installing Python packages from PyPI (to reduce download size and allow pip to sort out package dependencies and version compatibilities). Since all Python packages must be installed within the application folder (in <code>lib\Python\Lib\site-packages</code>), it is not possible to share modifiable Slicer installations between users.</p>
<p>You have two options:</p>
<ul>
<li>A. Share a single, pre-installed, pre-configured, read-only Slicer installation between users.</li>
<li>B. Let each user have his own Slicer where he can install any extensions and Python packages.</li>
</ul>
<p>This is the same how you would manage other Python distributions on a computer. You can either pre-install packages in the shared system Python (that users will not modify); or each user installs Anaconda in his own home folder where he is free to modify/install packages.</p>

---
