# Applying the same data description with one click when loading multiple files

**Topic ID**: 30289
**Date**: 2023-06-28
**URL**: https://discourse.slicer.org/t/applying-the-same-data-description-with-one-click-when-loading-multiple-files/30289

---

## Post #1 by @jhlegarreta (2023-06-28 21:02 UTC)

<p>Hi,<br>
when loading multiple files, is there a way to load them all as, say "FiberBundle"s with a single click, i.e. without needing to chose “FiberBundle” for every individual file? If yes, what is the way to do this?</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-06-30 15:43 UTC)

<p>If you mean in the Add Data dialog, yes, you can hold down Shift while changing the type of one file and it will change the other corresponding ones in the list.</p>

---

## Post #3 by @jhlegarreta (2023-06-30 16:10 UTC)

<blockquote>
<p>If you mean in the Add Data dialog, yes, you can hold down Shift while changing the type of one file and it will change the other corresponding ones in the list.</p>
</blockquote>
<p>Had tried with Shift before posting and it does not work: it only selects the last row I click on. Ubuntu 22.04; Slicer 5.2.2.</p>

---

## Post #4 by @jamesobutler (2023-06-30 16:24 UTC)

<p>I can confirm with Slicer 5.2.2 and latest Slicer preview on Windows, that holding shift and changing the type combobox selection in the “Description” column of the Add Data Dialog does propagate the change to other rows in the table.</p>
<p>In the video below I change the type without pressing shift and it changes only the individual row. Then I press and hold shift and change the type and it changes the type to the other row as well.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f174a253685461a6c9ca4894ea77787f418df3.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f174a253685461a6c9ca4894ea77787f418df3.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f174a253685461a6c9ca4894ea77787f418df3.mp4</a>
    </video>
  </div><p></p>
<p>Maybe the issue is unique to Ubuntu.</p>

---

## Post #5 by @lassoan (2023-06-30 16:33 UTC)

<p>We could use the new file introspection feature to recognize fiber bundle files and by default load them as “FiberBundle”.</p>

---

## Post #6 by @jhlegarreta (2023-06-30 19:19 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="30289">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>In the video below I change the type without pressing shift and it changes only the individual row. Then I press and hold shift and change the type and it changes the type to the other row as well.</p>
</blockquote>
</aside>
<p>OK, that works; my bad then, not the way I expected for it to work: I would have expected to be able to</p>
<ul>
<li>Select all files first holding the shift button; release the shift button (and have all files selected)</li>
<li>Change the Description</li>
<li>The Description to propagate across all files.</li>
</ul>
<p>As shown in here:</p>
<p></p><div class="video-placeholder-container" data-video-src="/404" data-orig-src="upload://rOLC5rITyt3ZXXf082L2dkKeZQV.mp4">
  </div><p></p>
<p>Instead of needing to hold shift when I change the Description. But thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a>; I appreciate a lot having explained it clearly. It saves me time</p>
<p>I also realize that regardless of the files that I select (following the procedure you explained, and regardless of the state of checkboxes), it will change the Description for all files in the list. Is this expected? See the recording:</p>
<p></p><div class="video-placeholder-container" data-video-src="/404" data-orig-src="upload://6z0dBo0s1fxO5bJeeM5aF4SJev4.mp4">
  </div><p></p>
<p>In both cases, the blue overlay adds to the confusion, as usually one expected it to be the span of the data the action will apply. Maybe the same reasoning applies to the checkboxes.</p>
<p>Thanks.</p>

---

## Post #7 by @jhlegarreta (2023-06-30 19:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="30289" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We could use the new file introspection feature to recognize fiber bundle files and by default load them as “FiberBundle”.</p>
</blockquote>
</aside>
<p>For my use case, this would be ideal, but not sure if this conflicts with other uses of those files within the Slicer community. Thanks Andras.</p>

---

## Post #8 by @lassoan (2023-06-30 19:57 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Is there a quick and robust way of determining that a vtk/vtp file contains fiber bundles? Even something like searching for some text in the first few hundred bytes of the file could work.</p>

---

## Post #9 by @pieper (2023-06-30 20:54 UTC)

<p>I wondered that too and took a quick look but didn’t see anything.  I haven’t looked at the vtk readers in a long time to know if there’s something that reads just the metadata of a .vtk file the way you could on, say, a nrrd header.  Does anyone know if that’s possible?</p>
<p>If would be trivial of course if we had thought ahead to use something like a .fiber.vtk file extension but we didn’t.  Maybe it’s not too late to start a convention like that to better support the whitematteranalysis usecase.  Also though since all the cases use the same naming conventions it’s possible to set up .mrml files that you can just copy into a new directory to load cases the way you want.</p>

