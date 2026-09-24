---
topic_id: 48238
title: "New extension: OMEZarr - open OME-Zarr images directly in Slicer"
date: 2026-09-23
url: https://discourse.slicer.org/t/48238
last_bumped: 2026-09-23T17:23:04.862Z
---

# New extension: OMEZarr - open OME-Zarr images directly in Slicer

**Topic ID**: 48238
**Date**: 2026-09-23
**URL**: https://discourse.slicer.org/t/new-extension-omezarr-open-ome-zarr-images-directly-in-slicer/48238

---

## Post #1 by @vboussot (2026-09-23 08:54 UTC)

<p>Hi all,</p>
<p>We’re happy to announce <strong>OMEZarr</strong>, a new extension from <a href="https://fideus.io/" rel="noopener nofollow ugc">Fideus Labs</a> that opens and saves OME-Zarr images. It is available in the Extensions Manager for Slicer 5.12.4 and the Preview release, on Linux, macOS and Windows.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb3980f05e0206553c1499f45d64d0536720a348.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53e523718582358d4e0ee916e266f1cb2adfa78c.jpeg" data-video-base62-sha1="zQr2RiiSCDgldUrSiWEb46wX5yg.mp4">
  </div>OME-Zarr is a format increasingly used for large microscopy datasets: a folder of compressed chunks at several resolutions, stored on disk, on a web server or in the cloud. Until now, looking at one in Slicer meant converting it to NRRD or NIfTI first. Now you can:<p></p>
<ul>
<li><strong>Drag an <code>.ome.zarr</code> folder onto Slicer</strong>, or open an <code>https://</code> or <code>s3://</code> address. No conversion.</li>
<li><strong>Open datasets larger than RAM</strong> and progressively refine the views at full resolution, or load a region of interest at any level.</li>
<li><strong>Work with regular Slicer nodes.</strong> Channels become volumes with their names and colours, labels become label maps or segmentations, time series become sequences. Segment Editor, registration and volume rendering work as usual.</li>
<li><strong>Get the geometry right.</strong> Spacing and units (µm, nm) are converted to mm, and the RFC-4 anatomical orientation becomes the IJK-to-RAS matrix.</li>
<li><strong>Save back to OME-Zarr.</strong> Volumes, label maps and segmentations are written as multiscale OME-Zarr, so the results open in napari, Fiji or Python.</li>
</ul>
<p>Reading and writing go through <a href="https://github.com/fideus-labs/ngff-zarr" rel="noopener nofollow ugc">ngff-zarr</a>, which we maintain.</p>
<p>The video is recorded on a public two-photon image of GFP-labelled neurons in a marmoset cortex, streamed from S3. To try it right away, paste this in the Python console:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.util.loadNodeFromFile("s3://ome-zarr-scivis/v0.5/96x2/marmoset_neurons.ome.zarr", "OMEZarr")

</code></pre>
<p>Code and step-by-step tutorial: <a href="https://github.com/fideus-labs/SlicerOMEZarr" class="inline-onebox" rel="noopener nofollow ugc">GitHub - fideus-labs/SlicerOMEZarr: 3D Slicer extension to open OME-Zarr (OME-NGFF) images, built on ngff-zarr · GitHub</a></p>
<p>Please give it a go and tell us what breaks, especially with your own datasets. Thanks to <a class="mention" href="/u/lassoan">@lassoan</a> for reviewing the extension and for the helpful feedback.</p>

---

## Post #2 by @muratmaga (2026-09-23 16:07 UTC)

<p>I am quite excited about this, thanks for implementing the ome-zarr support. When I tried the extension with you example on MacOS (5.12.4)</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.loadNodeFromFile("s3://ome-zarr-scivis/v0.5/96x2/marmoset_neurons.ome.zarr", "OMEZarr")

Traceback (most recent call last):

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/_remote_reader.py", line 498, in open_remote_node

    arr = _run(lambda: AsyncArray.open(store._store, path))

          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/_remote_reader.py", line 100, in _run

    return asyncio.run_coroutine_threadsafe(_invoke(), _io_loop()).result()

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/concurrent/futures/_base.py", line 456, in result

    return self.__get_result()

           ^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result

    raise self._exception

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/_remote_reader.py", line 98, in _invoke

    return await factory()

           ^^^^^^^^^^^^^^^

zarrista.exceptions.ArrayCreateError: Generic S3 error: Error performing PUT http://169.254.169.254/latest/api/token in 2.635813709s, after 10 retries, max_retries: 10, retry_timeout: 180s  - HTTP error: error sending request



The above exception was the direct cause of the following exception:



