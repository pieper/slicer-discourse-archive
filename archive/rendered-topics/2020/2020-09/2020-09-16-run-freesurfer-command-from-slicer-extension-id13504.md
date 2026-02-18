# Run Freesurfer command from Slicer extension

**Topic ID**: 13504
**Date**: 2020-09-16
**URL**: https://discourse.slicer.org/t/run-freesurfer-command-from-slicer-extension/13504

---

## Post #1 by @ezemikulan (2020-09-16 15:41 UTC)

<p>Hi, I’m developing an Extension in python to anonymize MRIs and I need to use some Freesurfer commands (mri_info, mris_convert and mri_watershed).</p>
<p>Is there a way to run Freesurfer commands from inside a Slicer Extension?</p>
<p>I’m using subprocess to perform the function calls but I get an error <strong>“non-zero exit status -6”</strong>. I tried the solution showed in <a href="https://discourse.slicer.org/t/subprocess-call-in-python-interpreter-results-in-memory-corruption/919/8" class="inline-onebox">Subprocess call in Python interpreter results in memory corruption</a>, adding the binaries directory to the path as done in Elastix, and also using <em>slicer.utils.startupEnvironment()</em> but I can’t make it work.</p>
<p>Here is an example code:</p>
<pre><code class="lang-auto">...
def getFsEnv(self):
    fsBinDir = '/path/to/binaries'
    fsEnv = os.environ.copy()
    fsEnv["PATH"] = fsBinDir + os.pathsep + fsEnv["PATH"] if fsEnv.get("PATH") else fsBinDir

...
fsEnv=self.getFsEnv()
subprocess.check_output(shlex.split('mri_info /path/to/file.mgz'), env=fsEnv)
</code></pre>
<p>I’ve also tried with <em>subprocess.Popen()</em>. In this case I think it starts and then stops:</p>
<pre><code class="lang-auto">logfile=open("filename", "w")
subprocess.Popen(shlex.split('mri_watershed -useSRAS -surf /path/ /file.mgz /path'), env=fsEnv, stdout=logfile)
logfile.close()
</code></pre>
<p>If i do like that, I see the beginning of the output on the logfile (only 2 lines) but the process doesn’t continue (i.e. the surfaces are not created and htop shows no cpu usage). If I use <em>subprocess.check_call()</em> I also get the -6 error.</p>
<p>Any help would be greatly appreaciated, thanks.</p>
<p>Operating system: OSX 10.15.6<br>
Slicer version: 4.10.2<br>
Expected behavior: Using subprocess to run Freesurfer commands<br>
Actual behavior: “non-zero exit status -6”</p>

---

## Post #2 by @lassoan (2020-09-17 01:03 UTC)

<p>Probably the freesurfer commands use some of the same dynamic libraries as Slicer and this causes a conflict. To resolve this, run the external process in the startup environment (instead of Slicer’s environment), as shown here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Run_process_in_default_environment">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Run_process_in_default_environment</a></p>

---

## Post #3 by @ezemikulan (2020-09-17 10:40 UTC)

<p>Thanks for your reply. I had tried using slicer.util.startupEnvironment() but it produces the same error.</p>
<p>For example:</p>
<pre><code class="lang-auto">subprocess.check_output(shlex.split('/Applications/freesurfer/bin/mri_info /filename.mgz'),
                        env=slicer.util.startupEnvironment())
</code></pre>
<p>I also tried adding the whole folder with binaries to the startupEnvironment:</p>
<pre><code class="lang-auto">slEnv=slicer.util.startupEnvironment()
slEnv['PATH']='/Applications/freesurfer/bin:' + slEnv['PATH']

subprocess.check_output(shlex.split('mri_info /filename.mgz'),
                        env=slEnv)
</code></pre>
<p>But I still get the same error. (The example code in the link you provided works without problems)</p>
<p>Thanks again,</p>

---

## Post #4 by @lassoan (2020-09-17 11:27 UTC)

<p>Please try with latest Slicer Preview Release.<br>
Also, try the same command from a regular Python3 interpreter to see if the syntax of the call is correct.</p>
<p>You may also use these convenience functions:</p>
<pre><code class="lang-python">proc = slicer.util.launchConsoleProcess(commandLine, useStartupEnvironment=True)
slicer.util.logProcessOutput(proc)
</code></pre>

