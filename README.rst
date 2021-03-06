scikit-surgeryutils 
===============================

.. image:: https://github.com/UCL/scikit-surgeryutils /raw/master/weiss_logo.png
   :height: 128px
   :width: 128px
   :target: https://github.com/UCL/scikit-surgeryutils 
   :alt: Logo

|

.. image:: https://github.com/UCL/scikit-surgeryutils/workflows/.github/workflows/ci.yml/badge.svg
   :target: https://github.com/UCL/scikit-surgeryutils/actions
   :alt: GitHub Actions CI statuss

.. image:: https://coveralls.io/repos/github/UCL/scikit-surgeryutils/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/UCL/scikit-surgeryutils?branch=master
    :alt: Test coverage

.. image:: https://readthedocs.org/projects/scikit-surgeryutils /badge/?version=latest
    :target: http://scikit-surgeryutils .readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


scikit-surgeryutils is part of the `SNAPPY`_ software project, developed at the `Wellcome EPSRC Centre for Interventional and Surgical Sciences`_, part of `University College London (UCL)`_.

scikit-surgeryutils containing small demo apps and utilities.

.. features-start

Features
--------
* `Common overlay apps <https://scikit-surgeryutils.readthedocs.io/en/latest/module_ref.html#module-sksurgeryutils.common_overlay_apps>`_ - Examples of common uses of scikit-surgeryvtk's VTKOverlayWindow. Includes overlaying on a video feed, duplicating a feed.

Command Line Apps
-----------------
* sksurgeryvideolag.py - shows a millisecond timer and video image to crudely measure measure lag.
* sksurgerycharucotest.py - extracts charuco points and annotates video image with each id detected.
* sksurgeryrendermodelslikecamera.py - renders a VTK model, over background image, using OpenCV camera intrinsics.
* sksurgerymakecalibrationdots.py - Create a calibraiton dot pattern.
* sksurgeryreslice.py - DICOM reslice widget demo.
* sksurgerytextoverlay.py - VTK text overlay demo.
* sksurgerytransformpolydata.py - Read a surface mesh (.vtk,.vtp,.stl,.ply file), transform by 4x4 matrix and write as .vtk.

.. features-end

Installing
----------

You can pip install directly from the repository as follows:

::

    pip install git+https://github.com/UCL/scikit-surgeryutils


Developing
----------

Cloning
^^^^^^^

You can clone the repository using the following command:

::

    git clone https://github.com/UCL/scikit-surgeryutils


Running the tests
^^^^^^^^^^^^^^^^^

You can run the unit tests by installing and running tox:

::

    pip install tox
    tox

Encountering Problems?
^^^^^^^^^^^^^^^^^^^^^^
Please check list of `common issues`_.

Contributing
^^^^^^^^^^^^

Please see the `contributing guidelines`_.


Useful links
^^^^^^^^^^^^

* `Source code repository`_
* `Documentation`_


Licensing and copyright
-----------------------

Copyright 2018 University College London.
scikit-surgeryutils is released under the BSD-3 license. Please see the `license file`_ for details.


Acknowledgements
----------------

Supported by `Wellcome`_ and `EPSRC`_.


.. _`Wellcome EPSRC Centre for Interventional and Surgical Sciences`: http://www.ucl.ac.uk/weiss
.. _`source code repository`: https://github.com/UCL/scikit-surgeryutils
.. _`Documentation`: https://scikit-surgeryutils.readthedocs.io
.. _`SNAPPY`: https://weisslab.cs.ucl.ac.uk/WEISS/PlatformManagement/SNAPPY/wikis/home
.. _`University College London (UCL)`: http://www.ucl.ac.uk/
.. _`Wellcome`: https://wellcome.ac.uk/
.. _`EPSRC`: https://www.epsrc.ac.uk/
.. _`contributing guidelines`: https://github.com/UCL/scikit-surgeryutils/blob/master/CONTRIBUTING.rst
.. _`license file`: https://github.com/UCL/scikit-surgeryutils/blob/master/LICENSE
.. _`common issues`: https://weisslab.cs.ucl.ac.uk/WEISS/SoftwareRepositories/SNAPPY/scikit-surgery/wikis/Common-Issues
