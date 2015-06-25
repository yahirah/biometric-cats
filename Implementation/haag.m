clear all
vid = videoinput('winvideo', 1, 'YUY2_640x480'); % Giving the framesize
vid.ReturnedColorSpace = 'RGB'; % Mentioning RGB format
vid.TriggerRepeat = Inf; % Triggers the camera repeatedly
vid.FrameGrabInterval = 1; % Time between successive frames
start(vid); % Starts capturing video
detector = vision.CascadeObjectDetector(); % Create a detector using Viola-Jones
while true % Infinite loop to continuously detect the face
    img = flipdim(getdata(vid, 1), 2); % Flips the image horizontally
    imshow(img); hold on; % Displays image
    bbox = step(detector, img); % Creating bounding box using detector
    if ~ isempty(bbox)
        for i=1:size(bbox,1)
            rectangle('position', bbox(i, :), 'lineWidth', 2, 'edgeColor', 'y');
        end
    end % Draws a yellow rectangle around the detected face
    flushdata(vid);
    hold off;
end