# Can't view DICOM in native plane

**Topic ID**: 44889
**Date**: 2025-10-27
**URL**: https://discourse.slicer.org/t/cant-view-dicom-in-native-plane/44889

---

## Post #1 by @invictus (2025-10-27 04:09 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.9.0-2025-10-23<br>
Expected behavior: Scroll through a stack of DICOM images in the plane acquired.<br>
Actual behavior: Plane is listed as ‘Reformat’, scroll tool doesn’t work, and if I drag the slider on the red image, it shows only half the volume, with volume averaging between slices.</p>
<p>I suspect there is some irregularity with the DICOM metadata that Slicer is not handling well, such as the patient position being negative and not evenly spaced. The data are highly anonymized, taken from the RSNA Intracranial Hemorrhage Detection Challenge (2019) dataset. Other DICOM viewers deal with it fine.</p>
<p>Here is a sample dataset:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fi/e23ddr49rvbgh0cnhk7cq/ID_1d3214c5b.zip?rlkey=6vpndotjo9zgqx6wvjzl9jkhl&amp;dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fi/e23ddr49rvbgh0cnhk7cq/ID_1d3214c5b.zip?rlkey=6vpndotjo9zgqx6wvjzl9jkhl&amp;dl=0" target="_blank" rel="noopener nofollow ugc">dropbox.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://www.dropbox.com/scl/fi/e23ddr49rvbgh0cnhk7cq/ID_1d3214c5b.zip?rlkey=6vpndotjo9zgqx6wvjzl9jkhl&amp;dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2025-10-27 14:23 UTC)

<p>That data is indeed weird.  It seems someone may have tried to compensate for gantry tilt somehow and the header geometry is non-standard.</p>
<p>If you manually switch the red and yellow views to axial and sagittal then things look correct, but I’d still use caution.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c08eef4e43537e0cb37b08ba26f112a430fc81.png" data-download-href="/uploads/short-url/767WViHMsU6VXdiWEWYOF4srnz3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31c08eef4e43537e0cb37b08ba26f112a430fc81_2_388x499.png" alt="image" data-base62-sha1="767WViHMsU6VXdiWEWYOF4srnz3" width="388" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31c08eef4e43537e0cb37b08ba26f112a430fc81_2_388x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31c08eef4e43537e0cb37b08ba26f112a430fc81_2_582x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c08eef4e43537e0cb37b08ba26f112a430fc81.png 2x" data-dominant-color="424046"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">750×965 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2025-10-29 14:48 UTC)

<p>It seems that the acquisition normalization does not compensate for cases when the IJK to RAS matrix is linear but non-orthogonal. As a result, a slice view may be set up with non-orthogonal axes, resulting in distorted appearance:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11aab39e08b840f4962e4eb84dc45b140ea45e0e.jpeg" data-download-href="/uploads/short-url/2whQiCqtqZpVmwhlBpATt8khv0q.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11aab39e08b840f4962e4eb84dc45b140ea45e0e_2_690x441.jpeg" alt="image" data-base62-sha1="2whQiCqtqZpVmwhlBpATt8khv0q" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11aab39e08b840f4962e4eb84dc45b140ea45e0e_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11aab39e08b840f4962e4eb84dc45b140ea45e0e_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11aab39e08b840f4962e4eb84dc45b140ea45e0e.jpeg 2x" data-dominant-color="4F4D47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×875 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/pieper">@pieper</a> could you have a look at the acquisition normalization code if this behavior is expected? It would be better if the IJKToRAS matrix in the volume would be always orthogonal because at many places this may be assumed. The acquisition transform could contain the skewing operation.</p>

---

## Post #4 by @pieper (2025-10-29 15:03 UTC)

<p>It’s not the acquisition normalization, it’s the behavior of the Slice view for this data that is wrong.</p>
<p>The transform is basically identity (no visible difference if you remove it), so at most it’s being overcautious.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; arrayFromGridTransform(getNode("U*m")).max()
0.043207675834310066
</code></pre>
<p>You can remove the nonlinear transform and volume render and the skull is not distrorted, but the slice view still is.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a58056d83283d25c024f59e14563da8de85f1622.jpeg" data-download-href="/uploads/short-url/nC5KnXQUrPcAyoPbGXk3QN7KcDw.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a58056d83283d25c024f59e14563da8de85f1622.jpeg" alt="image" data-base62-sha1="nC5KnXQUrPcAyoPbGXk3QN7KcDw" width="592" height="466"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">592×466 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The direction matrix is definitely sheared, and that seems not to be taken into account by the current slice view code.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1cd957f5bdcad0ebc5297887cce9454e1e01c14.png" data-download-href="/uploads/short-url/wdxTkIdmWsV6y44dSe093Nt4KmU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1cd957f5bdcad0ebc5297887cce9454e1e01c14_2_690x217.png" alt="image" data-base62-sha1="wdxTkIdmWsV6y44dSe093Nt4KmU" width="690" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1cd957f5bdcad0ebc5297887cce9454e1e01c14_2_690x217.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1cd957f5bdcad0ebc5297887cce9454e1e01c14_2_1035x325.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1cd957f5bdcad0ebc5297887cce9454e1e01c14.png 2x" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1262×398 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> as I described above this shearing is only in the reformat view, not in sagittal, so the problem is with the initial Reformat display.</p>

