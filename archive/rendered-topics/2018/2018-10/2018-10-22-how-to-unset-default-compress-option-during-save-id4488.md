# How to unset default 'compress' option during save

**Topic ID**: 4488
**Date**: 2018-10-22
**URL**: https://discourse.slicer.org/t/how-to-unset-default-compress-option-during-save/4488

---

## Post #1 by @muratmaga (2018-10-22 15:37 UTC)

<p>Hi,</p>
<p>Is there a way to default compress option to NO for save dialog? Compress option is not visible immediately to new Slicer users, and compressing single threaded such large dataset (2000^3) is extremely slow. We are talking about 15 sec for uncomressed data and dozens of minutes with compress enabled on an ssd. Again for a new user, it is not immediately clear to the user whether Slicer stalled/crashed or doing something.</p>
<p>In case someone wants to see, here is a test dataset:<br>
<a href="https://ndownloader.figshare.com/files/12808130" class="onebox" target="_blank" rel="noopener">https://ndownloader.figshare.com/files/12808130</a></p>

---

## Post #2 by @Andinet_Enquobahrie (2018-10-22 16:27 UTC)

<p>In the Save Dialog box, click on “Show options”,  then you can toggle off “Compress” option in the options column.</p>
<p>-Andinet</p>

---

## Post #3 by @lassoan (2018-10-22 17:55 UTC)

<p>For some users it makes more sense to enable compression by default, for some others, disabling compression by default is preferable.</p>
<p>You can set default file type and saving options by specifying a default storage node by adding 3 lines to your application startup script as shown in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_file_type_for_nodes_.28that_have_never_been_saved_yet.29">script repository</a>.</p>

---

## Post #4 by @pieper (2018-10-22 18:59 UTC)

<p>To me it’s easier to learn to set the save option than it is to add a .slicerrc.py option.</p>
<p>But rather than making this either compression or fast save, maybe we can try to get the benefits of both with something like this: <a href="https://zlib.net/pigz/">https://zlib.net/pigz/</a> (I haven’t tried this).</p>

---

## Post #5 by @muratmaga (2018-10-22 19:03 UTC)

<p>From a user point of view, this would make sense to be a setting under preferences option.</p>
<p>I use pigz from command line, and it works really well on multi core systems. It would be good to have it in slicer.</p>

---

## Post #6 by @pieper (2018-10-22 19:41 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="4488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>From a user point of view, this would make sense to be a setting under preferences option.</p>
</blockquote>
</aside>
<p>Yes, I can see how this would be a convenience for people who always want one thing or the other.  My concern is that this is pretty hidden away and is pretty obscure.  With nrrd files it’s not easy for users to know if it’s compressed (need to look in the header or guess based on file size).  So sticking with compressed all the time is the best thing if we can make it fast enough.</p>
<p>Just to confirm <a class="mention" href="/u/muratmaga">@muratmaga</a> would you really want lots of 2000^3 files on your disk that were mostly zeros?</p>

---

## Post #7 by @pieper (2018-10-22 20:48 UTC)

<p>Follow up on pigz, there’s a <a href="https://github.com/madler/pigz">github repo</a> and the author seems <a href="https://en.wikipedia.org/wiki/Mark_Adler">quite legit</a>.  But there’s no obvious windows support so probably a cmakeification effort would be needed.</p>

---

## Post #8 by @muratmaga (2018-10-22 22:04 UTC)

<p>Even SSD storage is so cheap now that the time consumption waiting for lots of zeros to be compressed into fewer zeros is hardly justifiable, IMO. People working with large volumes are very likely to be working with fewer datasets than people working on medical analyses, and more likely to use the software interactively doing bunch of one of things that will require them to save repeatedly derivative datasets.</p>
<p>I say +1 for the pigz implementation. Or some indication of progress of saving/compression process. Otherwise Slicer simply looks stalled.</p>

---

## Post #9 by @muratmaga (2018-10-22 22:10 UTC)

<p>Another suggestion I have is to make compress  visible field visible next to the format in the default save dialog box (as oppose to requiring user to click on options to expand the options). That can be good compromise.</p>

---

## Post #10 by @muratmaga (2018-10-22 22:14 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I am not finding a compress example. What would be option to specify for compress?</p>

---