---

## Post #5 by @ezemikulan (2020-09-17 13:37 UTC)

<p>I think I found the key to the problem. Your idea about dynamic libraries was correct.</p>
<p>If I add:</p>
<pre><code class="lang-auto">fsEnv['DYLD_LIBRARY_PATH']='/Applications/freesurfer/lib/gcc/lib'

</code></pre>
<p>I’m able to run freesurfer commands without problems. I’ll keep studying the problem and add any new insights and a more complete answer here for future reference. Thanks for all your help!</p>

---

## Post #6 by @ezemikulan (2021-04-02 09:41 UTC)

<p>I was able to make it work on both Mac and Linux, here’s what I did:</p>
<p>First I define a function to set up the environment:</p>
<pre><code>def getFsEnv(self):
    """Create an environment where executables are added to the path"""
    base_dir = os.path.split(slicer.modules.modulename.path)[0]
    fsBinDir = '%s/Resources/bin:/usr/lib:' % base_dir
    fsEnv = os.environ.copy()
    fsEnv["PATH"] = fsBinDir + os.pathsep + fsEnv["PATH"] if fsEnv.get("PATH") else fsBinDir
    fsEnv['DYLD_LIBRARY_PATH'] = '%s/Resources/lib/gcc/lib' % base_dir
    fsEnv['FREESURFER_HOME'] = '%s/Resources' % base_dir
    return fsEnv
</code></pre>
<p>Then at the point where I need to call freesurfer’s function I get the environment and run the command using it:</p>
<pre><code>import subprocess as sp
import shlex
fsEnv = self.getFsEnv()
command = 'mri_watershed -useSRAS -surf %s/%s %s %s/bems/ws' % (file_dir, base_name, f, file_dir)
p = sp.Popen(shlex.split(command), env=fsEnv, stdout=logfile, stderr=logfile)
p.wait()    
</code></pre>
<p>For this to work the freesurfer scripts and files required should be included in the right hierarchy or pointed to. For example on the code above I’m adding  <strong>‘%s/Resources/lib/gcc/lib’ % base_dir</strong> to <strong>‘DYLD_LIBRARY_PATH’</strong> and defining <strong>‘%s/Resources’ % base_dir</strong> as <strong>‘FREESURFER_HOME’</strong>.</p>
<p>The folder structure (including only the files relevant for this topic) in my case looks like this:</p>
<blockquote>
<p>.<br>
├── ModuleName.py<br>
├── ModuleName.pyc<br>
├── CMakeLists.txt<br>
├── Resources<br>
│   ├── bin<br>
│   │   ├── mri_info<br>
│   │   ├── mri_watershed<br>
│   │   └── mris_convert<br>
│   ├── lib<br>
│   │   ├── bem<br>
│   │   │   ├── ic0.tri<br>
│   │   │   ├── ic1.tri<br>
│   │   │   ├── ic2.tri<br>
│   │   │   ├── ic3.tri<br>
│   │   │   ├── ic4.tri<br>
│   │   │   ├── ic5.tri<br>
│   │   │   ├── ic6.tri<br>
│   │   │   ├── ic7.tri<br>
│   │   │   ├── inner_skull.dat<br>
│   │   │   ├── outer_skin.dat<br>
│   │   │   └── outer_skull.dat<br>
│   │   └── gcc<br>
│   │       └── lib<br>
│   │            ├── libgcc_s.1.dylib<br>
│   │            ├── libgfortran.3.dylib<br>
│   │             ├── libgomp.1.dylib<br>
│   │             ├── libquadmath.0.dylib<br>
│   │             └── libstdc++.6.dylib<br>
│   ├── license.txt</p>
</blockquote>
<p>Note that you will need to add a freesurfer <strong>license.txt</strong> for the scripts to work.</p>
<p>It is also possible to find a permissions problem on Mac computers when trying to run freesurfer commands. If this happens, for example on my case, I had to go to the Resources → bin, or Resources → lib → gcc folder and double click on the command that I was unable to run (e.g. mri_watershed) and then going to System Preferences → Security &amp; Privacy and allowing the execution from there (the window will show the last blocked command). If needed you will have to repeat the operation for each of the commands that are being blocked.</p>
<p>Hope this helps,</p>

---
