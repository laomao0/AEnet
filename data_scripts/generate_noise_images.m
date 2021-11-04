function generate_noise_images()
%% matlab code to genetate gaussion noise for our dataset

% set = 'train'
set = 'test'
imgDataPath = strcat('/DATA/wangshen_data/ShortLongDataset/Combined_Dataset/', set ,'_sharp/');
imgDataDir = dir(imgDataPath);  % travel all subdirs
imgDataSubDir = imgDataDir(3:end);  % clear implimt firs , 2c0094, c0041
numSubdir = length(imgDataSubDir);
fprintf('numSubdir:%i\n', numSubdir)


save_LR_folder = strcat('/DATA/wangshen_data/ShortLongDataset/Combined_Dataset/', set, '_noise');
if ~exist(save_LR_folder, 'dir')
    mkdir(save_LR_folder);
end


for vnumSubDir=1:numSubdir
    subDirPath = strcat(imgDataPath,imgDataSubDir(vnumSubDir).name,'/');
    disp(subDirPath)
    imgDataSubSubDir = dir(subDirPath);
    imgDataSubSubDir = imgDataSubSubDir(3:end);  % 00000, 00001, ...
    numSubSubDir = length(imgDataSubSubDir);
    
    save_LR_sub_folder = strcat(save_LR_folder,'/',imgDataSubDir(vnumSubDir).name);  % 2c0094, c0041
    disp(save_LR_sub_folder)
    if ~exist(save_LR_sub_folder, 'dir')
        mkdir(save_LR_sub_folder);
    end
    
    for vnumSubSubDir=1:numSubSubDir
        
        subsubDirPath = strcat(subDirPath, imgDataSubSubDir(vnumSubSubDir).name, '/', '*.png');
        filepaths = dir(subsubDirPath);
        
        save_LR_subsub_folder = strcat(save_LR_sub_folder,'/',imgDataSubSubDir(vnumSubSubDir).name);
        disp(save_LR_subsub_folder)
        if ~exist(save_LR_subsub_folder, 'dir')
            mkdir(save_LR_subsub_folder);
        end
        
        for i = 1 : length(filepaths)
            [~,imname,ext] = fileparts(filepaths(i).name);
            folder_path = strcat(subDirPath, imgDataSubSubDir(vnumSubSubDir).name);
            
  
            if isempty(imname)
                disp('Ignore . folder.');
            elseif strcmp(imname, '.')
                disp('Ignore .. folder.');
            else
                str_rlt = sprintf('%s.png\n', imname);
                fprintf(str_rlt);
                % read image
                im_path_in  = fullfile(folder_path, [imname, ext]);
                im_path_out = fullfile(save_LR_subsub_folder, [imname, '.png']); 

                if ~exist(im_path_out, 'file')
                    oriimg = imread(im_path_in);
                    img = imnoise(oriimg, 'gaussian', 0, 0.01); % mean=0 var=0.001
                    % LR
                    %img = imresize(img, 1/4, 'bicubic')
                    if exist('save_LR_subsub_folder', 'var')
                        imwrite(img, im_path_out);
                        %val_psnr = psnr(img, oriimg);
                        %fprintf('%f \n', val_psnr)
                    end
                else
                    continue
                end
                


            end
        end
    end
    


    
end
end
