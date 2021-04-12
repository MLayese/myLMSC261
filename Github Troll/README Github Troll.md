# ReadMe File

### Tesseract OCR

I found this Text Recognition Engine that looked pretty cool. Here's the link:

[Tesseract OCR](https://github.com/tesseract-ocr/tesseract/tree/master)

### Changes

Tesseract has been around for awhile (the 1980s if I'm not mistaken) and open sourced since 2005. The last version update was 4.1.1 in the winter of 2019. The majority of changes I saw this past week had less to do with actual devlopement of the engine but rather tweaks to make it run better.

#### Fuzzing 
[Fuzzer](https://github.com/tesseract-ocr/tesseract/commit/f2c6378b5a4051bbaede6809798c216dfd3b83d1) 

This change fixed a fuzzer within the code. Well more specifically, it fixed some lines on a wrapper the fuzzer was connected to (I think). I thought this was ironic because isn't a wrapper used to make a complicated/ poorly designed interface more accesible? Like...an API within an API kinda'. 

#### ReadME for Unit Testing
[ReadME](https://github.com/tesseract-ocr/tesseract/blob/master/unittest/README.md)

There were some typos in the ReadMe for a portion of the Tesseract. Not in the actual code but just in the description. I'm mainly putting this one in here becuase it occurred as I was scrolling through the repositrory for the first time. 

#### Modernize-use-Override
[Override](https://github.com/tesseract-ocr/tesseract/commit/cb80eb69635214780090af35baa4c5a7c81a4f3e) 

For this one they just added the 'override' keyword. I don't really use C++ 11 too much but after a quick google search I realized that this helped the workflow of the complier significantly because you can ignore a meaningless base class implentation change.

#### Communication

After looking at the changes I didn't see a lot of comments on them from the developers (in the Github commemt section I mean. From what I saw, they mainly communicated via the summaries in their changes or using commentys within the code.
