# -*- coding: utf-8 -*-
import os
import sys
import cv2
import pytest
import mock
import numpy as np
import sksurgeryutils.common_overlay_apps as coa

def test_OverlayOnVideoFeedCropRecord_from_file(setup_qt, tmpdir):

    in_github_ci = os.environ.get('CI')

    if in_github_ci and sys.platform.startswith("linux"):
        pytest.skip("Test not working on Linux runner \
                    because of unknown issue.")

    input_file = 'tests/data/100x50_100_frames.avi'

    out_file = os.path.join(tmpdir, 'overlay_test.avi')

    overlay_app = coa.OverlayOnVideoFeedCropRecord(input_file, out_file)

    # Start app and get a frame from input, so that
    # the window is showing something, before we start
    # recording.
    overlay_app.start()
    overlay_app.update()
    overlay_app.on_record_start()

    for i in range(50):
        overlay_app.update()

    overlay_app.on_record_stop()
    overlay_app.stop()
    
    # Check that 50 frames were actually written to the output file
    output_video = cv2.VideoCapture(out_file)

    for i in range(50):
        ret, _ = output_video.read()
    assert ret

    # Trying to read 51st frame should return False
    ret, _ = output_video.read()
    assert not ret

    output_video.release()

def test_OverlayOnVideoFeedCropRecord_from_webcam(setup_qt):
    """
    Test will only run if there is a camera avilable.
    """

    # Try to open a camera. If one isn't available, the rest of test
    # will be skipped.
    source = 0
    cam = cv2.VideoCapture(source)
    if not cam.isOpened():
        pytest.skip("No camera available")
    
    cam.release()
    
    # Don't pass an output filename as a parameter, so that
    # the code to generate a filename from current date/time is executed.
    overlay_app = coa.OverlayOnVideoFeedCropRecord(0)

    # Start app and get a frame from input, so that
    # the window is showing something, before we start
    # recording.
    overlay_app.start()
    overlay_app.update()
    overlay_app.on_record_start()

    for i in range(50):
        overlay_app.update()

    overlay_app.on_record_stop()
    overlay_app.stop()

def test_OverlayBaseAppRaisesNotImplementedError(setup_qt):

    class ErrorApp(coa.OverlayBaseApp):

        def something(self):
            pass

    with pytest.raises(NotImplementedError):
        input_file = 'tests/data/100x50_100_frames.avi'

        overlay_app = ErrorApp(input_file)
        overlay_app.update()

roi = [(25, 25), (50, 50)]
@mock.patch('sksurgeryutils.common_overlay_apps.ImageCropper.crop')
def test_OverlayOnVideoFeedCropRecord_set_roi(mock_crop, setup_qt):
        mock_crop.return_value = roi
        
        input_file = 'tests/data/100x50_100_frames.avi'
        overlay_app = coa.OverlayOnVideoFeedCropRecord(input_file)
        overlay_app.update() # Get a frame so that we can crop it
        overlay_app.set_roi()
        overlay_app.update() # This should apply the roi to the next frame

        expected_shape = (roi[1][0] - roi[0][0], roi[1][1] - roi[0][1])
        assert overlay_app.vtk_overlay_window.input.shape[:2] == expected_shape

def test_DuplicateOverlayWindow(setup_qt):

    input_file = 'tests/data/100x50_100_frames.avi'
    overlay_app = coa.OverlayOnVideoFeed(input_file)

    duplicate = coa.DuplicateOverlayWindow()
    duplicate.set_source_window(overlay_app)
    
    overlay_app.update()
    duplicate.update()

    np.testing.assert_array_equal(overlay_app.img, duplicate.vtk_overlay_window.input)

def test_DuplicateOverlayWindowWithCrop(setup_qt):
    input_file = 'tests/data/100x50_100_frames.avi'
    overlay_app = coa.OverlayOnVideoFeedCropRecord(input_file)

    duplicate = coa.DuplicateOverlayWindow()
    duplicate.set_source_window(overlay_app)
    
    overlay_app.update()
    duplicate.update()

    np.testing.assert_array_equal(overlay_app.img, duplicate.vtk_overlay_window.input)


