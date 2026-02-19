---
topic_id: 19734
title: "Build Error On Macosx When Install Simpleitk Modulenotfounde"
date: 2021-09-18
url: https://discourse.slicer.org/t/19734
---

# Build error on MacOSX, When install simpleITK, ModuleNotFoundError: No module named 'skbuild' occur

**Topic ID**: 19734
**Date**: 2021-09-18
**URL**: https://discourse.slicer.org/t/build-error-on-macosx-when-install-simpleitk-modulenotfounderror-no-module-named-skbuild-occur/19734

---

## Post #1 by @RuoyanMeng (2021-09-18 00:10 UTC)

<p>MacOS 11.5.2,<br>
Qt 5.15.2,<br>
Xcode 12.5.1,<br>
cmake 3.20.5</p>
<p>SimpleITK: install step failed with exit code ‘1’.</p>
<pre><code class="lang-auto">Best match: SimpleITK 2.1.0
Processing SimpleITK-2.1.0.tar.gz
Writing /tmp/easy_install-e5igwpuy/SimpleITK-2.1.0/setup.cfg
Running SimpleITK-2.1.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-e5igwpuy/SimpleITK-2.1.0/egg-dist-tmp-uwx0nksb

zip_safe flag not set; analyzing archive contents...
SimpleITK.__pycache__._SimpleITK.cpython-36: module references __file__
Traceback (most recent call last):
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 152, in save_modules
    yield saved
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 193, in setup_context
    yield
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 254, in run_setup
    _execfile(setup_script, ns)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 43, in _execfile
    exec(code, globals, locals)
  File "/tmp/easy_install-e5igwpuy/SimpleITK-2.1.0/setup.py", line 3, in &lt;module&gt;
    
ModuleNotFoundError: No module named 'skbuild'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "setup.py", line 85, in &lt;module&gt;
    cmdclass={'build_ext':build_ext}
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/__init__.py", line 153, in setup
    return distutils.core.setup(**attrs)
  File "/opt/s/python-install/lib/python3.6/distutils/core.py", line 148, in setup
    dist.run_commands()
  File "/opt/s/python-install/lib/python3.6/distutils/dist.py", line 955, in run_commands
    self.run_command(cmd)
  File "/opt/s/python-install/lib/python3.6/distutils/dist.py", line 974, in run_command
    cmd_obj.run()
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/install.py", line 67, in run
    self.do_egg_install()
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/install.py", line 117, in do_egg_install
    cmd.run(show_deprecation=False)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/easy_install.py", line 408, in run
    self.easy_install(spec, not self.no_deps)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/easy_install.py", line 650, in easy_install
    return self.install_item(None, spec, tmpdir, deps, True)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/easy_install.py", line 697, in install_item
    self.process_distribution(spec, dist, deps)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/easy_install.py", line 745, in process_distribution
    [requirement], self.local_index, self.easy_install
  File "/opt/s/python-install/lib/python3.6/site-packages/pkg_resources/__init__.py", line 768, in resolve
    replace_conflicting=replace_conflicting
  File "/opt/s/python-install/lib/python3.6/site-packages/pkg_resources/__init__.py", line 1051, in best_match
    return self.obtain(req, installer)
  File "/opt/s/python-install/lib/python3.6/site-packages/pkg_resources/__init__.py", line 1063, in obtain
    return installer(requirement)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/easy_install.py", line 669, in easy_install
    return self.install_item(spec, dist.location, tmpdir, deps)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/easy_install.py", line 695, in install_item
    dists = self.install_eggs(spec, download, tmpdir)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/easy_install.py", line 890, in install_eggs
    return self.build_and_install(setup_script, setup_base)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/easy_install.py", line 1162, in build_and_install
    self.run_setup(setup_script, setup_base, args)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/command/easy_install.py", line 1146, in run_setup
    run_setup(setup_script, args)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 257, in run_setup
    raise
  File "/opt/s/python-install/lib/python3.6/contextlib.py", line 99, in __exit__
    self.gen.throw(type, value, traceback)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 193, in setup_context
    yield
  File "/opt/s/python-install/lib/python3.6/contextlib.py", line 99, in __exit__
    self.gen.throw(type, value, traceback)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 164, in save_modules
    saved_exc.resume()
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 139, in resume
    raise exc.with_traceback(self._tb)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 152, in save_modules
    yield saved
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 193, in setup_context
    yield
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 254, in run_setup
    _execfile(setup_script, ns)
  File "/opt/s/python-install/lib/python3.6/site-packages/setuptools/sandbox.py", line 43, in _execfile
    exec(code, globals, locals)
  File "/tmp/easy_install-e5igwpuy/SimpleITK-2.1.0/setup.py", line 3, in &lt;module&gt;
    
ModuleNotFoundError: No module named 'skbuild'
CMake Error at 
  ../Slicer/CMake/ExternalProjectForNonCMakeProject.cmake:104 (message):
  SimpleITK: install step failed with exit code '1'.

  Outputs also captured in /opt/s/SimpleITK_install_step_output.txt and
  /opt/s/SimpleITK_install_step_error.txt.

  Setting env.  variable EP_EXECUTE_DISABLE_CAPTURE_OUTPUTS to 1 allows to
  disable file capture.

Call Stack (most recent call first):
  /opt/s/SimpleITK_install_step.cmake:3 (ExternalProject_Execute)