---

## Post #10 by @lassoan (2023-07-02 12:09 UTC)

<p>We could start using this naming convention now. It is easy to rename existing files to make loading more convenient.</p>
<p>If having hundreds of bundles has become common then it would make sense to develop the same kind of infrastructure as we have for dealing with many segments: multi-select, filter&amp;search, right-click menu for bulk operations, standard terminology (and use it for default naming and coloring).</p>

---

## Post #11 by @pieper (2023-07-02 18:01 UTC)

<p>I agree, at some level the fiber bundles <em>are</em> segments (subdivisions of anatomy).  Maybe they could be proxied to appear in the Segmentations module to avoid duplication of code and user interface concepts.  They are subclasses of Model nodes now, but have multiple display nodes for glyphs, lines, and tubes so there may be some complexities.  Stepping back, dealing with hundreds of anything is Slicer is hard, so maybe we can think of more generic interface tools that work for any kind of nodes.</p>
<p><a class="mention" href="/u/jhlegarreta">@jhlegarreta</a> if it would save you a lot of time, there are a few small (pure python) changes to implement the .fiber.vtk naming idea.  First would be to add it to the whitematteranalysis code as the default output filename.  Second would be to add a custom scripted IO class that detects the file extension and sets a high confidence so it becomes the default for that file extension.</p>

---

## Post #12 by @lassoan (2023-07-02 20:46 UTC)

<p>There is already a FIberBundle reader plugin, so probably all we would need to do is to add <code>.fiber.vtk</code> to the list of extensions.</p>
<p>Automatic detection (not 100% but probably very close) would be to search for <code>&lt;PointData Tensors="Tensors_"&gt;"</code> in the first 1000 bytes of the file - it should appear at around position 500, as fiber vtp files start like this:</p>
<pre><code class="lang-auto">&lt;?xml version="1.0"?&gt;
&lt;VTKFile type="PolyData" version="0.1" byte_order="LittleEndian" header_type="UInt32" compressor="vtkZLibDataCompressor"&gt;
  &lt;PolyData&gt;
    &lt;Piece NumberOfPoints="1079"                 NumberOfVerts="0"                    NumberOfLines="8"                    NumberOfStrips="0"                    NumberOfPolys="0"                   &gt;
      &lt;PointData Tensors="Tensors_"&gt;
        &lt;DataArray type="Float32" Name="Tensors_" NumberOfComponents="9" format="appended" RangeMin="0.00084
</code></pre>
<p>Automatic detection in .vtk files would be hard, as there is nothing very specific at the beginning of the file (the tensor data starts around the middle of the file, so a lot would need to be read, which might slow down the loading).</p>

---

## Post #13 by @pieper (2023-07-02 20:50 UTC)

<p>Thanks for checking <a class="mention" href="/u/lassoan">@lassoan</a> - yes, adding .fiber.vtk and .fiber.vtp to the existing plugin and using those extensions consistently would be the cleanest.</p>

---

## Post #14 by @jhlegarreta (2023-07-03 16:52 UTC)

<blockquote>
<p><a class="mention" href="/u/jhlegarreta">@jhlegarreta</a> if it would save you a lot of time, there are a few small (pure python) changes to implement the .fiber.vtk naming idea. First would be to add it to the whitematteranalysis code as the default output filename. Second would be to add a custom scripted IO class that detects the file extension and sets a high confidence so it becomes the default for that file extension.</p>
</blockquote>
<p>For dMRI/tractography users, having to change the <code>Description</code> every time they load VTP/VTK streamline data into Slicer is not practical, but I understand that there is no (easy) way to tell these files apart from other non-streamline data files. I’m fine even if changes are to be done in C++.</p>
<blockquote>
<p>search for <code>&lt;PointData Tensors="Tensors_"&gt;"</code> in the first 1000 bytes of the file - it should appear at around position 500</p>
</blockquote>
<p>I would not rely on the existence of tensor data in the file: even if some tools (e.g. UKF) may add such data to the file, such data is not strictly required to define a streamline.</p>
<p>As time permits, we can discuss about this to implement some strategy. My bandwidth is very limited now, but I could consider talking offline with Steve so that he can provide with some pointers about the Slicer environment.</p>
<p>Thanks for the thoughts.</p>

---
