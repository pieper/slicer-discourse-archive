# Parsing a json file for specifying the terminology for segment editor

**Topic ID**: 30505
**Date**: 2023-07-10
**URL**: https://discourse.slicer.org/t/parsing-a-json-file-for-specifying-the-terminology-for-segment-editor/30505

---

## Post #1 by @DeepaKrishnaswamy (2023-07-10 23:16 UTC)

<p>Hi,</p>
<p>I have a json file that contains the necessary information for specifying the terminology for the segment editor, similar to <a href="https://github.com/QIICR/dcmqi/blob/master/doc/schemas/segment-context-schema.json" rel="noopener nofollow ugc">this</a>.</p>
<p>To use this file, I see that I can do something like:<br>
<code>terminologyFile = path_to_json_file</code><br>
<code>tlogic = slicer.modules.terminologies.logic()</code><br>
<code>terminologyName = tlogic.LoadTerminologyFromFile(terminologyFile)</code></p>
<p>However, if I have a different json file that contains the terminology specification as well as other additional fields, I cannot use the above method. Has anyone tried to parse and set the terminology correctly in this case?</p>
<p>So far I have tried using <code>tlogic.DeserializeTerminologyEntry</code>, but I encounter errors in failing to get the terminology category.</p>
<p>Thank you,</p>
<p>Deepa</p>

---

## Post #2 by @muratmaga (2023-07-11 06:19 UTC)

<p>you may want to check whether your JSON file is valid using this tool.</p>
<p><a href="https://qiicr.org/dcmqi/#/validators" class="onebox" target="_blank" rel="noopener">https://qiicr.org/dcmqi/#/validators</a></p>

---

## Post #3 by @DeepaKrishnaswamy (2023-07-11 15:24 UTC)

<p>Sorry, perhaps I didn’t explain it properly.</p>
<p>My original json file is valid, here is a snippet:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55b2b30068d0723bca9bacbb00c42578b53da459.png" alt="image" data-base62-sha1="ce7rFCDUq2UarDW6q4cGPDzvxfr" width="685" height="445"></p>
<p>However the new json file I am creating contains the fields for the terminology along with extra fields required for the extension I’m working on. For instance, something like this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269f739a2bff65b55ae24b627e256b4b918b1b95.png" data-download-href="/uploads/short-url/5vFLztnbJMDwI4brdOl7kvSFkLH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269f739a2bff65b55ae24b627e256b4b918b1b95.png" alt="image" data-base62-sha1="5vFLztnbJMDwI4brdOl7kvSFkLH" width="688" height="500" data-dominant-color="FAFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">888×645 15.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Therefore, I need to parse this new json file to set up the terminology appropriately.</p>
<p>Thank you,</p>
<p>Deepa</p>

---