---

## Post #5 by @lassoan (2025-10-29 17:47 UTC)

<p>I agree, we should modify <code>vtkMRMLSliceNode::RotateToAxes</code> to always enforce the slice view axes to be orthogonal. However, we should still reduce the probability of having sheared images (images with non-orthogonal axes) in the scene, because orthogonal axes may be assumed in many other places (e.g., fit to volume feature seem to be misbehaving, too; and of course many extensions may not work well on sheared images either).</p>
<p>While non-orthogonal axes can come from various sources, a DICOM import is a very common one. It would be valuable if a DICOM import would never produce sheared images. Having an orthogonal image under a warping transform would work better, because this case is explicitly handled at many places. Since we already have acquisition geometry regularization during DICOM import to take care of some warping transforms, we could modify it to also include the shearing component of linear transforms.</p>

---

## Post #6 by @pieper (2025-10-29 18:27 UTC)

<p>Yes, the acquisition transform would be able to compensate if we enforced orthogonality of the directions.  I know we’ve talked about this before and researched it and my recollection was that ITK enforces orthogonal directions in some cases - maybe just for nifti?</p>
<p>As a reminder, the way the acquisition transform works is that it uses the vtkITK reader code, which internally uses DCMTK or GDCM, to get the vtkImageData and the IJKToRAS transform.  Then it looks at the corners of each slice and creates the oriented grid transform to put them where the ImagePositionPatient and ImageOrientationPatient says they should go.</p>
<p>For this data, because the IJKToRAS directions include the shear, the corners are basically in the right places and the acquisition transform is nearly identity.</p>
<p>I’m thinking what we should do at the ScalarVolumePlugin level is to load the original volume, the transform, and a resampled version of the volume into the scene.  The resampled one can have orthogonal directions.  Most times that resampled version is what people will want.  According to that recent study Avisio probably is doing this behind the scenes automatically.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://peerj.com/articles/20172/">
  <header class="source">
      <img src="https://d2pdyyx74uypu5.cloudfront.net/images/favicon/peerj/android-icon-192x192.png" class="site-icon" alt="" width="192" height="192">

      <a href="https://peerj.com/articles/20172/" target="_blank" rel="noopener">PeerJ</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:309/500;"><img src="https://dfzljdn9uc3pi.cloudfront.net/2025/20172/1/fig-1-1x.jpg" class="thumbnail" alt="" width="309" height="500"></div>

<h3><a href="https://peerj.com/articles/20172/" target="_blank" rel="noopener">Easier said than done: unexpected hurdles to preparing ∼1,000 cranial CT...</a></h3>

  <p>Background As science becomes more open and accessible, researchers are increasingly encouraged—and sometimes required—to share their digital data on public repositories. While this promotes transparency and reusability, it can also introduce...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2025-10-29 18:48 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="44889">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>ITK enforces orthogonal directions in some cases - maybe just for nifti?</p>
</blockquote>
</aside>
<p>ITK in general does not generally enforce orthogonal image axis when reading/writing, but its NIFTI reader/writer imposes orthogonality constraints. So, if we want orthogonal axes when reading DICOM then Slicer needs do it.</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="44889">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’m thinking what we should do at the ScalarVolumePlugin level is to load the original volume, the transform, and a resampled version of the volume into the scene.</p>
</blockquote>
</aside>
<p>Currently, the user can choose between skipping regularization, apply a transform, or harden a transform (and the choice is stored persistently in application settings / DICOM). Setting the default to “harden” would be the behavior that most users would expect. I don’t think we need to load two versions of the same volume, as it could be confusing; but if you think it could be useful then it could be fourth option.</p>

---

## Post #8 by @pieper (2025-10-29 19:36 UTC)

<p>Part of the problem is that we aren’t allowing the plugins to expose any GUI so that users can pick how they want to interpret the data on a per-<code>loadable</code> basis, they only get to pick which plugin to use.  Having the option in the application settings is suboptimal because it’s not available or discoverable when the data is being loaded.</p>
<p>In ambiguous cases it could make sense for the <code>examine</code> step to return data that the could inform a GUI layer of specific options and then a GUI could be created to select options to send back to the <code>load</code> step.  That way it would also be possible script the <code>examine/load</code> preferences when batch processing data.  It would be pretty easy to add a button next to the checkbox to raise a plugin-specific dialog if it’s available.  This could be simpler for things like sequences too so that instead of showing a bunch of <code>loadables</code> you would have one sequence loadable with a dialog to pick the dimension index.</p>

---
