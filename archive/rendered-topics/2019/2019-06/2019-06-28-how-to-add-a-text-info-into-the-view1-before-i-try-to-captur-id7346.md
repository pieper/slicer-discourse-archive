---
topic_id: 7346
title: "How To Add A Text Info Into The View1 Before I Try To Captur"
date: 2019-06-28
url: https://discourse.slicer.org/t/7346
---

# How to add a text-info into the View1 before I try to capture a video

**Topic ID**: 7346
**Date**: 2019-06-28
**URL**: https://discourse.slicer.org/t/how-to-add-a-text-info-into-the-view1-before-i-try-to-capture-a-video/7346

---

## Post #1 by @aiden.zhu (2019-06-28 02:39 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.0-2019-06-23 r28335<br>
Expected behavior: text inside View1<br>
Actual behavior: no idea</p>
<p><span class="mention">@all</span> Hi all,<br>
I am a new in Slicer community. I would like to add some text info into View1 region, how may I do that?<br>
Thanks a lot</p>

---

## Post #2 by @hherhold (2019-06-28 08:02 UTC)

<p>I’m on my phone so I don’t have the options in front of me, but if the windows version of slicer uses ffmpeg to make videos, you can feed all sorts of options to it to do text overlays. In the screen capture module, there’s a box to add options to give to ffmpeg. Sorry this post is short on specifics, but hopefully it will point you in the right direction. Check out the ffmpeg documentation, and there are lots of examples of text overlays using ffmpeg if you search around.</p>

---

## Post #3 by @lassoan (2019-06-28 15:40 UTC)

<p>There is an example <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ScreenCapture" rel="nofollow noopener">here</a> of specifying extra ffmpeg options for Screen Capture module to display a logo in the corner of the video.</p>
<p>For adding titles, subtitles, and transitions we used Windows Movie Maker (free, now replaced by Microsoft Photos) nowadays we mostly switched to Camtasia (not free, but quite good and simple to learn).</p>

---

## Post #4 by @aiden.zhu (2019-06-28 17:31 UTC)

<p>Thanks a lot, I will try as you suggested.</p>
<p>Aiden</p>

---

## Post #5 by @aiden.zhu (2019-08-05 14:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hi Thanks a lot again for the hint.</p>
<p>I tried as you suggested using drawtext from ffmpeg. Sort of I did reach my aim right after the original ffmpeg running in Screen Capture (Thanks a lot one more time, LOL), I did one more time running of ffmpeg as to add drawtext to the *.mp4 file to make a new file. The code is as follows (excuse my non-professional coding way since I am still kind new to python.)</p>
<pre><code class="lang-python">    print('..........................before second ffmpeg running ....................................')
    #No idea how to decide arialbd.ttf location
    #use an alternate way: copy a *.ttf to the current working dir
    #that is, copy my arialbd.ttf to the outputDir
    ttf_dirname =outputDir + '\\arialbd.ttf'
    if not os.path.isfile(ttf_dirname):
        from shutil import copyfile
        src = os.path.dirname(ffmpegPath)+'\\arialbd.ttf'
        dst = ttf_dirname
        print('copying file =' , src )
        print('to here = ', dst)
        copyfile(src , dst )


    #run_ffmpeg2 = 'C:\\Anaconda3\\envs\\aiden_00\\Scripts\\ffmpeg.exe '+ ' -i '+  outputVideoFilePath \
    run_ffmpeg2 = ffmpegPath + ' -i '+  outputVideoFilePath \
      + ' -y -vf \"format=yuv420p, drawtext=fontfile=arialbd.ttf:text=\'DigiM 2019\':fontcolor=yellow@0.7:fontsize=28:x=15:y=20, format=yuv420p\" '\
      + ' -c:v libx264 -c:a copy -movflags faststart '\
      + outputVideoFilePath.replace('.mp4', '_digim.mp4')
    
    print(run_ffmpeg2)
    print('...................... before second ffmpeg running........................................')

    
    p2 = subprocess.Popen(run_ffmpeg2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=outputDir)
    stdout2, stderr2 = p2.communicate()
    if p2.returncode != 0:
      self.addLog("ffmpeg error output: " + stderr2.decode())
      raise ValueError("ffmpeg returned with error")
    else:
      self.addLog("Video export succeeded to file: "+ outputVideoFilePath.replace('.mp4', '_digim.mp4') )
      logging.debug("ffmpeg standard output: " + stdout2.decode())
      logging.debug("ffmpeg error output: " + stderr2.decode())

    try: 
      os.remove(ttf_dirname)
    except:
      pass
    print('Supposed to be done successfully!')
</code></pre>
<p>The big issue I encountered was how to set up the ttf file in drawtext between two ’ " ’ which always brought me trouble with escaping.<br>
I have not still figure out how to set up that drawtext format, especially with the ttf-file part. So alternately I copied a ttf to the current working directory. It works fine but not professional. So please, if anybody, know how to figure it out, I will be well grateful and appreciate the help and effort.</p>
<p>Thanks a lot.</p>

---

## Post #6 by @lassoan (2019-08-05 16:00 UTC)

<p>There is no need to modify any source code. You can add any extra options to “Video extra options” field in advanced section. You can hardcode full path of .ttf file there (enclosed in double-quotes if the path contains space).</p>

---

## Post #7 by @aiden.zhu (2019-08-12 14:16 UTC)

<p>This topic will be closed right after this new updated from my exploration experience:</p>
<p>the other way to show text in the view is to use ConerAnnotation:<br>
view=slicer.app.layoutManager().threeDWidget(0).threeDView()</p>
<h1>Set text to “Something”</h1>
<p>view.cornerAnnotation().SetText(vtk.vtkCornerAnnotation.UpperRight,“Something”)</p>
<h1>Set color to red</h1>
<p>view.cornerAnnotation().GetTextProperty().SetColor(1,0,0)</p>
<h1>Update the view</h1>
<p>view.forceRender()</p>

---

## Post #8 by @lassoan (2019-08-12 15:05 UTC)

<p>Good idea!</p>
<p>You can also add a logo as described on the screen capture module documentation page.</p>

---
