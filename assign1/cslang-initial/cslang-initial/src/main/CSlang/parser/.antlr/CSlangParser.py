# Generated from e:/hocbaidcm/PPL/assignment/assign1/cslang-initial/cslang-initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,71,549,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,1,0,5,0,114,8,0,10,0,12,0,117,9,0,
        1,0,1,0,1,1,1,1,1,1,3,1,124,8,1,1,1,1,1,1,1,5,1,129,8,1,10,1,12,
        1,132,9,1,1,1,1,1,1,2,1,2,1,2,3,2,139,8,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,3,3,149,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,5,5,163,8,5,10,5,12,5,166,9,5,1,5,1,5,1,5,1,5,1,5,3,5,173,
        8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,187,8,7,
        1,8,1,8,3,8,191,8,8,1,8,1,8,1,9,1,9,1,9,3,9,198,8,9,1,10,1,10,1,
        10,3,10,203,8,10,1,11,1,11,1,11,1,11,3,11,209,8,11,1,12,1,12,1,12,
        1,12,3,12,215,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        3,12,226,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,3,15,
        237,8,15,1,15,1,15,1,15,1,15,3,15,243,8,15,1,16,1,16,1,16,1,16,1,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,
        19,1,20,1,20,1,20,3,20,266,8,20,1,20,1,20,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,22,1,22,3,22,279,8,22,1,22,1,22,1,22,1,22,1,22,1,
        23,1,23,1,23,1,23,1,24,1,24,5,24,292,8,24,10,24,12,24,295,9,24,1,
        24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,331,8,25,1,26,1,26,1,
        26,3,26,336,8,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,
        29,1,29,1,29,5,29,350,8,29,10,29,12,29,353,9,29,1,30,1,30,1,31,1,
        31,1,31,5,31,360,8,31,10,31,12,31,363,9,31,1,31,3,31,366,8,31,1,
        32,1,32,1,32,1,32,1,32,1,32,5,32,374,8,32,10,32,12,32,377,9,32,1,
        33,1,33,1,33,1,33,1,33,1,33,1,33,5,33,386,8,33,10,33,12,33,389,9,
        33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,5,34,398,8,34,10,34,12,34,
        401,9,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,5,35,410,8,35,10,35,
        12,35,413,9,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,5,36,422,8,36,
        10,36,12,36,425,9,36,1,37,1,37,1,37,1,37,3,37,431,8,37,1,38,1,38,
        1,38,3,38,436,8,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,5,39,
        446,8,39,10,39,12,39,449,9,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,
        1,40,1,40,1,40,1,40,1,40,1,40,5,40,464,8,40,10,40,12,40,467,9,40,
        1,41,1,41,3,41,471,8,41,1,41,1,41,1,41,3,41,476,8,41,1,41,1,41,1,
        41,1,41,1,41,1,41,3,41,484,8,41,1,42,1,42,1,42,1,42,1,42,1,42,1,
        42,3,42,493,8,42,1,43,1,43,1,43,1,43,1,43,1,43,3,43,501,8,43,1,44,
        1,44,3,44,505,8,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,49,
        1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,53,1,53,1,53,
        1,53,1,53,1,53,1,53,1,53,3,53,534,8,53,1,54,1,54,1,55,1,55,1,55,
        1,55,5,55,542,8,55,10,55,12,55,545,9,55,1,55,1,55,1,55,0,7,64,66,
        68,70,72,78,80,56,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,
        78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,0,8,2,0,
        62,62,64,64,1,0,36,37,1,0,38,41,1,0,46,49,1,0,44,45,1,0,34,35,2,
        0,18,21,64,64,1,0,16,17,558,0,115,1,0,0,0,2,120,1,0,0,0,4,138,1,
        0,0,0,6,140,1,0,0,0,8,152,1,0,0,0,10,172,1,0,0,0,12,174,1,0,0,0,
        14,186,1,0,0,0,16,190,1,0,0,0,18,194,1,0,0,0,20,199,1,0,0,0,22,204,
        1,0,0,0,24,225,1,0,0,0,26,227,1,0,0,0,28,230,1,0,0,0,30,234,1,0,
        0,0,32,244,1,0,0,0,34,252,1,0,0,0,36,255,1,0,0,0,38,259,1,0,0,0,
        40,265,1,0,0,0,42,269,1,0,0,0,44,278,1,0,0,0,46,285,1,0,0,0,48,289,
        1,0,0,0,50,330,1,0,0,0,52,335,1,0,0,0,54,337,1,0,0,0,56,342,1,0,
        0,0,58,346,1,0,0,0,60,354,1,0,0,0,62,365,1,0,0,0,64,367,1,0,0,0,
        66,378,1,0,0,0,68,390,1,0,0,0,70,402,1,0,0,0,72,414,1,0,0,0,74,430,
        1,0,0,0,76,435,1,0,0,0,78,437,1,0,0,0,80,450,1,0,0,0,82,483,1,0,
        0,0,84,492,1,0,0,0,86,500,1,0,0,0,88,504,1,0,0,0,90,506,1,0,0,0,
        92,508,1,0,0,0,94,510,1,0,0,0,96,512,1,0,0,0,98,514,1,0,0,0,100,
        516,1,0,0,0,102,518,1,0,0,0,104,520,1,0,0,0,106,533,1,0,0,0,108,
        535,1,0,0,0,110,537,1,0,0,0,112,114,3,2,1,0,113,112,1,0,0,0,114,
        117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,118,1,0,0,0,117,
        115,1,0,0,0,118,119,5,0,0,1,119,1,1,0,0,0,120,123,5,24,0,0,121,122,
        5,64,0,0,122,124,5,50,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,125,
        1,0,0,0,125,126,5,64,0,0,126,130,5,60,0,0,127,129,3,4,2,0,128,127,
        1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,133,
        1,0,0,0,132,130,1,0,0,0,133,134,5,61,0,0,134,3,1,0,0,0,135,139,3,
        6,3,0,136,139,3,8,4,0,137,139,3,16,8,0,138,135,1,0,0,0,138,136,1,
        0,0,0,138,137,1,0,0,0,139,5,1,0,0,0,140,141,5,32,0,0,141,142,7,0,
        0,0,142,143,5,57,0,0,143,144,3,10,5,0,144,145,5,56,0,0,145,148,5,
        55,0,0,146,149,3,102,51,0,147,149,5,29,0,0,148,146,1,0,0,0,148,147,
        1,0,0,0,149,150,1,0,0,0,150,151,3,48,24,0,151,7,1,0,0,0,152,153,
        5,32,0,0,153,154,5,25,0,0,154,155,5,57,0,0,155,156,3,10,5,0,156,
        157,5,56,0,0,157,158,3,48,24,0,158,9,1,0,0,0,159,164,3,12,6,0,160,
        161,5,53,0,0,161,163,3,12,6,0,162,160,1,0,0,0,163,166,1,0,0,0,164,
        162,1,0,0,0,164,165,1,0,0,0,165,173,1,0,0,0,166,164,1,0,0,0,167,
        168,3,58,29,0,168,169,5,55,0,0,169,170,3,102,51,0,170,173,1,0,0,
        0,171,173,1,0,0,0,172,159,1,0,0,0,172,167,1,0,0,0,172,171,1,0,0,
        0,173,11,1,0,0,0,174,175,3,60,30,0,175,176,5,55,0,0,176,177,3,102,
        51,0,177,13,1,0,0,0,178,187,3,16,8,0,179,187,3,26,13,0,180,187,3,
        30,15,0,181,187,3,32,16,0,182,187,3,38,19,0,183,187,3,34,17,0,184,
        187,3,36,18,0,185,187,3,40,20,0,186,178,1,0,0,0,186,179,1,0,0,0,
        186,180,1,0,0,0,186,181,1,0,0,0,186,182,1,0,0,0,186,183,1,0,0,0,
        186,184,1,0,0,0,186,185,1,0,0,0,187,15,1,0,0,0,188,191,3,18,9,0,
        189,191,3,20,10,0,190,188,1,0,0,0,190,189,1,0,0,0,191,192,1,0,0,
        0,192,193,5,54,0,0,193,17,1,0,0,0,194,197,5,30,0,0,195,198,3,22,
        11,0,196,198,3,24,12,0,197,195,1,0,0,0,197,196,1,0,0,0,198,19,1,
        0,0,0,199,202,5,26,0,0,200,203,3,22,11,0,201,203,3,24,12,0,202,200,
        1,0,0,0,202,201,1,0,0,0,203,21,1,0,0,0,204,205,3,58,29,0,205,208,
        5,55,0,0,206,209,3,102,51,0,207,209,3,104,52,0,208,206,1,0,0,0,208,
        207,1,0,0,0,209,23,1,0,0,0,210,211,3,60,30,0,211,214,5,55,0,0,212,
        215,3,102,51,0,213,215,3,104,52,0,214,212,1,0,0,0,214,213,1,0,0,
        0,215,216,1,0,0,0,216,217,5,42,0,0,217,218,3,64,32,0,218,226,1,0,
        0,0,219,220,3,60,30,0,220,221,5,53,0,0,221,222,3,24,12,0,222,223,
        5,53,0,0,223,224,3,64,32,0,224,226,1,0,0,0,225,210,1,0,0,0,225,219,
        1,0,0,0,226,25,1,0,0,0,227,228,3,28,14,0,228,229,5,54,0,0,229,27,
        1,0,0,0,230,231,3,52,26,0,231,232,5,43,0,0,232,233,3,64,32,0,233,
        29,1,0,0,0,234,236,5,13,0,0,235,237,3,48,24,0,236,235,1,0,0,0,236,
        237,1,0,0,0,237,238,1,0,0,0,238,239,3,64,32,0,239,242,3,48,24,0,
        240,241,5,14,0,0,241,243,3,48,24,0,242,240,1,0,0,0,242,243,1,0,0,
        0,243,31,1,0,0,0,244,245,5,15,0,0,245,246,3,28,14,0,246,247,5,54,
        0,0,247,248,3,64,32,0,248,249,5,54,0,0,249,250,3,28,14,0,250,251,
        3,48,24,0,251,33,1,0,0,0,252,253,5,12,0,0,253,254,5,54,0,0,254,35,
        1,0,0,0,255,256,5,22,0,0,256,257,3,64,32,0,257,258,5,54,0,0,258,
        37,1,0,0,0,259,260,5,11,0,0,260,261,5,54,0,0,261,39,1,0,0,0,262,
        266,3,42,21,0,263,266,3,44,22,0,264,266,3,46,23,0,265,262,1,0,0,
        0,265,263,1,0,0,0,265,264,1,0,0,0,266,267,1,0,0,0,267,268,5,54,0,
        0,268,41,1,0,0,0,269,270,3,64,32,0,270,271,5,52,0,0,271,272,5,64,
        0,0,272,273,5,57,0,0,273,274,3,62,31,0,274,275,5,56,0,0,275,43,1,
        0,0,0,276,277,5,64,0,0,277,279,5,52,0,0,278,276,1,0,0,0,278,279,
        1,0,0,0,279,280,1,0,0,0,280,281,5,62,0,0,281,282,5,57,0,0,282,283,
        3,62,31,0,283,284,5,56,0,0,284,45,1,0,0,0,285,286,3,64,32,0,286,
        287,5,52,0,0,287,288,3,50,25,0,288,47,1,0,0,0,289,293,5,60,0,0,290,
        292,3,14,7,0,291,290,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,
        294,1,0,0,0,294,296,1,0,0,0,295,293,1,0,0,0,296,297,5,61,0,0,297,
        49,1,0,0,0,298,299,5,1,0,0,299,300,5,57,0,0,300,331,5,56,0,0,301,
        302,5,2,0,0,302,303,5,57,0,0,303,304,3,62,31,0,304,305,5,56,0,0,
        305,331,1,0,0,0,306,307,5,3,0,0,307,308,5,57,0,0,308,331,5,56,0,
        0,309,310,5,4,0,0,310,311,5,57,0,0,311,312,3,62,31,0,312,313,5,56,
        0,0,313,331,1,0,0,0,314,315,5,5,0,0,315,316,5,57,0,0,316,331,5,56,
        0,0,317,318,5,6,0,0,318,319,5,57,0,0,319,320,3,62,31,0,320,321,5,
        56,0,0,321,331,1,0,0,0,322,323,5,7,0,0,323,324,5,57,0,0,324,331,
        5,56,0,0,325,326,5,8,0,0,326,327,5,57,0,0,327,328,3,62,31,0,328,
        329,5,56,0,0,329,331,1,0,0,0,330,298,1,0,0,0,330,301,1,0,0,0,330,
        306,1,0,0,0,330,309,1,0,0,0,330,314,1,0,0,0,330,317,1,0,0,0,330,
        322,1,0,0,0,330,325,1,0,0,0,331,51,1,0,0,0,332,336,3,60,30,0,333,
        336,3,54,27,0,334,336,3,56,28,0,335,332,1,0,0,0,335,333,1,0,0,0,
        335,334,1,0,0,0,336,53,1,0,0,0,337,338,3,64,32,0,338,339,5,58,0,
        0,339,340,3,64,32,0,340,341,5,59,0,0,341,55,1,0,0,0,342,343,3,60,
        30,0,343,344,5,52,0,0,344,345,3,64,32,0,345,57,1,0,0,0,346,351,3,
        60,30,0,347,348,5,53,0,0,348,350,3,60,30,0,349,347,1,0,0,0,350,353,
        1,0,0,0,351,349,1,0,0,0,351,352,1,0,0,0,352,59,1,0,0,0,353,351,1,
        0,0,0,354,355,7,0,0,0,355,61,1,0,0,0,356,361,3,64,32,0,357,358,5,
        53,0,0,358,360,3,64,32,0,359,357,1,0,0,0,360,363,1,0,0,0,361,359,
        1,0,0,0,361,362,1,0,0,0,362,366,1,0,0,0,363,361,1,0,0,0,364,366,
        1,0,0,0,365,356,1,0,0,0,365,364,1,0,0,0,366,63,1,0,0,0,367,368,6,
        32,-1,0,368,369,3,66,33,0,369,375,1,0,0,0,370,371,10,2,0,0,371,372,
        5,51,0,0,372,374,3,64,32,3,373,370,1,0,0,0,374,377,1,0,0,0,375,373,
        1,0,0,0,375,376,1,0,0,0,376,65,1,0,0,0,377,375,1,0,0,0,378,379,6,
        33,-1,0,379,380,3,68,34,0,380,387,1,0,0,0,381,382,10,2,0,0,382,383,
        3,88,44,0,383,384,3,66,33,3,384,386,1,0,0,0,385,381,1,0,0,0,386,
        389,1,0,0,0,387,385,1,0,0,0,387,388,1,0,0,0,388,67,1,0,0,0,389,387,
        1,0,0,0,390,391,6,34,-1,0,391,392,3,70,35,0,392,399,1,0,0,0,393,
        394,10,2,0,0,394,395,3,98,49,0,395,396,3,70,35,0,396,398,1,0,0,0,
        397,393,1,0,0,0,398,401,1,0,0,0,399,397,1,0,0,0,399,400,1,0,0,0,
        400,69,1,0,0,0,401,399,1,0,0,0,402,403,6,35,-1,0,403,404,3,72,36,
        0,404,411,1,0,0,0,405,406,10,2,0,0,406,407,3,96,48,0,407,408,3,72,
        36,0,408,410,1,0,0,0,409,405,1,0,0,0,410,413,1,0,0,0,411,409,1,0,
        0,0,411,412,1,0,0,0,412,71,1,0,0,0,413,411,1,0,0,0,414,415,6,36,
        -1,0,415,416,3,74,37,0,416,423,1,0,0,0,417,418,10,2,0,0,418,419,
        3,94,47,0,419,420,3,74,37,0,420,422,1,0,0,0,421,417,1,0,0,0,422,
        425,1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,73,1,0,0,0,425,423,
        1,0,0,0,426,427,3,100,50,0,427,428,3,76,38,0,428,431,1,0,0,0,429,
        431,3,76,38,0,430,426,1,0,0,0,430,429,1,0,0,0,431,75,1,0,0,0,432,
        433,5,45,0,0,433,436,3,76,38,0,434,436,3,78,39,0,435,432,1,0,0,0,
        435,434,1,0,0,0,436,77,1,0,0,0,437,438,6,39,-1,0,438,439,3,80,40,
        0,439,447,1,0,0,0,440,441,10,2,0,0,441,442,5,58,0,0,442,443,3,78,
        39,0,443,444,5,59,0,0,444,446,1,0,0,0,445,440,1,0,0,0,446,449,1,
        0,0,0,447,445,1,0,0,0,447,448,1,0,0,0,448,79,1,0,0,0,449,447,1,0,
        0,0,450,451,6,40,-1,0,451,452,3,82,41,0,452,465,1,0,0,0,453,454,
        10,3,0,0,454,455,5,52,0,0,455,464,5,64,0,0,456,457,10,2,0,0,457,
        458,5,52,0,0,458,459,5,64,0,0,459,460,5,57,0,0,460,461,3,62,31,0,
        461,462,5,56,0,0,462,464,1,0,0,0,463,453,1,0,0,0,463,456,1,0,0,0,
        464,467,1,0,0,0,465,463,1,0,0,0,465,466,1,0,0,0,466,81,1,0,0,0,467,
        465,1,0,0,0,468,469,5,64,0,0,469,471,5,52,0,0,470,468,1,0,0,0,470,
        471,1,0,0,0,471,472,1,0,0,0,472,484,5,62,0,0,473,474,5,64,0,0,474,
        476,5,52,0,0,475,473,1,0,0,0,475,476,1,0,0,0,476,477,1,0,0,0,477,
        478,5,62,0,0,478,479,5,57,0,0,479,480,3,62,31,0,480,481,5,56,0,0,
        481,484,1,0,0,0,482,484,3,84,42,0,483,470,1,0,0,0,483,475,1,0,0,
        0,483,482,1,0,0,0,484,83,1,0,0,0,485,486,5,28,0,0,486,487,5,64,0,
        0,487,488,5,57,0,0,488,489,3,62,31,0,489,490,5,56,0,0,490,493,1,
        0,0,0,491,493,3,86,43,0,492,485,1,0,0,0,492,491,1,0,0,0,493,85,1,
        0,0,0,494,495,5,57,0,0,495,496,3,64,32,0,496,497,5,56,0,0,497,501,
        1,0,0,0,498,501,3,106,53,0,499,501,5,64,0,0,500,494,1,0,0,0,500,
        498,1,0,0,0,500,499,1,0,0,0,501,87,1,0,0,0,502,505,3,90,45,0,503,
        505,3,92,46,0,504,502,1,0,0,0,504,503,1,0,0,0,505,89,1,0,0,0,506,
        507,7,1,0,0,507,91,1,0,0,0,508,509,7,2,0,0,509,93,1,0,0,0,510,511,
        7,3,0,0,511,95,1,0,0,0,512,513,7,4,0,0,513,97,1,0,0,0,514,515,7,
        5,0,0,515,99,1,0,0,0,516,517,5,33,0,0,517,101,1,0,0,0,518,519,7,
        6,0,0,519,103,1,0,0,0,520,521,5,58,0,0,521,522,5,66,0,0,522,523,
        5,59,0,0,523,524,3,102,51,0,524,105,1,0,0,0,525,534,5,67,0,0,526,
        534,5,65,0,0,527,534,3,108,54,0,528,534,5,63,0,0,529,534,3,110,55,
        0,530,534,5,66,0,0,531,534,5,23,0,0,532,534,5,27,0,0,533,525,1,0,
        0,0,533,526,1,0,0,0,533,527,1,0,0,0,533,528,1,0,0,0,533,529,1,0,
        0,0,533,530,1,0,0,0,533,531,1,0,0,0,533,532,1,0,0,0,534,107,1,0,
        0,0,535,536,7,7,0,0,536,109,1,0,0,0,537,538,5,58,0,0,538,543,3,106,
        53,0,539,540,5,53,0,0,540,542,3,106,53,0,541,539,1,0,0,0,542,545,
        1,0,0,0,543,541,1,0,0,0,543,544,1,0,0,0,544,546,1,0,0,0,545,543,
        1,0,0,0,546,547,5,59,0,0,547,111,1,0,0,0,42,115,123,130,138,148,
        164,172,186,190,197,202,208,214,225,236,242,265,278,293,330,335,
        351,361,365,375,387,399,411,423,430,435,447,463,465,470,475,483,
        492,500,504,533,543
    ]

