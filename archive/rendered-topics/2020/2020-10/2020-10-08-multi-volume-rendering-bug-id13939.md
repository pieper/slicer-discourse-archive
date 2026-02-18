# Multi-volume rendering bug

**Topic ID**: 13939
**Date**: 2020-10-08
**URL**: https://discourse.slicer.org/t/multi-volume-rendering-bug/13939

---

## Post #1 by @muratmaga (2020-10-08 18:19 UTC)

<p>Shading in the multi-volume rendering worked for a while for me, but in this dataset I am getting this error:</p>
<pre><code>Loaded volume from file: C:/Users/amaga/Desktop/Cuke_9.9um_2k__rec_Cor0556 Segment_1_1.nrrd. Dimensions: 326x805x343. Number of components: 1. Pixel type: unsigned char.
vtkMRMLScene::Clear
"Volume" Reader has successfully read the file "C:/Users/amaga/Desktop/Cuke_9.9um_2k__rec_Cor0556 Segment_1_1.nrrd" "[0.19s]"
Loaded volume from file: C:/Users/amaga/Desktop/Cuke_9.9um_2k__rec_Cor0556 Segment_2.nrrd. Dimensions: 648x2233x780. Number of components: 1. Pixel type: unsigned char.
vtkMRMLScene::Clear
"Volume" Reader has successfully read the file "C:/Users/amaga/Desktop/Cuke_9.9um_2k__rec_Cor0556 Segment_2.nrrd" "[1.29s]"
The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn't return data of type vtkObject. 
The slot ( "1onDisplayNodeModified(vtkObject*, vtkObject*)" ) owned by  QObject( "" )  may be incorrect.
void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject *,class vtkObject *) : Invalid object type calling display node modified event
The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLScalarVolumeNode )  doesn't return data of type vtkObject. 
The slot ( "1onDisplayNodeModified(vtkObject*, vtkObject*)" ) owned by  QObject( "" )  may be incorrect.
void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject *,class vtkObject *) : Invalid object type calling display node modified event
</code></pre>
<p>And it looks like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f60d9cfb5aee9f9bba9dbe41677adea4444fe908.png" alt="image" data-base62-sha1="z6GCGgDYZ1CKIwMAjdPwgcrFtI4" width="298" height="163"><br>
instead of<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0da79954ad8eec076e65875aa9a73e3a2b100479.jpeg" alt="image" data-base62-sha1="1WNhKb2GCp0fDGJzwz6Ole22Rxn" width="291" height="145"></p>

---

## Post #2 by @lassoan (2020-10-08 18:29 UTC)

<p>What Slicer version did the correct rendering and which one failed? Does it work well if you downsample the volume? How the image changes if you move the shift slider? Do Advanced/Techniques/Quality settings make a difference?</p>

---

## Post #3 by @muratmaga (2020-10-08 18:46 UTC)

<p>This error is with the current stable. Last time I played with multi-volume rendering was in august, but I can’t remember the specific version it worked (it wasn’t with this dataset either).</p>
<p>As far as I can tell none of those settings make a difference.</p>

---

## Post #4 by @muratmaga (2020-10-08 19:49 UTC)

<p>Here is a link to the data (contains two nrrds)</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1-a8ye6EJ7XyCKGuimRiSmAGCqjdJa0TN/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1-a8ye6EJ7XyCKGuimRiSmAGCqjdJa0TN/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1-a8ye6EJ7XyCKGuimRiSmAGCqjdJa0TN/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">multivolume_issue.zip</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2020-10-09 01:04 UTC)

<p>Thank you for the sample images, I was able to reproduce the issue. The problem is that automatic sampling step computation does not work in the multivolume renderer, so the image spacing has to be approximately 1 to get good-quality rendering. The easiest is to edit spacing information in Volumes module (change the decimal point location). It would be great if you could enter a bug report for this so that we can investigate after VTK9 migration is completed.</p>

---

## Post #6 by @muratmaga (2020-10-09 03:28 UTC)

<p>Thank you. I am trying. But why is changing the location of decimal place is so hard in volumes? The field is trying to be smart at guessing what I am trying to do and failing miserably. For example, try shifting the decimal place one to the left in the origin tab of the MRHead. My behavior is to delete the decimal point and I can’t edit because the moment I delete that, Slicer adds a new decimal point at the end followed by 000.</p>
<p>I really find it frustrating that those field to do things automatically before I finish entering values.</p>

---

## Post #7 by @lassoan (2020-10-09 04:38 UTC)

<p>I agree, it’s very annoying. The ctkDoubleSpinBox widget tries to be smart, but enforcing valid input during typing (after each keypress) is just so hard, probably in many cases it is not even feasible. See also <a href="https://discourse.slicer.org/t/slicer-roi-dimensions-input-numbers-autofill/12773/6">this discussion</a>. We should probably only validate values on Enter/leave.</p>

---

## Post #8 by @muratmaga (2023-04-25 21:05 UTC)

<p>Today I accidentally turned on the VTK MultiVolume Rendering on 5.2.2 and pleasantly surprised to see that shading is now supported even with the small voxel sizes.</p>
<p>Performance is slow with Normal quality, but quite reasonable with Adaptive setting. Also there seems a centering bug, but otherwise it actually looks quite nice.</p>
<p>Well done.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b07932695ec59e4131ae0674dac8d1ab471eb502.jpeg" data-download-href="/uploads/short-url/pb9Hh7IPivmmqQKJrN5UitfERDI.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b07932695ec59e4131ae0674dac8d1ab471eb502_2_554x500.jpeg" alt="image" data-base62-sha1="pb9Hh7IPivmmqQKJrN5UitfERDI" width="554" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b07932695ec59e4131ae0674dac8d1ab471eb502_2_554x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b07932695ec59e4131ae0674dac8d1ab471eb502_2_831x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b07932695ec59e4131ae0674dac8d1ab471eb502_2_1108x1000.jpeg 2x" data-dominant-color="9994B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1354×1222 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @muratmaga (2023-04-26 01:04 UTC)

<p>I really like the new multi-volume rendering. it allows striking visualizations. It is so nice to see all these tools coming together (done in about 3 minutes using, total segmentator, SegmentEditor with split volumes, and volume rendering).</p>
<p>Now let’s have the cropping working in the MultiVolume Rendering and it will be great.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81b3bbc5f75d3d8559627d7554a373900cf0155e.jpeg" data-download-href="/uploads/short-url/ivoFAZosgKwFNJFfZtGfJe97M5g.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81b3bbc5f75d3d8559627d7554a373900cf0155e_2_405x500.jpeg" alt="image" data-base62-sha1="ivoFAZosgKwFNJFfZtGfJe97M5g" width="405" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81b3bbc5f75d3d8559627d7554a373900cf0155e_2_405x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81b3bbc5f75d3d8559627d7554a373900cf0155e_2_607x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81b3bbc5f75d3d8559627d7554a373900cf0155e_2_810x1000.jpeg 2x" data-dominant-color="272629"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">855×1053 38.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