## Post #11 by @pieper (2018-10-22 22:38 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="4488" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Another suggestion I have is to make compress visible field visible next to the format in the default save dialog box (as oppose to requiring user to click on options to expand the options). That can be good compromise.</p>
</blockquote>
</aside>
<p>Yes, if we think that’s a commonly used option it could make a lot of sense to make it visible by default.</p>

---

## Post #12 by @lassoan (2018-10-22 22:47 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="4488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I am not finding a compress example. What would be option to specify for compress?</p>
</blockquote>
</aside>
<p>You can enable/disable compression using storage node’s <a href="http://apidocs.slicer.org/master/classvtkMRMLStorageNode.html#a279187e9687b417aa391de0078698e33">SetUseCompression</a> method.</p>

---

## Post #13 by @muratmaga (2018-10-23 17:18 UTC)

<p>Thank you. Based on the example, this works:</p>
<p><span class="hashtag">#set</span> the default 3D model format to PLY (instead of VTK)<br>
defaultModelStorageNode = slicer.vtkMRMLModelStorageNode()<br>
defaultModelStorageNode.SetDefaultWriteFileExtension(‘ply’)<br>
<span class="hashtag">#to</span> turn off compression for the models<br>
defaultModelStorageNode.SetUseCompression(0)<br>
slicer.mrmlScene.AddDefaultNode(defaultModelStorageNode)</p>
<p>But I couldn’t figure out how to use the provided <strong><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_file_type_for_saving_for_all_volumes_.28with_already_existing_storage_nodes.29" rel="nofollow noopener">Change file type for saving for all volumes (with already existing storage nodes</a>)</strong> example to work with fresh scenes with no volume loaded.</p>
<p>defaultVolumeNode = slicer.vtkMRMLScalarVolumeNode()<br>
defaultVolumeNode.SetDefaultWriteFileExtension(‘mha’)</p>
<p>fails with AttributeError: ‘vtkCommonCorePython.vtkMRMLScalarVolumeNode’ object has no attribute ‘SetDefaultWriteFileExtension’</p>

---

## Post #14 by @lassoan (2018-10-23 17:28 UTC)

<p>You need to change the default volume storage node (not the default volume node).</p>

---

## Post #15 by @muratmaga (2018-10-23 17:58 UTC)

<p>Thanks, but looks like I need more guidance…</p>
<p>defaultStorageNode = slicer.vtkMRMLStorageNode()</p>
<p>fails with TypeError: this is an abstract class and cannot be instantiated</p>
<p>and I can’t locate a vtkMRMLVolumeStorageNode() (or rather how/where to find it).</p>

---

## Post #16 by @pieper (2018-10-26 14:51 UTC)

