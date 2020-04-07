 funcprot(0)

function [] = convolution(img)
    g = 1/25. * ones(3, 3);
    conv_img = imfilter(img, g);
    imshow(conv_img);
endfunction

function [] = correlation(img, g1)
    i1 = img;
    i1 = rgb2gray(i1);
    g1 = rgb2gray(g1);
    i2 = imcomplement(i1);
    //imshow(i2);
    g2 = imcomplement(g1);
    //imshow(g2);
    i3 = im2double(i2);
    g3 = im2double(g2);
    i4 = imfilter(i3, g3);
    i5 = imnorm(i4);
    imshow(i5);
    loc =   i5 > 0.9;
    [rows, cols] = find(loc);
    imshow(img);
    sz = size(img);
    plot(cols, sz(1) - rows, 'r.');
endfunction

function []= main()
    cd "G:\Academics\Semester 7\Image Processing\Practicals\Practical 2\";
    /*img = imread('1conv.jpg');
    imshow(img);
    convolution(img);*/
    //i1 = imread('1.png');
    //g1 = imread('a.png');
    //acorrelation(i1, g1);
    i = imread('C:\Users\HIMANSHU\Desktop\1.png');
    i = rgb2gray(i);
    imshow(i);
endfunction

main
