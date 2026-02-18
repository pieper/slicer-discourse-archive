# Exporting Transformations from Sequence in 3D Slicer

**Topic ID**: 28868
**Date**: 2023-04-12
**URL**: https://discourse.slicer.org/t/exporting-transformations-from-sequence-in-3d-slicer/28868

---

## Post #1 by @AliciaPose (2023-04-12 16:21 UTC)

<p>Hi everyone,<br>
I have a sequence in 3D Slicer that reproduces the movement of some 3D models by modifying their associated transforms. The sequence was originally recorded using a tracking system that navigated 4 different tools (so I have 4 transforms).</p>
<p>Whenever I click the Play button, the transforms change based on the recorded pattern.<br>
I would like to play the sequence and export the successive transforms to an external file, such as a CSV file. The ultimate goal is to have a file that contains all the positions and rotations associated with the transform matrices over time.<br>
I would like to obtain this to replicate the animation in another software that doesn’t support “seq” files (such as Unity).</p>
<p>Could anybody provide me with a Python code to extract and save this information?</p>
<p>Thank you very much in advance for your assistance.</p>
<p>Operating system: Windows 11<br>
Slicer version: 5.2.2</p>

---

## Post #2 by @pieper (2023-04-12 16:29 UTC)

<p>I don’t think you can do this without some programming either in Slicer or in Unity.  The transform sequences are saved in mrml with your scene, so it should be straightforward to parse the XML either in C# or some other language to put them in a form for your Unity program.  You’ll need to reverse engineer the mrml format but that shouldn’t be too hard.</p>

---

## Post #3 by @AliciaPose (2023-04-14 08:32 UTC)

<p>Hello Steve,<br>
Thank you for your prompt response.<br>
I was thinking of a piece of Python code that plays the sequence frame by frame in a loop and extracts the transform matrix information at each point using something like transformNode.GetTransformToParentInfo().<br>
While I am able to start the sequence with sequenceNode.PlaybackActiveOn() and stop it with sequenceNode.PlaybackActiveOff(), I am unsure if there is a way to skip to the next frame with Python commands (similar to pressing ctrl+shift+right on my keyboard).<br>
Thank you again for your assistance.</p>

---

## Post #4 by @pieper (2023-04-14 12:17 UTC)

<p>This may be a good example to learn from:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1352-L1360">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1352-L1360" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1352-L1360" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/ScreenCapture/ScreenCapture.py#L1352-L1360</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1352" style="counter-reset: li-counter 1351 ;">
          <li>renderView = self.viewFromNode(viewNode)</li>
          <li>stepSize = (sequenceEndIndex - sequenceStartIndex) / (numberOfImages - 1)</li>
          <li>for offsetIndex in range(numberOfImages):</li>
          <li>    sequenceBrowserNode.SetSelectedItemNumber(int(sequenceStartIndex + offsetIndex * stepSize))</li>
          <li>    filename = filePathPattern % offsetIndex</li>
          <li>    self.addLog("Write " + filename)</li>
          <li>    self.captureImageFromView(None if captureAllViews else renderView, filename, transparentBackground)</li>
          <li>    if self.cancelRequested:</li>
          <li>        break</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2023-04-15 03:31 UTC)

<p>I’m not sure if CSV files would be much easier to parse than seq.nrrd files (both are just simple text files) and introducing yet another file custom format would be a significant overhead in the long-term. Text files are also really slow to read when we record a few sensors for a few ten minutes at dozens of frames per second.</p>
<p>Are you aware of a standard file format for storing transform sequences? (When we looked 10 years ago we did not find one, that’s why we used custom fields in image sequence files - but things might have changed since then.)</p>
<p>If there are commonly used standard file formats for transform sequences then we can add reader/writer for those in Slicer.</p>

---

## Post #6 by @pieper (2023-04-15 14:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="28868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If there are commonly used standard file formats for transform sequences then we can add reader/writer for those in</p>
</blockquote>
</aside>
<p>How about gltf / glb?</p>

---

## Post #7 by @AliciaPose (2023-04-17 12:21 UTC)

<p>Thank you, Steve and Andras.<br>
The piece of code provided by Steve is exactly what I wanted.<br>
Just in case anybody is interested in the final code, it is something like:</p>
<h1><a name="p-93639-code-1" class="anchor" href="#p-93639-code-1" aria-label="Heading link"></a>Code:</h1>
<pre><code># Iterate over the sequence frames
for offsetIndex in range(int(numberOfImages / stepSize)):
    sequenceNode.SetSelectedItemNumber(int(sequenceStartIndex + offsetIndex * stepSize)) # Set sequence frame
    transform = transformNode.GetTransformToParentInfo() # Get the transform at this pint
    listOfTransforms.append([transform.split("\n")[1], transform.split("\n")[2], transform.split("\n")[3], transform.split("\n")[4]]) # Append each row of the transform matrix

# Open the CSV file for writing
with open(myPath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile) # Create a CSV writer object
    for i in range(len(listOfTransforms)):
        csvwriter.writerow([listOfTimestamps[i], listOfTransforms[i]])
</code></pre>
<p>The CSV file contains as many rows as analyzed frames (numberOfImages/stepSize). Each row is something like:<br>
[’    -0.257538  -0.966068  -0.0162887  384.981’, ’    0.660495  -0.163762  -0.732819  -37.6163’, ’    0.705438  -0.199489  0.680316  -221.679’, ’    0  0  0  1’]<br>
Where ’   -0.257538  -0.966068  -0.0162887  384.981’ is the first row of the transform matrix and so on.</p>
<p>Thank you again.</p>

---

## Post #8 by @lassoan (2023-04-23 12:52 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="28868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>How about gltf / glb?</p>
</blockquote>
</aside>
<p>This is an interesting idea. It is a quote widely use standard, if it’s very efficient, and can store animations.</p>
<p>However, it is an export format for 3D rendering and fully optimized for that purpose and it is hard to use it for anything else. For example, extending with custom metadata in a standard way (e.g., so that the extra data survives when it is read into some software and saves from there) is not practically possible. For example, we may be able to read transform sequence into Blender but if we store the transform status in some custom way (or associated image data, etc) then Blender just discards all that data.</p>
<p>Probably all we could use from glTF is some high-level concepts and low-level glTF reader/writer libraries.</p>

---