</code></pre>

---

## Post #2 by @lassoan (2021-09-18 00:28 UTC)

<p>It seems that you have run into this issue (SimeITK finds system Python instead of Slicer’s):</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5498">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5498" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5498" target="_blank" rel="noopener">Slicer build error with VTK9 in debug mode due to SimpleITK Python configuration problem</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-01" data-time="16:01:57" data-timezone="UTC">04:01PM - 01 Mar 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          domain:vtk9
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When building latest master version on Windows, using Visual Studio, in debug mo<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">de, then build fails with this error:

```
  -- Detecting CXX compiler ABI info - done
  -- Detecting CXX compile features
  -- Detecting CXX compile features - done
  CMake Error at C:/Program Files/CMake/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
    Could NOT find Python3 (missing: Python3_EXECUTABLE Interpreter) (found
    suitable version "3.7", minimum required is "3.6")
  Call Stack (most recent call first):
    C:/Program Files/CMake/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:393 (_FPHSA_FAILURE_MESSAGE)
    C:/D/S4D/VTK-build/lib/cmake/vtk-9.0/patches/3.18/FindPython/Support.cmake:2578 (find_package_handle_standard_args)
    C:/D/S4D/VTK-build/lib/cmake/vtk-9.0/patches/3.18/FindPython3.cmake:348 (include)
    C:/D/S4D/VTK-build/lib/cmake/vtk-9.0/VTK-vtk-module-find-packages.cmake:303 (find_package)
    C:/D/S4D/VTK-build/lib/cmake/vtk-9.0/vtk-config.cmake:138 (include)
    C:/D/S4D/VTK-build/vtk-config.cmake:1 (include)
    C:/D/S4D/ITK-build/lib/cmake/ITK-5.1/Modules/ITKVtkGlue.cmake:30 (find_package)
    C:/D/S4D/ITK/CMake/ITKModuleAPI.cmake:76 (include)
    C:/D/S4D/ITK/CMake/ITKModuleAPI.cmake:31 (itk_module_load)
    C:/D/S4D/ITK/CMake/ITKModuleAPI.cmake:129 (_itk_module_config_recurse)
    C:/D/S4D/ITK-build/ITKConfig.cmake:77 (itk_module_config)
    SuperBuild.cmake:386 (find_package)
    CMakeLists.txt:38 (include)


  -- Configuring incomplete, errors occurred!
  See also "C:/D/S4D/SimpleITK-build/CMakeFiles/CMakeOutput.log".
  See also "C:/D/S4D/SimpleITK-build/CMakeFiles/CMakeError.log".
C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(238
,5): error MSB8066: Custom build for 'C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-mkdir.rule;C:\D\S4
D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-download.rule;C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde629
1e1\SimpleITK-update.rule;C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-patch.rule;C:\D\S4D\CMakeFiles
\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-configure.rule;C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleI
TK-build.rule;C:\D\S4D\CMakeFiles\76a3bb6e84cfb300f8ba64bbde6291e1\SimpleITK-install.rule;C:\D\S4D\CMakeFiles\55773c0e5
810be009a8f38bd18c05739\SimpleITK-complete.rule;C:\D\S4D\CMakeFiles\f5993a3ec64cf58c5707908b20f354e5\SimpleITK.rule;C:\
D\S4\CMakeLists.txt' exited with code 1. [C:\D\S4D\SimpleITK.vcxproj]
```

I don't know if it is related, but SimpleITK CMake cache (c:\D\S4D\SimpleITK-build\CMakeCache.txt) picks up pieces of anaconda, which is strange because my environment variables are clean (there is absolutely no mention of anaconda or python in any of the variables):

```
//Path to a program.
_Python3_CONFIG:INTERNAL=_Python3_CONFIG-NOTFOUND
_Python3_DEVELOPMENT_EMBED_SIGNATURE:INTERNAL=0993e8f7af6d2f88f03f3f71fd289925
_Python3_DEVELOPMENT_MODULE_SIGNATURE:INTERNAL=0993e8f7af6d2f88f03f3f71fd289925
//Path to a program.
_Python3_EXECUTABLE:INTERNAL=_Python3_EXECUTABLE-NOTFOUND
//Path to a file.
_Python3_INCLUDE_DIR:INTERNAL=C:/Users/andra/anaconda3/include
//Path to a library.
_Python3_LIBRARY_DEBUG:INTERNAL=_Python3_LIBRARY_DEBUG-NOTFOUND
//Path to a library.
_Python3_LIBRARY_RELEASE:INTERNAL=C:/Users/andra/anaconda3/libs/python37.lib
//Path to a library.
_Python3_RUNTIME_LIBRARY_RELEASE:INTERNAL=C:/Users/andra/anaconda3/python37.dll
//Result of TRY_COMPILE
project_compiles:INTERNAL=FALSE
```

You can find the full logs here: https://1drv.ms/u/s!Arm_AFxB9yqHxaN2aILYudYPjN5xdA?e=Fhpgcf</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please check in the issue tracker if there is an easy workaround.</p>

---

## Post #3 by @RuoyanMeng (2021-09-19 12:12 UTC)

<p>Hi, thank you for the information. I can see that I met the same problem that SimpleITK just find the wrong python path( which is my system path).</p>

---
