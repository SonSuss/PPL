# Generated from e:/hocbaidcm/PPL/assignment/assign1/cslang-initial/cslang-initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,71,586,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,248,8,8,10,8,12,8,251,9,
        8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,262,8,9,10,9,12,9,265,
        9,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,
        1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,
        1,31,1,31,1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,
        1,36,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,
        1,41,1,41,1,42,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,
        1,47,1,47,1,48,1,48,1,49,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,
        1,53,1,53,1,54,1,54,1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,58,1,59,
        1,59,1,60,1,60,1,61,1,61,1,61,1,62,1,62,1,62,5,62,471,8,62,10,62,
        12,62,474,9,62,1,62,1,62,1,62,1,63,1,63,5,63,481,8,63,10,63,12,63,
        484,9,63,1,64,4,64,487,8,64,11,64,12,64,488,1,64,1,64,1,64,1,64,
        1,64,3,64,496,8,64,1,65,1,65,5,65,500,8,65,10,65,12,65,503,9,65,
        1,66,4,66,506,8,66,11,66,12,66,507,1,67,1,67,3,67,512,8,67,1,68,
        1,68,5,68,516,8,68,10,68,12,68,519,9,68,1,69,1,69,3,69,523,8,69,
        1,69,4,69,526,8,69,11,69,12,69,527,1,70,1,70,1,71,1,71,1,71,1,71,
        1,71,1,71,1,71,1,71,1,71,1,71,1,71,1,71,1,71,1,71,3,71,546,8,71,
        1,72,1,72,1,72,3,72,551,8,72,1,73,4,73,554,8,73,11,73,12,73,555,
        1,73,1,73,1,74,1,74,1,74,1,75,1,75,1,75,5,75,566,8,75,10,75,12,75,
        569,9,75,1,75,3,75,572,8,75,1,75,1,75,1,76,1,76,1,76,5,76,579,8,
        76,10,76,12,76,582,9,76,1,76,1,76,1,76,1,249,0,77,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,
        16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,
        27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,
        38,77,39,79,40,81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,
        49,99,50,101,51,103,52,105,53,107,54,109,55,111,56,113,57,115,58,
        117,59,119,60,121,61,123,62,125,63,127,64,129,65,131,66,133,67,135,
        0,137,0,139,0,141,0,143,0,145,0,147,68,149,69,151,70,153,71,1,0,
        11,5,0,10,10,13,13,69,70,79,79,124,124,2,0,10,10,13,13,4,0,8,10,
        12,13,34,34,92,92,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,
        122,1,0,49,57,1,0,48,57,2,0,69,69,101,101,5,0,98,98,102,102,110,
        110,114,114,116,116,3,0,9,10,13,13,32,32,3,1,8,10,12,13,32,32,605,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,
        1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,
        1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,
        1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,
        1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,
        1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,
        1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,
        1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,
        1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,
        1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,
        0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,
        0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,
        129,1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,147,1,0,0,0,0,149,1,0,
        0,0,0,151,1,0,0,0,0,153,1,0,0,0,1,155,1,0,0,0,3,164,1,0,0,0,5,174,
        1,0,0,0,7,185,1,0,0,0,9,197,1,0,0,0,11,207,1,0,0,0,13,218,1,0,0,
        0,15,230,1,0,0,0,17,243,1,0,0,0,19,257,1,0,0,0,21,270,1,0,0,0,23,
        276,1,0,0,0,25,285,1,0,0,0,27,288,1,0,0,0,29,293,1,0,0,0,31,297,
        1,0,0,0,33,302,1,0,0,0,35,308,1,0,0,0,37,312,1,0,0,0,39,318,1,0,
        0,0,41,323,1,0,0,0,43,330,1,0,0,0,45,337,1,0,0,0,47,342,1,0,0,0,
        49,348,1,0,0,0,51,360,1,0,0,0,53,364,1,0,0,0,55,369,1,0,0,0,57,373,
        1,0,0,0,59,378,1,0,0,0,61,384,1,0,0,0,63,393,1,0,0,0,65,398,1,0,
        0,0,67,400,1,0,0,0,69,403,1,0,0,0,71,406,1,0,0,0,73,409,1,0,0,0,
        75,412,1,0,0,0,77,414,1,0,0,0,79,416,1,0,0,0,81,419,1,0,0,0,83,422,
        1,0,0,0,85,424,1,0,0,0,87,427,1,0,0,0,89,429,1,0,0,0,91,431,1,0,
        0,0,93,433,1,0,0,0,95,435,1,0,0,0,97,437,1,0,0,0,99,439,1,0,0,0,
        101,442,1,0,0,0,103,444,1,0,0,0,105,446,1,0,0,0,107,448,1,0,0,0,
        109,450,1,0,0,0,111,452,1,0,0,0,113,454,1,0,0,0,115,456,1,0,0,0,
        117,458,1,0,0,0,119,460,1,0,0,0,121,462,1,0,0,0,123,464,1,0,0,0,
        125,467,1,0,0,0,127,478,1,0,0,0,129,486,1,0,0,0,131,497,1,0,0,0,
        133,505,1,0,0,0,135,511,1,0,0,0,137,513,1,0,0,0,139,520,1,0,0,0,
        141,529,1,0,0,0,143,545,1,0,0,0,145,550,1,0,0,0,147,553,1,0,0,0,
        149,559,1,0,0,0,151,562,1,0,0,0,153,575,1,0,0,0,155,156,5,64,0,0,
        156,157,5,114,0,0,157,158,5,101,0,0,158,159,5,97,0,0,159,160,5,100,
        0,0,160,161,5,73,0,0,161,162,5,110,0,0,162,163,5,116,0,0,163,2,1,
        0,0,0,164,165,5,64,0,0,165,166,5,119,0,0,166,167,5,114,0,0,167,168,
        5,105,0,0,168,169,5,116,0,0,169,170,5,101,0,0,170,171,5,73,0,0,171,
        172,5,110,0,0,172,173,5,116,0,0,173,4,1,0,0,0,174,175,5,64,0,0,175,
        176,5,114,0,0,176,177,5,101,0,0,177,178,5,97,0,0,178,179,5,100,0,
        0,179,180,5,70,0,0,180,181,5,108,0,0,181,182,5,111,0,0,182,183,5,
        97,0,0,183,184,5,116,0,0,184,6,1,0,0,0,185,186,5,64,0,0,186,187,
        5,119,0,0,187,188,5,114,0,0,188,189,5,105,0,0,189,190,5,116,0,0,
        190,191,5,101,0,0,191,192,5,70,0,0,192,193,5,108,0,0,193,194,5,111,
        0,0,194,195,5,97,0,0,195,196,5,116,0,0,196,8,1,0,0,0,197,198,5,64,
        0,0,198,199,5,114,0,0,199,200,5,101,0,0,200,201,5,97,0,0,201,202,
        5,100,0,0,202,203,5,66,0,0,203,204,5,111,0,0,204,205,5,111,0,0,205,
        206,5,108,0,0,206,10,1,0,0,0,207,208,5,64,0,0,208,209,5,119,0,0,
        209,210,5,114,0,0,210,211,5,105,0,0,211,212,5,116,0,0,212,213,5,
        101,0,0,213,214,5,66,0,0,214,215,5,111,0,0,215,216,5,111,0,0,216,
        217,5,108,0,0,217,12,1,0,0,0,218,219,5,64,0,0,219,220,5,114,0,0,
        220,221,5,101,0,0,221,222,5,97,0,0,222,223,5,100,0,0,223,224,5,83,
        0,0,224,225,5,116,0,0,225,226,5,114,0,0,226,227,5,105,0,0,227,228,
        5,110,0,0,228,229,5,103,0,0,229,14,1,0,0,0,230,231,5,64,0,0,231,
        232,5,119,0,0,232,233,5,114,0,0,233,234,5,105,0,0,234,235,5,116,
        0,0,235,236,5,101,0,0,236,237,5,83,0,0,237,238,5,116,0,0,238,239,
        5,114,0,0,239,240,5,105,0,0,240,241,5,110,0,0,241,242,5,103,0,0,
        242,16,1,0,0,0,243,244,5,47,0,0,244,245,5,42,0,0,245,249,1,0,0,0,
        246,248,9,0,0,0,247,246,1,0,0,0,248,251,1,0,0,0,249,250,1,0,0,0,
        249,247,1,0,0,0,250,252,1,0,0,0,251,249,1,0,0,0,252,253,5,42,0,0,
        253,254,5,47,0,0,254,255,1,0,0,0,255,256,6,8,0,0,256,18,1,0,0,0,
        257,258,5,47,0,0,258,259,5,47,0,0,259,263,1,0,0,0,260,262,8,0,0,
        0,261,260,1,0,0,0,262,265,1,0,0,0,263,261,1,0,0,0,263,264,1,0,0,
        0,264,266,1,0,0,0,265,263,1,0,0,0,266,267,7,1,0,0,267,268,1,0,0,
        0,268,269,6,9,0,0,269,20,1,0,0,0,270,271,5,98,0,0,271,272,5,114,
        0,0,272,273,5,101,0,0,273,274,5,97,0,0,274,275,5,107,0,0,275,22,
        1,0,0,0,276,277,5,99,0,0,277,278,5,111,0,0,278,279,5,110,0,0,279,
        280,5,116,0,0,280,281,5,105,0,0,281,282,5,110,0,0,282,283,5,117,
        0,0,283,284,5,101,0,0,284,24,1,0,0,0,285,286,5,105,0,0,286,287,5,
        102,0,0,287,26,1,0,0,0,288,289,5,101,0,0,289,290,5,108,0,0,290,291,
        5,115,0,0,291,292,5,101,0,0,292,28,1,0,0,0,293,294,5,102,0,0,294,
        295,5,111,0,0,295,296,5,114,0,0,296,30,1,0,0,0,297,298,5,116,0,0,
        298,299,5,114,0,0,299,300,5,117,0,0,300,301,5,101,0,0,301,32,1,0,
        0,0,302,303,5,102,0,0,303,304,5,97,0,0,304,305,5,108,0,0,305,306,
        5,115,0,0,306,307,5,101,0,0,307,34,1,0,0,0,308,309,5,105,0,0,309,
        310,5,110,0,0,310,311,5,116,0,0,311,36,1,0,0,0,312,313,5,102,0,0,
        313,314,5,108,0,0,314,315,5,111,0,0,315,316,5,97,0,0,316,317,5,116,
        0,0,317,38,1,0,0,0,318,319,5,98,0,0,319,320,5,111,0,0,320,321,5,
        111,0,0,321,322,5,108,0,0,322,40,1,0,0,0,323,324,5,115,0,0,324,325,
        5,116,0,0,325,326,5,114,0,0,326,327,5,105,0,0,327,328,5,110,0,0,
        328,329,5,103,0,0,329,42,1,0,0,0,330,331,5,114,0,0,331,332,5,101,
        0,0,332,333,5,116,0,0,333,334,5,117,0,0,334,335,5,114,0,0,335,336,
        5,110,0,0,336,44,1,0,0,0,337,338,5,110,0,0,338,339,5,117,0,0,339,
        340,5,108,0,0,340,341,5,108,0,0,341,46,1,0,0,0,342,343,5,99,0,0,
        343,344,5,108,0,0,344,345,5,97,0,0,345,346,5,115,0,0,346,347,5,115,
        0,0,347,48,1,0,0,0,348,349,5,99,0,0,349,350,5,111,0,0,350,351,5,
        110,0,0,351,352,5,115,0,0,352,353,5,116,0,0,353,354,5,114,0,0,354,
        355,5,117,0,0,355,356,5,99,0,0,356,357,5,116,0,0,357,358,5,111,0,
        0,358,359,5,114,0,0,359,50,1,0,0,0,360,361,5,118,0,0,361,362,5,97,
        0,0,362,363,5,114,0,0,363,52,1,0,0,0,364,365,5,115,0,0,365,366,5,
        101,0,0,366,367,5,108,0,0,367,368,5,102,0,0,368,54,1,0,0,0,369,370,
        5,110,0,0,370,371,5,101,0,0,371,372,5,119,0,0,372,56,1,0,0,0,373,
        374,5,118,0,0,374,375,5,111,0,0,375,376,5,105,0,0,376,377,5,100,
        0,0,377,58,1,0,0,0,378,379,5,99,0,0,379,380,5,111,0,0,380,381,5,
        110,0,0,381,382,5,115,0,0,382,383,5,116,0,0,383,60,1,0,0,0,384,385,
        5,99,0,0,385,386,5,111,0,0,386,387,5,110,0,0,387,388,5,115,0,0,388,
        389,5,116,0,0,389,390,5,97,0,0,390,391,5,110,0,0,391,392,5,116,0,
        0,392,62,1,0,0,0,393,394,5,102,0,0,394,395,5,117,0,0,395,396,5,110,
        0,0,396,397,5,99,0,0,397,64,1,0,0,0,398,399,5,33,0,0,399,66,1,0,
        0,0,400,401,5,38,0,0,401,402,5,38,0,0,402,68,1,0,0,0,403,404,5,124,
        0,0,404,405,5,124,0,0,405,70,1,0,0,0,406,407,5,61,0,0,407,408,5,
        61,0,0,408,72,1,0,0,0,409,410,5,33,0,0,410,411,5,61,0,0,411,74,1,
        0,0,0,412,413,5,60,0,0,413,76,1,0,0,0,414,415,5,62,0,0,415,78,1,
        0,0,0,416,417,5,60,0,0,417,418,5,61,0,0,418,80,1,0,0,0,419,420,5,
        62,0,0,420,421,5,61,0,0,421,82,1,0,0,0,422,423,5,61,0,0,423,84,1,
        0,0,0,424,425,5,58,0,0,425,426,5,61,0,0,426,86,1,0,0,0,427,428,5,
        43,0,0,428,88,1,0,0,0,429,430,5,45,0,0,430,90,1,0,0,0,431,432,5,
        42,0,0,432,92,1,0,0,0,433,434,5,92,0,0,434,94,1,0,0,0,435,436,5,
        37,0,0,436,96,1,0,0,0,437,438,5,47,0,0,438,98,1,0,0,0,439,440,5,
        60,0,0,440,441,5,45,0,0,441,100,1,0,0,0,442,443,5,94,0,0,443,102,
        1,0,0,0,444,445,5,46,0,0,445,104,1,0,0,0,446,447,5,44,0,0,447,106,
        1,0,0,0,448,449,5,59,0,0,449,108,1,0,0,0,450,451,5,58,0,0,451,110,
        1,0,0,0,452,453,5,41,0,0,453,112,1,0,0,0,454,455,5,40,0,0,455,114,
        1,0,0,0,456,457,5,91,0,0,457,116,1,0,0,0,458,459,5,93,0,0,459,118,
        1,0,0,0,460,461,5,123,0,0,461,120,1,0,0,0,462,463,5,125,0,0,463,
        122,1,0,0,0,464,465,5,64,0,0,465,466,3,127,63,0,466,124,1,0,0,0,
        467,472,5,34,0,0,468,471,3,143,71,0,469,471,8,2,0,0,470,468,1,0,
        0,0,470,469,1,0,0,0,471,474,1,0,0,0,472,470,1,0,0,0,472,473,1,0,
        0,0,473,475,1,0,0,0,474,472,1,0,0,0,475,476,5,34,0,0,476,477,6,62,
        1,0,477,126,1,0,0,0,478,482,7,3,0,0,479,481,7,4,0,0,480,479,1,0,
        0,0,481,484,1,0,0,0,482,480,1,0,0,0,482,483,1,0,0,0,483,128,1,0,
        0,0,484,482,1,0,0,0,485,487,3,141,70,0,486,485,1,0,0,0,487,488,1,
        0,0,0,488,486,1,0,0,0,488,489,1,0,0,0,489,495,1,0,0,0,490,496,3,
        137,68,0,491,496,3,139,69,0,492,493,3,137,68,0,493,494,3,139,69,
        0,494,496,1,0,0,0,495,490,1,0,0,0,495,491,1,0,0,0,495,492,1,0,0,
        0,496,130,1,0,0,0,497,501,7,5,0,0,498,500,7,6,0,0,499,498,1,0,0,
        0,500,503,1,0,0,0,501,499,1,0,0,0,501,502,1,0,0,0,502,132,1,0,0,
        0,503,501,1,0,0,0,504,506,3,141,70,0,505,504,1,0,0,0,506,507,1,0,
        0,0,507,505,1,0,0,0,507,508,1,0,0,0,508,134,1,0,0,0,509,512,3,87,
        43,0,510,512,3,89,44,0,511,509,1,0,0,0,511,510,1,0,0,0,512,136,1,
        0,0,0,513,517,3,103,51,0,514,516,3,141,70,0,515,514,1,0,0,0,516,
        519,1,0,0,0,517,515,1,0,0,0,517,518,1,0,0,0,518,138,1,0,0,0,519,
        517,1,0,0,0,520,522,7,7,0,0,521,523,3,135,67,0,522,521,1,0,0,0,522,
        523,1,0,0,0,523,525,1,0,0,0,524,526,3,141,70,0,525,524,1,0,0,0,526,
        527,1,0,0,0,527,525,1,0,0,0,527,528,1,0,0,0,528,140,1,0,0,0,529,
        530,7,6,0,0,530,142,1,0,0,0,531,532,5,92,0,0,532,546,5,92,0,0,533,
        534,5,92,0,0,534,546,5,98,0,0,535,536,5,92,0,0,536,546,5,102,0,0,
        537,538,5,92,0,0,538,546,5,114,0,0,539,540,5,92,0,0,540,546,5,110,
        0,0,541,542,5,92,0,0,542,546,5,116,0,0,543,544,5,92,0,0,544,546,
        5,34,0,0,545,531,1,0,0,0,545,533,1,0,0,0,545,535,1,0,0,0,545,537,
        1,0,0,0,545,539,1,0,0,0,545,541,1,0,0,0,545,543,1,0,0,0,546,144,
        1,0,0,0,547,548,5,92,0,0,548,551,8,8,0,0,549,551,5,92,0,0,550,547,
        1,0,0,0,550,549,1,0,0,0,551,146,1,0,0,0,552,554,7,9,0,0,553,552,
        1,0,0,0,554,555,1,0,0,0,555,553,1,0,0,0,555,556,1,0,0,0,556,557,
        1,0,0,0,557,558,6,73,0,0,558,148,1,0,0,0,559,560,9,0,0,0,560,561,
        6,74,2,0,561,150,1,0,0,0,562,567,5,34,0,0,563,566,3,143,71,0,564,
        566,8,2,0,0,565,563,1,0,0,0,565,564,1,0,0,0,566,569,1,0,0,0,567,
        565,1,0,0,0,567,568,1,0,0,0,568,571,1,0,0,0,569,567,1,0,0,0,570,
        572,7,10,0,0,571,570,1,0,0,0,572,573,1,0,0,0,573,574,6,75,3,0,574,
        152,1,0,0,0,575,580,5,34,0,0,576,579,3,143,71,0,577,579,8,2,0,0,
        578,576,1,0,0,0,578,577,1,0,0,0,579,582,1,0,0,0,580,578,1,0,0,0,
        580,581,1,0,0,0,581,583,1,0,0,0,582,580,1,0,0,0,583,584,3,145,72,
        0,584,585,6,76,4,0,585,154,1,0,0,0,22,0,249,263,470,472,482,488,
        495,501,507,511,517,522,527,545,550,555,565,567,571,578,580,5,6,
        0,0,1,62,0,1,74,1,1,75,2,1,76,3
    ]