<p>Here’s an example:</p>
<pre><code class="lang-auto">#set the default volume storage to not compress by default
defaultVolumeStorageNode = slicer.vtkMRMLSegmentationStorageNode()
defaultVolumeStorageNode.SetUseCompression(0)
slicer.mrmlScene.AddDefaultNode(defaultVolumeStorageNode)
logging.info("Segmentation nodes will be stored uncompressed 
</code></pre>
<p>This is also in the<a href="https://www.slicer.org/w/index.php?title=Documentation%2FNightly%2FScriptRepository&amp;type=revision&amp;diff=60488&amp;oldid=60480">Script Repository now.</a></p>

---

## Post #17 by @ihnorton (2018-10-29 13:43 UTC)

<p>This came up in another thread recently:</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="3785">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/can-slicer-load-save-to-archives-instead-of-folders-on-mac-windows/3785/4">Can Slicer load/save to archives instead of folders, on Mac/Windows?</a></div>
<blockquote>
<p>Also note that volumes get compressed on save by default and for large volumes that can be big. Then the zip (mrb) process re-runs compression of those which is also wasteful. If performance is a big issue for you it’s possible to bypass that.</p>
</blockquote>
</aside>
<p>We could potentially get a big performance boost at minimal file size cost by changing the default gz compression level to 1. In some small-scale tests I did a few months ago, there was a major time cost between high and low settings, for only a tiny compression improvement (e.g. 90-&gt; 26 MB at level 9 in 34s, vs 90-&gt;27 MB at level 1 in &lt;1s). This was only a small test on a few brain MR datasets, but it seems reasonable.</p>

---

## Post #18 by @lassoan (2018-10-29 14:32 UTC)

<p>Using a low compression level would make a lot of sense, as one of the main reasons I would keep compression enabled is to deflate blank voxels around images that have a non-rectangular shape.</p>
<p>Is there an API to change compression level in ITK IO classes?</p>

---

## Post #19 by @ihnorton (2018-10-29 15:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="4488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is there an API to change compression level in ITK IO classes?</p>
</blockquote>
</aside>
<p>Looks like only for a few specific formats (MINC, PNG). For NRRD we can set it in teem directly.</p>

---

## Post #20 by @pieper (2018-10-31 20:36 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> tomorrow’s nightly build will have this commit which changes the default nrrd compression to ‘low’ so it should be faster and still pretty good compression.  Let us know how it works in your use cases.</p>
<p><a href="https://github.com/Slicer/Slicer/commit/d87fdfd3eeca502c97cf611c92e443571e569292" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/commit/d87fdfd3eeca502c97cf611c92e443571e569292</a></p>

---

## Post #21 by @muratmaga (2018-11-01 17:26 UTC)

<p>downloading right now!</p>

---

## Post #22 by @muratmaga (2018-11-01 18:13 UTC)

<p>So, I don’t need to do anything to enable this right? I am seeing about 10% gain over the behavior in 4.8.1 for a dataset about 1.8GB. (took 40 seconds on 4.8.1 to save, 36 second wtth todays nightly). Perhaps gains are more for larger dataset. I will try with a larger one.</p>
<p>Also, there is problem with file renaming at the save dialog box. Whatever I type, it reverts to the original file name when I click save.</p>

---

## Post #23 by @pieper (2018-11-01 18:28 UTC)

<p>Thanks for testing <a class="mention" href="/u/muratmaga">@muratmaga</a> - what’s the original size of the data and maybe <a class="mention" href="/u/ihnorton">@ihnorton</a> can comment if that’s in line with his expectations.</p>
<p>Regarding the save dialog it works for me here on my local build (mac).  I can change the name of the file in the save dialog and the file is saved under that name.  But the node name is slicer is unchanged.  If I change the name in slicer then the suggested file name is updated next time I go into the save dialog.</p>

---

## Post #24 by @muratmaga (2018-11-01 18:39 UTC)

<p>This is what I see when I hit save:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82dc026015cc29fa7f54152c56165dbc83ad6b4c.png" data-download-href="/uploads/short-url/iFDrcZz6JE0yXbCpcVQRYCprGBS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82dc026015cc29fa7f54152c56165dbc83ad6b4c_2_690x315.png" alt="image" data-base62-sha1="iFDrcZz6JE0yXbCpcVQRYCprGBS" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82dc026015cc29fa7f54152c56165dbc83ad6b4c_2_690x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82dc026015cc29fa7f54152c56165dbc83ad6b4c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82dc026015cc29fa7f54152c56165dbc83ad6b4c.png 2x" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">900×412 67.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I click the checkbox and type and alternate name (I don’t want to overwrite).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/491f64450432be965fc77910c84d1c5c28fff895.png" data-download-href="/uploads/short-url/aqS6VnWc3JbADvqO91nmlIcIelD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/491f64450432be965fc77910c84d1c5c28fff895_2_690x312.png" alt="image" data-base62-sha1="aqS6VnWc3JbADvqO91nmlIcIelD" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/491f64450432be965fc77910c84d1c5c28fff895_2_690x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/491f64450432be965fc77910c84d1c5c28fff895.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/491f64450432be965fc77910c84d1c5c28fff895.png 2x" data-dominant-color="E7E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">919×416 65.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The moment I click save, this appears, and note that name has reverted<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d8e4f7655bb90ba1abab9bcc7e5611f283c5422.png" data-download-href="/uploads/short-url/8My1vuAUtFK56hsZQLJqKpW6HaW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d8e4f7655bb90ba1abab9bcc7e5611f283c5422_2_690x262.png" alt="image" data-base62-sha1="8My1vuAUtFK56hsZQLJqKpW6HaW" width="690" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d8e4f7655bb90ba1abab9bcc7e5611f283c5422_2_690x262.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d8e4f7655bb90ba1abab9bcc7e5611f283c5422_2_1035x393.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d8e4f7655bb90ba1abab9bcc7e5611f283c5422.png 2x" data-dominant-color="E6E6E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×398 83.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In fact name gets reverted to the original the moment I unfocus from the text field.</p>

---

## Post #25 by @pieper (2018-11-01 18:52 UTC)

<p>Ah - I think I see - here you are changing the extension to ‘.save’ and so it changes back.  What if you change it to ‘testing.nrrd’ ?</p>

---

## Post #26 by @muratmaga (2018-11-01 19:23 UTC)

<p>Yep, it doesn’t do if I don’t use a ‘.’ to separate words.<br>
But 4.8.1 happily accepted multiple '.'s in a file name, and appended its proper extension.<br>
Is this change intentional?</p>

---

## Post #27 by @pieper (2018-11-01 19:41 UTC)

<p>I don’t think it’s intentional, but it may have be related to the use of compound names like file.seg.nrrd for segmentations.  <a class="mention" href="/u/lassoan">@lassoan</a> any comments?</p>
<p>But I find it I type something like testing.save.nrrd it works as expected so if there’s a reason it needs to be like this the workaround doesn’t seem too bad (granted it’s another thing to learn so it’s not ideal).</p>

---

## Post #28 by @jamesobutler (2018-11-01 20:30 UTC)

<p>Another user recently had problems (see <a href="https://discourse.slicer.org/t/save-scene-with-written-name/4469">Save scene with written name</a>) regarding the file name being reverted without their knowledge.  The name isn’t reverted until the file name field is no longer being actively edited. It can be confusing when going from actively editing to pressing the save button.  If the file doesn’t already exist, it will use the reverted name which the user won’t know and the dialog immediately closes.  At least here <a class="mention" href="/u/muratmaga">@muratmaga</a> was able to notice that it wasn’t using the file name “testing.save” because an “already exists” warning appeared for the reverted file name.</p>

---

## Post #29 by @muratmaga (2018-11-01 20:39 UTC)

<p>I agree this can potentially frustrate a lot of new people. The change is too quick to notice if you hit save directly, and it there is no older version it will get written with a different file name than you intended.</p>

---

## Post #30 by @lassoan (2018-11-01 20:57 UTC)

<p>Name of the column is “file name” because it actually contains the file name, including extension. You cannot enter a filename with an invalid extension, such as <em>volume.abc</em> or <em>volume.nrrd.abc</em>. I understand that you would expect to edit the file base name there. Maybe adding a “show extension” checkbox would help (that would switch between showing the file base name and complete file name)?</p>
<p>I don’t like the current behavior of resetting file name based on node name. Unfortunately, if we don’t do it then it may lead to other problems: you may not be able to find your data easily, may mix up data sets because you only renamed the node in the scene but not the filename. I don’t know if there is an easy solution to this.</p>

---

## Post #31 by @muratmaga (2018-11-01 21:02 UTC)

<p>The use case is someone importing a new stack, and then saving it as an nrrd, where they may want to rename the imported dataset as more appropriate for their workflow. If you are not going to let them do this at the save time, then I think actually it will be better to make the save as filename box not editable at all, and force them to make the change at the node level using data or subject hierarchy. As it is, it is confusing…</p>

---

## Post #32 by @lassoan (2018-11-01 21:05 UTC)

<p>You may be right. Currently, Save dialog in Slicer serves two purposes: Save and Export. It could help if these two functions would be more clearly separated (allow saving with a single click, without asking anything; use the current Save dialog for export only).</p>

---

## Post #33 by @jamesobutler (2018-11-01 21:41 UTC)

<p>At least in Windows, the native file dialog has a “File name” entry, but it refers to the basename and “Save as type” is for defining the extension.  I personally find it unusual to have to type the extension in a “File name” cell.  It seems redundant when “File format” is defined next to it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9133841d0e826b532432fee8dadb56cbf7e4a31.png" data-download-href="/uploads/short-url/uYkMVLtBBha4TqKbbQb3C3oVoPv.png?dl=1" title="save_dialog" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9133841d0e826b532432fee8dadb56cbf7e4a31.png" alt="save_dialog" data-base62-sha1="uYkMVLtBBha4TqKbbQb3C3oVoPv" width="690" height="84" data-dominant-color="C5DDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">save_dialog</span><span class="informations">936×114 2.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #34 by @lassoan (2018-11-02 00:05 UTC)

<p>In general, file extensions are shown in native file dialogs:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55508b59c388890be3ae98e4fbfdb1a4c9ee9056.png" data-download-href="/uploads/short-url/caJ9khrFYzsOJCgml0TNmx6QXwa.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55508b59c388890be3ae98e4fbfdb1a4c9ee9056_2_674x500.png" alt="image" data-base62-sha1="caJ9khrFYzsOJCgml0TNmx6QXwa" width="674" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55508b59c388890be3ae98e4fbfdb1a4c9ee9056_2_674x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55508b59c388890be3ae98e4fbfdb1a4c9ee9056_2_1011x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55508b59c388890be3ae98e4fbfdb1a4c9ee9056.png 2x" data-dominant-color="F1F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1133×840 77.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You have an option in Windows explorer to hide them (if you disable “File extensions” option), but even then they can only be hidden for files that have an extension that is associated with an application.</p>

---

## Post #35 by @jamesobutler (2018-11-02 01:45 UTC)

<p>From what I’ve read and experienced, file extensions are hidden by default in native file dialogs and users can change a setting to then show them. In recent Windows and Mac the setting is written something like “Show extensions” with a checkbox, though at least in Windows 7 in an advanced area it is referred as the opposite as “Hide extensions” and that is checked.</p>
<ul>
<li>For Windows, extensions are hidden in Explorer by default (see <a href="https://www.howtogeek.com/205086/beginner-how-to-make-windows-show-file-extensions/" rel="nofollow noopener">Article</a> telling users how to show them.)</li>
<li>For macOS, extensions are hidden in Finder by default (see <a href="https://www.mactrast.com/2018/01/show-file-extensions-macos-finder/" rel="nofollow noopener">Article</a> telling users how to show them.)</li>
</ul>
<p>I think it would be best for Slicer to expect that users are familiar using the defaults of the major OS platforms. I would be in favor of Slicer’s save dialog not requiring the extension to be specified by default and letting the autoselection of File Format to be used as the extension. The Slicer save dialog could have a user setting to then show extensions in the file name and that would reimplement the option that is present for native file dialogs on the major OS platforms.</p>

---

## Post #36 by @lassoan (2018-11-02 02:02 UTC)

<p>Native dialogs only hide <em>known</em> file extensions, while most medical image computing file formats that Slicer uses (nrrd, nii, mha, fcsv, …) are not known. So, they so show up regardless you check/uncheck “File extensions” option.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9b8c50fb5056f104307727d362d3c952ed52329.png" data-download-href="/uploads/short-url/xlB7jGd60OIPmpetPkelpqdAirD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9b8c50fb5056f104307727d362d3c952ed52329_2_690x411.png" alt="image" data-base62-sha1="xlB7jGd60OIPmpetPkelpqdAirD" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9b8c50fb5056f104307727d362d3c952ed52329_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9b8c50fb5056f104307727d362d3c952ed52329_2_1035x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9b8c50fb5056f104307727d362d3c952ed52329_2_1380x822.png 2x" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1439×858 96.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regardless, I agree that having a “File extensions” checkbox (similarly to Explorer) would be useful as it could make things look more familiar for some users.</p>

---

## Post #37 by @jamesobutler (2018-11-02 02:44 UTC)

<p>Ok, I understand now. You are correct the typical file types used won’t be known extensions. Is there a reason for the redundancy of showing the extension in the file name and having it shown in the column directly to the right of it? When the file format is changed it automatically changes the extension in the file name cell, but if you change the extension in the file name it doesn’t choose the correct file format even if it is a valid file format. Reading left to right I change the file name first and then choose the file format second.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64b97b9a3705e786625cb9036eea5d5cdab581b5.png" alt="extension_duplication" data-base62-sha1="en38OseIvtjr91UjzLwuJ75FTyR" width="336" height="165"></p>

---

## Post #38 by @ihnorton (2018-11-09 15:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="23" data-topic="4488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>maybe <a class="mention" href="/u/ihnorton">@ihnorton</a> can comment if that’s in line with his expectations.</p>
</blockquote>
</aside>
<p>With release build, it’s similar to the numbers in the PR. I think the vtk&lt;-&gt;teem nrrdio&lt;-&gt;zlib interface might be suboptimal, because I get much better numbers with pure python.</p>
<p>level 0: 9s (2.1 GB)<br>
level 1 (default): 22s (529 MB)<br>
level 9: 41s (519 MB)</p>

---