class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@readInt'", "'@writeInt'", "'@readFloat'", 
                     "'@writeFloat'", "'@readBool'", "'@writeBool'", "'@readString'", 
                     "'@writeString'", "<INVALID>", "<INVALID>", "'break'", 
                     "'continue'", "'if'", "'else'", "'for'", "'true'", 
                     "'false'", "'int'", "'float'", "'bool'", "'string'", 
                     "'return'", "'null'", "'class'", "'constructor'", "'var'", 
                     "'self'", "'new'", "'void'", "'const'", "'constant'", 
                     "'func'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'='", "':='", "'+'", "'-'", 
                     "'*'", "'\\'", "'%'", "'/'", "'<-'", "'^'", "'.'", 
                     "','", "';'", "':'", "')'", "'('", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                      "INT", "FLOAT", "BOOL", "STRING", "RETURN", "NULL", 
                      "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", "VOID", 
                      "CONST", "CONSTANT", "FUNC", "NOT", "AND", "OR", "EQUAL", 
                      "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
                      "INITIAL", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", "SUPER_CLASS", 
                      "STRING_CONCAT", "DOT", "COMMA", "SEMICOLON", "COLON", 
                      "RPAREN", "LPAREN", "LBRACK", "RBRACK", "LBRASE", 
                      "RBRASE", "AT_ID", "STRING_LITERAL", "ID", "FLOAT_LITERAL", 
                      "NON_ZERO_INT", "INT_LITERAL", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_dcl = 1
    RULE_class_body = 2
    RULE_method_dcl = 3
    RULE_constructor_decl = 4
    RULE_param_lst = 5
    RULE_param = 6
    RULE_statements = 7
    RULE_storedecl = 8
    RULE_constdecl = 9
    RULE_vardecl = 10
    RULE_non_inital_decl = 11
    RULE_inital_decl = 12
    RULE_assigndecl = 13
    RULE_assign = 14
    RULE_ifstmt = 15
    RULE_forstmt = 16
    RULE_continue_state = 17
    RULE_return_state = 18
    RULE_break_state = 19
    RULE_callstmt = 20
    RULE_instance_method_invo_access = 21
    RULE_static_method_invo_access = 22
    RULE_io_st = 23
    RULE_block = 24
    RULE_io_mt = 25
    RULE_lhs = 26
    RULE_arraycell = 27
    RULE_fieldaccess = 28
    RULE_idlst = 29
    RULE_iden = 30
    RULE_expr_lst = 31
    RULE_expr = 32
    RULE_expr1 = 33
    RULE_expr2 = 34
    RULE_expr3 = 35
    RULE_expr4 = 36
    RULE_expr5 = 37
    RULE_expr6 = 38
    RULE_expr7 = 39
    RULE_expr8 = 40
    RULE_expr9 = 41
    RULE_expr10 = 42
    RULE_expr11 = 43
    RULE_relational = 44
    RULE_relat_bool = 45
    RULE_relat_int_float = 46
    RULE_multiplying = 47
    RULE_adding = 48
    RULE_logical_bin = 49
    RULE_logical_not = 50
    RULE_typ = 51
    RULE_array_type = 52
    RULE_literal = 53
    RULE_bool_literal = 54
    RULE_array = 55

    ruleNames =  [ "program", "class_dcl", "class_body", "method_dcl", "constructor_decl", 
                   "param_lst", "param", "statements", "storedecl", "constdecl", 
                   "vardecl", "non_inital_decl", "inital_decl", "assigndecl", 
                   "assign", "ifstmt", "forstmt", "continue_state", "return_state", 
                   "break_state", "callstmt", "instance_method_invo_access", 
                   "static_method_invo_access", "io_st", "block", "io_mt", 
                   "lhs", "arraycell", "fieldaccess", "idlst", "iden", "expr_lst", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
                   "relational", "relat_bool", "relat_int_float", "multiplying", 
                   "adding", "logical_bin", "logical_not", "typ", "array_type", 
                   "literal", "bool_literal", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    BLOCK_COMMENT=9
    LINE_COMMENT=10
    BREAK=11
    CONTINUE=12
    IF=13
    ELSE=14
    FOR=15
    TRUE=16
    FALSE=17
    INT=18
    FLOAT=19
    BOOL=20
    STRING=21
    RETURN=22
    NULL=23
    CLASS=24
    CONSTRUCTOR=25
    VAR=26
    SELF=27
    NEW=28
    VOID=29
    CONST=30
    CONSTANT=31
    FUNC=32
    NOT=33
    AND=34
    OR=35
    EQUAL=36
    NOT_EQUAL=37
    LESS=38
    GREATER=39
    LESS_EQUAL=40
    GREATER_EQUAL=41
    INITIAL=42
    ASSIGN=43
    PLUS=44
    MINUS=45
    MULTIPLY=46
    DIVIDE_I=47
    DIVIDE_I_L=48
    DIVIDE_F=49
    SUPER_CLASS=50
    STRING_CONCAT=51
    DOT=52
    COMMA=53
    SEMICOLON=54
    COLON=55
    RPAREN=56
    LPAREN=57
    LBRACK=58
    RBRACK=59
    LBRASE=60
    RBRASE=61
    AT_ID=62
    STRING_LITERAL=63
    ID=64
    FLOAT_LITERAL=65
    NON_ZERO_INT=66
    INT_LITERAL=67
    WS=68
    ERROR_CHAR=69
    UNCLOSE_STRING=70
    ILLEGAL_ESCAPE=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def class_dcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_dclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_dclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 112
                self.class_dcl()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def LBRASE(self):
            return self.getToken(CSlangParser.LBRASE, 0)

        def RBRASE(self):
            return self.getToken(CSlangParser.RBRASE, 0)

        def SUPER_CLASS(self):
            return self.getToken(CSlangParser.SUPER_CLASS, 0)

        def class_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Class_bodyContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Class_bodyContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_dcl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_dcl" ):
                listener.enterClass_dcl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_dcl" ):
                listener.exitClass_dcl(self)




    def class_dcl(self):

        localctx = CSlangParser.Class_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(CSlangParser.CLASS)
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 121
                self.match(CSlangParser.ID)
                self.state = 122
                self.match(CSlangParser.SUPER_CLASS)


            self.state = 125
            self.match(CSlangParser.ID)
            self.state = 126
            self.match(CSlangParser.LBRASE)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 5435817984) != 0):
                self.state = 127
                self.class_body()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(CSlangParser.RBRASE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_dcl(self):
            return self.getTypedRuleContext(CSlangParser.Method_dclContext,0)


        def constructor_decl(self):
            return self.getTypedRuleContext(CSlangParser.Constructor_declContext,0)


        def storedecl(self):
            return self.getTypedRuleContext(CSlangParser.StoredeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_class_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_body" ):
                listener.enterClass_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_body" ):
                listener.exitClass_body(self)




    def class_body(self):

        localctx = CSlangParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 135
                self.method_dcl()
                pass

            elif la_ == 2:
                self.state = 136
                self.constructor_decl()
                pass

            elif la_ == 3:
                self.state = 137
                self.storedecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_dclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def param_lst(self):
            return self.getTypedRuleContext(CSlangParser.Param_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(CSlangParser.BlockContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_method_dcl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_dcl" ):
                listener.enterMethod_dcl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_dcl" ):
                listener.exitMethod_dcl(self)




    def method_dcl(self):

        localctx = CSlangParser.Method_dclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_method_dcl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CSlangParser.FUNC)
            self.state = 141
            _la = self._input.LA(1)
            if not(_la==62 or _la==64):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 142
            self.match(CSlangParser.LPAREN)
            self.state = 143
            self.param_lst()
            self.state = 144
            self.match(CSlangParser.RPAREN)
            self.state = 145
            self.match(CSlangParser.COLON)
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 21, 64]:
                self.state = 146
                self.typ()
                pass
            elif token in [29]:
                self.state = 147
                self.match(CSlangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 150
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def param_lst(self):
            return self.getTypedRuleContext(CSlangParser.Param_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(CSlangParser.BlockContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constructor_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor_decl" ):
                listener.enterConstructor_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor_decl" ):
                listener.exitConstructor_decl(self)




    def constructor_decl(self):

        localctx = CSlangParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constructor_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(CSlangParser.FUNC)
            self.state = 153
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 154
            self.match(CSlangParser.LPAREN)
            self.state = 155
            self.param_lst()
            self.state = 156
            self.match(CSlangParser.RPAREN)
            self.state = 157
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ParamContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def idlst(self):
            return self.getTypedRuleContext(CSlangParser.IdlstContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param_lst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_lst" ):
                listener.enterParam_lst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_lst" ):
                listener.exitParam_lst(self)




    def param_lst(self):

        localctx = CSlangParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param_lst)
        self._la = 0 # Token type
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.param()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==53:
                    self.state = 160
                    self.match(CSlangParser.COMMA)
                    self.state = 161
                    self.param()
                    self.state = 166
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.idlst()
                self.state = 168
                self.match(CSlangParser.COLON)
                self.state = 169
                self.typ()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.iden()
            self.state = 175
            self.match(CSlangParser.COLON)
            self.state = 176
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def storedecl(self):
            return self.getTypedRuleContext(CSlangParser.StoredeclContext,0)


        def assigndecl(self):
            return self.getTypedRuleContext(CSlangParser.AssigndeclContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(CSlangParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(CSlangParser.ForstmtContext,0)


        def break_state(self):
            return self.getTypedRuleContext(CSlangParser.Break_stateContext,0)


        def continue_state(self):
            return self.getTypedRuleContext(CSlangParser.Continue_stateContext,0)


        def return_state(self):
            return self.getTypedRuleContext(CSlangParser.Return_stateContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(CSlangParser.CallstmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = CSlangParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statements)
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.storedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.assigndecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.break_state()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.continue_state()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.return_state()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 185
                self.callstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoredeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def constdecl(self):
            return self.getTypedRuleContext(CSlangParser.ConstdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(CSlangParser.VardeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_storedecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoredecl" ):
                listener.enterStoredecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoredecl" ):
                listener.exitStoredecl(self)




    def storedecl(self):

        localctx = CSlangParser.StoredeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_storedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.state = 188
                self.constdecl()
                pass
            elif token in [26]:
                self.state = 189
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 192
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def non_inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Non_inital_declContext,0)


        def inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Inital_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_constdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstdecl" ):
                listener.enterConstdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstdecl" ):
                listener.exitConstdecl(self)




    def constdecl(self):

        localctx = CSlangParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(CSlangParser.CONST)
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 195
                self.non_inital_decl()
                pass

            elif la_ == 2:
                self.state = 196
                self.inital_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def non_inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Non_inital_declContext,0)


        def inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Inital_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_vardecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl" ):
                listener.enterVardecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl" ):
                listener.exitVardecl(self)




    def vardecl(self):

        localctx = CSlangParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(CSlangParser.VAR)
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 200
                self.non_inital_decl()
                pass

            elif la_ == 2:
                self.state = 201
                self.inital_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_inital_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlst(self):
            return self.getTypedRuleContext(CSlangParser.IdlstContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_non_inital_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_inital_decl" ):
                listener.enterNon_inital_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_inital_decl" ):
                listener.exitNon_inital_decl(self)




    def non_inital_decl(self):

        localctx = CSlangParser.Non_inital_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_non_inital_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.idlst()
            self.state = 205
            self.match(CSlangParser.COLON)
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 21, 64]:
                self.state = 206
                self.typ()
                pass
            elif token in [58]:
                self.state = 207
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inital_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def INITIAL(self):
            return self.getToken(CSlangParser.INITIAL, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def inital_decl(self):
            return self.getTypedRuleContext(CSlangParser.Inital_declContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_inital_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInital_decl" ):
                listener.enterInital_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInital_decl" ):
                listener.exitInital_decl(self)




    def inital_decl(self):

        localctx = CSlangParser.Inital_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inital_decl)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.iden()
                self.state = 211
                self.match(CSlangParser.COLON)
                self.state = 214
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18, 19, 20, 21, 64]:
                    self.state = 212
                    self.typ()
                    pass
                elif token in [58]:
                    self.state = 213
                    self.array_type()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 216
                self.match(CSlangParser.INITIAL)
                self.state = 217
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.iden()
                self.state = 220
                self.match(CSlangParser.COMMA)
                self.state = 221
                self.inital_decl()
                self.state = 222
                self.match(CSlangParser.COMMA)
                self.state = 223
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigndeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(CSlangParser.AssignContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_assigndecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigndecl" ):
                listener.enterAssigndecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigndecl" ):
                listener.exitAssigndecl(self)




    def assigndecl(self):

        localctx = CSlangParser.AssigndeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assigndecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.assign()
            self.state = 228
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSlangParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = CSlangParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.lhs()
            self.state = 231
            self.match(CSlangParser.ASSIGN)
            self.state = 232
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.BlockContext)
            else:
                return self.getTypedRuleContext(CSlangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_ifstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstmt" ):
                listener.enterIfstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstmt" ):
                listener.exitIfstmt(self)




    def ifstmt(self):

        localctx = CSlangParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(CSlangParser.IF)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==60:
                self.state = 235
                self.block()


            self.state = 238
            self.expr(0)
            self.state = 239
            self.block()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 240
                self.match(CSlangParser.ELSE)
                self.state = 241
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.AssignContext)
            else:
                return self.getTypedRuleContext(CSlangParser.AssignContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SEMICOLON)
            else:
                return self.getToken(CSlangParser.SEMICOLON, i)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(CSlangParser.BlockContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_forstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForstmt" ):
                listener.enterForstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForstmt" ):
                listener.exitForstmt(self)




    def forstmt(self):

        localctx = CSlangParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(CSlangParser.FOR)
            self.state = 245
            self.assign()
            self.state = 246
            self.match(CSlangParser.SEMICOLON)
            self.state = 247
            self.expr(0)
            self.state = 248
            self.match(CSlangParser.SEMICOLON)
            self.state = 249
            self.assign()
            self.state = 250
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_state

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_state" ):
                listener.enterContinue_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_state" ):
                listener.exitContinue_state(self)




    def continue_state(self):

        localctx = CSlangParser.Continue_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_continue_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(CSlangParser.CONTINUE)
            self.state = 253
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_return_state

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_state" ):
                listener.enterReturn_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_state" ):
                listener.exitReturn_state(self)




    def return_state(self):

        localctx = CSlangParser.Return_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(CSlangParser.RETURN)
            self.state = 256
            self.expr(0)
            self.state = 257
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_state

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_state" ):
                listener.enterBreak_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_state" ):
                listener.exitBreak_state(self)




    def break_state(self):

        localctx = CSlangParser.Break_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_break_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(CSlangParser.BREAK)
            self.state = 260
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(CSlangParser.SEMICOLON, 0)

        def instance_method_invo_access(self):
            return self.getTypedRuleContext(CSlangParser.Instance_method_invo_accessContext,0)


        def static_method_invo_access(self):
            return self.getTypedRuleContext(CSlangParser.Static_method_invo_accessContext,0)


        def io_st(self):
            return self.getTypedRuleContext(CSlangParser.Io_stContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_callstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallstmt" ):
                listener.enterCallstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallstmt" ):
                listener.exitCallstmt(self)




    def callstmt(self):

        localctx = CSlangParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 262
                self.instance_method_invo_access()
                pass

            elif la_ == 2:
                self.state = 263
                self.static_method_invo_access()
                pass

            elif la_ == 3:
                self.state = 264
                self.io_st()
                pass


            self.state = 267
            self.match(CSlangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_invo_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_instance_method_invo_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstance_method_invo_access" ):
                listener.enterInstance_method_invo_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstance_method_invo_access" ):
                listener.exitInstance_method_invo_access(self)




    def instance_method_invo_access(self):

        localctx = CSlangParser.Instance_method_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_instance_method_invo_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.expr(0)
            self.state = 270
            self.match(CSlangParser.DOT)
            self.state = 271
            self.match(CSlangParser.ID)

            self.state = 272
            self.match(CSlangParser.LPAREN)
            self.state = 273
            self.expr_lst()
            self.state = 274
            self.match(CSlangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invo_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_static_method_invo_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatic_method_invo_access" ):
                listener.enterStatic_method_invo_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatic_method_invo_access" ):
                listener.exitStatic_method_invo_access(self)




    def static_method_invo_access(self):

        localctx = CSlangParser.Static_method_invo_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_static_method_invo_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 276
                self.match(CSlangParser.ID)
                self.state = 277
                self.match(CSlangParser.DOT)


            self.state = 280
            self.match(CSlangParser.AT_ID)

            self.state = 281
            self.match(CSlangParser.LPAREN)
            self.state = 282
            self.expr_lst()
            self.state = 283
            self.match(CSlangParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Io_stContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def io_mt(self):
            return self.getTypedRuleContext(CSlangParser.Io_mtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_io_st

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIo_st" ):
                listener.enterIo_st(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIo_st" ):
                listener.exitIo_st(self)




    def io_st(self):

        localctx = CSlangParser.Io_stContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_io_st)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.expr(0)
            self.state = 286
            self.match(CSlangParser.DOT)
            self.state = 287
            self.io_mt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRASE(self):
            return self.getToken(CSlangParser.LBRASE, 0)

        def RBRASE(self):
            return self.getToken(CSlangParser.RBRASE, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StatementsContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StatementsContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = CSlangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(CSlangParser.LBRASE)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 11)) & ~0x3f) == 0 and ((1 << (_la - 11)) & 142074511679527031) != 0):
                self.state = 290
                self.statements()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 296
            self.match(CSlangParser.RBRASE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Io_mtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_io_mt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIo_mt" ):
                listener.enterIo_mt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIo_mt" ):
                listener.exitIo_mt(self)




    def io_mt(self):

        localctx = CSlangParser.Io_mtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_io_mt)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(CSlangParser.T__0)
                self.state = 299
                self.match(CSlangParser.LPAREN)
                self.state = 300
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(CSlangParser.T__1)
                self.state = 302
                self.match(CSlangParser.LPAREN)
                self.state = 303
                self.expr_lst()
                self.state = 304
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.match(CSlangParser.T__2)
                self.state = 307
                self.match(CSlangParser.LPAREN)
                self.state = 308
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                self.match(CSlangParser.T__3)
                self.state = 310
                self.match(CSlangParser.LPAREN)
                self.state = 311
                self.expr_lst()
                self.state = 312
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 314
                self.match(CSlangParser.T__4)
                self.state = 315
                self.match(CSlangParser.LPAREN)
                self.state = 316
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 317
                self.match(CSlangParser.T__5)
                self.state = 318
                self.match(CSlangParser.LPAREN)
                self.state = 319
                self.expr_lst()
                self.state = 320
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 322
                self.match(CSlangParser.T__6)
                self.state = 323
                self.match(CSlangParser.LPAREN)
                self.state = 324
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 8)
                self.state = 325
                self.match(CSlangParser.T__7)
                self.state = 326
                self.match(CSlangParser.LPAREN)
                self.state = 327
                self.expr_lst()
                self.state = 328
                self.match(CSlangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def arraycell(self):
            return self.getTypedRuleContext(CSlangParser.ArraycellContext,0)


        def fieldaccess(self):
            return self.getTypedRuleContext(CSlangParser.FieldaccessContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_lhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhs" ):
                listener.enterLhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhs" ):
                listener.exitLhs(self)




    def lhs(self):

        localctx = CSlangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lhs)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.iden()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.arraycell()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
                self.fieldaccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraycellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_arraycell

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraycell" ):
                listener.enterArraycell(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraycell" ):
                listener.exitArraycell(self)




    def arraycell(self):

        localctx = CSlangParser.ArraycellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_arraycell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.expr(0)
            self.state = 338
            self.match(CSlangParser.LBRACK)
            self.state = 339
            self.expr(0)
            self.state = 340
            self.match(CSlangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self):
            return self.getTypedRuleContext(CSlangParser.IdenContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_fieldaccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldaccess" ):
                listener.enterFieldaccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldaccess" ):
                listener.exitFieldaccess(self)




    def fieldaccess(self):

        localctx = CSlangParser.FieldaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_fieldaccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.iden()
            self.state = 343
            self.match(CSlangParser.DOT)
            self.state = 344
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iden(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.IdenContext)
            else:
                return self.getTypedRuleContext(CSlangParser.IdenContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_idlst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdlst" ):
                listener.enterIdlst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdlst" ):
                listener.exitIdlst(self)




    def idlst(self):

        localctx = CSlangParser.IdlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_idlst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.iden()
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 347
                self.match(CSlangParser.COMMA)
                self.state = 348
                self.iden()
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_iden

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIden" ):
                listener.enterIden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIden" ):
                listener.exitIden(self)




    def iden(self):

        localctx = CSlangParser.IdenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_iden)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            _la = self._input.LA(1)
            if not(_la==62 or _la==64):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr_lst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_lst" ):
                listener.enterExpr_lst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_lst" ):
                listener.exitExpr_lst(self)




    def expr_lst(self):

        localctx = CSlangParser.Expr_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr_lst)
        self._la = 0 # Token type
        try:
            self.state = 365
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 17, 23, 27, 28, 33, 45, 57, 58, 62, 63, 64, 65, 66, 67]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.expr(0)
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==53:
                    self.state = 357
                    self.match(CSlangParser.COMMA)
                    self.state = 358
                    self.expr(0)
                    self.state = 363
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(CSlangParser.Expr1Context,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def STRING_CONCAT(self):
            return self.getToken(CSlangParser.STRING_CONCAT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 375
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 370
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 371
                    self.match(CSlangParser.STRING_CONCAT)
                    self.state = 372
                    self.expr(3) 
                self.state = 377
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr1Context,i)


        def relational(self):
            return self.getTypedRuleContext(CSlangParser.RelationalContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr1" ):
                listener.enterExpr1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr1" ):
                listener.exitExpr1(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 381
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 382
                    self.relational()
                    self.state = 383
                    self.expr1(3) 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def logical_bin(self):
            return self.getTypedRuleContext(CSlangParser.Logical_binContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr2" ):
                listener.enterExpr2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr2" ):
                listener.exitExpr2(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 393
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 394
                    self.logical_bin()
                    self.state = 395
                    self.expr3(0) 
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def adding(self):
            return self.getTypedRuleContext(CSlangParser.AddingContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr3" ):
                listener.enterExpr3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr3" ):
                listener.exitExpr3(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 411
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 405
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 406
                    self.adding()
                    self.state = 407
                    self.expr4(0) 
                self.state = 413
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def multiplying(self):
            return self.getTypedRuleContext(CSlangParser.MultiplyingContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr4" ):
                listener.enterExpr4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr4" ):
                listener.exitExpr4(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 417
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 418
                    self.multiplying()
                    self.state = 419
                    self.expr5() 
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_not(self):
            return self.getTypedRuleContext(CSlangParser.Logical_notContext,0)


        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr5" ):
                listener.enterExpr5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr5" ):
                listener.exitExpr5(self)




    def expr5(self):

        localctx = CSlangParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr5)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.logical_not()
                self.state = 427
                self.expr6()
                pass
            elif token in [16, 17, 23, 27, 28, 45, 57, 58, 62, 63, 64, 65, 66, 67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr6" ):
                listener.enterExpr6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr6" ):
                listener.exitExpr6(self)




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr6)
        try:
            self.state = 435
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(CSlangParser.MINUS)
                self.state = 433
                self.expr6()
                pass
            elif token in [16, 17, 23, 27, 28, 57, 58, 62, 63, 64, 65, 66, 67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def expr7(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr7Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr7Context,i)


        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr7" ):
                listener.enterExpr7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr7" ):
                listener.exitExpr7(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 447
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 440
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 441
                    self.match(CSlangParser.LBRACK)
                    self.state = 442
                    self.expr7(0)
                    self.state = 443
                    self.match(CSlangParser.RBRACK) 
                self.state = 449
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr8" ):
                listener.enterExpr8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr8" ):
                listener.exitExpr8(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 463
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 453
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 454
                        self.match(CSlangParser.DOT)
                        self.state = 455
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 456
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 457
                        self.match(CSlangParser.DOT)
                        self.state = 458
                        self.match(CSlangParser.ID)

                        self.state = 459
                        self.match(CSlangParser.LPAREN)
                        self.state = 460
                        self.expr_lst()
                        self.state = 461
                        self.match(CSlangParser.RPAREN)
                        pass

             
                self.state = 467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT_ID(self):
            return self.getToken(CSlangParser.AT_ID, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr9

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr9" ):
                listener.enterExpr9(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr9" ):
                listener.exitExpr9(self)




    def expr9(self):

        localctx = CSlangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 468
                    self.match(CSlangParser.ID)
                    self.state = 469
                    self.match(CSlangParser.DOT)


                self.state = 472
                self.match(CSlangParser.AT_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 473
                    self.match(CSlangParser.ID)
                    self.state = 474
                    self.match(CSlangParser.DOT)


                self.state = 477
                self.match(CSlangParser.AT_ID)

                self.state = 478
                self.match(CSlangParser.LPAREN)
                self.state = 479
                self.expr_lst()
                self.state = 480
                self.match(CSlangParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 482
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr_lst(self):
            return self.getTypedRuleContext(CSlangParser.Expr_lstContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def expr11(self):
            return self.getTypedRuleContext(CSlangParser.Expr11Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr10

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr10" ):
                listener.enterExpr10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr10" ):
                listener.exitExpr10(self)




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr10)
        try:
            self.state = 492
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.match(CSlangParser.NEW)
                self.state = 486
                self.match(CSlangParser.ID)
                self.state = 487
                self.match(CSlangParser.LPAREN)
                self.state = 488
                self.expr_lst()
                self.state = 489
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [16, 17, 23, 27, 57, 58, 63, 64, 65, 66, 67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CSlangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CSlangParser.RPAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(CSlangParser.LiteralContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr11

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr11" ):
                listener.enterExpr11(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr11" ):
                listener.exitExpr11(self)




    def expr11(self):

        localctx = CSlangParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr11)
        try:
            self.state = 500
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.match(CSlangParser.LPAREN)
                self.state = 495
                self.expr(0)
                self.state = 496
                self.match(CSlangParser.RPAREN)
                pass
            elif token in [16, 17, 23, 27, 58, 63, 65, 66, 67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.literal()
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 3)
                self.state = 499
                self.match(CSlangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relat_bool(self):
            return self.getTypedRuleContext(CSlangParser.Relat_boolContext,0)


        def relat_int_float(self):
            return self.getTypedRuleContext(CSlangParser.Relat_int_floatContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_relational

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)




    def relational(self):

        localctx = CSlangParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_relational)
        try:
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 502
                self.relat_bool()
                pass
            elif token in [38, 39, 40, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.relat_int_float()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relat_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(CSlangParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_relat_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelat_bool" ):
                listener.enterRelat_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelat_bool" ):
                listener.exitRelat_bool(self)




    def relat_bool(self):

        localctx = CSlangParser.Relat_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_relat_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relat_int_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(CSlangParser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(CSlangParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(CSlangParser.GREATER_EQUAL, 0)

        def GREATER(self):
            return self.getToken(CSlangParser.GREATER, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_relat_int_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelat_int_float" ):
                listener.enterRelat_int_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelat_int_float" ):
                listener.exitRelat_int_float(self)




    def relat_int_float(self):

        localctx = CSlangParser.Relat_int_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_relat_int_float)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4123168604160) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(CSlangParser.MULTIPLY, 0)

        def DIVIDE_F(self):
            return self.getToken(CSlangParser.DIVIDE_F, 0)

        def DIVIDE_I(self):
            return self.getToken(CSlangParser.DIVIDE_I, 0)

        def DIVIDE_I_L(self):
            return self.getToken(CSlangParser.DIVIDE_I_L, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_multiplying

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplying" ):
                listener.enterMultiplying(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplying" ):
                listener.exitMultiplying(self)




    def multiplying(self):

        localctx = CSlangParser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1055531162664960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(CSlangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CSlangParser.MINUS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_adding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdding" ):
                listener.enterAdding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdding" ):
                listener.exitAdding(self)




    def adding(self):

        localctx = CSlangParser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            _la = self._input.LA(1)
            if not(_la==44 or _la==45):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_binContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_logical_bin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_bin" ):
                listener.enterLogical_bin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_bin" ):
                listener.exitLogical_bin(self)




    def logical_bin(self):

        localctx = CSlangParser.Logical_binContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_logical_bin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            _la = self._input.LA(1)
            if not(_la==34 or _la==35):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_logical_not

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_not" ):
                listener.enterLogical_not(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_not" ):
                listener.exitLogical_not(self)




    def logical_not(self):

        localctx = CSlangParser.Logical_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_logical_not)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.match(CSlangParser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_typ

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp" ):
                listener.enterTyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp" ):
                listener.exitTyp(self)




    def typ(self):

        localctx = CSlangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            _la = self._input.LA(1)
            if not(((((_la - 18)) & ~0x3f) == 0 and ((1 << (_la - 18)) & 70368744177679) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def NON_ZERO_INT(self):
            return self.getToken(CSlangParser.NON_ZERO_INT, 0)

        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def typ(self):
            return self.getTypedRuleContext(CSlangParser.TypContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_array_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type" ):
                listener.enterArray_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type" ):
                listener.exitArray_type(self)




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(CSlangParser.LBRACK)
            self.state = 521
            self.match(CSlangParser.NON_ZERO_INT)
            self.state = 522
            self.match(CSlangParser.RBRACK)
            self.state = 523
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(CSlangParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(CSlangParser.FLOAT_LITERAL, 0)

        def bool_literal(self):
            return self.getTypedRuleContext(CSlangParser.Bool_literalContext,0)


        def STRING_LITERAL(self):
            return self.getToken(CSlangParser.STRING_LITERAL, 0)

        def array(self):
            return self.getTypedRuleContext(CSlangParser.ArrayContext,0)


        def NON_ZERO_INT(self):
            return self.getToken(CSlangParser.NON_ZERO_INT, 0)

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_literal)
        try:
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [67]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.match(CSlangParser.INT_LITERAL)
                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.match(CSlangParser.FLOAT_LITERAL)
                pass
            elif token in [16, 17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 527
                self.bool_literal()
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 4)
                self.state = 528
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 5)
                self.state = 529
                self.array()
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 6)
                self.state = 530
                self.match(CSlangParser.NON_ZERO_INT)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 7)
                self.state = 531
                self.match(CSlangParser.NULL)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 8)
                self.state = 532
                self.match(CSlangParser.SELF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(CSlangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CSlangParser.FALSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_bool_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_literal" ):
                listener.enterBool_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_literal" ):
                listener.exitBool_literal(self)




    def bool_literal(self):

        localctx = CSlangParser.Bool_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(CSlangParser.LBRACK, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.LiteralContext)
            else:
                return self.getTypedRuleContext(CSlangParser.LiteralContext,i)


        def RBRACK(self):
            return self.getToken(CSlangParser.RBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.COMMA)
            else:
                return self.getToken(CSlangParser.COMMA, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = CSlangParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(CSlangParser.LBRACK)
            self.state = 538
            self.literal()
            self.state = 543
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 539
                self.match(CSlangParser.COMMA)
                self.state = 540
                self.literal()
                self.state = 545
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 546
            self.match(CSlangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[32] = self.expr_sempred
        self._predicates[33] = self.expr1_sempred
        self._predicates[34] = self.expr2_sempred
        self._predicates[35] = self.expr3_sempred
        self._predicates[36] = self.expr4_sempred
        self._predicates[39] = self.expr7_sempred
        self._predicates[40] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         