class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    BLOCK_COMMENT = 9
    LINE_COMMENT = 10
    BREAK = 11
    CONTINUE = 12
    IF = 13
    ELSE = 14
    FOR = 15
    TRUE = 16
    FALSE = 17
    INT = 18
    FLOAT = 19
    BOOL = 20
    STRING = 21
    RETURN = 22
    NULL = 23
    CLASS = 24
    CONSTRUCTOR = 25
    VAR = 26
    SELF = 27
    NEW = 28
    VOID = 29
    CONST = 30
    CONSTANT = 31
    FUNC = 32
    NOT = 33
    AND = 34
    OR = 35
    EQUAL = 36
    NOT_EQUAL = 37
    LESS = 38
    GREATER = 39
    LESS_EQUAL = 40
    GREATER_EQUAL = 41
    INITIAL = 42
    ASSIGN = 43
    PLUS = 44
    MINUS = 45
    MULTIPLY = 46
    DIVIDE_I = 47
    DIVIDE_I_L = 48
    DIVIDE_F = 49
    SUPER_CLASS = 50
    STRING_CONCAT = 51
    DOT = 52
    COMMA = 53
    SEMICOLON = 54
    COLON = 55
    RPAREN = 56
    LPAREN = 57
    LBRACK = 58
    RBRACK = 59
    LBRASE = 60
    RBRASE = 61
    AT_ID = 62
    STRING_LITERAL = 63
    ID = 64
    FLOAT_LITERAL = 65
    NON_ZERO_INT = 66
    INT_LITERAL = 67
    WS = 68
    ERROR_CHAR = 69
    UNCLOSE_STRING = 70
    ILLEGAL_ESCAPE = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'@readInt'", "'@writeInt'", "'@readFloat'", "'@writeFloat'", 
            "'@readBool'", "'@writeBool'", "'@readString'", "'@writeString'", 
            "'break'", "'continue'", "'if'", "'else'", "'for'", "'true'", 
            "'false'", "'int'", "'float'", "'bool'", "'string'", "'return'", 
            "'null'", "'class'", "'constructor'", "'var'", "'self'", "'new'", 
            "'void'", "'const'", "'constant'", "'func'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
            "':='", "'+'", "'-'", "'*'", "'\\'", "'%'", "'/'", "'<-'", "'^'", 
            "'.'", "','", "';'", "':'", "')'", "'('", "'['", "']'", "'{'", 
            "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", "CONTINUE", "IF", 
            "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", "BOOL", "STRING", 
            "RETURN", "NULL", "CLASS", "CONSTRUCTOR", "VAR", "SELF", "NEW", 
            "VOID", "CONST", "CONSTANT", "FUNC", "NOT", "AND", "OR", "EQUAL", 
            "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
            "INITIAL", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", "DIVIDE_I", 
            "DIVIDE_I_L", "DIVIDE_F", "SUPER_CLASS", "STRING_CONCAT", "DOT", 
            "COMMA", "SEMICOLON", "COLON", "RPAREN", "LPAREN", "LBRACK", 
            "RBRACK", "LBRASE", "RBRASE", "AT_ID", "STRING_LITERAL", "ID", 
            "FLOAT_LITERAL", "NON_ZERO_INT", "INT_LITERAL", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "TRUE", "FALSE", "INT", "FLOAT", 
                  "BOOL", "STRING", "RETURN", "NULL", "CLASS", "CONSTRUCTOR", 
                  "VAR", "SELF", "NEW", "VOID", "CONST", "CONSTANT", "FUNC", 
                  "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS", "GREATER", 
                  "LESS_EQUAL", "GREATER_EQUAL", "INITIAL", "ASSIGN", "PLUS", 
                  "MINUS", "MULTIPLY", "DIVIDE_I", "DIVIDE_I_L", "DIVIDE_F", 
                  "SUPER_CLASS", "STRING_CONCAT", "DOT", "COMMA", "SEMICOLON", 
                  "COLON", "RPAREN", "LPAREN", "LBRACK", "RBRACK", "LBRASE", 
                  "RBRASE", "AT_ID", "STRING_LITERAL", "ID", "FLOAT_LITERAL", 
                  "NON_ZERO_INT", "INT_LITERAL", "SIGN", "DECIMAL", "EXPONENT", 
                  "DIGIT", "ESC_SEQ", "ILL_ESQ", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[62] = self.STRING_LITERAL_action 
            actions[74] = self.ERROR_CHAR_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            unclose_string= str(self.text);
            whatif =['\b', '\t', '\f', '\n', '\r', '\\']
            if unclose_string[-1] in whatif:
                raise UncloseString(unclose_string[1:-1])
            else:
                raise UncloseString(unclose_string[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            raise IllegalEscape(self.text[1:])

     