Traceback (most recent call last):

  File "/Applications/Slicer.app/Contents/Extensions-34645/OMEZarr/lib/Slicer-5.12/qt-scripted-modules/OMEZarr.py", line 1575, in load

    nodes = OMEZarrLogic.loadImage(

            ^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/Extensions-34645/OMEZarr/lib/Slicer-5.12/qt-scripted-modules/OMEZarr.py", line 763, in loadImage

    multiscales = multiscales or cls.openMultiscales(path)

                                 ^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/Extensions-34645/OMEZarr/lib/Slicer-5.12/qt-scripted-modules/OMEZarr.py", line 378, in openMultiscales

    ngff_zarr.from_ome_zarr(source, storage_options=options) if options else ngff_zarr.from_ome_zarr(source)

                                                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/from_ngff_zarr.py", line 264, in from_ome_zarr

    root = _open_root_node(store, version)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/from_ngff_zarr.py", line 158, in _open_root_node

    return _open_remote_root(store, version)

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/from_ngff_zarr.py", line 141, in _open_remote_root

    node = open_remote_node(store)

           ^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/_remote_reader.py", line 504, in open_remote_node

    raise group_error from array_error

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/_remote_reader.py", line 493, in open_remote_node

    group = _run(lambda: AsyncGroup.open(store._store, path))

            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/_remote_reader.py", line 100, in _run

    return asyncio.run_coroutine_threadsafe(_invoke(), _io_loop()).result()

           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/concurrent/futures/_base.py", line 456, in result

    return self.__get_result()

           ^^^^^^^^^^^^^^^^^^^

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/concurrent/futures/_base.py", line 401, in __get_result

    raise self._exception

  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.12/site-packages/ngff_zarr/_remote_reader.py", line 98, in _invoke

    return await factory()

           ^^^^^^^^^^^^^^^

zarrista.exceptions.GroupCreateError: Generic S3 error: Error performing PUT http://169.254.169.254/latest/api/token in 6.812037334s, after 10 retries, max_retries: 10, retry_timeout: 180s  - HTTP error: error sending request

Traceback (most recent call last):

  File "&lt;console&gt;", line 1, in &lt;module&gt;

  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 913, in loadNodeFromFile

    raise RuntimeError(errorMessage)

RuntimeError: Failed to load node from file: s3://ome-zarr-scivis/v0.5/96x2/marmoset_neurons.ome.zarr

Error: Loading s3://ome-zarr-scivis/v0.5/96x2/marmoset_neurons.ome.zarr - Failed to read OME-Zarr: Generic S3 error: Error performing PUT http://169.254.169.254/latest/api/token in 6.812037334s, after 10 retries, max_retries: 10, retry_timeout: 180s  - HTTP error: error sending request
</code></pre>

---

## Post #3 by @vboussot (2026-09-23 16:32 UTC)

<p>Thanks for the report, the traceback pointed straight at it. The extension treated a <code>~/.aws/credentials</code> file as AWS credentials, but the S3 client it uses only reads environment variables, so it ended up asking the EC2 metadata service and failing.</p>
<p>Fixed in <a href="https://github.com/fideus-labs/SlicerOMEZarr/commit/eb3cbbf" class="inline-onebox" rel="noopener nofollow ugc">fix: read public S3 stores anonymously even when an AWS credentials f… · fideus-labs/SlicerOMEZarr@eb3cbbf · GitHub</a> , in tomorrow’s extension build. Until then, in the OME-Zarr module go to Settings → Remote storage options, enter <code>{"anon": true}</code>, and the example loads.</p>

---

## Post #4 by @muratmaga (2026-09-23 16:35 UTC)

<p>I was just about to post it, you beat me to it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>A second suggestion: please consider writing <strong>OME-Zarr 0.6</strong> when a volume has a rotation. Right now the writer uses the 0.5 default, which can only store scale and translation. A volume with a rotated direction matrix, which is common in Slicer after reorienting, is quietly saved axis-aligned, so it no longer lines up with segmentations made on the original. ngff-zarr already supports 0.6 (RFC-5) affines. I tried a small patch locally:</p>
<ul>
<li><strong>Saving:</strong> keep the per-level scale and translation as they are, and add the leftover rotation as an image-level affine, written as 0.6 only when needed.</li>
<li><strong>Loading:</strong> apply that affine when building IJK-to-RAS.</li>
</ul>
<p>With that, an oblique uint16 volume round-trips exactly, and a <code>.seg.nrrd</code> made on the original lines up voxel for voxel. I’m happy to send it as a PR if that’s useful.</p>
<p>This extension is important for us. We are evaluating OME-Zarr as the source-volume format for MorphoDepot, so thanks again for putting it together.</p>

---

## Post #5 by @vboussot (2026-09-23 16:43 UTC)

<p>You are right, thanks for checking it. A PR is very welcome. Great to hear about MorphoDepot.</p>

---

## Post #6 by @muratmaga (2026-09-23 17:23 UTC)

<p>PR is open <a href="https://github.com/fideus-labs/SlicerOMEZarr/pull/13" class="inline-onebox" rel="noopener nofollow ugc">Keep oblique directions by writing an OME-Zarr 0.6 (RFC-5) affine by muratmaga · Pull Request #13 · fideus-labs/SlicerOMEZarr · GitHub</a></p>

---
