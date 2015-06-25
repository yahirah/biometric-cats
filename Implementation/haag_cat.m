%%
rootfile = 'E:\Projekty\Studia\02238\';
positiveFolder = fullfile(rootfile,'test-images-cats');
negativeFolder = fullfile(rootfile,'test-images-scene','f','forest','broadleaf');
%% Create positive array

img = (imread('lost.jpg'));

faceDetector = vision.CascadeObjectDetector;
bboxes = step(faceDetector, img);
figure, imshow(img), title('Detected faces');hold on
for i=1:size(bboxes,1)
    rectangle('Position',bboxes(i,:),'LineWidth',2,'EdgeColor','y');
end
