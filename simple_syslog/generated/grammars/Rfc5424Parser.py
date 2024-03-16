# Generated from grammars/Rfc5424.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
from typing import Optional

if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


#CHECKSTYLE:OFF
#
# Copyright 2018-2022 simple-syslog authors
# All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


def serializedATN():
    return [
        4,1,258,354,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,1,0,1,0,1,0,1,0,3,0,91,8,0,1,0,
        3,0,94,8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,104,8,2,1,2,3,2,107,
        8,2,1,2,3,2,110,8,2,1,3,1,3,5,3,114,8,3,10,3,12,3,117,9,3,1,4,3,
        4,120,8,4,1,4,3,4,123,8,4,1,4,3,4,126,8,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,3,6,144,8,6,1,6,1,6,1,
        6,3,6,149,8,6,1,7,1,7,3,7,153,8,7,1,7,1,7,1,7,3,7,158,8,7,1,8,1,
        8,5,8,162,8,8,10,8,12,8,165,9,8,3,8,167,8,8,1,9,1,9,5,9,171,8,9,
        10,9,12,9,174,9,9,3,9,176,8,9,1,10,1,10,5,10,180,8,10,10,10,12,10,
        183,9,10,3,10,185,8,10,1,11,1,11,5,11,189,8,11,10,11,12,11,192,9,
        11,3,11,194,8,11,1,12,1,12,1,12,1,12,1,12,3,12,201,8,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,16,
        1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,229,
        8,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,
        3,22,243,8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,263,8,22,1,23,1,23,
        3,23,267,8,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,5,25,282,8,25,10,25,12,25,285,9,25,3,25,287,8,25,
        1,26,1,26,1,26,1,26,5,26,293,8,26,10,26,12,26,296,9,26,1,27,1,27,
        1,27,1,27,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,5,30,311,
        8,30,10,30,12,30,314,9,30,1,31,5,31,317,8,31,10,31,12,31,320,9,31,
        1,32,1,32,1,33,1,33,1,34,1,34,1,34,1,34,3,34,330,8,34,1,35,5,35,
        333,8,35,10,35,12,35,336,9,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,
        1,39,1,40,1,40,1,41,1,41,3,41,350,8,41,1,42,1,42,1,42,0,0,43,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,0,6,2,0,15,
        15,17,17,2,0,6,6,64,65,1,0,1,256,1,0,5,98,4,0,5,5,7,32,34,64,66,
        98,1,0,21,29,348,0,86,1,0,0,0,2,95,1,0,0,0,4,99,1,0,0,0,6,111,1,
        0,0,0,8,119,1,0,0,0,10,137,1,0,0,0,12,141,1,0,0,0,14,150,1,0,0,0,
        16,166,1,0,0,0,18,175,1,0,0,0,20,184,1,0,0,0,22,193,1,0,0,0,24,200,
        1,0,0,0,26,202,1,0,0,0,28,208,1,0,0,0,30,213,1,0,0,0,32,216,1,0,
        0,0,34,219,1,0,0,0,36,222,1,0,0,0,38,230,1,0,0,0,40,233,1,0,0,0,
        42,236,1,0,0,0,44,239,1,0,0,0,46,266,1,0,0,0,48,268,1,0,0,0,50,286,
        1,0,0,0,52,288,1,0,0,0,54,297,1,0,0,0,56,303,1,0,0,0,58,305,1,0,
        0,0,60,312,1,0,0,0,62,318,1,0,0,0,64,321,1,0,0,0,66,323,1,0,0,0,
        68,329,1,0,0,0,70,334,1,0,0,0,72,337,1,0,0,0,74,339,1,0,0,0,76,341,
        1,0,0,0,78,343,1,0,0,0,80,345,1,0,0,0,82,349,1,0,0,0,84,351,1,0,
        0,0,86,87,3,6,3,0,87,88,3,74,37,0,88,90,3,8,4,0,89,91,3,74,37,0,
        90,89,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,94,3,64,32,0,93,92,
        1,0,0,0,93,94,1,0,0,0,94,1,1,0,0,0,95,96,3,6,3,0,96,97,3,74,37,0,
        97,98,3,4,2,0,98,3,1,0,0,0,99,100,3,8,4,0,100,101,3,74,37,0,101,
        103,3,50,25,0,102,104,3,74,37,0,103,102,1,0,0,0,103,104,1,0,0,0,
        104,106,1,0,0,0,105,107,3,68,34,0,106,105,1,0,0,0,106,107,1,0,0,
        0,107,109,1,0,0,0,108,110,3,64,32,0,109,108,1,0,0,0,109,110,1,0,
        0,0,110,5,1,0,0,0,111,115,3,80,40,0,112,114,3,82,41,0,113,112,1,
        0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,0,0,0,116,7,1,0,
        0,0,117,115,1,0,0,0,118,120,3,10,5,0,119,118,1,0,0,0,119,120,1,0,
        0,0,120,122,1,0,0,0,121,123,3,14,7,0,122,121,1,0,0,0,122,123,1,0,
        0,0,123,125,1,0,0,0,124,126,3,74,37,0,125,124,1,0,0,0,125,126,1,
        0,0,0,126,127,1,0,0,0,127,128,3,24,12,0,128,129,3,74,37,0,129,130,
        3,16,8,0,130,131,3,74,37,0,131,132,3,18,9,0,132,133,3,74,37,0,133,
        134,3,20,10,0,134,135,3,74,37,0,135,136,3,22,11,0,136,9,1,0,0,0,
        137,138,5,32,0,0,138,139,3,12,6,0,139,140,5,34,0,0,140,11,1,0,0,
        0,141,148,3,82,41,0,142,144,3,82,41,0,143,142,1,0,0,0,143,144,1,
        0,0,0,144,149,1,0,0,0,145,146,3,82,41,0,146,147,3,82,41,0,147,149,
        1,0,0,0,148,143,1,0,0,0,148,145,1,0,0,0,149,13,1,0,0,0,150,157,3,
        80,40,0,151,153,3,82,41,0,152,151,1,0,0,0,152,153,1,0,0,0,153,158,
        1,0,0,0,154,155,3,82,41,0,155,156,3,82,41,0,156,158,1,0,0,0,157,
        152,1,0,0,0,157,154,1,0,0,0,158,15,1,0,0,0,159,167,3,84,42,0,160,
        162,3,76,38,0,161,160,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,
        164,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,166,159,1,0,0,0,166,
        163,1,0,0,0,167,17,1,0,0,0,168,176,3,84,42,0,169,171,3,76,38,0,170,
        169,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,
        176,1,0,0,0,174,172,1,0,0,0,175,168,1,0,0,0,175,172,1,0,0,0,176,
        19,1,0,0,0,177,185,3,84,42,0,178,180,3,76,38,0,179,178,1,0,0,0,180,
        183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,185,1,0,0,0,183,
        181,1,0,0,0,184,177,1,0,0,0,184,181,1,0,0,0,185,21,1,0,0,0,186,194,
        3,84,42,0,187,189,3,76,38,0,188,187,1,0,0,0,189,192,1,0,0,0,190,
        188,1,0,0,0,190,191,1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,193,
        186,1,0,0,0,193,190,1,0,0,0,194,23,1,0,0,0,195,201,3,84,42,0,196,
        197,3,26,13,0,197,198,5,56,0,0,198,199,3,34,17,0,199,201,1,0,0,0,
        200,195,1,0,0,0,200,196,1,0,0,0,201,25,1,0,0,0,202,203,3,28,14,0,
        203,204,5,17,0,0,204,205,3,30,15,0,205,206,5,17,0,0,206,207,3,32,
        16,0,207,27,1,0,0,0,208,209,3,82,41,0,209,210,3,82,41,0,210,211,
        3,82,41,0,211,212,3,82,41,0,212,29,1,0,0,0,213,214,3,82,41,0,214,
        215,3,82,41,0,215,31,1,0,0,0,216,217,3,82,41,0,217,218,3,82,41,0,
        218,33,1,0,0,0,219,220,3,36,18,0,220,221,3,46,23,0,221,35,1,0,0,
        0,222,223,3,38,19,0,223,224,5,30,0,0,224,225,3,40,20,0,225,226,5,
        30,0,0,226,228,3,42,21,0,227,229,3,44,22,0,228,227,1,0,0,0,228,229,
        1,0,0,0,229,37,1,0,0,0,230,231,3,82,41,0,231,232,3,82,41,0,232,39,
        1,0,0,0,233,234,3,82,41,0,234,235,3,82,41,0,235,41,1,0,0,0,236,237,
        3,82,41,0,237,238,3,82,41,0,238,43,1,0,0,0,239,240,5,18,0,0,240,
        262,3,82,41,0,241,243,3,82,41,0,242,241,1,0,0,0,242,243,1,0,0,0,
        243,263,1,0,0,0,244,245,3,82,41,0,245,246,3,82,41,0,246,263,1,0,
        0,0,247,248,3,82,41,0,248,249,3,82,41,0,249,250,3,82,41,0,250,263,
        1,0,0,0,251,252,3,82,41,0,252,253,3,82,41,0,253,254,3,82,41,0,254,
        255,3,82,41,0,255,263,1,0,0,0,256,257,3,82,41,0,257,258,3,82,41,
        0,258,259,3,82,41,0,259,260,3,82,41,0,260,261,3,82,41,0,261,263,
        1,0,0,0,262,242,1,0,0,0,262,244,1,0,0,0,262,247,1,0,0,0,262,251,
        1,0,0,0,262,256,1,0,0,0,263,45,1,0,0,0,264,267,5,62,0,0,265,267,
        3,48,24,0,266,264,1,0,0,0,266,265,1,0,0,0,267,47,1,0,0,0,268,269,
        7,0,0,0,269,270,3,38,19,0,270,271,5,30,0,0,271,272,3,40,20,0,272,
        49,1,0,0,0,273,287,3,84,42,0,274,275,5,63,0,0,275,276,3,52,26,0,
        276,283,5,65,0,0,277,278,5,63,0,0,278,279,3,52,26,0,279,280,5,65,
        0,0,280,282,1,0,0,0,281,277,1,0,0,0,282,285,1,0,0,0,283,281,1,0,
        0,0,283,284,1,0,0,0,284,287,1,0,0,0,285,283,1,0,0,0,286,273,1,0,
        0,0,286,274,1,0,0,0,287,51,1,0,0,0,288,294,3,56,28,0,289,290,3,74,
        37,0,290,291,3,54,27,0,291,293,1,0,0,0,292,289,1,0,0,0,293,296,1,
        0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,53,1,0,0,0,296,294,1,0,
        0,0,297,298,3,58,29,0,298,299,5,33,0,0,299,300,5,6,0,0,300,301,3,
        60,30,0,301,302,5,6,0,0,302,55,1,0,0,0,303,304,3,62,31,0,304,57,
        1,0,0,0,305,306,3,62,31,0,306,59,1,0,0,0,307,311,8,1,0,0,308,309,
        5,64,0,0,309,311,7,1,0,0,310,307,1,0,0,0,310,308,1,0,0,0,311,314,
        1,0,0,0,312,310,1,0,0,0,312,313,1,0,0,0,313,61,1,0,0,0,314,312,1,
        0,0,0,315,317,3,78,39,0,316,315,1,0,0,0,317,320,1,0,0,0,318,316,
        1,0,0,0,318,319,1,0,0,0,319,63,1,0,0,0,320,318,1,0,0,0,321,322,3,
        66,33,0,322,65,1,0,0,0,323,324,3,70,35,0,324,67,1,0,0,0,325,326,
        5,240,0,0,326,327,5,188,0,0,327,330,5,192,0,0,328,330,5,257,0,0,
        329,325,1,0,0,0,329,328,1,0,0,0,330,69,1,0,0,0,331,333,3,72,36,0,
        332,331,1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,0,334,335,1,0,0,0,
        335,71,1,0,0,0,336,334,1,0,0,0,337,338,7,2,0,0,338,73,1,0,0,0,339,
        340,5,4,0,0,340,75,1,0,0,0,341,342,7,3,0,0,342,77,1,0,0,0,343,344,
        7,4,0,0,344,79,1,0,0,0,345,346,7,5,0,0,346,81,1,0,0,0,347,350,5,
        20,0,0,348,350,3,80,40,0,349,347,1,0,0,0,349,348,1,0,0,0,350,83,
        1,0,0,0,351,352,5,17,0,0,352,85,1,0,0,0,35,90,93,103,106,109,115,
        119,122,125,143,148,152,157,163,166,172,175,181,184,190,193,200,
        228,242,262,266,283,286,294,310,312,318,329,334,349
    ]

class Rfc5424Parser ( Parser ):

    grammarFileName = "Rfc5424.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u0009'", "'\\u000A'", "'\\u000D'", 
                     "' '", "'!'", "'\"'", "'#'", "'$'", "'%'", "'&'", "'''", 
                     "'('", "')'", "'*'", "'+'", "','", "'-'", "'.'", "'/'", 
                     "'0'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", 
                     "'8'", "'9'", "':'", "';'", "'<'", "'='", "'>'", "'?'", 
                     "'@'", "'A'", "'B'", "'C'", "'D'", "'E'", "'F'", "'G'", 
                     "'H'", "'I'", "'J'", "'K'", "'L'", "'M'", "'N'", "'O'", 
                     "'P'", "'Q'", "'R'", "'S'", "'T'", "'U'", "'V'", "'W'", 
                     "'X'", "'Y'", "'Z'", "'['", "'\\'", "']'", "'^'", "'_'", 
                     "'`'", "'a'", "'b'", "'c'", "'d'", "'e'", "'f'", "'g'", 
                     "'h'", "'i'", "'j'", "'k'", "'l'", "'m'", "'n'", "'o'", 
                     "'p'", "'q'", "'r'", "'s'", "'t'", "'u'", "'v'", "'w'", 
                     "'x'", "'y'", "'z'", "'{'", "'|'", "'}'", "'~'", "'\\u0000'", 
                     "'\\u0001'", "'\\u0002'", "'\\u0003'", "'\\u0004'", 
                     "'\\u0005'", "'\\u0006'", "'\\u0007'", "'\\u0008'", 
                     "'\\u000B'", "'\\u000C'", "'\\u000E'", "'\\u000F'", 
                     "'\\u0010'", "'\\u0011'", "'\\u0012'", "'\\u0013'", 
                     "'\\u0014'", "'\\u0015'", "'\\u0016'", "'\\u0017'", 
                     "'\\u0018'", "'\\u0019'", "'\\u001A'", "'\\u001B'", 
                     "'\\u001C'", "'\\u001D'", "'\\u001E'", "'\\u001F'", 
                     "'\\u007F'", "'\\u0080'", "'\\u0081'", "'\\u0082'", 
                     "'\\u0083'", "'\\u0084'", "'\\u0085'", "'\\u0086'", 
                     "'\\u0087'", "'\\u0088'", "'\\u0089'", "'\\u008A'", 
                     "'\\u008B'", "'\\u008C'", "'\\u008D'", "'\\u008E'", 
                     "'\\u008F'", "'\\u0090'", "'\\u0091'", "'\\u0092'", 
                     "'\\u0093'", "'\\u0094'", "'\\u0095'", "'\\u0096'", 
                     "'\\u0097'", "'\\u0098'", "'\\u0099'", "'\\u009A'", 
                     "'\\u009B'", "'\\u009C'", "'\\u009D'", "'\\u009E'", 
                     "'\\u009F'", "'\\u00A0'", "'\\u00A1'", "'\\u00A2'", 
                     "'\\u00A3'", "'\\u00A4'", "'\\u00A5'", "'\\u00A6'", 
                     "'\\u00A7'", "'\\u00A8'", "'\\u00A9'", "'\\u00AA'", 
                     "'\\u00AB'", "'\\u00AC'", "'\\u00AD'", "'\\u00AE'", 
                     "'\\u00AF'", "'\\u00B0'", "'\\u00B1'", "'\\u00B2'", 
                     "'\\u00B3'", "'\\u00B4'", "'\\u00B5'", "'\\u00B6'", 
                     "'\\u00B7'", "'\\u00B8'", "'\\u00B9'", "'\\u00BA'", 
                     "'\\u00BB'", "'\\u00BC'", "'\\u00BD'", "'\\u00BE'", 
                     "'\\u00BF'", "'\\u00C0'", "'\\u00C1'", "'\\u00C2'", 
                     "'\\u00C3'", "'\\u00C4'", "'\\u00C5'", "'\\u00C6'", 
                     "'\\u00C7'", "'\\u00C8'", "'\\u00C9'", "'\\u00CA'", 
                     "'\\u00CB'", "'\\u00CC'", "'\\u00CD'", "'\\u00CE'", 
                     "'\\u00CF'", "'\\u00D0'", "'\\u00D1'", "'\\u00D2'", 
                     "'\\u00D3'", "'\\u00D4'", "'\\u00D5'", "'\\u00D6'", 
                     "'\\u00D7'", "'\\u00D8'", "'\\u00D9'", "'\\u00DA'", 
                     "'\\u00DB'", "'\\u00DC'", "'\\u00DD'", "'\\u00DE'", 
                     "'\\u00DF'", "'\\u00E0'", "'\\u00E1'", "'\\u00E2'", 
                     "'\\u00E3'", "'\\u00E4'", "'\\u00E5'", "'\\u00E6'", 
                     "'\\u00E7'", "'\\u00E8'", "'\\u00E9'", "'\\u00EA'", 
                     "'\\u00EB'", "'\\u00EC'", "'\\u00ED'", "'\\u00EE'", 
                     "'\\u00EF'", "'\\u00F0'", "'\\u00F1'", "'\\u00F2'", 
                     "'\\u00F3'", "'\\u00F4'", "'\\u00F5'", "'\\u00F6'", 
                     "'\\u00F7'", "'\\u00F8'", "'\\u00F9'", "'\\u00FA'", 
                     "'\\u00FB'", "'\\u00FC'", "'\\u00FD'", "'\\u00FE'", 
                     "'\\u00FF'", "'\\uFEFF'" ]

    symbolicNames = [ "<INVALID>", "TAB", "LF", "CR", "SPACE", "EXCLAMATION", 
                      "QUOTE", "POUND", "DOLLAR", "PERCENT", "AMPERSAND", 
                      "APOSTROPHE", "LEFT_PAREN", "RIGHT_PAREN", "ASTERISK", 
                      "PLUS", "COMMA", "DASH", "PERIOD", "SLASH", "ZERO", 
                      "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", 
                      "EIGHT", "NINE", "COLON", "SEMICOLON", "LESS_THAN", 
                      "EQUALS", "GREATER_THAN", "QUESTION", "AT", "CAP_A", 
                      "CAP_B", "CAP_C", "CAP_D", "CAP_E", "CAP_F", "CAP_G", 
                      "CAP_H", "CAP_I", "CAP_J", "CAP_K", "CAP_L", "CAP_M", 
                      "CAP_N", "CAP_O", "CAP_P", "CAP_Q", "CAP_R", "CAP_S", 
                      "CAP_T", "CAP_U", "CAP_V", "CAP_W", "CAP_X", "CAP_Y", 
                      "CAP_Z", "LEFT_BRACE", "BACKSLASH", "RIGHT_BRACE", 
                      "CARAT", "UNDERSCORE", "ACCENT", "A", "B", "C", "D", 
                      "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
                      "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                      "Y", "Z", "LEFT_CURLY_BRACE", "PIPE", "RIGHT_CURLY_BRACE", 
                      "TILDE", "U_0000", "U_0001", "U_0002", "U_0003", "U_0004", 
                      "U_0005", "U_0006", "U_0007", "U_0008", "U_000B", 
                      "U_000C", "U_000E", "U_000F", "U_0010", "U_0011", 
                      "U_0012", "U_0013", "U_0014", "U_0015", "U_0016", 
                      "U_0017", "U_0018", "U_0019", "U_001A", "U_001B", 
                      "U_001C", "U_001D", "U_001E", "U_001F", "U_007F", 
                      "U_0080", "U_0081", "U_0082", "U_0083", "U_0084", 
                      "U_0085", "U_0086", "U_0087", "U_0088", "U_0089", 
                      "U_008A", "U_008B", "U_008C", "U_008D", "U_008E", 
                      "U_008F", "U_0090", "U_0091", "U_0092", "U_0093", 
                      "U_0094", "U_0095", "U_0096", "U_0097", "U_0098", 
                      "U_0099", "U_009A", "U_009B", "U_009C", "U_009D", 
                      "U_009E", "U_009F", "U_00A0", "U_00A1", "U_00A2", 
                      "U_00A3", "U_00A4", "U_00A5", "U_00A6", "U_00A7", 
                      "U_00A8", "U_00A9", "U_00AA", "U_00AB", "U_00AC", 
                      "U_00AD", "U_00AE", "U_00AF", "U_00B0", "U_00B1", 
                      "U_00B2", "U_00B3", "U_00B4", "U_00B5", "U_00B6", 
                      "U_00B7", "U_00B8", "U_00B9", "U_00BA", "U_00BB", 
                      "U_00BC", "U_00BD", "U_00BE", "U_00BF", "U_00C0", 
                      "U_00C1", "U_00C2", "U_00C3", "U_00C4", "U_00C5", 
                      "U_00C6", "U_00C7", "U_00C8", "U_00C9", "U_00CA", 
                      "U_00CB", "U_00CC", "U_00CD", "U_00CE", "U_00CF", 
                      "U_00D0", "U_00D1", "U_00D2", "U_00D3", "U_00D4", 
                      "U_00D5", "U_00D6", "U_00D7", "U_00D8", "U_00D9", 
                      "U_00DA", "U_00DB", "U_00DC", "U_00DD", "U_00DE", 
                      "U_00DF", "U_00E0", "U_00E1", "U_00E2", "U_00E3", 
                      "U_00E4", "U_00E5", "U_00E6", "U_00E7", "U_00E8", 
                      "U_00E9", "U_00EA", "U_00EB", "U_00EC", "U_00ED", 
                      "U_00EE", "U_00EF", "U_00F0", "U_00F1", "U_00F2", 
                      "U_00F3", "U_00F4", "U_00F5", "U_00F6", "U_00F7", 
                      "U_00F8", "U_00F9", "U_00FA", "U_00FB", "U_00FC", 
                      "U_00FD", "U_00FE", "U_00FF", "U_FEFF", "WS" ]

    RULE_heroku_https_log_drain = 0
    RULE_octet_prefixed = 1
    RULE_syslog_msg = 2
    RULE_octet_prefix = 3
    RULE_header = 4
    RULE_pri = 5
    RULE_prival = 6
    RULE_version = 7
    RULE_hostname = 8
    RULE_app_name = 9
    RULE_procid = 10
    RULE_msgid = 11
    RULE_timestamp = 12
    RULE_full_date = 13
    RULE_date_fullyear = 14
    RULE_date_month = 15
    RULE_date_mday = 16
    RULE_full_time = 17
    RULE_partial_time = 18
    RULE_time_hour = 19
    RULE_time_minute = 20
    RULE_time_second = 21
    RULE_time_secfrac = 22
    RULE_time_offset = 23
    RULE_time_numoffset = 24
    RULE_structured_data = 25
    RULE_sd_element = 26
    RULE_sd_param = 27
    RULE_sd_id = 28
    RULE_param_name = 29
    RULE_param_value = 30
    RULE_sd_name = 31
    RULE_msg = 32
    RULE_msg_utf8 = 33
    RULE_bom = 34
    RULE_utf_8_string = 35
    RULE_octet = 36
    RULE_sp = 37
    RULE_printusascii = 38
    RULE_printusasciinospecials = 39
    RULE_nonzero_digit = 40
    RULE_digit = 41
    RULE_nilvalue = 42

    ruleNames =  [ "heroku_https_log_drain", "octet_prefixed", "syslog_msg", 
                   "octet_prefix", "header", "pri", "prival", "version", 
                   "hostname", "app_name", "procid", "msgid", "timestamp", 
                   "full_date", "date_fullyear", "date_month", "date_mday", 
                   "full_time", "partial_time", "time_hour", "time_minute", 
                   "time_second", "time_secfrac", "time_offset", "time_numoffset", 
                   "structured_data", "sd_element", "sd_param", "sd_id", 
                   "param_name", "param_value", "sd_name", "msg", "msg_utf8", 
                   "bom", "utf_8_string", "octet", "sp", "printusascii", 
                   "printusasciinospecials", "nonzero_digit", "digit", "nilvalue" ]

    EOF = Token.EOF
    TAB=1
    LF=2
    CR=3
    SPACE=4
    EXCLAMATION=5
    QUOTE=6
    POUND=7
    DOLLAR=8
    PERCENT=9
    AMPERSAND=10
    APOSTROPHE=11
    LEFT_PAREN=12
    RIGHT_PAREN=13
    ASTERISK=14
    PLUS=15
    COMMA=16
    DASH=17
    PERIOD=18
    SLASH=19
    ZERO=20
    ONE=21
    TWO=22
    THREE=23
    FOUR=24
    FIVE=25
    SIX=26
    SEVEN=27
    EIGHT=28
    NINE=29
    COLON=30
    SEMICOLON=31
    LESS_THAN=32
    EQUALS=33
    GREATER_THAN=34
    QUESTION=35
    AT=36
    CAP_A=37
    CAP_B=38
    CAP_C=39
    CAP_D=40
    CAP_E=41
    CAP_F=42
    CAP_G=43
    CAP_H=44
    CAP_I=45
    CAP_J=46
    CAP_K=47
    CAP_L=48
    CAP_M=49
    CAP_N=50
    CAP_O=51
    CAP_P=52
    CAP_Q=53
    CAP_R=54
    CAP_S=55
    CAP_T=56
    CAP_U=57
    CAP_V=58
    CAP_W=59
    CAP_X=60
    CAP_Y=61
    CAP_Z=62
    LEFT_BRACE=63
    BACKSLASH=64
    RIGHT_BRACE=65
    CARAT=66
    UNDERSCORE=67
    ACCENT=68
    A=69
    B=70
    C=71
    D=72
    E=73
    F=74
    G=75
    H=76
    I=77
    J=78
    K=79
    L=80
    M=81
    N=82
    O=83
    P=84
    Q=85
    R=86
    S=87
    T=88
    U=89
    V=90
    W=91
    X=92
    Y=93
    Z=94
    LEFT_CURLY_BRACE=95
    PIPE=96
    RIGHT_CURLY_BRACE=97
    TILDE=98
    U_0000=99
    U_0001=100
    U_0002=101
    U_0003=102
    U_0004=103
    U_0005=104
    U_0006=105
    U_0007=106
    U_0008=107
    U_000B=108
    U_000C=109
    U_000E=110
    U_000F=111
    U_0010=112
    U_0011=113
    U_0012=114
    U_0013=115
    U_0014=116
    U_0015=117
    U_0016=118
    U_0017=119
    U_0018=120
    U_0019=121
    U_001A=122
    U_001B=123
    U_001C=124
    U_001D=125
    U_001E=126
    U_001F=127
    U_007F=128
    U_0080=129
    U_0081=130
    U_0082=131
    U_0083=132
    U_0084=133
    U_0085=134
    U_0086=135
    U_0087=136
    U_0088=137
    U_0089=138
    U_008A=139
    U_008B=140
    U_008C=141
    U_008D=142
    U_008E=143
    U_008F=144
    U_0090=145
    U_0091=146
    U_0092=147
    U_0093=148
    U_0094=149
    U_0095=150
    U_0096=151
    U_0097=152
    U_0098=153
    U_0099=154
    U_009A=155
    U_009B=156
    U_009C=157
    U_009D=158
    U_009E=159
    U_009F=160
    U_00A0=161
    U_00A1=162
    U_00A2=163
    U_00A3=164
    U_00A4=165
    U_00A5=166
    U_00A6=167
    U_00A7=168
    U_00A8=169
    U_00A9=170
    U_00AA=171
    U_00AB=172
    U_00AC=173
    U_00AD=174
    U_00AE=175
    U_00AF=176
    U_00B0=177
    U_00B1=178
    U_00B2=179
    U_00B3=180
    U_00B4=181
    U_00B5=182
    U_00B6=183
    U_00B7=184
    U_00B8=185
    U_00B9=186
    U_00BA=187
    U_00BB=188
    U_00BC=189
    U_00BD=190
    U_00BE=191
    U_00BF=192
    U_00C0=193
    U_00C1=194
    U_00C2=195
    U_00C3=196
    U_00C4=197
    U_00C5=198
    U_00C6=199
    U_00C7=200
    U_00C8=201
    U_00C9=202
    U_00CA=203
    U_00CB=204
    U_00CC=205
    U_00CD=206
    U_00CE=207
    U_00CF=208
    U_00D0=209
    U_00D1=210
    U_00D2=211
    U_00D3=212
    U_00D4=213
    U_00D5=214
    U_00D6=215
    U_00D7=216
    U_00D8=217
    U_00D9=218
    U_00DA=219
    U_00DB=220
    U_00DC=221
    U_00DD=222
    U_00DE=223
    U_00DF=224
    U_00E0=225
    U_00E1=226
    U_00E2=227
    U_00E3=228
    U_00E4=229
    U_00E5=230
    U_00E6=231
    U_00E7=232
    U_00E8=233
    U_00E9=234
    U_00EA=235
    U_00EB=236
    U_00EC=237
    U_00ED=238
    U_00EE=239
    U_00EF=240
    U_00F0=241
    U_00F1=242
    U_00F2=243
    U_00F3=244
    U_00F4=245
    U_00F5=246
    U_00F6=247
    U_00F7=248
    U_00F8=249
    U_00F9=250
    U_00FA=251
    U_00FB=252
    U_00FC=253
    U_00FD=254
    U_00FE=255
    U_00FF=256
    U_FEFF=257
    WS=258

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Heroku_https_log_drainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_heroku_https_log_drain

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HerokuHttpsMsgContext(Heroku_https_log_drainContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.Heroku_https_log_drainContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def octet_prefix(self):
            return self.getTypedRuleContext(Rfc5424Parser.Octet_prefixContext,0)

        def sp(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.SpContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.SpContext,i)

        def header(self):
            return self.getTypedRuleContext(Rfc5424Parser.HeaderContext,0)

        def msg(self):
            return self.getTypedRuleContext(Rfc5424Parser.MsgContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHerokuHttpsMsg" ):
                listener.enterHerokuHttpsMsg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHerokuHttpsMsg" ):
                listener.exitHerokuHttpsMsg(self)



    def heroku_https_log_drain(self):

        localctx = Rfc5424Parser.Heroku_https_log_drainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_heroku_https_log_drain)
        try:
            localctx = Rfc5424Parser.HerokuHttpsMsgContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.octet_prefix()
            self.state = 87
            self.sp()
            self.state = 88
            self.header()
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 89
                self.sp()


            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 92
                self.msg()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Octet_prefixedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def octet_prefix(self):
            return self.getTypedRuleContext(Rfc5424Parser.Octet_prefixContext,0)


        def sp(self):
            return self.getTypedRuleContext(Rfc5424Parser.SpContext,0)


        def syslog_msg(self):
            return self.getTypedRuleContext(Rfc5424Parser.Syslog_msgContext,0)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_octet_prefixed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOctet_prefixed" ):
                listener.enterOctet_prefixed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOctet_prefixed" ):
                listener.exitOctet_prefixed(self)




    def octet_prefixed(self):

        localctx = Rfc5424Parser.Octet_prefixedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_octet_prefixed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.octet_prefix()
            self.state = 96
            self.sp()
            self.state = 97
            self.syslog_msg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Syslog_msgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_syslog_msg

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SyslogMsgContext(Syslog_msgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.Syslog_msgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def header(self):
            return self.getTypedRuleContext(Rfc5424Parser.HeaderContext,0)

        def sp(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.SpContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.SpContext,i)

        def structured_data(self):
            return self.getTypedRuleContext(Rfc5424Parser.Structured_dataContext,0)

        def bom(self):
            return self.getTypedRuleContext(Rfc5424Parser.BomContext,0)

        def msg(self):
            return self.getTypedRuleContext(Rfc5424Parser.MsgContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSyslogMsg" ):
                listener.enterSyslogMsg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSyslogMsg" ):
                listener.exitSyslogMsg(self)



    def syslog_msg(self):

        localctx = Rfc5424Parser.Syslog_msgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_syslog_msg)
        try:
            localctx = Rfc5424Parser.SyslogMsgContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.header()
            self.state = 100
            self.sp()
            self.state = 101
            self.structured_data()
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 102
                self.sp()


            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 105
                self.bom()


            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 108
                self.msg()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Octet_prefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonzero_digit(self):
            return self.getTypedRuleContext(Rfc5424Parser.Nonzero_digitContext,0)


        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_octet_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOctet_prefix" ):
                listener.enterOctet_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOctet_prefix" ):
                listener.exitOctet_prefix(self)




    def octet_prefix(self):

        localctx = Rfc5424Parser.Octet_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_octet_prefix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.nonzero_digit()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE))) != 0):
                self.state = 112
                self.digit()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_header

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SyslogHeaderContext(HeaderContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.HeaderContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def timestamp(self):
            return self.getTypedRuleContext(Rfc5424Parser.TimestampContext,0)

        def sp(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.SpContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.SpContext,i)

        def hostname(self):
            return self.getTypedRuleContext(Rfc5424Parser.HostnameContext,0)

        def app_name(self):
            return self.getTypedRuleContext(Rfc5424Parser.App_nameContext,0)

        def procid(self):
            return self.getTypedRuleContext(Rfc5424Parser.ProcidContext,0)

        def msgid(self):
            return self.getTypedRuleContext(Rfc5424Parser.MsgidContext,0)

        def pri(self):
            return self.getTypedRuleContext(Rfc5424Parser.PriContext,0)

        def version(self):
            return self.getTypedRuleContext(Rfc5424Parser.VersionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSyslogHeader" ):
                listener.enterSyslogHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSyslogHeader" ):
                listener.exitSyslogHeader(self)



    def header(self):

        localctx = Rfc5424Parser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_header)
        self._la = 0 # Token type
        try:
            localctx = Rfc5424Parser.SyslogHeaderContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Rfc5424Parser.LESS_THAN:
                self.state = 118
                self.pri()


            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 121
                self.version()


            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Rfc5424Parser.SPACE:
                self.state = 124
                self.sp()


            self.state = 127
            self.timestamp()
            self.state = 128
            self.sp()
            self.state = 129
            self.hostname()
            self.state = 130
            self.sp()
            self.state = 131
            self.app_name()
            self.state = 132
            self.sp()
            self.state = 133
            self.procid()
            self.state = 134
            self.sp()
            self.state = 135
            self.msgid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PriContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_pri

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderPriorityContext(PriContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.PriContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LESS_THAN(self):
            return self.getToken(Rfc5424Parser.LESS_THAN, 0)
        def prival(self):
            return self.getTypedRuleContext(Rfc5424Parser.PrivalContext,0)

        def GREATER_THAN(self):
            return self.getToken(Rfc5424Parser.GREATER_THAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderPriority" ):
                listener.enterHeaderPriority(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderPriority" ):
                listener.exitHeaderPriority(self)



    def pri(self):

        localctx = Rfc5424Parser.PriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pri)
        try:
            localctx = Rfc5424Parser.HeaderPriorityContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(Rfc5424Parser.LESS_THAN)
            self.state = 138
            self.prival()
            self.state = 139
            self.match(Rfc5424Parser.GREATER_THAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrivalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_prival

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderPriorityValueContext(PrivalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.PrivalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderPriorityValue" ):
                listener.enterHeaderPriorityValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderPriorityValue" ):
                listener.exitHeaderPriorityValue(self)



    def prival(self):

        localctx = Rfc5424Parser.PrivalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_prival)
        self._la = 0 # Token type
        try:
            localctx = Rfc5424Parser.HeaderPriorityValueContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.digit()
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE))) != 0):
                    self.state = 142
                    self.digit()


                pass

            elif la_ == 2:
                self.state = 145
                self.digit()
                self.state = 146
                self.digit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VersionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_version

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderVersionContext(VersionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.VersionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nonzero_digit(self):
            return self.getTypedRuleContext(Rfc5424Parser.Nonzero_digitContext,0)

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderVersion" ):
                listener.enterHeaderVersion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderVersion" ):
                listener.exitHeaderVersion(self)



    def version(self):

        localctx = Rfc5424Parser.VersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_version)
        try:
            localctx = Rfc5424Parser.HeaderVersionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.nonzero_digit()
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 152
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 151
                    self.digit()


                pass

            elif la_ == 2:
                self.state = 154
                self.digit()
                self.state = 155
                self.digit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HostnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_hostname

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderHostNameContext(HostnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.HostnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printusascii(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.PrintusasciiContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.PrintusasciiContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderHostName" ):
                listener.enterHeaderHostName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderHostName" ):
                listener.exitHeaderHostName(self)


    class HeaderNilHostNameContext(HostnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.HostnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nilvalue(self):
            return self.getTypedRuleContext(Rfc5424Parser.NilvalueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderNilHostName" ):
                listener.enterHeaderNilHostName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderNilHostName" ):
                listener.exitHeaderNilHostName(self)



    def hostname(self):

        localctx = Rfc5424Parser.HostnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_hostname)
        self._la = 0 # Token type
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = Rfc5424Parser.HeaderNilHostNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.nilvalue()
                pass

            elif la_ == 2:
                localctx = Rfc5424Parser.HeaderHostNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.EXCLAMATION) | (1 << Rfc5424Parser.QUOTE) | (1 << Rfc5424Parser.POUND) | (1 << Rfc5424Parser.DOLLAR) | (1 << Rfc5424Parser.PERCENT) | (1 << Rfc5424Parser.AMPERSAND) | (1 << Rfc5424Parser.APOSTROPHE) | (1 << Rfc5424Parser.LEFT_PAREN) | (1 << Rfc5424Parser.RIGHT_PAREN) | (1 << Rfc5424Parser.ASTERISK) | (1 << Rfc5424Parser.PLUS) | (1 << Rfc5424Parser.COMMA) | (1 << Rfc5424Parser.DASH) | (1 << Rfc5424Parser.PERIOD) | (1 << Rfc5424Parser.SLASH) | (1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE) | (1 << Rfc5424Parser.COLON) | (1 << Rfc5424Parser.SEMICOLON) | (1 << Rfc5424Parser.LESS_THAN) | (1 << Rfc5424Parser.EQUALS) | (1 << Rfc5424Parser.GREATER_THAN) | (1 << Rfc5424Parser.QUESTION) | (1 << Rfc5424Parser.AT) | (1 << Rfc5424Parser.CAP_A) | (1 << Rfc5424Parser.CAP_B) | (1 << Rfc5424Parser.CAP_C) | (1 << Rfc5424Parser.CAP_D) | (1 << Rfc5424Parser.CAP_E) | (1 << Rfc5424Parser.CAP_F) | (1 << Rfc5424Parser.CAP_G) | (1 << Rfc5424Parser.CAP_H) | (1 << Rfc5424Parser.CAP_I) | (1 << Rfc5424Parser.CAP_J) | (1 << Rfc5424Parser.CAP_K) | (1 << Rfc5424Parser.CAP_L) | (1 << Rfc5424Parser.CAP_M) | (1 << Rfc5424Parser.CAP_N) | (1 << Rfc5424Parser.CAP_O) | (1 << Rfc5424Parser.CAP_P) | (1 << Rfc5424Parser.CAP_Q) | (1 << Rfc5424Parser.CAP_R) | (1 << Rfc5424Parser.CAP_S) | (1 << Rfc5424Parser.CAP_T) | (1 << Rfc5424Parser.CAP_U) | (1 << Rfc5424Parser.CAP_V) | (1 << Rfc5424Parser.CAP_W) | (1 << Rfc5424Parser.CAP_X) | (1 << Rfc5424Parser.CAP_Y) | (1 << Rfc5424Parser.CAP_Z) | (1 << Rfc5424Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc5424Parser.BACKSLASH - 64)) | (1 << (Rfc5424Parser.RIGHT_BRACE - 64)) | (1 << (Rfc5424Parser.CARAT - 64)) | (1 << (Rfc5424Parser.UNDERSCORE - 64)) | (1 << (Rfc5424Parser.ACCENT - 64)) | (1 << (Rfc5424Parser.A - 64)) | (1 << (Rfc5424Parser.B - 64)) | (1 << (Rfc5424Parser.C - 64)) | (1 << (Rfc5424Parser.D - 64)) | (1 << (Rfc5424Parser.E - 64)) | (1 << (Rfc5424Parser.F - 64)) | (1 << (Rfc5424Parser.G - 64)) | (1 << (Rfc5424Parser.H - 64)) | (1 << (Rfc5424Parser.I - 64)) | (1 << (Rfc5424Parser.J - 64)) | (1 << (Rfc5424Parser.K - 64)) | (1 << (Rfc5424Parser.L - 64)) | (1 << (Rfc5424Parser.M - 64)) | (1 << (Rfc5424Parser.N - 64)) | (1 << (Rfc5424Parser.O - 64)) | (1 << (Rfc5424Parser.P - 64)) | (1 << (Rfc5424Parser.Q - 64)) | (1 << (Rfc5424Parser.R - 64)) | (1 << (Rfc5424Parser.S - 64)) | (1 << (Rfc5424Parser.T - 64)) | (1 << (Rfc5424Parser.U - 64)) | (1 << (Rfc5424Parser.V - 64)) | (1 << (Rfc5424Parser.W - 64)) | (1 << (Rfc5424Parser.X - 64)) | (1 << (Rfc5424Parser.Y - 64)) | (1 << (Rfc5424Parser.Z - 64)) | (1 << (Rfc5424Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.PIPE - 64)) | (1 << (Rfc5424Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.TILDE - 64)))) != 0):
                    self.state = 160
                    self.printusascii()
                    self.state = 165
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class App_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_app_name

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderNilAppNameContext(App_nameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.App_nameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nilvalue(self):
            return self.getTypedRuleContext(Rfc5424Parser.NilvalueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderNilAppName" ):
                listener.enterHeaderNilAppName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderNilAppName" ):
                listener.exitHeaderNilAppName(self)


    class HeaderAppNameContext(App_nameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.App_nameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printusascii(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.PrintusasciiContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.PrintusasciiContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderAppName" ):
                listener.enterHeaderAppName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderAppName" ):
                listener.exitHeaderAppName(self)



    def app_name(self):

        localctx = Rfc5424Parser.App_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_app_name)
        self._la = 0 # Token type
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = Rfc5424Parser.HeaderNilAppNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.nilvalue()
                pass

            elif la_ == 2:
                localctx = Rfc5424Parser.HeaderAppNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.EXCLAMATION) | (1 << Rfc5424Parser.QUOTE) | (1 << Rfc5424Parser.POUND) | (1 << Rfc5424Parser.DOLLAR) | (1 << Rfc5424Parser.PERCENT) | (1 << Rfc5424Parser.AMPERSAND) | (1 << Rfc5424Parser.APOSTROPHE) | (1 << Rfc5424Parser.LEFT_PAREN) | (1 << Rfc5424Parser.RIGHT_PAREN) | (1 << Rfc5424Parser.ASTERISK) | (1 << Rfc5424Parser.PLUS) | (1 << Rfc5424Parser.COMMA) | (1 << Rfc5424Parser.DASH) | (1 << Rfc5424Parser.PERIOD) | (1 << Rfc5424Parser.SLASH) | (1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE) | (1 << Rfc5424Parser.COLON) | (1 << Rfc5424Parser.SEMICOLON) | (1 << Rfc5424Parser.LESS_THAN) | (1 << Rfc5424Parser.EQUALS) | (1 << Rfc5424Parser.GREATER_THAN) | (1 << Rfc5424Parser.QUESTION) | (1 << Rfc5424Parser.AT) | (1 << Rfc5424Parser.CAP_A) | (1 << Rfc5424Parser.CAP_B) | (1 << Rfc5424Parser.CAP_C) | (1 << Rfc5424Parser.CAP_D) | (1 << Rfc5424Parser.CAP_E) | (1 << Rfc5424Parser.CAP_F) | (1 << Rfc5424Parser.CAP_G) | (1 << Rfc5424Parser.CAP_H) | (1 << Rfc5424Parser.CAP_I) | (1 << Rfc5424Parser.CAP_J) | (1 << Rfc5424Parser.CAP_K) | (1 << Rfc5424Parser.CAP_L) | (1 << Rfc5424Parser.CAP_M) | (1 << Rfc5424Parser.CAP_N) | (1 << Rfc5424Parser.CAP_O) | (1 << Rfc5424Parser.CAP_P) | (1 << Rfc5424Parser.CAP_Q) | (1 << Rfc5424Parser.CAP_R) | (1 << Rfc5424Parser.CAP_S) | (1 << Rfc5424Parser.CAP_T) | (1 << Rfc5424Parser.CAP_U) | (1 << Rfc5424Parser.CAP_V) | (1 << Rfc5424Parser.CAP_W) | (1 << Rfc5424Parser.CAP_X) | (1 << Rfc5424Parser.CAP_Y) | (1 << Rfc5424Parser.CAP_Z) | (1 << Rfc5424Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc5424Parser.BACKSLASH - 64)) | (1 << (Rfc5424Parser.RIGHT_BRACE - 64)) | (1 << (Rfc5424Parser.CARAT - 64)) | (1 << (Rfc5424Parser.UNDERSCORE - 64)) | (1 << (Rfc5424Parser.ACCENT - 64)) | (1 << (Rfc5424Parser.A - 64)) | (1 << (Rfc5424Parser.B - 64)) | (1 << (Rfc5424Parser.C - 64)) | (1 << (Rfc5424Parser.D - 64)) | (1 << (Rfc5424Parser.E - 64)) | (1 << (Rfc5424Parser.F - 64)) | (1 << (Rfc5424Parser.G - 64)) | (1 << (Rfc5424Parser.H - 64)) | (1 << (Rfc5424Parser.I - 64)) | (1 << (Rfc5424Parser.J - 64)) | (1 << (Rfc5424Parser.K - 64)) | (1 << (Rfc5424Parser.L - 64)) | (1 << (Rfc5424Parser.M - 64)) | (1 << (Rfc5424Parser.N - 64)) | (1 << (Rfc5424Parser.O - 64)) | (1 << (Rfc5424Parser.P - 64)) | (1 << (Rfc5424Parser.Q - 64)) | (1 << (Rfc5424Parser.R - 64)) | (1 << (Rfc5424Parser.S - 64)) | (1 << (Rfc5424Parser.T - 64)) | (1 << (Rfc5424Parser.U - 64)) | (1 << (Rfc5424Parser.V - 64)) | (1 << (Rfc5424Parser.W - 64)) | (1 << (Rfc5424Parser.X - 64)) | (1 << (Rfc5424Parser.Y - 64)) | (1 << (Rfc5424Parser.Z - 64)) | (1 << (Rfc5424Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.PIPE - 64)) | (1 << (Rfc5424Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.TILDE - 64)))) != 0):
                    self.state = 169
                    self.printusascii()
                    self.state = 174
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_procid

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderNilProcIdContext(ProcidContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.ProcidContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nilvalue(self):
            return self.getTypedRuleContext(Rfc5424Parser.NilvalueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderNilProcId" ):
                listener.enterHeaderNilProcId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderNilProcId" ):
                listener.exitHeaderNilProcId(self)


    class HeaderProcIdContext(ProcidContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.ProcidContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printusascii(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.PrintusasciiContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.PrintusasciiContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderProcId" ):
                listener.enterHeaderProcId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderProcId" ):
                listener.exitHeaderProcId(self)



    def procid(self):

        localctx = Rfc5424Parser.ProcidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_procid)
        self._la = 0 # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = Rfc5424Parser.HeaderNilProcIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.nilvalue()
                pass

            elif la_ == 2:
                localctx = Rfc5424Parser.HeaderProcIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.EXCLAMATION) | (1 << Rfc5424Parser.QUOTE) | (1 << Rfc5424Parser.POUND) | (1 << Rfc5424Parser.DOLLAR) | (1 << Rfc5424Parser.PERCENT) | (1 << Rfc5424Parser.AMPERSAND) | (1 << Rfc5424Parser.APOSTROPHE) | (1 << Rfc5424Parser.LEFT_PAREN) | (1 << Rfc5424Parser.RIGHT_PAREN) | (1 << Rfc5424Parser.ASTERISK) | (1 << Rfc5424Parser.PLUS) | (1 << Rfc5424Parser.COMMA) | (1 << Rfc5424Parser.DASH) | (1 << Rfc5424Parser.PERIOD) | (1 << Rfc5424Parser.SLASH) | (1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE) | (1 << Rfc5424Parser.COLON) | (1 << Rfc5424Parser.SEMICOLON) | (1 << Rfc5424Parser.LESS_THAN) | (1 << Rfc5424Parser.EQUALS) | (1 << Rfc5424Parser.GREATER_THAN) | (1 << Rfc5424Parser.QUESTION) | (1 << Rfc5424Parser.AT) | (1 << Rfc5424Parser.CAP_A) | (1 << Rfc5424Parser.CAP_B) | (1 << Rfc5424Parser.CAP_C) | (1 << Rfc5424Parser.CAP_D) | (1 << Rfc5424Parser.CAP_E) | (1 << Rfc5424Parser.CAP_F) | (1 << Rfc5424Parser.CAP_G) | (1 << Rfc5424Parser.CAP_H) | (1 << Rfc5424Parser.CAP_I) | (1 << Rfc5424Parser.CAP_J) | (1 << Rfc5424Parser.CAP_K) | (1 << Rfc5424Parser.CAP_L) | (1 << Rfc5424Parser.CAP_M) | (1 << Rfc5424Parser.CAP_N) | (1 << Rfc5424Parser.CAP_O) | (1 << Rfc5424Parser.CAP_P) | (1 << Rfc5424Parser.CAP_Q) | (1 << Rfc5424Parser.CAP_R) | (1 << Rfc5424Parser.CAP_S) | (1 << Rfc5424Parser.CAP_T) | (1 << Rfc5424Parser.CAP_U) | (1 << Rfc5424Parser.CAP_V) | (1 << Rfc5424Parser.CAP_W) | (1 << Rfc5424Parser.CAP_X) | (1 << Rfc5424Parser.CAP_Y) | (1 << Rfc5424Parser.CAP_Z) | (1 << Rfc5424Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc5424Parser.BACKSLASH - 64)) | (1 << (Rfc5424Parser.RIGHT_BRACE - 64)) | (1 << (Rfc5424Parser.CARAT - 64)) | (1 << (Rfc5424Parser.UNDERSCORE - 64)) | (1 << (Rfc5424Parser.ACCENT - 64)) | (1 << (Rfc5424Parser.A - 64)) | (1 << (Rfc5424Parser.B - 64)) | (1 << (Rfc5424Parser.C - 64)) | (1 << (Rfc5424Parser.D - 64)) | (1 << (Rfc5424Parser.E - 64)) | (1 << (Rfc5424Parser.F - 64)) | (1 << (Rfc5424Parser.G - 64)) | (1 << (Rfc5424Parser.H - 64)) | (1 << (Rfc5424Parser.I - 64)) | (1 << (Rfc5424Parser.J - 64)) | (1 << (Rfc5424Parser.K - 64)) | (1 << (Rfc5424Parser.L - 64)) | (1 << (Rfc5424Parser.M - 64)) | (1 << (Rfc5424Parser.N - 64)) | (1 << (Rfc5424Parser.O - 64)) | (1 << (Rfc5424Parser.P - 64)) | (1 << (Rfc5424Parser.Q - 64)) | (1 << (Rfc5424Parser.R - 64)) | (1 << (Rfc5424Parser.S - 64)) | (1 << (Rfc5424Parser.T - 64)) | (1 << (Rfc5424Parser.U - 64)) | (1 << (Rfc5424Parser.V - 64)) | (1 << (Rfc5424Parser.W - 64)) | (1 << (Rfc5424Parser.X - 64)) | (1 << (Rfc5424Parser.Y - 64)) | (1 << (Rfc5424Parser.Z - 64)) | (1 << (Rfc5424Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.PIPE - 64)) | (1 << (Rfc5424Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.TILDE - 64)))) != 0):
                    self.state = 178
                    self.printusascii()
                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MsgidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_msgid

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderNilMsgIdContext(MsgidContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.MsgidContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nilvalue(self):
            return self.getTypedRuleContext(Rfc5424Parser.NilvalueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderNilMsgId" ):
                listener.enterHeaderNilMsgId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderNilMsgId" ):
                listener.exitHeaderNilMsgId(self)


    class HeaderMsgIdContext(MsgidContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.MsgidContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printusascii(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.PrintusasciiContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.PrintusasciiContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderMsgId" ):
                listener.enterHeaderMsgId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderMsgId" ):
                listener.exitHeaderMsgId(self)



    def msgid(self):

        localctx = Rfc5424Parser.MsgidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_msgid)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = Rfc5424Parser.HeaderNilMsgIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.nilvalue()
                pass

            elif la_ == 2:
                localctx = Rfc5424Parser.HeaderMsgIdContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 187
                        self.printusascii() 
                    self.state = 192
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimestampContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_timestamp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderNilTimestampContext(TimestampContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.TimestampContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nilvalue(self):
            return self.getTypedRuleContext(Rfc5424Parser.NilvalueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderNilTimestamp" ):
                listener.enterHeaderNilTimestamp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderNilTimestamp" ):
                listener.exitHeaderNilTimestamp(self)


    class HeaderTimeStampContext(TimestampContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.TimestampContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def full_date(self):
            return self.getTypedRuleContext(Rfc5424Parser.Full_dateContext,0)

        def CAP_T(self):
            return self.getToken(Rfc5424Parser.CAP_T, 0)
        def full_time(self):
            return self.getTypedRuleContext(Rfc5424Parser.Full_timeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderTimeStamp" ):
                listener.enterHeaderTimeStamp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderTimeStamp" ):
                listener.exitHeaderTimeStamp(self)



    def timestamp(self):

        localctx = Rfc5424Parser.TimestampContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_timestamp)
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Rfc5424Parser.DASH]:
                localctx = Rfc5424Parser.HeaderNilTimestampContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.nilvalue()
                pass
            elif token in [Rfc5424Parser.ZERO, Rfc5424Parser.ONE, Rfc5424Parser.TWO, Rfc5424Parser.THREE, Rfc5424Parser.FOUR, Rfc5424Parser.FIVE, Rfc5424Parser.SIX, Rfc5424Parser.SEVEN, Rfc5424Parser.EIGHT, Rfc5424Parser.NINE]:
                localctx = Rfc5424Parser.HeaderTimeStampContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.full_date()
                self.state = 197
                self.match(Rfc5424Parser.CAP_T)
                self.state = 198
                self.full_time()
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


    class Full_dateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def date_fullyear(self):
            return self.getTypedRuleContext(Rfc5424Parser.Date_fullyearContext,0)


        def DASH(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc5424Parser.DASH)
            else:
                return self.getToken(Rfc5424Parser.DASH, i)

        def date_month(self):
            return self.getTypedRuleContext(Rfc5424Parser.Date_monthContext,0)


        def date_mday(self):
            return self.getTypedRuleContext(Rfc5424Parser.Date_mdayContext,0)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_full_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFull_date" ):
                listener.enterFull_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFull_date" ):
                listener.exitFull_date(self)




    def full_date(self):

        localctx = Rfc5424Parser.Full_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_full_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.date_fullyear()
            self.state = 203
            self.match(Rfc5424Parser.DASH)
            self.state = 204
            self.date_month()
            self.state = 205
            self.match(Rfc5424Parser.DASH)
            self.state = 206
            self.date_mday()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Date_fullyearContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_date_fullyear

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate_fullyear" ):
                listener.enterDate_fullyear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate_fullyear" ):
                listener.exitDate_fullyear(self)




    def date_fullyear(self):

        localctx = Rfc5424Parser.Date_fullyearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_date_fullyear)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.digit()
            self.state = 209
            self.digit()
            self.state = 210
            self.digit()
            self.state = 211
            self.digit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Date_monthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_date_month

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate_month" ):
                listener.enterDate_month(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate_month" ):
                listener.exitDate_month(self)




    def date_month(self):

        localctx = Rfc5424Parser.Date_monthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_date_month)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.digit()
            self.state = 214
            self.digit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Date_mdayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_date_mday

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate_mday" ):
                listener.enterDate_mday(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate_mday" ):
                listener.exitDate_mday(self)




    def date_mday(self):

        localctx = Rfc5424Parser.Date_mdayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_date_mday)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.digit()
            self.state = 217
            self.digit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Full_timeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def partial_time(self):
            return self.getTypedRuleContext(Rfc5424Parser.Partial_timeContext,0)


        def time_offset(self):
            return self.getTypedRuleContext(Rfc5424Parser.Time_offsetContext,0)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_full_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFull_time" ):
                listener.enterFull_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFull_time" ):
                listener.exitFull_time(self)




    def full_time(self):

        localctx = Rfc5424Parser.Full_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_full_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.partial_time()
            self.state = 220
            self.time_offset()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Partial_timeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def time_hour(self):
            return self.getTypedRuleContext(Rfc5424Parser.Time_hourContext,0)


        def COLON(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc5424Parser.COLON)
            else:
                return self.getToken(Rfc5424Parser.COLON, i)

        def time_minute(self):
            return self.getTypedRuleContext(Rfc5424Parser.Time_minuteContext,0)


        def time_second(self):
            return self.getTypedRuleContext(Rfc5424Parser.Time_secondContext,0)


        def time_secfrac(self):
            return self.getTypedRuleContext(Rfc5424Parser.Time_secfracContext,0)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_partial_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartial_time" ):
                listener.enterPartial_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartial_time" ):
                listener.exitPartial_time(self)




    def partial_time(self):

        localctx = Rfc5424Parser.Partial_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_partial_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.time_hour()
            self.state = 223
            self.match(Rfc5424Parser.COLON)
            self.state = 224
            self.time_minute()
            self.state = 225
            self.match(Rfc5424Parser.COLON)
            self.state = 226
            self.time_second()
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Rfc5424Parser.PERIOD:
                self.state = 227
                self.time_secfrac()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Time_hourContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_time_hour

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_hour" ):
                listener.enterTime_hour(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_hour" ):
                listener.exitTime_hour(self)




    def time_hour(self):

        localctx = Rfc5424Parser.Time_hourContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_time_hour)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.digit()
            self.state = 231
            self.digit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Time_minuteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_time_minute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_minute" ):
                listener.enterTime_minute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_minute" ):
                listener.exitTime_minute(self)




    def time_minute(self):

        localctx = Rfc5424Parser.Time_minuteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_time_minute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.digit()
            self.state = 234
            self.digit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Time_secondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_time_second

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_second" ):
                listener.enterTime_second(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_second" ):
                listener.exitTime_second(self)




    def time_second(self):

        localctx = Rfc5424Parser.Time_secondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_time_second)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.digit()
            self.state = 237
            self.digit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Time_secfracContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERIOD(self):
            return self.getToken(Rfc5424Parser.PERIOD, 0)

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_time_secfrac

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_secfrac" ):
                listener.enterTime_secfrac(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_secfrac" ):
                listener.exitTime_secfrac(self)




    def time_secfrac(self):

        localctx = Rfc5424Parser.Time_secfracContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_time_secfrac)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(Rfc5424Parser.PERIOD)
            self.state = 240
            self.digit()
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE))) != 0):
                    self.state = 241
                    self.digit()


                pass

            elif la_ == 2:
                self.state = 244
                self.digit()
                self.state = 245
                self.digit()
                pass

            elif la_ == 3:
                self.state = 247
                self.digit()
                self.state = 248
                self.digit()
                self.state = 249
                self.digit()
                pass

            elif la_ == 4:
                self.state = 251
                self.digit()
                self.state = 252
                self.digit()
                self.state = 253
                self.digit()
                self.state = 254
                self.digit()
                pass

            elif la_ == 5:
                self.state = 256
                self.digit()
                self.state = 257
                self.digit()
                self.state = 258
                self.digit()
                self.state = 259
                self.digit()
                self.state = 260
                self.digit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Time_offsetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAP_Z(self):
            return self.getToken(Rfc5424Parser.CAP_Z, 0)

        def time_numoffset(self):
            return self.getTypedRuleContext(Rfc5424Parser.Time_numoffsetContext,0)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_time_offset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_offset" ):
                listener.enterTime_offset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_offset" ):
                listener.exitTime_offset(self)




    def time_offset(self):

        localctx = Rfc5424Parser.Time_offsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_time_offset)
        try:
            self.state = 266
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Rfc5424Parser.CAP_Z]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(Rfc5424Parser.CAP_Z)
                pass
            elif token in [Rfc5424Parser.PLUS, Rfc5424Parser.DASH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.time_numoffset()
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


    class Time_numoffsetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def time_hour(self):
            return self.getTypedRuleContext(Rfc5424Parser.Time_hourContext,0)


        def COLON(self):
            return self.getToken(Rfc5424Parser.COLON, 0)

        def time_minute(self):
            return self.getTypedRuleContext(Rfc5424Parser.Time_minuteContext,0)


        def PLUS(self):
            return self.getToken(Rfc5424Parser.PLUS, 0)

        def DASH(self):
            return self.getToken(Rfc5424Parser.DASH, 0)

        def getRuleIndex(self):
            return Rfc5424Parser.RULE_time_numoffset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_numoffset" ):
                listener.enterTime_numoffset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_numoffset" ):
                listener.exitTime_numoffset(self)




    def time_numoffset(self):

        localctx = Rfc5424Parser.Time_numoffsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_time_numoffset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not(_la==Rfc5424Parser.PLUS or _la==Rfc5424Parser.DASH):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 269
            self.time_hour()
            self.state = 270
            self.match(Rfc5424Parser.COLON)
            self.state = 271
            self.time_minute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Structured_dataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nilvalue(self):
            return self.getTypedRuleContext(Rfc5424Parser.NilvalueContext,0)


        def LEFT_BRACE(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc5424Parser.LEFT_BRACE)
            else:
                return self.getToken(Rfc5424Parser.LEFT_BRACE, i)

        def sd_element(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.Sd_elementContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.Sd_elementContext,i)


        def RIGHT_BRACE(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc5424Parser.RIGHT_BRACE)
            else:
                return self.getToken(Rfc5424Parser.RIGHT_BRACE, i)

        def getRuleIndex(self):
            return Rfc5424Parser.RULE_structured_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructured_data" ):
                listener.enterStructured_data(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructured_data" ):
                listener.exitStructured_data(self)




    def structured_data(self):

        localctx = Rfc5424Parser.Structured_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_structured_data)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Rfc5424Parser.DASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.nilvalue()
                pass
            elif token in [Rfc5424Parser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.match(Rfc5424Parser.LEFT_BRACE)
                self.state = 275
                self.sd_element()
                self.state = 276
                self.match(Rfc5424Parser.RIGHT_BRACE)
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 277
                        self.match(Rfc5424Parser.LEFT_BRACE)
                        self.state = 278
                        self.sd_element()
                        self.state = 279
                        self.match(Rfc5424Parser.RIGHT_BRACE) 
                    self.state = 285
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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


    class Sd_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_sd_element

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SdElementContext(Sd_elementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.Sd_elementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sd_id(self):
            return self.getTypedRuleContext(Rfc5424Parser.Sd_idContext,0)

        def sp(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.SpContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.SpContext,i)

        def sd_param(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.Sd_paramContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.Sd_paramContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSdElement" ):
                listener.enterSdElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSdElement" ):
                listener.exitSdElement(self)



    def sd_element(self):

        localctx = Rfc5424Parser.Sd_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_sd_element)
        self._la = 0 # Token type
        try:
            localctx = Rfc5424Parser.SdElementContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.sd_id()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Rfc5424Parser.SPACE:
                self.state = 289
                self.sp()
                self.state = 290
                self.sd_param()
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sd_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_sd_param

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SdParamContext(Sd_paramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.Sd_paramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def param_name(self):
            return self.getTypedRuleContext(Rfc5424Parser.Param_nameContext,0)

        def EQUALS(self):
            return self.getToken(Rfc5424Parser.EQUALS, 0)
        def QUOTE(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc5424Parser.QUOTE)
            else:
                return self.getToken(Rfc5424Parser.QUOTE, i)
        def param_value(self):
            return self.getTypedRuleContext(Rfc5424Parser.Param_valueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSdParam" ):
                listener.enterSdParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSdParam" ):
                listener.exitSdParam(self)



    def sd_param(self):

        localctx = Rfc5424Parser.Sd_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_sd_param)
        try:
            localctx = Rfc5424Parser.SdParamContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.param_name()
            self.state = 298
            self.match(Rfc5424Parser.EQUALS)
            self.state = 299
            self.match(Rfc5424Parser.QUOTE)
            self.state = 300
            self.param_value()
            self.state = 301
            self.match(Rfc5424Parser.QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sd_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sd_name(self):
            return self.getTypedRuleContext(Rfc5424Parser.Sd_nameContext,0)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_sd_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSd_id" ):
                listener.enterSd_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSd_id" ):
                listener.exitSd_id(self)




    def sd_id(self):

        localctx = Rfc5424Parser.Sd_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_sd_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.sd_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_param_name

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParamNameContext(Param_nameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.Param_nameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sd_name(self):
            return self.getTypedRuleContext(Rfc5424Parser.Sd_nameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamName" ):
                listener.enterParamName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamName" ):
                listener.exitParamName(self)



    def param_name(self):

        localctx = Rfc5424Parser.Param_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_param_name)
        try:
            localctx = Rfc5424Parser.ParamNameContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.sd_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_param_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParamValueContext(Param_valueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.Param_valueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BACKSLASH(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc5424Parser.BACKSLASH)
            else:
                return self.getToken(Rfc5424Parser.BACKSLASH, i)
        def QUOTE(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc5424Parser.QUOTE)
            else:
                return self.getToken(Rfc5424Parser.QUOTE, i)
        def RIGHT_BRACE(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc5424Parser.RIGHT_BRACE)
            else:
                return self.getToken(Rfc5424Parser.RIGHT_BRACE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamValue" ):
                listener.enterParamValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamValue" ):
                listener.exitParamValue(self)



    def param_value(self):

        localctx = Rfc5424Parser.Param_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_param_value)
        self._la = 0 # Token type
        try:
            localctx = Rfc5424Parser.ParamValueContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.TAB) | (1 << Rfc5424Parser.LF) | (1 << Rfc5424Parser.CR) | (1 << Rfc5424Parser.SPACE) | (1 << Rfc5424Parser.EXCLAMATION) | (1 << Rfc5424Parser.POUND) | (1 << Rfc5424Parser.DOLLAR) | (1 << Rfc5424Parser.PERCENT) | (1 << Rfc5424Parser.AMPERSAND) | (1 << Rfc5424Parser.APOSTROPHE) | (1 << Rfc5424Parser.LEFT_PAREN) | (1 << Rfc5424Parser.RIGHT_PAREN) | (1 << Rfc5424Parser.ASTERISK) | (1 << Rfc5424Parser.PLUS) | (1 << Rfc5424Parser.COMMA) | (1 << Rfc5424Parser.DASH) | (1 << Rfc5424Parser.PERIOD) | (1 << Rfc5424Parser.SLASH) | (1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE) | (1 << Rfc5424Parser.COLON) | (1 << Rfc5424Parser.SEMICOLON) | (1 << Rfc5424Parser.LESS_THAN) | (1 << Rfc5424Parser.EQUALS) | (1 << Rfc5424Parser.GREATER_THAN) | (1 << Rfc5424Parser.QUESTION) | (1 << Rfc5424Parser.AT) | (1 << Rfc5424Parser.CAP_A) | (1 << Rfc5424Parser.CAP_B) | (1 << Rfc5424Parser.CAP_C) | (1 << Rfc5424Parser.CAP_D) | (1 << Rfc5424Parser.CAP_E) | (1 << Rfc5424Parser.CAP_F) | (1 << Rfc5424Parser.CAP_G) | (1 << Rfc5424Parser.CAP_H) | (1 << Rfc5424Parser.CAP_I) | (1 << Rfc5424Parser.CAP_J) | (1 << Rfc5424Parser.CAP_K) | (1 << Rfc5424Parser.CAP_L) | (1 << Rfc5424Parser.CAP_M) | (1 << Rfc5424Parser.CAP_N) | (1 << Rfc5424Parser.CAP_O) | (1 << Rfc5424Parser.CAP_P) | (1 << Rfc5424Parser.CAP_Q) | (1 << Rfc5424Parser.CAP_R) | (1 << Rfc5424Parser.CAP_S) | (1 << Rfc5424Parser.CAP_T) | (1 << Rfc5424Parser.CAP_U) | (1 << Rfc5424Parser.CAP_V) | (1 << Rfc5424Parser.CAP_W) | (1 << Rfc5424Parser.CAP_X) | (1 << Rfc5424Parser.CAP_Y) | (1 << Rfc5424Parser.CAP_Z) | (1 << Rfc5424Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc5424Parser.BACKSLASH - 64)) | (1 << (Rfc5424Parser.CARAT - 64)) | (1 << (Rfc5424Parser.UNDERSCORE - 64)) | (1 << (Rfc5424Parser.ACCENT - 64)) | (1 << (Rfc5424Parser.A - 64)) | (1 << (Rfc5424Parser.B - 64)) | (1 << (Rfc5424Parser.C - 64)) | (1 << (Rfc5424Parser.D - 64)) | (1 << (Rfc5424Parser.E - 64)) | (1 << (Rfc5424Parser.F - 64)) | (1 << (Rfc5424Parser.G - 64)) | (1 << (Rfc5424Parser.H - 64)) | (1 << (Rfc5424Parser.I - 64)) | (1 << (Rfc5424Parser.J - 64)) | (1 << (Rfc5424Parser.K - 64)) | (1 << (Rfc5424Parser.L - 64)) | (1 << (Rfc5424Parser.M - 64)) | (1 << (Rfc5424Parser.N - 64)) | (1 << (Rfc5424Parser.O - 64)) | (1 << (Rfc5424Parser.P - 64)) | (1 << (Rfc5424Parser.Q - 64)) | (1 << (Rfc5424Parser.R - 64)) | (1 << (Rfc5424Parser.S - 64)) | (1 << (Rfc5424Parser.T - 64)) | (1 << (Rfc5424Parser.U - 64)) | (1 << (Rfc5424Parser.V - 64)) | (1 << (Rfc5424Parser.W - 64)) | (1 << (Rfc5424Parser.X - 64)) | (1 << (Rfc5424Parser.Y - 64)) | (1 << (Rfc5424Parser.Z - 64)) | (1 << (Rfc5424Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.PIPE - 64)) | (1 << (Rfc5424Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.TILDE - 64)) | (1 << (Rfc5424Parser.U_0000 - 64)) | (1 << (Rfc5424Parser.U_0001 - 64)) | (1 << (Rfc5424Parser.U_0002 - 64)) | (1 << (Rfc5424Parser.U_0003 - 64)) | (1 << (Rfc5424Parser.U_0004 - 64)) | (1 << (Rfc5424Parser.U_0005 - 64)) | (1 << (Rfc5424Parser.U_0006 - 64)) | (1 << (Rfc5424Parser.U_0007 - 64)) | (1 << (Rfc5424Parser.U_0008 - 64)) | (1 << (Rfc5424Parser.U_000B - 64)) | (1 << (Rfc5424Parser.U_000C - 64)) | (1 << (Rfc5424Parser.U_000E - 64)) | (1 << (Rfc5424Parser.U_000F - 64)) | (1 << (Rfc5424Parser.U_0010 - 64)) | (1 << (Rfc5424Parser.U_0011 - 64)) | (1 << (Rfc5424Parser.U_0012 - 64)) | (1 << (Rfc5424Parser.U_0013 - 64)) | (1 << (Rfc5424Parser.U_0014 - 64)) | (1 << (Rfc5424Parser.U_0015 - 64)) | (1 << (Rfc5424Parser.U_0016 - 64)) | (1 << (Rfc5424Parser.U_0017 - 64)) | (1 << (Rfc5424Parser.U_0018 - 64)) | (1 << (Rfc5424Parser.U_0019 - 64)) | (1 << (Rfc5424Parser.U_001A - 64)) | (1 << (Rfc5424Parser.U_001B - 64)) | (1 << (Rfc5424Parser.U_001C - 64)) | (1 << (Rfc5424Parser.U_001D - 64)) | (1 << (Rfc5424Parser.U_001E - 64)) | (1 << (Rfc5424Parser.U_001F - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (Rfc5424Parser.U_007F - 128)) | (1 << (Rfc5424Parser.U_0080 - 128)) | (1 << (Rfc5424Parser.U_0081 - 128)) | (1 << (Rfc5424Parser.U_0082 - 128)) | (1 << (Rfc5424Parser.U_0083 - 128)) | (1 << (Rfc5424Parser.U_0084 - 128)) | (1 << (Rfc5424Parser.U_0085 - 128)) | (1 << (Rfc5424Parser.U_0086 - 128)) | (1 << (Rfc5424Parser.U_0087 - 128)) | (1 << (Rfc5424Parser.U_0088 - 128)) | (1 << (Rfc5424Parser.U_0089 - 128)) | (1 << (Rfc5424Parser.U_008A - 128)) | (1 << (Rfc5424Parser.U_008B - 128)) | (1 << (Rfc5424Parser.U_008C - 128)) | (1 << (Rfc5424Parser.U_008D - 128)) | (1 << (Rfc5424Parser.U_008E - 128)) | (1 << (Rfc5424Parser.U_008F - 128)) | (1 << (Rfc5424Parser.U_0090 - 128)) | (1 << (Rfc5424Parser.U_0091 - 128)) | (1 << (Rfc5424Parser.U_0092 - 128)) | (1 << (Rfc5424Parser.U_0093 - 128)) | (1 << (Rfc5424Parser.U_0094 - 128)) | (1 << (Rfc5424Parser.U_0095 - 128)) | (1 << (Rfc5424Parser.U_0096 - 128)) | (1 << (Rfc5424Parser.U_0097 - 128)) | (1 << (Rfc5424Parser.U_0098 - 128)) | (1 << (Rfc5424Parser.U_0099 - 128)) | (1 << (Rfc5424Parser.U_009A - 128)) | (1 << (Rfc5424Parser.U_009B - 128)) | (1 << (Rfc5424Parser.U_009C - 128)) | (1 << (Rfc5424Parser.U_009D - 128)) | (1 << (Rfc5424Parser.U_009E - 128)) | (1 << (Rfc5424Parser.U_009F - 128)) | (1 << (Rfc5424Parser.U_00A0 - 128)) | (1 << (Rfc5424Parser.U_00A1 - 128)) | (1 << (Rfc5424Parser.U_00A2 - 128)) | (1 << (Rfc5424Parser.U_00A3 - 128)) | (1 << (Rfc5424Parser.U_00A4 - 128)) | (1 << (Rfc5424Parser.U_00A5 - 128)) | (1 << (Rfc5424Parser.U_00A6 - 128)) | (1 << (Rfc5424Parser.U_00A7 - 128)) | (1 << (Rfc5424Parser.U_00A8 - 128)) | (1 << (Rfc5424Parser.U_00A9 - 128)) | (1 << (Rfc5424Parser.U_00AA - 128)) | (1 << (Rfc5424Parser.U_00AB - 128)) | (1 << (Rfc5424Parser.U_00AC - 128)) | (1 << (Rfc5424Parser.U_00AD - 128)) | (1 << (Rfc5424Parser.U_00AE - 128)) | (1 << (Rfc5424Parser.U_00AF - 128)) | (1 << (Rfc5424Parser.U_00B0 - 128)) | (1 << (Rfc5424Parser.U_00B1 - 128)) | (1 << (Rfc5424Parser.U_00B2 - 128)) | (1 << (Rfc5424Parser.U_00B3 - 128)) | (1 << (Rfc5424Parser.U_00B4 - 128)) | (1 << (Rfc5424Parser.U_00B5 - 128)) | (1 << (Rfc5424Parser.U_00B6 - 128)) | (1 << (Rfc5424Parser.U_00B7 - 128)) | (1 << (Rfc5424Parser.U_00B8 - 128)) | (1 << (Rfc5424Parser.U_00B9 - 128)) | (1 << (Rfc5424Parser.U_00BA - 128)) | (1 << (Rfc5424Parser.U_00BB - 128)) | (1 << (Rfc5424Parser.U_00BC - 128)) | (1 << (Rfc5424Parser.U_00BD - 128)) | (1 << (Rfc5424Parser.U_00BE - 128)))) != 0) or ((((_la - 192)) & ~0x3f) == 0 and ((1 << (_la - 192)) & ((1 << (Rfc5424Parser.U_00BF - 192)) | (1 << (Rfc5424Parser.U_00C0 - 192)) | (1 << (Rfc5424Parser.U_00C1 - 192)) | (1 << (Rfc5424Parser.U_00C2 - 192)) | (1 << (Rfc5424Parser.U_00C3 - 192)) | (1 << (Rfc5424Parser.U_00C4 - 192)) | (1 << (Rfc5424Parser.U_00C5 - 192)) | (1 << (Rfc5424Parser.U_00C6 - 192)) | (1 << (Rfc5424Parser.U_00C7 - 192)) | (1 << (Rfc5424Parser.U_00C8 - 192)) | (1 << (Rfc5424Parser.U_00C9 - 192)) | (1 << (Rfc5424Parser.U_00CA - 192)) | (1 << (Rfc5424Parser.U_00CB - 192)) | (1 << (Rfc5424Parser.U_00CC - 192)) | (1 << (Rfc5424Parser.U_00CD - 192)) | (1 << (Rfc5424Parser.U_00CE - 192)) | (1 << (Rfc5424Parser.U_00CF - 192)) | (1 << (Rfc5424Parser.U_00D0 - 192)) | (1 << (Rfc5424Parser.U_00D1 - 192)) | (1 << (Rfc5424Parser.U_00D2 - 192)) | (1 << (Rfc5424Parser.U_00D3 - 192)) | (1 << (Rfc5424Parser.U_00D4 - 192)) | (1 << (Rfc5424Parser.U_00D5 - 192)) | (1 << (Rfc5424Parser.U_00D6 - 192)) | (1 << (Rfc5424Parser.U_00D7 - 192)) | (1 << (Rfc5424Parser.U_00D8 - 192)) | (1 << (Rfc5424Parser.U_00D9 - 192)) | (1 << (Rfc5424Parser.U_00DA - 192)) | (1 << (Rfc5424Parser.U_00DB - 192)) | (1 << (Rfc5424Parser.U_00DC - 192)) | (1 << (Rfc5424Parser.U_00DD - 192)) | (1 << (Rfc5424Parser.U_00DE - 192)) | (1 << (Rfc5424Parser.U_00DF - 192)) | (1 << (Rfc5424Parser.U_00E0 - 192)) | (1 << (Rfc5424Parser.U_00E1 - 192)) | (1 << (Rfc5424Parser.U_00E2 - 192)) | (1 << (Rfc5424Parser.U_00E3 - 192)) | (1 << (Rfc5424Parser.U_00E4 - 192)) | (1 << (Rfc5424Parser.U_00E5 - 192)) | (1 << (Rfc5424Parser.U_00E6 - 192)) | (1 << (Rfc5424Parser.U_00E7 - 192)) | (1 << (Rfc5424Parser.U_00E8 - 192)) | (1 << (Rfc5424Parser.U_00E9 - 192)) | (1 << (Rfc5424Parser.U_00EA - 192)) | (1 << (Rfc5424Parser.U_00EB - 192)) | (1 << (Rfc5424Parser.U_00EC - 192)) | (1 << (Rfc5424Parser.U_00ED - 192)) | (1 << (Rfc5424Parser.U_00EE - 192)) | (1 << (Rfc5424Parser.U_00EF - 192)) | (1 << (Rfc5424Parser.U_00F0 - 192)) | (1 << (Rfc5424Parser.U_00F1 - 192)) | (1 << (Rfc5424Parser.U_00F2 - 192)) | (1 << (Rfc5424Parser.U_00F3 - 192)) | (1 << (Rfc5424Parser.U_00F4 - 192)) | (1 << (Rfc5424Parser.U_00F5 - 192)) | (1 << (Rfc5424Parser.U_00F6 - 192)) | (1 << (Rfc5424Parser.U_00F7 - 192)) | (1 << (Rfc5424Parser.U_00F8 - 192)) | (1 << (Rfc5424Parser.U_00F9 - 192)) | (1 << (Rfc5424Parser.U_00FA - 192)) | (1 << (Rfc5424Parser.U_00FB - 192)) | (1 << (Rfc5424Parser.U_00FC - 192)) | (1 << (Rfc5424Parser.U_00FD - 192)) | (1 << (Rfc5424Parser.U_00FE - 192)))) != 0) or ((((_la - 256)) & ~0x3f) == 0 and ((1 << (_la - 256)) & ((1 << (Rfc5424Parser.U_00FF - 256)) | (1 << (Rfc5424Parser.U_FEFF - 256)) | (1 << (Rfc5424Parser.WS - 256)))) != 0):
                self.state = 310
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [Rfc5424Parser.TAB, Rfc5424Parser.LF, Rfc5424Parser.CR, Rfc5424Parser.SPACE, Rfc5424Parser.EXCLAMATION, Rfc5424Parser.POUND, Rfc5424Parser.DOLLAR, Rfc5424Parser.PERCENT, Rfc5424Parser.AMPERSAND, Rfc5424Parser.APOSTROPHE, Rfc5424Parser.LEFT_PAREN, Rfc5424Parser.RIGHT_PAREN, Rfc5424Parser.ASTERISK, Rfc5424Parser.PLUS, Rfc5424Parser.COMMA, Rfc5424Parser.DASH, Rfc5424Parser.PERIOD, Rfc5424Parser.SLASH, Rfc5424Parser.ZERO, Rfc5424Parser.ONE, Rfc5424Parser.TWO, Rfc5424Parser.THREE, Rfc5424Parser.FOUR, Rfc5424Parser.FIVE, Rfc5424Parser.SIX, Rfc5424Parser.SEVEN, Rfc5424Parser.EIGHT, Rfc5424Parser.NINE, Rfc5424Parser.COLON, Rfc5424Parser.SEMICOLON, Rfc5424Parser.LESS_THAN, Rfc5424Parser.EQUALS, Rfc5424Parser.GREATER_THAN, Rfc5424Parser.QUESTION, Rfc5424Parser.AT, Rfc5424Parser.CAP_A, Rfc5424Parser.CAP_B, Rfc5424Parser.CAP_C, Rfc5424Parser.CAP_D, Rfc5424Parser.CAP_E, Rfc5424Parser.CAP_F, Rfc5424Parser.CAP_G, Rfc5424Parser.CAP_H, Rfc5424Parser.CAP_I, Rfc5424Parser.CAP_J, Rfc5424Parser.CAP_K, Rfc5424Parser.CAP_L, Rfc5424Parser.CAP_M, Rfc5424Parser.CAP_N, Rfc5424Parser.CAP_O, Rfc5424Parser.CAP_P, Rfc5424Parser.CAP_Q, Rfc5424Parser.CAP_R, Rfc5424Parser.CAP_S, Rfc5424Parser.CAP_T, Rfc5424Parser.CAP_U, Rfc5424Parser.CAP_V, Rfc5424Parser.CAP_W, Rfc5424Parser.CAP_X, Rfc5424Parser.CAP_Y, Rfc5424Parser.CAP_Z, Rfc5424Parser.LEFT_BRACE, Rfc5424Parser.CARAT, Rfc5424Parser.UNDERSCORE, Rfc5424Parser.ACCENT, Rfc5424Parser.A, Rfc5424Parser.B, Rfc5424Parser.C, Rfc5424Parser.D, Rfc5424Parser.E, Rfc5424Parser.F, Rfc5424Parser.G, Rfc5424Parser.H, Rfc5424Parser.I, Rfc5424Parser.J, Rfc5424Parser.K, Rfc5424Parser.L, Rfc5424Parser.M, Rfc5424Parser.N, Rfc5424Parser.O, Rfc5424Parser.P, Rfc5424Parser.Q, Rfc5424Parser.R, Rfc5424Parser.S, Rfc5424Parser.T, Rfc5424Parser.U, Rfc5424Parser.V, Rfc5424Parser.W, Rfc5424Parser.X, Rfc5424Parser.Y, Rfc5424Parser.Z, Rfc5424Parser.LEFT_CURLY_BRACE, Rfc5424Parser.PIPE, Rfc5424Parser.RIGHT_CURLY_BRACE, Rfc5424Parser.TILDE, Rfc5424Parser.U_0000, Rfc5424Parser.U_0001, Rfc5424Parser.U_0002, Rfc5424Parser.U_0003, Rfc5424Parser.U_0004, Rfc5424Parser.U_0005, Rfc5424Parser.U_0006, Rfc5424Parser.U_0007, Rfc5424Parser.U_0008, Rfc5424Parser.U_000B, Rfc5424Parser.U_000C, Rfc5424Parser.U_000E, Rfc5424Parser.U_000F, Rfc5424Parser.U_0010, Rfc5424Parser.U_0011, Rfc5424Parser.U_0012, Rfc5424Parser.U_0013, Rfc5424Parser.U_0014, Rfc5424Parser.U_0015, Rfc5424Parser.U_0016, Rfc5424Parser.U_0017, Rfc5424Parser.U_0018, Rfc5424Parser.U_0019, Rfc5424Parser.U_001A, Rfc5424Parser.U_001B, Rfc5424Parser.U_001C, Rfc5424Parser.U_001D, Rfc5424Parser.U_001E, Rfc5424Parser.U_001F, Rfc5424Parser.U_007F, Rfc5424Parser.U_0080, Rfc5424Parser.U_0081, Rfc5424Parser.U_0082, Rfc5424Parser.U_0083, Rfc5424Parser.U_0084, Rfc5424Parser.U_0085, Rfc5424Parser.U_0086, Rfc5424Parser.U_0087, Rfc5424Parser.U_0088, Rfc5424Parser.U_0089, Rfc5424Parser.U_008A, Rfc5424Parser.U_008B, Rfc5424Parser.U_008C, Rfc5424Parser.U_008D, Rfc5424Parser.U_008E, Rfc5424Parser.U_008F, Rfc5424Parser.U_0090, Rfc5424Parser.U_0091, Rfc5424Parser.U_0092, Rfc5424Parser.U_0093, Rfc5424Parser.U_0094, Rfc5424Parser.U_0095, Rfc5424Parser.U_0096, Rfc5424Parser.U_0097, Rfc5424Parser.U_0098, Rfc5424Parser.U_0099, Rfc5424Parser.U_009A, Rfc5424Parser.U_009B, Rfc5424Parser.U_009C, Rfc5424Parser.U_009D, Rfc5424Parser.U_009E, Rfc5424Parser.U_009F, Rfc5424Parser.U_00A0, Rfc5424Parser.U_00A1, Rfc5424Parser.U_00A2, Rfc5424Parser.U_00A3, Rfc5424Parser.U_00A4, Rfc5424Parser.U_00A5, Rfc5424Parser.U_00A6, Rfc5424Parser.U_00A7, Rfc5424Parser.U_00A8, Rfc5424Parser.U_00A9, Rfc5424Parser.U_00AA, Rfc5424Parser.U_00AB, Rfc5424Parser.U_00AC, Rfc5424Parser.U_00AD, Rfc5424Parser.U_00AE, Rfc5424Parser.U_00AF, Rfc5424Parser.U_00B0, Rfc5424Parser.U_00B1, Rfc5424Parser.U_00B2, Rfc5424Parser.U_00B3, Rfc5424Parser.U_00B4, Rfc5424Parser.U_00B5, Rfc5424Parser.U_00B6, Rfc5424Parser.U_00B7, Rfc5424Parser.U_00B8, Rfc5424Parser.U_00B9, Rfc5424Parser.U_00BA, Rfc5424Parser.U_00BB, Rfc5424Parser.U_00BC, Rfc5424Parser.U_00BD, Rfc5424Parser.U_00BE, Rfc5424Parser.U_00BF, Rfc5424Parser.U_00C0, Rfc5424Parser.U_00C1, Rfc5424Parser.U_00C2, Rfc5424Parser.U_00C3, Rfc5424Parser.U_00C4, Rfc5424Parser.U_00C5, Rfc5424Parser.U_00C6, Rfc5424Parser.U_00C7, Rfc5424Parser.U_00C8, Rfc5424Parser.U_00C9, Rfc5424Parser.U_00CA, Rfc5424Parser.U_00CB, Rfc5424Parser.U_00CC, Rfc5424Parser.U_00CD, Rfc5424Parser.U_00CE, Rfc5424Parser.U_00CF, Rfc5424Parser.U_00D0, Rfc5424Parser.U_00D1, Rfc5424Parser.U_00D2, Rfc5424Parser.U_00D3, Rfc5424Parser.U_00D4, Rfc5424Parser.U_00D5, Rfc5424Parser.U_00D6, Rfc5424Parser.U_00D7, Rfc5424Parser.U_00D8, Rfc5424Parser.U_00D9, Rfc5424Parser.U_00DA, Rfc5424Parser.U_00DB, Rfc5424Parser.U_00DC, Rfc5424Parser.U_00DD, Rfc5424Parser.U_00DE, Rfc5424Parser.U_00DF, Rfc5424Parser.U_00E0, Rfc5424Parser.U_00E1, Rfc5424Parser.U_00E2, Rfc5424Parser.U_00E3, Rfc5424Parser.U_00E4, Rfc5424Parser.U_00E5, Rfc5424Parser.U_00E6, Rfc5424Parser.U_00E7, Rfc5424Parser.U_00E8, Rfc5424Parser.U_00E9, Rfc5424Parser.U_00EA, Rfc5424Parser.U_00EB, Rfc5424Parser.U_00EC, Rfc5424Parser.U_00ED, Rfc5424Parser.U_00EE, Rfc5424Parser.U_00EF, Rfc5424Parser.U_00F0, Rfc5424Parser.U_00F1, Rfc5424Parser.U_00F2, Rfc5424Parser.U_00F3, Rfc5424Parser.U_00F4, Rfc5424Parser.U_00F5, Rfc5424Parser.U_00F6, Rfc5424Parser.U_00F7, Rfc5424Parser.U_00F8, Rfc5424Parser.U_00F9, Rfc5424Parser.U_00FA, Rfc5424Parser.U_00FB, Rfc5424Parser.U_00FC, Rfc5424Parser.U_00FD, Rfc5424Parser.U_00FE, Rfc5424Parser.U_00FF, Rfc5424Parser.U_FEFF, Rfc5424Parser.WS]:
                    self.state = 307
                    _la = self._input.LA(1)
                    if _la <= 0 or ((((_la - 6)) & ~0x3f) == 0 and ((1 << (_la - 6)) & ((1 << (Rfc5424Parser.QUOTE - 6)) | (1 << (Rfc5424Parser.BACKSLASH - 6)) | (1 << (Rfc5424Parser.RIGHT_BRACE - 6)))) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                elif token in [Rfc5424Parser.BACKSLASH]:
                    self.state = 308
                    self.match(Rfc5424Parser.BACKSLASH)
                    self.state = 309
                    _la = self._input.LA(1)
                    if not(((((_la - 6)) & ~0x3f) == 0 and ((1 << (_la - 6)) & ((1 << (Rfc5424Parser.QUOTE - 6)) | (1 << (Rfc5424Parser.BACKSLASH - 6)) | (1 << (Rfc5424Parser.RIGHT_BRACE - 6)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sd_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printusasciinospecials(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.PrintusasciinospecialsContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.PrintusasciinospecialsContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_sd_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSd_name" ):
                listener.enterSd_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSd_name" ):
                listener.exitSd_name(self)




    def sd_name(self):

        localctx = Rfc5424Parser.Sd_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_sd_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.EXCLAMATION) | (1 << Rfc5424Parser.POUND) | (1 << Rfc5424Parser.DOLLAR) | (1 << Rfc5424Parser.PERCENT) | (1 << Rfc5424Parser.AMPERSAND) | (1 << Rfc5424Parser.APOSTROPHE) | (1 << Rfc5424Parser.LEFT_PAREN) | (1 << Rfc5424Parser.RIGHT_PAREN) | (1 << Rfc5424Parser.ASTERISK) | (1 << Rfc5424Parser.PLUS) | (1 << Rfc5424Parser.COMMA) | (1 << Rfc5424Parser.DASH) | (1 << Rfc5424Parser.PERIOD) | (1 << Rfc5424Parser.SLASH) | (1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE) | (1 << Rfc5424Parser.COLON) | (1 << Rfc5424Parser.SEMICOLON) | (1 << Rfc5424Parser.LESS_THAN) | (1 << Rfc5424Parser.GREATER_THAN) | (1 << Rfc5424Parser.QUESTION) | (1 << Rfc5424Parser.AT) | (1 << Rfc5424Parser.CAP_A) | (1 << Rfc5424Parser.CAP_B) | (1 << Rfc5424Parser.CAP_C) | (1 << Rfc5424Parser.CAP_D) | (1 << Rfc5424Parser.CAP_E) | (1 << Rfc5424Parser.CAP_F) | (1 << Rfc5424Parser.CAP_G) | (1 << Rfc5424Parser.CAP_H) | (1 << Rfc5424Parser.CAP_I) | (1 << Rfc5424Parser.CAP_J) | (1 << Rfc5424Parser.CAP_K) | (1 << Rfc5424Parser.CAP_L) | (1 << Rfc5424Parser.CAP_M) | (1 << Rfc5424Parser.CAP_N) | (1 << Rfc5424Parser.CAP_O) | (1 << Rfc5424Parser.CAP_P) | (1 << Rfc5424Parser.CAP_Q) | (1 << Rfc5424Parser.CAP_R) | (1 << Rfc5424Parser.CAP_S) | (1 << Rfc5424Parser.CAP_T) | (1 << Rfc5424Parser.CAP_U) | (1 << Rfc5424Parser.CAP_V) | (1 << Rfc5424Parser.CAP_W) | (1 << Rfc5424Parser.CAP_X) | (1 << Rfc5424Parser.CAP_Y) | (1 << Rfc5424Parser.CAP_Z) | (1 << Rfc5424Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc5424Parser.BACKSLASH - 64)) | (1 << (Rfc5424Parser.CARAT - 64)) | (1 << (Rfc5424Parser.UNDERSCORE - 64)) | (1 << (Rfc5424Parser.ACCENT - 64)) | (1 << (Rfc5424Parser.A - 64)) | (1 << (Rfc5424Parser.B - 64)) | (1 << (Rfc5424Parser.C - 64)) | (1 << (Rfc5424Parser.D - 64)) | (1 << (Rfc5424Parser.E - 64)) | (1 << (Rfc5424Parser.F - 64)) | (1 << (Rfc5424Parser.G - 64)) | (1 << (Rfc5424Parser.H - 64)) | (1 << (Rfc5424Parser.I - 64)) | (1 << (Rfc5424Parser.J - 64)) | (1 << (Rfc5424Parser.K - 64)) | (1 << (Rfc5424Parser.L - 64)) | (1 << (Rfc5424Parser.M - 64)) | (1 << (Rfc5424Parser.N - 64)) | (1 << (Rfc5424Parser.O - 64)) | (1 << (Rfc5424Parser.P - 64)) | (1 << (Rfc5424Parser.Q - 64)) | (1 << (Rfc5424Parser.R - 64)) | (1 << (Rfc5424Parser.S - 64)) | (1 << (Rfc5424Parser.T - 64)) | (1 << (Rfc5424Parser.U - 64)) | (1 << (Rfc5424Parser.V - 64)) | (1 << (Rfc5424Parser.W - 64)) | (1 << (Rfc5424Parser.X - 64)) | (1 << (Rfc5424Parser.Y - 64)) | (1 << (Rfc5424Parser.Z - 64)) | (1 << (Rfc5424Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.PIPE - 64)) | (1 << (Rfc5424Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.TILDE - 64)))) != 0):
                self.state = 315
                self.printusasciinospecials()
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MsgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_msg

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MsgUTF8Context(MsgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.MsgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def msg_utf8(self):
            return self.getTypedRuleContext(Rfc5424Parser.Msg_utf8Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMsgUTF8" ):
                listener.enterMsgUTF8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMsgUTF8" ):
                listener.exitMsgUTF8(self)



    def msg(self):

        localctx = Rfc5424Parser.MsgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_msg)
        try:
            localctx = Rfc5424Parser.MsgUTF8Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.msg_utf8()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Msg_utf8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def utf_8_string(self):
            return self.getTypedRuleContext(Rfc5424Parser.Utf_8_stringContext,0)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_msg_utf8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMsg_utf8" ):
                listener.enterMsg_utf8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMsg_utf8" ):
                listener.exitMsg_utf8(self)




    def msg_utf8(self):

        localctx = Rfc5424Parser.Msg_utf8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_msg_utf8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.utf_8_string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def U_00EF(self):
            return self.getToken(Rfc5424Parser.U_00EF, 0)

        def U_00BB(self):
            return self.getToken(Rfc5424Parser.U_00BB, 0)

        def U_00BF(self):
            return self.getToken(Rfc5424Parser.U_00BF, 0)

        def U_FEFF(self):
            return self.getToken(Rfc5424Parser.U_FEFF, 0)

        def getRuleIndex(self):
            return Rfc5424Parser.RULE_bom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBom" ):
                listener.enterBom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBom" ):
                listener.exitBom(self)




    def bom(self):

        localctx = Rfc5424Parser.BomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_bom)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Rfc5424Parser.U_00EF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(Rfc5424Parser.U_00EF)
                self.state = 326
                self.match(Rfc5424Parser.U_00BB)
                self.state = 327
                self.match(Rfc5424Parser.U_00BF)
                pass
            elif token in [Rfc5424Parser.U_FEFF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.match(Rfc5424Parser.U_FEFF)
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


    class Utf_8_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def octet(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc5424Parser.OctetContext)
            else:
                return self.getTypedRuleContext(Rfc5424Parser.OctetContext,i)


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_utf_8_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUtf_8_string" ):
                listener.enterUtf_8_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUtf_8_string" ):
                listener.exitUtf_8_string(self)




    def utf_8_string(self):

        localctx = Rfc5424Parser.Utf_8_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_utf_8_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (Rfc5424Parser.TAB - 1)) | (1 << (Rfc5424Parser.LF - 1)) | (1 << (Rfc5424Parser.CR - 1)) | (1 << (Rfc5424Parser.SPACE - 1)) | (1 << (Rfc5424Parser.EXCLAMATION - 1)) | (1 << (Rfc5424Parser.QUOTE - 1)) | (1 << (Rfc5424Parser.POUND - 1)) | (1 << (Rfc5424Parser.DOLLAR - 1)) | (1 << (Rfc5424Parser.PERCENT - 1)) | (1 << (Rfc5424Parser.AMPERSAND - 1)) | (1 << (Rfc5424Parser.APOSTROPHE - 1)) | (1 << (Rfc5424Parser.LEFT_PAREN - 1)) | (1 << (Rfc5424Parser.RIGHT_PAREN - 1)) | (1 << (Rfc5424Parser.ASTERISK - 1)) | (1 << (Rfc5424Parser.PLUS - 1)) | (1 << (Rfc5424Parser.COMMA - 1)) | (1 << (Rfc5424Parser.DASH - 1)) | (1 << (Rfc5424Parser.PERIOD - 1)) | (1 << (Rfc5424Parser.SLASH - 1)) | (1 << (Rfc5424Parser.ZERO - 1)) | (1 << (Rfc5424Parser.ONE - 1)) | (1 << (Rfc5424Parser.TWO - 1)) | (1 << (Rfc5424Parser.THREE - 1)) | (1 << (Rfc5424Parser.FOUR - 1)) | (1 << (Rfc5424Parser.FIVE - 1)) | (1 << (Rfc5424Parser.SIX - 1)) | (1 << (Rfc5424Parser.SEVEN - 1)) | (1 << (Rfc5424Parser.EIGHT - 1)) | (1 << (Rfc5424Parser.NINE - 1)) | (1 << (Rfc5424Parser.COLON - 1)) | (1 << (Rfc5424Parser.SEMICOLON - 1)) | (1 << (Rfc5424Parser.LESS_THAN - 1)) | (1 << (Rfc5424Parser.EQUALS - 1)) | (1 << (Rfc5424Parser.GREATER_THAN - 1)) | (1 << (Rfc5424Parser.QUESTION - 1)) | (1 << (Rfc5424Parser.AT - 1)) | (1 << (Rfc5424Parser.CAP_A - 1)) | (1 << (Rfc5424Parser.CAP_B - 1)) | (1 << (Rfc5424Parser.CAP_C - 1)) | (1 << (Rfc5424Parser.CAP_D - 1)) | (1 << (Rfc5424Parser.CAP_E - 1)) | (1 << (Rfc5424Parser.CAP_F - 1)) | (1 << (Rfc5424Parser.CAP_G - 1)) | (1 << (Rfc5424Parser.CAP_H - 1)) | (1 << (Rfc5424Parser.CAP_I - 1)) | (1 << (Rfc5424Parser.CAP_J - 1)) | (1 << (Rfc5424Parser.CAP_K - 1)) | (1 << (Rfc5424Parser.CAP_L - 1)) | (1 << (Rfc5424Parser.CAP_M - 1)) | (1 << (Rfc5424Parser.CAP_N - 1)) | (1 << (Rfc5424Parser.CAP_O - 1)) | (1 << (Rfc5424Parser.CAP_P - 1)) | (1 << (Rfc5424Parser.CAP_Q - 1)) | (1 << (Rfc5424Parser.CAP_R - 1)) | (1 << (Rfc5424Parser.CAP_S - 1)) | (1 << (Rfc5424Parser.CAP_T - 1)) | (1 << (Rfc5424Parser.CAP_U - 1)) | (1 << (Rfc5424Parser.CAP_V - 1)) | (1 << (Rfc5424Parser.CAP_W - 1)) | (1 << (Rfc5424Parser.CAP_X - 1)) | (1 << (Rfc5424Parser.CAP_Y - 1)) | (1 << (Rfc5424Parser.CAP_Z - 1)) | (1 << (Rfc5424Parser.LEFT_BRACE - 1)) | (1 << (Rfc5424Parser.BACKSLASH - 1)))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Rfc5424Parser.RIGHT_BRACE - 65)) | (1 << (Rfc5424Parser.CARAT - 65)) | (1 << (Rfc5424Parser.UNDERSCORE - 65)) | (1 << (Rfc5424Parser.ACCENT - 65)) | (1 << (Rfc5424Parser.A - 65)) | (1 << (Rfc5424Parser.B - 65)) | (1 << (Rfc5424Parser.C - 65)) | (1 << (Rfc5424Parser.D - 65)) | (1 << (Rfc5424Parser.E - 65)) | (1 << (Rfc5424Parser.F - 65)) | (1 << (Rfc5424Parser.G - 65)) | (1 << (Rfc5424Parser.H - 65)) | (1 << (Rfc5424Parser.I - 65)) | (1 << (Rfc5424Parser.J - 65)) | (1 << (Rfc5424Parser.K - 65)) | (1 << (Rfc5424Parser.L - 65)) | (1 << (Rfc5424Parser.M - 65)) | (1 << (Rfc5424Parser.N - 65)) | (1 << (Rfc5424Parser.O - 65)) | (1 << (Rfc5424Parser.P - 65)) | (1 << (Rfc5424Parser.Q - 65)) | (1 << (Rfc5424Parser.R - 65)) | (1 << (Rfc5424Parser.S - 65)) | (1 << (Rfc5424Parser.T - 65)) | (1 << (Rfc5424Parser.U - 65)) | (1 << (Rfc5424Parser.V - 65)) | (1 << (Rfc5424Parser.W - 65)) | (1 << (Rfc5424Parser.X - 65)) | (1 << (Rfc5424Parser.Y - 65)) | (1 << (Rfc5424Parser.Z - 65)) | (1 << (Rfc5424Parser.LEFT_CURLY_BRACE - 65)) | (1 << (Rfc5424Parser.PIPE - 65)) | (1 << (Rfc5424Parser.RIGHT_CURLY_BRACE - 65)) | (1 << (Rfc5424Parser.TILDE - 65)) | (1 << (Rfc5424Parser.U_0000 - 65)) | (1 << (Rfc5424Parser.U_0001 - 65)) | (1 << (Rfc5424Parser.U_0002 - 65)) | (1 << (Rfc5424Parser.U_0003 - 65)) | (1 << (Rfc5424Parser.U_0004 - 65)) | (1 << (Rfc5424Parser.U_0005 - 65)) | (1 << (Rfc5424Parser.U_0006 - 65)) | (1 << (Rfc5424Parser.U_0007 - 65)) | (1 << (Rfc5424Parser.U_0008 - 65)) | (1 << (Rfc5424Parser.U_000B - 65)) | (1 << (Rfc5424Parser.U_000C - 65)) | (1 << (Rfc5424Parser.U_000E - 65)) | (1 << (Rfc5424Parser.U_000F - 65)) | (1 << (Rfc5424Parser.U_0010 - 65)) | (1 << (Rfc5424Parser.U_0011 - 65)) | (1 << (Rfc5424Parser.U_0012 - 65)) | (1 << (Rfc5424Parser.U_0013 - 65)) | (1 << (Rfc5424Parser.U_0014 - 65)) | (1 << (Rfc5424Parser.U_0015 - 65)) | (1 << (Rfc5424Parser.U_0016 - 65)) | (1 << (Rfc5424Parser.U_0017 - 65)) | (1 << (Rfc5424Parser.U_0018 - 65)) | (1 << (Rfc5424Parser.U_0019 - 65)) | (1 << (Rfc5424Parser.U_001A - 65)) | (1 << (Rfc5424Parser.U_001B - 65)) | (1 << (Rfc5424Parser.U_001C - 65)) | (1 << (Rfc5424Parser.U_001D - 65)) | (1 << (Rfc5424Parser.U_001E - 65)) | (1 << (Rfc5424Parser.U_001F - 65)) | (1 << (Rfc5424Parser.U_007F - 65)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (Rfc5424Parser.U_0080 - 129)) | (1 << (Rfc5424Parser.U_0081 - 129)) | (1 << (Rfc5424Parser.U_0082 - 129)) | (1 << (Rfc5424Parser.U_0083 - 129)) | (1 << (Rfc5424Parser.U_0084 - 129)) | (1 << (Rfc5424Parser.U_0085 - 129)) | (1 << (Rfc5424Parser.U_0086 - 129)) | (1 << (Rfc5424Parser.U_0087 - 129)) | (1 << (Rfc5424Parser.U_0088 - 129)) | (1 << (Rfc5424Parser.U_0089 - 129)) | (1 << (Rfc5424Parser.U_008A - 129)) | (1 << (Rfc5424Parser.U_008B - 129)) | (1 << (Rfc5424Parser.U_008C - 129)) | (1 << (Rfc5424Parser.U_008D - 129)) | (1 << (Rfc5424Parser.U_008E - 129)) | (1 << (Rfc5424Parser.U_008F - 129)) | (1 << (Rfc5424Parser.U_0090 - 129)) | (1 << (Rfc5424Parser.U_0091 - 129)) | (1 << (Rfc5424Parser.U_0092 - 129)) | (1 << (Rfc5424Parser.U_0093 - 129)) | (1 << (Rfc5424Parser.U_0094 - 129)) | (1 << (Rfc5424Parser.U_0095 - 129)) | (1 << (Rfc5424Parser.U_0096 - 129)) | (1 << (Rfc5424Parser.U_0097 - 129)) | (1 << (Rfc5424Parser.U_0098 - 129)) | (1 << (Rfc5424Parser.U_0099 - 129)) | (1 << (Rfc5424Parser.U_009A - 129)) | (1 << (Rfc5424Parser.U_009B - 129)) | (1 << (Rfc5424Parser.U_009C - 129)) | (1 << (Rfc5424Parser.U_009D - 129)) | (1 << (Rfc5424Parser.U_009E - 129)) | (1 << (Rfc5424Parser.U_009F - 129)) | (1 << (Rfc5424Parser.U_00A0 - 129)) | (1 << (Rfc5424Parser.U_00A1 - 129)) | (1 << (Rfc5424Parser.U_00A2 - 129)) | (1 << (Rfc5424Parser.U_00A3 - 129)) | (1 << (Rfc5424Parser.U_00A4 - 129)) | (1 << (Rfc5424Parser.U_00A5 - 129)) | (1 << (Rfc5424Parser.U_00A6 - 129)) | (1 << (Rfc5424Parser.U_00A7 - 129)) | (1 << (Rfc5424Parser.U_00A8 - 129)) | (1 << (Rfc5424Parser.U_00A9 - 129)) | (1 << (Rfc5424Parser.U_00AA - 129)) | (1 << (Rfc5424Parser.U_00AB - 129)) | (1 << (Rfc5424Parser.U_00AC - 129)) | (1 << (Rfc5424Parser.U_00AD - 129)) | (1 << (Rfc5424Parser.U_00AE - 129)) | (1 << (Rfc5424Parser.U_00AF - 129)) | (1 << (Rfc5424Parser.U_00B0 - 129)) | (1 << (Rfc5424Parser.U_00B1 - 129)) | (1 << (Rfc5424Parser.U_00B2 - 129)) | (1 << (Rfc5424Parser.U_00B3 - 129)) | (1 << (Rfc5424Parser.U_00B4 - 129)) | (1 << (Rfc5424Parser.U_00B5 - 129)) | (1 << (Rfc5424Parser.U_00B6 - 129)) | (1 << (Rfc5424Parser.U_00B7 - 129)) | (1 << (Rfc5424Parser.U_00B8 - 129)) | (1 << (Rfc5424Parser.U_00B9 - 129)) | (1 << (Rfc5424Parser.U_00BA - 129)) | (1 << (Rfc5424Parser.U_00BB - 129)) | (1 << (Rfc5424Parser.U_00BC - 129)) | (1 << (Rfc5424Parser.U_00BD - 129)) | (1 << (Rfc5424Parser.U_00BE - 129)) | (1 << (Rfc5424Parser.U_00BF - 129)))) != 0) or ((((_la - 193)) & ~0x3f) == 0 and ((1 << (_la - 193)) & ((1 << (Rfc5424Parser.U_00C0 - 193)) | (1 << (Rfc5424Parser.U_00C1 - 193)) | (1 << (Rfc5424Parser.U_00C2 - 193)) | (1 << (Rfc5424Parser.U_00C3 - 193)) | (1 << (Rfc5424Parser.U_00C4 - 193)) | (1 << (Rfc5424Parser.U_00C5 - 193)) | (1 << (Rfc5424Parser.U_00C6 - 193)) | (1 << (Rfc5424Parser.U_00C7 - 193)) | (1 << (Rfc5424Parser.U_00C8 - 193)) | (1 << (Rfc5424Parser.U_00C9 - 193)) | (1 << (Rfc5424Parser.U_00CA - 193)) | (1 << (Rfc5424Parser.U_00CB - 193)) | (1 << (Rfc5424Parser.U_00CC - 193)) | (1 << (Rfc5424Parser.U_00CD - 193)) | (1 << (Rfc5424Parser.U_00CE - 193)) | (1 << (Rfc5424Parser.U_00CF - 193)) | (1 << (Rfc5424Parser.U_00D0 - 193)) | (1 << (Rfc5424Parser.U_00D1 - 193)) | (1 << (Rfc5424Parser.U_00D2 - 193)) | (1 << (Rfc5424Parser.U_00D3 - 193)) | (1 << (Rfc5424Parser.U_00D4 - 193)) | (1 << (Rfc5424Parser.U_00D5 - 193)) | (1 << (Rfc5424Parser.U_00D6 - 193)) | (1 << (Rfc5424Parser.U_00D7 - 193)) | (1 << (Rfc5424Parser.U_00D8 - 193)) | (1 << (Rfc5424Parser.U_00D9 - 193)) | (1 << (Rfc5424Parser.U_00DA - 193)) | (1 << (Rfc5424Parser.U_00DB - 193)) | (1 << (Rfc5424Parser.U_00DC - 193)) | (1 << (Rfc5424Parser.U_00DD - 193)) | (1 << (Rfc5424Parser.U_00DE - 193)) | (1 << (Rfc5424Parser.U_00DF - 193)) | (1 << (Rfc5424Parser.U_00E0 - 193)) | (1 << (Rfc5424Parser.U_00E1 - 193)) | (1 << (Rfc5424Parser.U_00E2 - 193)) | (1 << (Rfc5424Parser.U_00E3 - 193)) | (1 << (Rfc5424Parser.U_00E4 - 193)) | (1 << (Rfc5424Parser.U_00E5 - 193)) | (1 << (Rfc5424Parser.U_00E6 - 193)) | (1 << (Rfc5424Parser.U_00E7 - 193)) | (1 << (Rfc5424Parser.U_00E8 - 193)) | (1 << (Rfc5424Parser.U_00E9 - 193)) | (1 << (Rfc5424Parser.U_00EA - 193)) | (1 << (Rfc5424Parser.U_00EB - 193)) | (1 << (Rfc5424Parser.U_00EC - 193)) | (1 << (Rfc5424Parser.U_00ED - 193)) | (1 << (Rfc5424Parser.U_00EE - 193)) | (1 << (Rfc5424Parser.U_00EF - 193)) | (1 << (Rfc5424Parser.U_00F0 - 193)) | (1 << (Rfc5424Parser.U_00F1 - 193)) | (1 << (Rfc5424Parser.U_00F2 - 193)) | (1 << (Rfc5424Parser.U_00F3 - 193)) | (1 << (Rfc5424Parser.U_00F4 - 193)) | (1 << (Rfc5424Parser.U_00F5 - 193)) | (1 << (Rfc5424Parser.U_00F6 - 193)) | (1 << (Rfc5424Parser.U_00F7 - 193)) | (1 << (Rfc5424Parser.U_00F8 - 193)) | (1 << (Rfc5424Parser.U_00F9 - 193)) | (1 << (Rfc5424Parser.U_00FA - 193)) | (1 << (Rfc5424Parser.U_00FB - 193)) | (1 << (Rfc5424Parser.U_00FC - 193)) | (1 << (Rfc5424Parser.U_00FD - 193)) | (1 << (Rfc5424Parser.U_00FE - 193)) | (1 << (Rfc5424Parser.U_00FF - 193)))) != 0):
                self.state = 331
                self.octet()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OctetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def U_0000(self):
            return self.getToken(Rfc5424Parser.U_0000, 0)

        def U_0001(self):
            return self.getToken(Rfc5424Parser.U_0001, 0)

        def U_0002(self):
            return self.getToken(Rfc5424Parser.U_0002, 0)

        def U_0003(self):
            return self.getToken(Rfc5424Parser.U_0003, 0)

        def U_0004(self):
            return self.getToken(Rfc5424Parser.U_0004, 0)

        def U_0005(self):
            return self.getToken(Rfc5424Parser.U_0005, 0)

        def U_0006(self):
            return self.getToken(Rfc5424Parser.U_0006, 0)

        def U_0007(self):
            return self.getToken(Rfc5424Parser.U_0007, 0)

        def U_0008(self):
            return self.getToken(Rfc5424Parser.U_0008, 0)

        def TAB(self):
            return self.getToken(Rfc5424Parser.TAB, 0)

        def LF(self):
            return self.getToken(Rfc5424Parser.LF, 0)

        def U_000B(self):
            return self.getToken(Rfc5424Parser.U_000B, 0)

        def U_000C(self):
            return self.getToken(Rfc5424Parser.U_000C, 0)

        def CR(self):
            return self.getToken(Rfc5424Parser.CR, 0)

        def U_000E(self):
            return self.getToken(Rfc5424Parser.U_000E, 0)

        def U_000F(self):
            return self.getToken(Rfc5424Parser.U_000F, 0)

        def U_0010(self):
            return self.getToken(Rfc5424Parser.U_0010, 0)

        def U_0011(self):
            return self.getToken(Rfc5424Parser.U_0011, 0)

        def U_0012(self):
            return self.getToken(Rfc5424Parser.U_0012, 0)

        def U_0013(self):
            return self.getToken(Rfc5424Parser.U_0013, 0)

        def U_0014(self):
            return self.getToken(Rfc5424Parser.U_0014, 0)

        def U_0015(self):
            return self.getToken(Rfc5424Parser.U_0015, 0)

        def U_0016(self):
            return self.getToken(Rfc5424Parser.U_0016, 0)

        def U_0017(self):
            return self.getToken(Rfc5424Parser.U_0017, 0)

        def U_0018(self):
            return self.getToken(Rfc5424Parser.U_0018, 0)

        def U_0019(self):
            return self.getToken(Rfc5424Parser.U_0019, 0)

        def U_001A(self):
            return self.getToken(Rfc5424Parser.U_001A, 0)

        def U_001B(self):
            return self.getToken(Rfc5424Parser.U_001B, 0)

        def U_001C(self):
            return self.getToken(Rfc5424Parser.U_001C, 0)

        def U_001D(self):
            return self.getToken(Rfc5424Parser.U_001D, 0)

        def U_001E(self):
            return self.getToken(Rfc5424Parser.U_001E, 0)

        def U_001F(self):
            return self.getToken(Rfc5424Parser.U_001F, 0)

        def SPACE(self):
            return self.getToken(Rfc5424Parser.SPACE, 0)

        def EXCLAMATION(self):
            return self.getToken(Rfc5424Parser.EXCLAMATION, 0)

        def QUOTE(self):
            return self.getToken(Rfc5424Parser.QUOTE, 0)

        def POUND(self):
            return self.getToken(Rfc5424Parser.POUND, 0)

        def DOLLAR(self):
            return self.getToken(Rfc5424Parser.DOLLAR, 0)

        def PERCENT(self):
            return self.getToken(Rfc5424Parser.PERCENT, 0)

        def AMPERSAND(self):
            return self.getToken(Rfc5424Parser.AMPERSAND, 0)

        def APOSTROPHE(self):
            return self.getToken(Rfc5424Parser.APOSTROPHE, 0)

        def LEFT_PAREN(self):
            return self.getToken(Rfc5424Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(Rfc5424Parser.RIGHT_PAREN, 0)

        def ASTERISK(self):
            return self.getToken(Rfc5424Parser.ASTERISK, 0)

        def PLUS(self):
            return self.getToken(Rfc5424Parser.PLUS, 0)

        def COMMA(self):
            return self.getToken(Rfc5424Parser.COMMA, 0)

        def DASH(self):
            return self.getToken(Rfc5424Parser.DASH, 0)

        def PERIOD(self):
            return self.getToken(Rfc5424Parser.PERIOD, 0)

        def SLASH(self):
            return self.getToken(Rfc5424Parser.SLASH, 0)

        def ZERO(self):
            return self.getToken(Rfc5424Parser.ZERO, 0)

        def ONE(self):
            return self.getToken(Rfc5424Parser.ONE, 0)

        def TWO(self):
            return self.getToken(Rfc5424Parser.TWO, 0)

        def THREE(self):
            return self.getToken(Rfc5424Parser.THREE, 0)

        def FOUR(self):
            return self.getToken(Rfc5424Parser.FOUR, 0)

        def FIVE(self):
            return self.getToken(Rfc5424Parser.FIVE, 0)

        def SIX(self):
            return self.getToken(Rfc5424Parser.SIX, 0)

        def SEVEN(self):
            return self.getToken(Rfc5424Parser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(Rfc5424Parser.EIGHT, 0)

        def NINE(self):
            return self.getToken(Rfc5424Parser.NINE, 0)

        def COLON(self):
            return self.getToken(Rfc5424Parser.COLON, 0)

        def SEMICOLON(self):
            return self.getToken(Rfc5424Parser.SEMICOLON, 0)

        def LESS_THAN(self):
            return self.getToken(Rfc5424Parser.LESS_THAN, 0)

        def EQUALS(self):
            return self.getToken(Rfc5424Parser.EQUALS, 0)

        def GREATER_THAN(self):
            return self.getToken(Rfc5424Parser.GREATER_THAN, 0)

        def QUESTION(self):
            return self.getToken(Rfc5424Parser.QUESTION, 0)

        def AT(self):
            return self.getToken(Rfc5424Parser.AT, 0)

        def CAP_A(self):
            return self.getToken(Rfc5424Parser.CAP_A, 0)

        def CAP_B(self):
            return self.getToken(Rfc5424Parser.CAP_B, 0)

        def CAP_C(self):
            return self.getToken(Rfc5424Parser.CAP_C, 0)

        def CAP_D(self):
            return self.getToken(Rfc5424Parser.CAP_D, 0)

        def CAP_E(self):
            return self.getToken(Rfc5424Parser.CAP_E, 0)

        def CAP_F(self):
            return self.getToken(Rfc5424Parser.CAP_F, 0)

        def CAP_G(self):
            return self.getToken(Rfc5424Parser.CAP_G, 0)

        def CAP_H(self):
            return self.getToken(Rfc5424Parser.CAP_H, 0)

        def CAP_I(self):
            return self.getToken(Rfc5424Parser.CAP_I, 0)

        def CAP_J(self):
            return self.getToken(Rfc5424Parser.CAP_J, 0)

        def CAP_K(self):
            return self.getToken(Rfc5424Parser.CAP_K, 0)

        def CAP_L(self):
            return self.getToken(Rfc5424Parser.CAP_L, 0)

        def CAP_M(self):
            return self.getToken(Rfc5424Parser.CAP_M, 0)

        def CAP_N(self):
            return self.getToken(Rfc5424Parser.CAP_N, 0)

        def CAP_O(self):
            return self.getToken(Rfc5424Parser.CAP_O, 0)

        def CAP_P(self):
            return self.getToken(Rfc5424Parser.CAP_P, 0)

        def CAP_Q(self):
            return self.getToken(Rfc5424Parser.CAP_Q, 0)

        def CAP_R(self):
            return self.getToken(Rfc5424Parser.CAP_R, 0)

        def CAP_S(self):
            return self.getToken(Rfc5424Parser.CAP_S, 0)

        def CAP_T(self):
            return self.getToken(Rfc5424Parser.CAP_T, 0)

        def CAP_U(self):
            return self.getToken(Rfc5424Parser.CAP_U, 0)

        def CAP_V(self):
            return self.getToken(Rfc5424Parser.CAP_V, 0)

        def CAP_W(self):
            return self.getToken(Rfc5424Parser.CAP_W, 0)

        def CAP_X(self):
            return self.getToken(Rfc5424Parser.CAP_X, 0)

        def CAP_Y(self):
            return self.getToken(Rfc5424Parser.CAP_Y, 0)

        def CAP_Z(self):
            return self.getToken(Rfc5424Parser.CAP_Z, 0)

        def LEFT_BRACE(self):
            return self.getToken(Rfc5424Parser.LEFT_BRACE, 0)

        def BACKSLASH(self):
            return self.getToken(Rfc5424Parser.BACKSLASH, 0)

        def RIGHT_BRACE(self):
            return self.getToken(Rfc5424Parser.RIGHT_BRACE, 0)

        def CARAT(self):
            return self.getToken(Rfc5424Parser.CARAT, 0)

        def UNDERSCORE(self):
            return self.getToken(Rfc5424Parser.UNDERSCORE, 0)

        def ACCENT(self):
            return self.getToken(Rfc5424Parser.ACCENT, 0)

        def A(self):
            return self.getToken(Rfc5424Parser.A, 0)

        def B(self):
            return self.getToken(Rfc5424Parser.B, 0)

        def C(self):
            return self.getToken(Rfc5424Parser.C, 0)

        def D(self):
            return self.getToken(Rfc5424Parser.D, 0)

        def E(self):
            return self.getToken(Rfc5424Parser.E, 0)

        def F(self):
            return self.getToken(Rfc5424Parser.F, 0)

        def G(self):
            return self.getToken(Rfc5424Parser.G, 0)

        def H(self):
            return self.getToken(Rfc5424Parser.H, 0)

        def I(self):
            return self.getToken(Rfc5424Parser.I, 0)

        def J(self):
            return self.getToken(Rfc5424Parser.J, 0)

        def K(self):
            return self.getToken(Rfc5424Parser.K, 0)

        def L(self):
            return self.getToken(Rfc5424Parser.L, 0)

        def M(self):
            return self.getToken(Rfc5424Parser.M, 0)

        def N(self):
            return self.getToken(Rfc5424Parser.N, 0)

        def O(self):
            return self.getToken(Rfc5424Parser.O, 0)

        def P(self):
            return self.getToken(Rfc5424Parser.P, 0)

        def Q(self):
            return self.getToken(Rfc5424Parser.Q, 0)

        def R(self):
            return self.getToken(Rfc5424Parser.R, 0)

        def S(self):
            return self.getToken(Rfc5424Parser.S, 0)

        def T(self):
            return self.getToken(Rfc5424Parser.T, 0)

        def U(self):
            return self.getToken(Rfc5424Parser.U, 0)

        def V(self):
            return self.getToken(Rfc5424Parser.V, 0)

        def W(self):
            return self.getToken(Rfc5424Parser.W, 0)

        def X(self):
            return self.getToken(Rfc5424Parser.X, 0)

        def Y(self):
            return self.getToken(Rfc5424Parser.Y, 0)

        def Z(self):
            return self.getToken(Rfc5424Parser.Z, 0)

        def LEFT_CURLY_BRACE(self):
            return self.getToken(Rfc5424Parser.LEFT_CURLY_BRACE, 0)

        def PIPE(self):
            return self.getToken(Rfc5424Parser.PIPE, 0)

        def RIGHT_CURLY_BRACE(self):
            return self.getToken(Rfc5424Parser.RIGHT_CURLY_BRACE, 0)

        def TILDE(self):
            return self.getToken(Rfc5424Parser.TILDE, 0)

        def U_007F(self):
            return self.getToken(Rfc5424Parser.U_007F, 0)

        def U_0080(self):
            return self.getToken(Rfc5424Parser.U_0080, 0)

        def U_0081(self):
            return self.getToken(Rfc5424Parser.U_0081, 0)

        def U_0082(self):
            return self.getToken(Rfc5424Parser.U_0082, 0)

        def U_0083(self):
            return self.getToken(Rfc5424Parser.U_0083, 0)

        def U_0084(self):
            return self.getToken(Rfc5424Parser.U_0084, 0)

        def U_0085(self):
            return self.getToken(Rfc5424Parser.U_0085, 0)

        def U_0086(self):
            return self.getToken(Rfc5424Parser.U_0086, 0)

        def U_0087(self):
            return self.getToken(Rfc5424Parser.U_0087, 0)

        def U_0088(self):
            return self.getToken(Rfc5424Parser.U_0088, 0)

        def U_0089(self):
            return self.getToken(Rfc5424Parser.U_0089, 0)

        def U_008A(self):
            return self.getToken(Rfc5424Parser.U_008A, 0)

        def U_008B(self):
            return self.getToken(Rfc5424Parser.U_008B, 0)

        def U_008C(self):
            return self.getToken(Rfc5424Parser.U_008C, 0)

        def U_008D(self):
            return self.getToken(Rfc5424Parser.U_008D, 0)

        def U_008E(self):
            return self.getToken(Rfc5424Parser.U_008E, 0)

        def U_008F(self):
            return self.getToken(Rfc5424Parser.U_008F, 0)

        def U_0090(self):
            return self.getToken(Rfc5424Parser.U_0090, 0)

        def U_0091(self):
            return self.getToken(Rfc5424Parser.U_0091, 0)

        def U_0092(self):
            return self.getToken(Rfc5424Parser.U_0092, 0)

        def U_0093(self):
            return self.getToken(Rfc5424Parser.U_0093, 0)

        def U_0094(self):
            return self.getToken(Rfc5424Parser.U_0094, 0)

        def U_0095(self):
            return self.getToken(Rfc5424Parser.U_0095, 0)

        def U_0096(self):
            return self.getToken(Rfc5424Parser.U_0096, 0)

        def U_0097(self):
            return self.getToken(Rfc5424Parser.U_0097, 0)

        def U_0098(self):
            return self.getToken(Rfc5424Parser.U_0098, 0)

        def U_0099(self):
            return self.getToken(Rfc5424Parser.U_0099, 0)

        def U_009A(self):
            return self.getToken(Rfc5424Parser.U_009A, 0)

        def U_009B(self):
            return self.getToken(Rfc5424Parser.U_009B, 0)

        def U_009C(self):
            return self.getToken(Rfc5424Parser.U_009C, 0)

        def U_009D(self):
            return self.getToken(Rfc5424Parser.U_009D, 0)

        def U_009E(self):
            return self.getToken(Rfc5424Parser.U_009E, 0)

        def U_009F(self):
            return self.getToken(Rfc5424Parser.U_009F, 0)

        def U_00A0(self):
            return self.getToken(Rfc5424Parser.U_00A0, 0)

        def U_00A1(self):
            return self.getToken(Rfc5424Parser.U_00A1, 0)

        def U_00A2(self):
            return self.getToken(Rfc5424Parser.U_00A2, 0)

        def U_00A3(self):
            return self.getToken(Rfc5424Parser.U_00A3, 0)

        def U_00A4(self):
            return self.getToken(Rfc5424Parser.U_00A4, 0)

        def U_00A5(self):
            return self.getToken(Rfc5424Parser.U_00A5, 0)

        def U_00A6(self):
            return self.getToken(Rfc5424Parser.U_00A6, 0)

        def U_00A7(self):
            return self.getToken(Rfc5424Parser.U_00A7, 0)

        def U_00A8(self):
            return self.getToken(Rfc5424Parser.U_00A8, 0)

        def U_00A9(self):
            return self.getToken(Rfc5424Parser.U_00A9, 0)

        def U_00AA(self):
            return self.getToken(Rfc5424Parser.U_00AA, 0)

        def U_00AB(self):
            return self.getToken(Rfc5424Parser.U_00AB, 0)

        def U_00AC(self):
            return self.getToken(Rfc5424Parser.U_00AC, 0)

        def U_00AD(self):
            return self.getToken(Rfc5424Parser.U_00AD, 0)

        def U_00AE(self):
            return self.getToken(Rfc5424Parser.U_00AE, 0)

        def U_00AF(self):
            return self.getToken(Rfc5424Parser.U_00AF, 0)

        def U_00B0(self):
            return self.getToken(Rfc5424Parser.U_00B0, 0)

        def U_00B1(self):
            return self.getToken(Rfc5424Parser.U_00B1, 0)

        def U_00B2(self):
            return self.getToken(Rfc5424Parser.U_00B2, 0)

        def U_00B3(self):
            return self.getToken(Rfc5424Parser.U_00B3, 0)

        def U_00B4(self):
            return self.getToken(Rfc5424Parser.U_00B4, 0)

        def U_00B5(self):
            return self.getToken(Rfc5424Parser.U_00B5, 0)

        def U_00B6(self):
            return self.getToken(Rfc5424Parser.U_00B6, 0)

        def U_00B7(self):
            return self.getToken(Rfc5424Parser.U_00B7, 0)

        def U_00B8(self):
            return self.getToken(Rfc5424Parser.U_00B8, 0)

        def U_00B9(self):
            return self.getToken(Rfc5424Parser.U_00B9, 0)

        def U_00BA(self):
            return self.getToken(Rfc5424Parser.U_00BA, 0)

        def U_00BB(self):
            return self.getToken(Rfc5424Parser.U_00BB, 0)

        def U_00BC(self):
            return self.getToken(Rfc5424Parser.U_00BC, 0)

        def U_00BD(self):
            return self.getToken(Rfc5424Parser.U_00BD, 0)

        def U_00BE(self):
            return self.getToken(Rfc5424Parser.U_00BE, 0)

        def U_00BF(self):
            return self.getToken(Rfc5424Parser.U_00BF, 0)

        def U_00C0(self):
            return self.getToken(Rfc5424Parser.U_00C0, 0)

        def U_00C1(self):
            return self.getToken(Rfc5424Parser.U_00C1, 0)

        def U_00C2(self):
            return self.getToken(Rfc5424Parser.U_00C2, 0)

        def U_00C3(self):
            return self.getToken(Rfc5424Parser.U_00C3, 0)

        def U_00C4(self):
            return self.getToken(Rfc5424Parser.U_00C4, 0)

        def U_00C5(self):
            return self.getToken(Rfc5424Parser.U_00C5, 0)

        def U_00C6(self):
            return self.getToken(Rfc5424Parser.U_00C6, 0)

        def U_00C7(self):
            return self.getToken(Rfc5424Parser.U_00C7, 0)

        def U_00C8(self):
            return self.getToken(Rfc5424Parser.U_00C8, 0)

        def U_00C9(self):
            return self.getToken(Rfc5424Parser.U_00C9, 0)

        def U_00CA(self):
            return self.getToken(Rfc5424Parser.U_00CA, 0)

        def U_00CB(self):
            return self.getToken(Rfc5424Parser.U_00CB, 0)

        def U_00CC(self):
            return self.getToken(Rfc5424Parser.U_00CC, 0)

        def U_00CD(self):
            return self.getToken(Rfc5424Parser.U_00CD, 0)

        def U_00CE(self):
            return self.getToken(Rfc5424Parser.U_00CE, 0)

        def U_00CF(self):
            return self.getToken(Rfc5424Parser.U_00CF, 0)

        def U_00D0(self):
            return self.getToken(Rfc5424Parser.U_00D0, 0)

        def U_00D1(self):
            return self.getToken(Rfc5424Parser.U_00D1, 0)

        def U_00D2(self):
            return self.getToken(Rfc5424Parser.U_00D2, 0)

        def U_00D3(self):
            return self.getToken(Rfc5424Parser.U_00D3, 0)

        def U_00D4(self):
            return self.getToken(Rfc5424Parser.U_00D4, 0)

        def U_00D5(self):
            return self.getToken(Rfc5424Parser.U_00D5, 0)

        def U_00D6(self):
            return self.getToken(Rfc5424Parser.U_00D6, 0)

        def U_00D7(self):
            return self.getToken(Rfc5424Parser.U_00D7, 0)

        def U_00D8(self):
            return self.getToken(Rfc5424Parser.U_00D8, 0)

        def U_00D9(self):
            return self.getToken(Rfc5424Parser.U_00D9, 0)

        def U_00DA(self):
            return self.getToken(Rfc5424Parser.U_00DA, 0)

        def U_00DB(self):
            return self.getToken(Rfc5424Parser.U_00DB, 0)

        def U_00DC(self):
            return self.getToken(Rfc5424Parser.U_00DC, 0)

        def U_00DD(self):
            return self.getToken(Rfc5424Parser.U_00DD, 0)

        def U_00DE(self):
            return self.getToken(Rfc5424Parser.U_00DE, 0)

        def U_00DF(self):
            return self.getToken(Rfc5424Parser.U_00DF, 0)

        def U_00E0(self):
            return self.getToken(Rfc5424Parser.U_00E0, 0)

        def U_00E1(self):
            return self.getToken(Rfc5424Parser.U_00E1, 0)

        def U_00E2(self):
            return self.getToken(Rfc5424Parser.U_00E2, 0)

        def U_00E3(self):
            return self.getToken(Rfc5424Parser.U_00E3, 0)

        def U_00E4(self):
            return self.getToken(Rfc5424Parser.U_00E4, 0)

        def U_00E5(self):
            return self.getToken(Rfc5424Parser.U_00E5, 0)

        def U_00E6(self):
            return self.getToken(Rfc5424Parser.U_00E6, 0)

        def U_00E7(self):
            return self.getToken(Rfc5424Parser.U_00E7, 0)

        def U_00E8(self):
            return self.getToken(Rfc5424Parser.U_00E8, 0)

        def U_00E9(self):
            return self.getToken(Rfc5424Parser.U_00E9, 0)

        def U_00EA(self):
            return self.getToken(Rfc5424Parser.U_00EA, 0)

        def U_00EB(self):
            return self.getToken(Rfc5424Parser.U_00EB, 0)

        def U_00EC(self):
            return self.getToken(Rfc5424Parser.U_00EC, 0)

        def U_00ED(self):
            return self.getToken(Rfc5424Parser.U_00ED, 0)

        def U_00EE(self):
            return self.getToken(Rfc5424Parser.U_00EE, 0)

        def U_00EF(self):
            return self.getToken(Rfc5424Parser.U_00EF, 0)

        def U_00F0(self):
            return self.getToken(Rfc5424Parser.U_00F0, 0)

        def U_00F1(self):
            return self.getToken(Rfc5424Parser.U_00F1, 0)

        def U_00F2(self):
            return self.getToken(Rfc5424Parser.U_00F2, 0)

        def U_00F3(self):
            return self.getToken(Rfc5424Parser.U_00F3, 0)

        def U_00F4(self):
            return self.getToken(Rfc5424Parser.U_00F4, 0)

        def U_00F5(self):
            return self.getToken(Rfc5424Parser.U_00F5, 0)

        def U_00F6(self):
            return self.getToken(Rfc5424Parser.U_00F6, 0)

        def U_00F7(self):
            return self.getToken(Rfc5424Parser.U_00F7, 0)

        def U_00F8(self):
            return self.getToken(Rfc5424Parser.U_00F8, 0)

        def U_00F9(self):
            return self.getToken(Rfc5424Parser.U_00F9, 0)

        def U_00FA(self):
            return self.getToken(Rfc5424Parser.U_00FA, 0)

        def U_00FB(self):
            return self.getToken(Rfc5424Parser.U_00FB, 0)

        def U_00FC(self):
            return self.getToken(Rfc5424Parser.U_00FC, 0)

        def U_00FD(self):
            return self.getToken(Rfc5424Parser.U_00FD, 0)

        def U_00FE(self):
            return self.getToken(Rfc5424Parser.U_00FE, 0)

        def U_00FF(self):
            return self.getToken(Rfc5424Parser.U_00FF, 0)

        def getRuleIndex(self):
            return Rfc5424Parser.RULE_octet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOctet" ):
                listener.enterOctet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOctet" ):
                listener.exitOctet(self)




    def octet(self):

        localctx = Rfc5424Parser.OctetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_octet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            _la = self._input.LA(1)
            if not(((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (Rfc5424Parser.TAB - 1)) | (1 << (Rfc5424Parser.LF - 1)) | (1 << (Rfc5424Parser.CR - 1)) | (1 << (Rfc5424Parser.SPACE - 1)) | (1 << (Rfc5424Parser.EXCLAMATION - 1)) | (1 << (Rfc5424Parser.QUOTE - 1)) | (1 << (Rfc5424Parser.POUND - 1)) | (1 << (Rfc5424Parser.DOLLAR - 1)) | (1 << (Rfc5424Parser.PERCENT - 1)) | (1 << (Rfc5424Parser.AMPERSAND - 1)) | (1 << (Rfc5424Parser.APOSTROPHE - 1)) | (1 << (Rfc5424Parser.LEFT_PAREN - 1)) | (1 << (Rfc5424Parser.RIGHT_PAREN - 1)) | (1 << (Rfc5424Parser.ASTERISK - 1)) | (1 << (Rfc5424Parser.PLUS - 1)) | (1 << (Rfc5424Parser.COMMA - 1)) | (1 << (Rfc5424Parser.DASH - 1)) | (1 << (Rfc5424Parser.PERIOD - 1)) | (1 << (Rfc5424Parser.SLASH - 1)) | (1 << (Rfc5424Parser.ZERO - 1)) | (1 << (Rfc5424Parser.ONE - 1)) | (1 << (Rfc5424Parser.TWO - 1)) | (1 << (Rfc5424Parser.THREE - 1)) | (1 << (Rfc5424Parser.FOUR - 1)) | (1 << (Rfc5424Parser.FIVE - 1)) | (1 << (Rfc5424Parser.SIX - 1)) | (1 << (Rfc5424Parser.SEVEN - 1)) | (1 << (Rfc5424Parser.EIGHT - 1)) | (1 << (Rfc5424Parser.NINE - 1)) | (1 << (Rfc5424Parser.COLON - 1)) | (1 << (Rfc5424Parser.SEMICOLON - 1)) | (1 << (Rfc5424Parser.LESS_THAN - 1)) | (1 << (Rfc5424Parser.EQUALS - 1)) | (1 << (Rfc5424Parser.GREATER_THAN - 1)) | (1 << (Rfc5424Parser.QUESTION - 1)) | (1 << (Rfc5424Parser.AT - 1)) | (1 << (Rfc5424Parser.CAP_A - 1)) | (1 << (Rfc5424Parser.CAP_B - 1)) | (1 << (Rfc5424Parser.CAP_C - 1)) | (1 << (Rfc5424Parser.CAP_D - 1)) | (1 << (Rfc5424Parser.CAP_E - 1)) | (1 << (Rfc5424Parser.CAP_F - 1)) | (1 << (Rfc5424Parser.CAP_G - 1)) | (1 << (Rfc5424Parser.CAP_H - 1)) | (1 << (Rfc5424Parser.CAP_I - 1)) | (1 << (Rfc5424Parser.CAP_J - 1)) | (1 << (Rfc5424Parser.CAP_K - 1)) | (1 << (Rfc5424Parser.CAP_L - 1)) | (1 << (Rfc5424Parser.CAP_M - 1)) | (1 << (Rfc5424Parser.CAP_N - 1)) | (1 << (Rfc5424Parser.CAP_O - 1)) | (1 << (Rfc5424Parser.CAP_P - 1)) | (1 << (Rfc5424Parser.CAP_Q - 1)) | (1 << (Rfc5424Parser.CAP_R - 1)) | (1 << (Rfc5424Parser.CAP_S - 1)) | (1 << (Rfc5424Parser.CAP_T - 1)) | (1 << (Rfc5424Parser.CAP_U - 1)) | (1 << (Rfc5424Parser.CAP_V - 1)) | (1 << (Rfc5424Parser.CAP_W - 1)) | (1 << (Rfc5424Parser.CAP_X - 1)) | (1 << (Rfc5424Parser.CAP_Y - 1)) | (1 << (Rfc5424Parser.CAP_Z - 1)) | (1 << (Rfc5424Parser.LEFT_BRACE - 1)) | (1 << (Rfc5424Parser.BACKSLASH - 1)))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Rfc5424Parser.RIGHT_BRACE - 65)) | (1 << (Rfc5424Parser.CARAT - 65)) | (1 << (Rfc5424Parser.UNDERSCORE - 65)) | (1 << (Rfc5424Parser.ACCENT - 65)) | (1 << (Rfc5424Parser.A - 65)) | (1 << (Rfc5424Parser.B - 65)) | (1 << (Rfc5424Parser.C - 65)) | (1 << (Rfc5424Parser.D - 65)) | (1 << (Rfc5424Parser.E - 65)) | (1 << (Rfc5424Parser.F - 65)) | (1 << (Rfc5424Parser.G - 65)) | (1 << (Rfc5424Parser.H - 65)) | (1 << (Rfc5424Parser.I - 65)) | (1 << (Rfc5424Parser.J - 65)) | (1 << (Rfc5424Parser.K - 65)) | (1 << (Rfc5424Parser.L - 65)) | (1 << (Rfc5424Parser.M - 65)) | (1 << (Rfc5424Parser.N - 65)) | (1 << (Rfc5424Parser.O - 65)) | (1 << (Rfc5424Parser.P - 65)) | (1 << (Rfc5424Parser.Q - 65)) | (1 << (Rfc5424Parser.R - 65)) | (1 << (Rfc5424Parser.S - 65)) | (1 << (Rfc5424Parser.T - 65)) | (1 << (Rfc5424Parser.U - 65)) | (1 << (Rfc5424Parser.V - 65)) | (1 << (Rfc5424Parser.W - 65)) | (1 << (Rfc5424Parser.X - 65)) | (1 << (Rfc5424Parser.Y - 65)) | (1 << (Rfc5424Parser.Z - 65)) | (1 << (Rfc5424Parser.LEFT_CURLY_BRACE - 65)) | (1 << (Rfc5424Parser.PIPE - 65)) | (1 << (Rfc5424Parser.RIGHT_CURLY_BRACE - 65)) | (1 << (Rfc5424Parser.TILDE - 65)) | (1 << (Rfc5424Parser.U_0000 - 65)) | (1 << (Rfc5424Parser.U_0001 - 65)) | (1 << (Rfc5424Parser.U_0002 - 65)) | (1 << (Rfc5424Parser.U_0003 - 65)) | (1 << (Rfc5424Parser.U_0004 - 65)) | (1 << (Rfc5424Parser.U_0005 - 65)) | (1 << (Rfc5424Parser.U_0006 - 65)) | (1 << (Rfc5424Parser.U_0007 - 65)) | (1 << (Rfc5424Parser.U_0008 - 65)) | (1 << (Rfc5424Parser.U_000B - 65)) | (1 << (Rfc5424Parser.U_000C - 65)) | (1 << (Rfc5424Parser.U_000E - 65)) | (1 << (Rfc5424Parser.U_000F - 65)) | (1 << (Rfc5424Parser.U_0010 - 65)) | (1 << (Rfc5424Parser.U_0011 - 65)) | (1 << (Rfc5424Parser.U_0012 - 65)) | (1 << (Rfc5424Parser.U_0013 - 65)) | (1 << (Rfc5424Parser.U_0014 - 65)) | (1 << (Rfc5424Parser.U_0015 - 65)) | (1 << (Rfc5424Parser.U_0016 - 65)) | (1 << (Rfc5424Parser.U_0017 - 65)) | (1 << (Rfc5424Parser.U_0018 - 65)) | (1 << (Rfc5424Parser.U_0019 - 65)) | (1 << (Rfc5424Parser.U_001A - 65)) | (1 << (Rfc5424Parser.U_001B - 65)) | (1 << (Rfc5424Parser.U_001C - 65)) | (1 << (Rfc5424Parser.U_001D - 65)) | (1 << (Rfc5424Parser.U_001E - 65)) | (1 << (Rfc5424Parser.U_001F - 65)) | (1 << (Rfc5424Parser.U_007F - 65)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (Rfc5424Parser.U_0080 - 129)) | (1 << (Rfc5424Parser.U_0081 - 129)) | (1 << (Rfc5424Parser.U_0082 - 129)) | (1 << (Rfc5424Parser.U_0083 - 129)) | (1 << (Rfc5424Parser.U_0084 - 129)) | (1 << (Rfc5424Parser.U_0085 - 129)) | (1 << (Rfc5424Parser.U_0086 - 129)) | (1 << (Rfc5424Parser.U_0087 - 129)) | (1 << (Rfc5424Parser.U_0088 - 129)) | (1 << (Rfc5424Parser.U_0089 - 129)) | (1 << (Rfc5424Parser.U_008A - 129)) | (1 << (Rfc5424Parser.U_008B - 129)) | (1 << (Rfc5424Parser.U_008C - 129)) | (1 << (Rfc5424Parser.U_008D - 129)) | (1 << (Rfc5424Parser.U_008E - 129)) | (1 << (Rfc5424Parser.U_008F - 129)) | (1 << (Rfc5424Parser.U_0090 - 129)) | (1 << (Rfc5424Parser.U_0091 - 129)) | (1 << (Rfc5424Parser.U_0092 - 129)) | (1 << (Rfc5424Parser.U_0093 - 129)) | (1 << (Rfc5424Parser.U_0094 - 129)) | (1 << (Rfc5424Parser.U_0095 - 129)) | (1 << (Rfc5424Parser.U_0096 - 129)) | (1 << (Rfc5424Parser.U_0097 - 129)) | (1 << (Rfc5424Parser.U_0098 - 129)) | (1 << (Rfc5424Parser.U_0099 - 129)) | (1 << (Rfc5424Parser.U_009A - 129)) | (1 << (Rfc5424Parser.U_009B - 129)) | (1 << (Rfc5424Parser.U_009C - 129)) | (1 << (Rfc5424Parser.U_009D - 129)) | (1 << (Rfc5424Parser.U_009E - 129)) | (1 << (Rfc5424Parser.U_009F - 129)) | (1 << (Rfc5424Parser.U_00A0 - 129)) | (1 << (Rfc5424Parser.U_00A1 - 129)) | (1 << (Rfc5424Parser.U_00A2 - 129)) | (1 << (Rfc5424Parser.U_00A3 - 129)) | (1 << (Rfc5424Parser.U_00A4 - 129)) | (1 << (Rfc5424Parser.U_00A5 - 129)) | (1 << (Rfc5424Parser.U_00A6 - 129)) | (1 << (Rfc5424Parser.U_00A7 - 129)) | (1 << (Rfc5424Parser.U_00A8 - 129)) | (1 << (Rfc5424Parser.U_00A9 - 129)) | (1 << (Rfc5424Parser.U_00AA - 129)) | (1 << (Rfc5424Parser.U_00AB - 129)) | (1 << (Rfc5424Parser.U_00AC - 129)) | (1 << (Rfc5424Parser.U_00AD - 129)) | (1 << (Rfc5424Parser.U_00AE - 129)) | (1 << (Rfc5424Parser.U_00AF - 129)) | (1 << (Rfc5424Parser.U_00B0 - 129)) | (1 << (Rfc5424Parser.U_00B1 - 129)) | (1 << (Rfc5424Parser.U_00B2 - 129)) | (1 << (Rfc5424Parser.U_00B3 - 129)) | (1 << (Rfc5424Parser.U_00B4 - 129)) | (1 << (Rfc5424Parser.U_00B5 - 129)) | (1 << (Rfc5424Parser.U_00B6 - 129)) | (1 << (Rfc5424Parser.U_00B7 - 129)) | (1 << (Rfc5424Parser.U_00B8 - 129)) | (1 << (Rfc5424Parser.U_00B9 - 129)) | (1 << (Rfc5424Parser.U_00BA - 129)) | (1 << (Rfc5424Parser.U_00BB - 129)) | (1 << (Rfc5424Parser.U_00BC - 129)) | (1 << (Rfc5424Parser.U_00BD - 129)) | (1 << (Rfc5424Parser.U_00BE - 129)) | (1 << (Rfc5424Parser.U_00BF - 129)))) != 0) or ((((_la - 193)) & ~0x3f) == 0 and ((1 << (_la - 193)) & ((1 << (Rfc5424Parser.U_00C0 - 193)) | (1 << (Rfc5424Parser.U_00C1 - 193)) | (1 << (Rfc5424Parser.U_00C2 - 193)) | (1 << (Rfc5424Parser.U_00C3 - 193)) | (1 << (Rfc5424Parser.U_00C4 - 193)) | (1 << (Rfc5424Parser.U_00C5 - 193)) | (1 << (Rfc5424Parser.U_00C6 - 193)) | (1 << (Rfc5424Parser.U_00C7 - 193)) | (1 << (Rfc5424Parser.U_00C8 - 193)) | (1 << (Rfc5424Parser.U_00C9 - 193)) | (1 << (Rfc5424Parser.U_00CA - 193)) | (1 << (Rfc5424Parser.U_00CB - 193)) | (1 << (Rfc5424Parser.U_00CC - 193)) | (1 << (Rfc5424Parser.U_00CD - 193)) | (1 << (Rfc5424Parser.U_00CE - 193)) | (1 << (Rfc5424Parser.U_00CF - 193)) | (1 << (Rfc5424Parser.U_00D0 - 193)) | (1 << (Rfc5424Parser.U_00D1 - 193)) | (1 << (Rfc5424Parser.U_00D2 - 193)) | (1 << (Rfc5424Parser.U_00D3 - 193)) | (1 << (Rfc5424Parser.U_00D4 - 193)) | (1 << (Rfc5424Parser.U_00D5 - 193)) | (1 << (Rfc5424Parser.U_00D6 - 193)) | (1 << (Rfc5424Parser.U_00D7 - 193)) | (1 << (Rfc5424Parser.U_00D8 - 193)) | (1 << (Rfc5424Parser.U_00D9 - 193)) | (1 << (Rfc5424Parser.U_00DA - 193)) | (1 << (Rfc5424Parser.U_00DB - 193)) | (1 << (Rfc5424Parser.U_00DC - 193)) | (1 << (Rfc5424Parser.U_00DD - 193)) | (1 << (Rfc5424Parser.U_00DE - 193)) | (1 << (Rfc5424Parser.U_00DF - 193)) | (1 << (Rfc5424Parser.U_00E0 - 193)) | (1 << (Rfc5424Parser.U_00E1 - 193)) | (1 << (Rfc5424Parser.U_00E2 - 193)) | (1 << (Rfc5424Parser.U_00E3 - 193)) | (1 << (Rfc5424Parser.U_00E4 - 193)) | (1 << (Rfc5424Parser.U_00E5 - 193)) | (1 << (Rfc5424Parser.U_00E6 - 193)) | (1 << (Rfc5424Parser.U_00E7 - 193)) | (1 << (Rfc5424Parser.U_00E8 - 193)) | (1 << (Rfc5424Parser.U_00E9 - 193)) | (1 << (Rfc5424Parser.U_00EA - 193)) | (1 << (Rfc5424Parser.U_00EB - 193)) | (1 << (Rfc5424Parser.U_00EC - 193)) | (1 << (Rfc5424Parser.U_00ED - 193)) | (1 << (Rfc5424Parser.U_00EE - 193)) | (1 << (Rfc5424Parser.U_00EF - 193)) | (1 << (Rfc5424Parser.U_00F0 - 193)) | (1 << (Rfc5424Parser.U_00F1 - 193)) | (1 << (Rfc5424Parser.U_00F2 - 193)) | (1 << (Rfc5424Parser.U_00F3 - 193)) | (1 << (Rfc5424Parser.U_00F4 - 193)) | (1 << (Rfc5424Parser.U_00F5 - 193)) | (1 << (Rfc5424Parser.U_00F6 - 193)) | (1 << (Rfc5424Parser.U_00F7 - 193)) | (1 << (Rfc5424Parser.U_00F8 - 193)) | (1 << (Rfc5424Parser.U_00F9 - 193)) | (1 << (Rfc5424Parser.U_00FA - 193)) | (1 << (Rfc5424Parser.U_00FB - 193)) | (1 << (Rfc5424Parser.U_00FC - 193)) | (1 << (Rfc5424Parser.U_00FD - 193)) | (1 << (Rfc5424Parser.U_00FE - 193)) | (1 << (Rfc5424Parser.U_00FF - 193)))) != 0)):
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


    class SpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self):
            return self.getToken(Rfc5424Parser.SPACE, 0)

        def getRuleIndex(self):
            return Rfc5424Parser.RULE_sp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSp" ):
                listener.enterSp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSp" ):
                listener.exitSp(self)




    def sp(self):

        localctx = Rfc5424Parser.SpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_sp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(Rfc5424Parser.SPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintusasciiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCLAMATION(self):
            return self.getToken(Rfc5424Parser.EXCLAMATION, 0)

        def QUOTE(self):
            return self.getToken(Rfc5424Parser.QUOTE, 0)

        def POUND(self):
            return self.getToken(Rfc5424Parser.POUND, 0)

        def DOLLAR(self):
            return self.getToken(Rfc5424Parser.DOLLAR, 0)

        def PERCENT(self):
            return self.getToken(Rfc5424Parser.PERCENT, 0)

        def AMPERSAND(self):
            return self.getToken(Rfc5424Parser.AMPERSAND, 0)

        def APOSTROPHE(self):
            return self.getToken(Rfc5424Parser.APOSTROPHE, 0)

        def LEFT_PAREN(self):
            return self.getToken(Rfc5424Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(Rfc5424Parser.RIGHT_PAREN, 0)

        def ASTERISK(self):
            return self.getToken(Rfc5424Parser.ASTERISK, 0)

        def PLUS(self):
            return self.getToken(Rfc5424Parser.PLUS, 0)

        def COMMA(self):
            return self.getToken(Rfc5424Parser.COMMA, 0)

        def DASH(self):
            return self.getToken(Rfc5424Parser.DASH, 0)

        def PERIOD(self):
            return self.getToken(Rfc5424Parser.PERIOD, 0)

        def SLASH(self):
            return self.getToken(Rfc5424Parser.SLASH, 0)

        def ZERO(self):
            return self.getToken(Rfc5424Parser.ZERO, 0)

        def ONE(self):
            return self.getToken(Rfc5424Parser.ONE, 0)

        def TWO(self):
            return self.getToken(Rfc5424Parser.TWO, 0)

        def THREE(self):
            return self.getToken(Rfc5424Parser.THREE, 0)

        def FOUR(self):
            return self.getToken(Rfc5424Parser.FOUR, 0)

        def FIVE(self):
            return self.getToken(Rfc5424Parser.FIVE, 0)

        def SIX(self):
            return self.getToken(Rfc5424Parser.SIX, 0)

        def SEVEN(self):
            return self.getToken(Rfc5424Parser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(Rfc5424Parser.EIGHT, 0)

        def NINE(self):
            return self.getToken(Rfc5424Parser.NINE, 0)

        def COLON(self):
            return self.getToken(Rfc5424Parser.COLON, 0)

        def SEMICOLON(self):
            return self.getToken(Rfc5424Parser.SEMICOLON, 0)

        def LESS_THAN(self):
            return self.getToken(Rfc5424Parser.LESS_THAN, 0)

        def EQUALS(self):
            return self.getToken(Rfc5424Parser.EQUALS, 0)

        def GREATER_THAN(self):
            return self.getToken(Rfc5424Parser.GREATER_THAN, 0)

        def QUESTION(self):
            return self.getToken(Rfc5424Parser.QUESTION, 0)

        def AT(self):
            return self.getToken(Rfc5424Parser.AT, 0)

        def CAP_A(self):
            return self.getToken(Rfc5424Parser.CAP_A, 0)

        def CAP_B(self):
            return self.getToken(Rfc5424Parser.CAP_B, 0)

        def CAP_C(self):
            return self.getToken(Rfc5424Parser.CAP_C, 0)

        def CAP_D(self):
            return self.getToken(Rfc5424Parser.CAP_D, 0)

        def CAP_E(self):
            return self.getToken(Rfc5424Parser.CAP_E, 0)

        def CAP_F(self):
            return self.getToken(Rfc5424Parser.CAP_F, 0)

        def CAP_G(self):
            return self.getToken(Rfc5424Parser.CAP_G, 0)

        def CAP_H(self):
            return self.getToken(Rfc5424Parser.CAP_H, 0)

        def CAP_I(self):
            return self.getToken(Rfc5424Parser.CAP_I, 0)

        def CAP_J(self):
            return self.getToken(Rfc5424Parser.CAP_J, 0)

        def CAP_K(self):
            return self.getToken(Rfc5424Parser.CAP_K, 0)

        def CAP_L(self):
            return self.getToken(Rfc5424Parser.CAP_L, 0)

        def CAP_M(self):
            return self.getToken(Rfc5424Parser.CAP_M, 0)

        def CAP_N(self):
            return self.getToken(Rfc5424Parser.CAP_N, 0)

        def CAP_O(self):
            return self.getToken(Rfc5424Parser.CAP_O, 0)

        def CAP_P(self):
            return self.getToken(Rfc5424Parser.CAP_P, 0)

        def CAP_Q(self):
            return self.getToken(Rfc5424Parser.CAP_Q, 0)

        def CAP_R(self):
            return self.getToken(Rfc5424Parser.CAP_R, 0)

        def CAP_S(self):
            return self.getToken(Rfc5424Parser.CAP_S, 0)

        def CAP_T(self):
            return self.getToken(Rfc5424Parser.CAP_T, 0)

        def CAP_U(self):
            return self.getToken(Rfc5424Parser.CAP_U, 0)

        def CAP_V(self):
            return self.getToken(Rfc5424Parser.CAP_V, 0)

        def CAP_W(self):
            return self.getToken(Rfc5424Parser.CAP_W, 0)

        def CAP_X(self):
            return self.getToken(Rfc5424Parser.CAP_X, 0)

        def CAP_Y(self):
            return self.getToken(Rfc5424Parser.CAP_Y, 0)

        def CAP_Z(self):
            return self.getToken(Rfc5424Parser.CAP_Z, 0)

        def LEFT_BRACE(self):
            return self.getToken(Rfc5424Parser.LEFT_BRACE, 0)

        def BACKSLASH(self):
            return self.getToken(Rfc5424Parser.BACKSLASH, 0)

        def RIGHT_BRACE(self):
            return self.getToken(Rfc5424Parser.RIGHT_BRACE, 0)

        def CARAT(self):
            return self.getToken(Rfc5424Parser.CARAT, 0)

        def UNDERSCORE(self):
            return self.getToken(Rfc5424Parser.UNDERSCORE, 0)

        def ACCENT(self):
            return self.getToken(Rfc5424Parser.ACCENT, 0)

        def A(self):
            return self.getToken(Rfc5424Parser.A, 0)

        def B(self):
            return self.getToken(Rfc5424Parser.B, 0)

        def C(self):
            return self.getToken(Rfc5424Parser.C, 0)

        def D(self):
            return self.getToken(Rfc5424Parser.D, 0)

        def E(self):
            return self.getToken(Rfc5424Parser.E, 0)

        def F(self):
            return self.getToken(Rfc5424Parser.F, 0)

        def G(self):
            return self.getToken(Rfc5424Parser.G, 0)

        def H(self):
            return self.getToken(Rfc5424Parser.H, 0)

        def I(self):
            return self.getToken(Rfc5424Parser.I, 0)

        def J(self):
            return self.getToken(Rfc5424Parser.J, 0)

        def K(self):
            return self.getToken(Rfc5424Parser.K, 0)

        def L(self):
            return self.getToken(Rfc5424Parser.L, 0)

        def M(self):
            return self.getToken(Rfc5424Parser.M, 0)

        def N(self):
            return self.getToken(Rfc5424Parser.N, 0)

        def O(self):
            return self.getToken(Rfc5424Parser.O, 0)

        def P(self):
            return self.getToken(Rfc5424Parser.P, 0)

        def Q(self):
            return self.getToken(Rfc5424Parser.Q, 0)

        def R(self):
            return self.getToken(Rfc5424Parser.R, 0)

        def S(self):
            return self.getToken(Rfc5424Parser.S, 0)

        def T(self):
            return self.getToken(Rfc5424Parser.T, 0)

        def U(self):
            return self.getToken(Rfc5424Parser.U, 0)

        def V(self):
            return self.getToken(Rfc5424Parser.V, 0)

        def W(self):
            return self.getToken(Rfc5424Parser.W, 0)

        def X(self):
            return self.getToken(Rfc5424Parser.X, 0)

        def Y(self):
            return self.getToken(Rfc5424Parser.Y, 0)

        def Z(self):
            return self.getToken(Rfc5424Parser.Z, 0)

        def LEFT_CURLY_BRACE(self):
            return self.getToken(Rfc5424Parser.LEFT_CURLY_BRACE, 0)

        def PIPE(self):
            return self.getToken(Rfc5424Parser.PIPE, 0)

        def RIGHT_CURLY_BRACE(self):
            return self.getToken(Rfc5424Parser.RIGHT_CURLY_BRACE, 0)

        def TILDE(self):
            return self.getToken(Rfc5424Parser.TILDE, 0)

        def getRuleIndex(self):
            return Rfc5424Parser.RULE_printusascii

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintusascii" ):
                listener.enterPrintusascii(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintusascii" ):
                listener.exitPrintusascii(self)




    def printusascii(self):

        localctx = Rfc5424Parser.PrintusasciiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_printusascii)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.EXCLAMATION) | (1 << Rfc5424Parser.QUOTE) | (1 << Rfc5424Parser.POUND) | (1 << Rfc5424Parser.DOLLAR) | (1 << Rfc5424Parser.PERCENT) | (1 << Rfc5424Parser.AMPERSAND) | (1 << Rfc5424Parser.APOSTROPHE) | (1 << Rfc5424Parser.LEFT_PAREN) | (1 << Rfc5424Parser.RIGHT_PAREN) | (1 << Rfc5424Parser.ASTERISK) | (1 << Rfc5424Parser.PLUS) | (1 << Rfc5424Parser.COMMA) | (1 << Rfc5424Parser.DASH) | (1 << Rfc5424Parser.PERIOD) | (1 << Rfc5424Parser.SLASH) | (1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE) | (1 << Rfc5424Parser.COLON) | (1 << Rfc5424Parser.SEMICOLON) | (1 << Rfc5424Parser.LESS_THAN) | (1 << Rfc5424Parser.EQUALS) | (1 << Rfc5424Parser.GREATER_THAN) | (1 << Rfc5424Parser.QUESTION) | (1 << Rfc5424Parser.AT) | (1 << Rfc5424Parser.CAP_A) | (1 << Rfc5424Parser.CAP_B) | (1 << Rfc5424Parser.CAP_C) | (1 << Rfc5424Parser.CAP_D) | (1 << Rfc5424Parser.CAP_E) | (1 << Rfc5424Parser.CAP_F) | (1 << Rfc5424Parser.CAP_G) | (1 << Rfc5424Parser.CAP_H) | (1 << Rfc5424Parser.CAP_I) | (1 << Rfc5424Parser.CAP_J) | (1 << Rfc5424Parser.CAP_K) | (1 << Rfc5424Parser.CAP_L) | (1 << Rfc5424Parser.CAP_M) | (1 << Rfc5424Parser.CAP_N) | (1 << Rfc5424Parser.CAP_O) | (1 << Rfc5424Parser.CAP_P) | (1 << Rfc5424Parser.CAP_Q) | (1 << Rfc5424Parser.CAP_R) | (1 << Rfc5424Parser.CAP_S) | (1 << Rfc5424Parser.CAP_T) | (1 << Rfc5424Parser.CAP_U) | (1 << Rfc5424Parser.CAP_V) | (1 << Rfc5424Parser.CAP_W) | (1 << Rfc5424Parser.CAP_X) | (1 << Rfc5424Parser.CAP_Y) | (1 << Rfc5424Parser.CAP_Z) | (1 << Rfc5424Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc5424Parser.BACKSLASH - 64)) | (1 << (Rfc5424Parser.RIGHT_BRACE - 64)) | (1 << (Rfc5424Parser.CARAT - 64)) | (1 << (Rfc5424Parser.UNDERSCORE - 64)) | (1 << (Rfc5424Parser.ACCENT - 64)) | (1 << (Rfc5424Parser.A - 64)) | (1 << (Rfc5424Parser.B - 64)) | (1 << (Rfc5424Parser.C - 64)) | (1 << (Rfc5424Parser.D - 64)) | (1 << (Rfc5424Parser.E - 64)) | (1 << (Rfc5424Parser.F - 64)) | (1 << (Rfc5424Parser.G - 64)) | (1 << (Rfc5424Parser.H - 64)) | (1 << (Rfc5424Parser.I - 64)) | (1 << (Rfc5424Parser.J - 64)) | (1 << (Rfc5424Parser.K - 64)) | (1 << (Rfc5424Parser.L - 64)) | (1 << (Rfc5424Parser.M - 64)) | (1 << (Rfc5424Parser.N - 64)) | (1 << (Rfc5424Parser.O - 64)) | (1 << (Rfc5424Parser.P - 64)) | (1 << (Rfc5424Parser.Q - 64)) | (1 << (Rfc5424Parser.R - 64)) | (1 << (Rfc5424Parser.S - 64)) | (1 << (Rfc5424Parser.T - 64)) | (1 << (Rfc5424Parser.U - 64)) | (1 << (Rfc5424Parser.V - 64)) | (1 << (Rfc5424Parser.W - 64)) | (1 << (Rfc5424Parser.X - 64)) | (1 << (Rfc5424Parser.Y - 64)) | (1 << (Rfc5424Parser.Z - 64)) | (1 << (Rfc5424Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.PIPE - 64)) | (1 << (Rfc5424Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.TILDE - 64)))) != 0)):
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


    class PrintusasciinospecialsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCLAMATION(self):
            return self.getToken(Rfc5424Parser.EXCLAMATION, 0)

        def POUND(self):
            return self.getToken(Rfc5424Parser.POUND, 0)

        def DOLLAR(self):
            return self.getToken(Rfc5424Parser.DOLLAR, 0)

        def PERCENT(self):
            return self.getToken(Rfc5424Parser.PERCENT, 0)

        def AMPERSAND(self):
            return self.getToken(Rfc5424Parser.AMPERSAND, 0)

        def APOSTROPHE(self):
            return self.getToken(Rfc5424Parser.APOSTROPHE, 0)

        def LEFT_PAREN(self):
            return self.getToken(Rfc5424Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(Rfc5424Parser.RIGHT_PAREN, 0)

        def ASTERISK(self):
            return self.getToken(Rfc5424Parser.ASTERISK, 0)

        def PLUS(self):
            return self.getToken(Rfc5424Parser.PLUS, 0)

        def COMMA(self):
            return self.getToken(Rfc5424Parser.COMMA, 0)

        def DASH(self):
            return self.getToken(Rfc5424Parser.DASH, 0)

        def PERIOD(self):
            return self.getToken(Rfc5424Parser.PERIOD, 0)

        def SLASH(self):
            return self.getToken(Rfc5424Parser.SLASH, 0)

        def ZERO(self):
            return self.getToken(Rfc5424Parser.ZERO, 0)

        def ONE(self):
            return self.getToken(Rfc5424Parser.ONE, 0)

        def TWO(self):
            return self.getToken(Rfc5424Parser.TWO, 0)

        def THREE(self):
            return self.getToken(Rfc5424Parser.THREE, 0)

        def FOUR(self):
            return self.getToken(Rfc5424Parser.FOUR, 0)

        def FIVE(self):
            return self.getToken(Rfc5424Parser.FIVE, 0)

        def SIX(self):
            return self.getToken(Rfc5424Parser.SIX, 0)

        def SEVEN(self):
            return self.getToken(Rfc5424Parser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(Rfc5424Parser.EIGHT, 0)

        def NINE(self):
            return self.getToken(Rfc5424Parser.NINE, 0)

        def COLON(self):
            return self.getToken(Rfc5424Parser.COLON, 0)

        def SEMICOLON(self):
            return self.getToken(Rfc5424Parser.SEMICOLON, 0)

        def LESS_THAN(self):
            return self.getToken(Rfc5424Parser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(Rfc5424Parser.GREATER_THAN, 0)

        def QUESTION(self):
            return self.getToken(Rfc5424Parser.QUESTION, 0)

        def AT(self):
            return self.getToken(Rfc5424Parser.AT, 0)

        def CAP_A(self):
            return self.getToken(Rfc5424Parser.CAP_A, 0)

        def CAP_B(self):
            return self.getToken(Rfc5424Parser.CAP_B, 0)

        def CAP_C(self):
            return self.getToken(Rfc5424Parser.CAP_C, 0)

        def CAP_D(self):
            return self.getToken(Rfc5424Parser.CAP_D, 0)

        def CAP_E(self):
            return self.getToken(Rfc5424Parser.CAP_E, 0)

        def CAP_F(self):
            return self.getToken(Rfc5424Parser.CAP_F, 0)

        def CAP_G(self):
            return self.getToken(Rfc5424Parser.CAP_G, 0)

        def CAP_H(self):
            return self.getToken(Rfc5424Parser.CAP_H, 0)

        def CAP_I(self):
            return self.getToken(Rfc5424Parser.CAP_I, 0)

        def CAP_J(self):
            return self.getToken(Rfc5424Parser.CAP_J, 0)

        def CAP_K(self):
            return self.getToken(Rfc5424Parser.CAP_K, 0)

        def CAP_L(self):
            return self.getToken(Rfc5424Parser.CAP_L, 0)

        def CAP_M(self):
            return self.getToken(Rfc5424Parser.CAP_M, 0)

        def CAP_N(self):
            return self.getToken(Rfc5424Parser.CAP_N, 0)

        def CAP_O(self):
            return self.getToken(Rfc5424Parser.CAP_O, 0)

        def CAP_P(self):
            return self.getToken(Rfc5424Parser.CAP_P, 0)

        def CAP_Q(self):
            return self.getToken(Rfc5424Parser.CAP_Q, 0)

        def CAP_R(self):
            return self.getToken(Rfc5424Parser.CAP_R, 0)

        def CAP_S(self):
            return self.getToken(Rfc5424Parser.CAP_S, 0)

        def CAP_T(self):
            return self.getToken(Rfc5424Parser.CAP_T, 0)

        def CAP_U(self):
            return self.getToken(Rfc5424Parser.CAP_U, 0)

        def CAP_V(self):
            return self.getToken(Rfc5424Parser.CAP_V, 0)

        def CAP_W(self):
            return self.getToken(Rfc5424Parser.CAP_W, 0)

        def CAP_X(self):
            return self.getToken(Rfc5424Parser.CAP_X, 0)

        def CAP_Y(self):
            return self.getToken(Rfc5424Parser.CAP_Y, 0)

        def CAP_Z(self):
            return self.getToken(Rfc5424Parser.CAP_Z, 0)

        def LEFT_BRACE(self):
            return self.getToken(Rfc5424Parser.LEFT_BRACE, 0)

        def BACKSLASH(self):
            return self.getToken(Rfc5424Parser.BACKSLASH, 0)

        def CARAT(self):
            return self.getToken(Rfc5424Parser.CARAT, 0)

        def UNDERSCORE(self):
            return self.getToken(Rfc5424Parser.UNDERSCORE, 0)

        def ACCENT(self):
            return self.getToken(Rfc5424Parser.ACCENT, 0)

        def A(self):
            return self.getToken(Rfc5424Parser.A, 0)

        def B(self):
            return self.getToken(Rfc5424Parser.B, 0)

        def C(self):
            return self.getToken(Rfc5424Parser.C, 0)

        def D(self):
            return self.getToken(Rfc5424Parser.D, 0)

        def E(self):
            return self.getToken(Rfc5424Parser.E, 0)

        def F(self):
            return self.getToken(Rfc5424Parser.F, 0)

        def G(self):
            return self.getToken(Rfc5424Parser.G, 0)

        def H(self):
            return self.getToken(Rfc5424Parser.H, 0)

        def I(self):
            return self.getToken(Rfc5424Parser.I, 0)

        def J(self):
            return self.getToken(Rfc5424Parser.J, 0)

        def K(self):
            return self.getToken(Rfc5424Parser.K, 0)

        def L(self):
            return self.getToken(Rfc5424Parser.L, 0)

        def M(self):
            return self.getToken(Rfc5424Parser.M, 0)

        def N(self):
            return self.getToken(Rfc5424Parser.N, 0)

        def O(self):
            return self.getToken(Rfc5424Parser.O, 0)

        def P(self):
            return self.getToken(Rfc5424Parser.P, 0)

        def Q(self):
            return self.getToken(Rfc5424Parser.Q, 0)

        def R(self):
            return self.getToken(Rfc5424Parser.R, 0)

        def S(self):
            return self.getToken(Rfc5424Parser.S, 0)

        def T(self):
            return self.getToken(Rfc5424Parser.T, 0)

        def U(self):
            return self.getToken(Rfc5424Parser.U, 0)

        def V(self):
            return self.getToken(Rfc5424Parser.V, 0)

        def W(self):
            return self.getToken(Rfc5424Parser.W, 0)

        def X(self):
            return self.getToken(Rfc5424Parser.X, 0)

        def Y(self):
            return self.getToken(Rfc5424Parser.Y, 0)

        def Z(self):
            return self.getToken(Rfc5424Parser.Z, 0)

        def LEFT_CURLY_BRACE(self):
            return self.getToken(Rfc5424Parser.LEFT_CURLY_BRACE, 0)

        def PIPE(self):
            return self.getToken(Rfc5424Parser.PIPE, 0)

        def RIGHT_CURLY_BRACE(self):
            return self.getToken(Rfc5424Parser.RIGHT_CURLY_BRACE, 0)

        def TILDE(self):
            return self.getToken(Rfc5424Parser.TILDE, 0)

        def getRuleIndex(self):
            return Rfc5424Parser.RULE_printusasciinospecials

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintusasciinospecials" ):
                listener.enterPrintusasciinospecials(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintusasciinospecials" ):
                listener.exitPrintusasciinospecials(self)




    def printusasciinospecials(self):

        localctx = Rfc5424Parser.PrintusasciinospecialsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_printusasciinospecials)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.EXCLAMATION) | (1 << Rfc5424Parser.POUND) | (1 << Rfc5424Parser.DOLLAR) | (1 << Rfc5424Parser.PERCENT) | (1 << Rfc5424Parser.AMPERSAND) | (1 << Rfc5424Parser.APOSTROPHE) | (1 << Rfc5424Parser.LEFT_PAREN) | (1 << Rfc5424Parser.RIGHT_PAREN) | (1 << Rfc5424Parser.ASTERISK) | (1 << Rfc5424Parser.PLUS) | (1 << Rfc5424Parser.COMMA) | (1 << Rfc5424Parser.DASH) | (1 << Rfc5424Parser.PERIOD) | (1 << Rfc5424Parser.SLASH) | (1 << Rfc5424Parser.ZERO) | (1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE) | (1 << Rfc5424Parser.COLON) | (1 << Rfc5424Parser.SEMICOLON) | (1 << Rfc5424Parser.LESS_THAN) | (1 << Rfc5424Parser.GREATER_THAN) | (1 << Rfc5424Parser.QUESTION) | (1 << Rfc5424Parser.AT) | (1 << Rfc5424Parser.CAP_A) | (1 << Rfc5424Parser.CAP_B) | (1 << Rfc5424Parser.CAP_C) | (1 << Rfc5424Parser.CAP_D) | (1 << Rfc5424Parser.CAP_E) | (1 << Rfc5424Parser.CAP_F) | (1 << Rfc5424Parser.CAP_G) | (1 << Rfc5424Parser.CAP_H) | (1 << Rfc5424Parser.CAP_I) | (1 << Rfc5424Parser.CAP_J) | (1 << Rfc5424Parser.CAP_K) | (1 << Rfc5424Parser.CAP_L) | (1 << Rfc5424Parser.CAP_M) | (1 << Rfc5424Parser.CAP_N) | (1 << Rfc5424Parser.CAP_O) | (1 << Rfc5424Parser.CAP_P) | (1 << Rfc5424Parser.CAP_Q) | (1 << Rfc5424Parser.CAP_R) | (1 << Rfc5424Parser.CAP_S) | (1 << Rfc5424Parser.CAP_T) | (1 << Rfc5424Parser.CAP_U) | (1 << Rfc5424Parser.CAP_V) | (1 << Rfc5424Parser.CAP_W) | (1 << Rfc5424Parser.CAP_X) | (1 << Rfc5424Parser.CAP_Y) | (1 << Rfc5424Parser.CAP_Z) | (1 << Rfc5424Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc5424Parser.BACKSLASH - 64)) | (1 << (Rfc5424Parser.CARAT - 64)) | (1 << (Rfc5424Parser.UNDERSCORE - 64)) | (1 << (Rfc5424Parser.ACCENT - 64)) | (1 << (Rfc5424Parser.A - 64)) | (1 << (Rfc5424Parser.B - 64)) | (1 << (Rfc5424Parser.C - 64)) | (1 << (Rfc5424Parser.D - 64)) | (1 << (Rfc5424Parser.E - 64)) | (1 << (Rfc5424Parser.F - 64)) | (1 << (Rfc5424Parser.G - 64)) | (1 << (Rfc5424Parser.H - 64)) | (1 << (Rfc5424Parser.I - 64)) | (1 << (Rfc5424Parser.J - 64)) | (1 << (Rfc5424Parser.K - 64)) | (1 << (Rfc5424Parser.L - 64)) | (1 << (Rfc5424Parser.M - 64)) | (1 << (Rfc5424Parser.N - 64)) | (1 << (Rfc5424Parser.O - 64)) | (1 << (Rfc5424Parser.P - 64)) | (1 << (Rfc5424Parser.Q - 64)) | (1 << (Rfc5424Parser.R - 64)) | (1 << (Rfc5424Parser.S - 64)) | (1 << (Rfc5424Parser.T - 64)) | (1 << (Rfc5424Parser.U - 64)) | (1 << (Rfc5424Parser.V - 64)) | (1 << (Rfc5424Parser.W - 64)) | (1 << (Rfc5424Parser.X - 64)) | (1 << (Rfc5424Parser.Y - 64)) | (1 << (Rfc5424Parser.Z - 64)) | (1 << (Rfc5424Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.PIPE - 64)) | (1 << (Rfc5424Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc5424Parser.TILDE - 64)))) != 0)):
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


    class Nonzero_digitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ONE(self):
            return self.getToken(Rfc5424Parser.ONE, 0)

        def TWO(self):
            return self.getToken(Rfc5424Parser.TWO, 0)

        def THREE(self):
            return self.getToken(Rfc5424Parser.THREE, 0)

        def FOUR(self):
            return self.getToken(Rfc5424Parser.FOUR, 0)

        def FIVE(self):
            return self.getToken(Rfc5424Parser.FIVE, 0)

        def SIX(self):
            return self.getToken(Rfc5424Parser.SIX, 0)

        def SEVEN(self):
            return self.getToken(Rfc5424Parser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(Rfc5424Parser.EIGHT, 0)

        def NINE(self):
            return self.getToken(Rfc5424Parser.NINE, 0)

        def getRuleIndex(self):
            return Rfc5424Parser.RULE_nonzero_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonzero_digit" ):
                listener.enterNonzero_digit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonzero_digit" ):
                listener.exitNonzero_digit(self)




    def nonzero_digit(self):

        localctx = Rfc5424Parser.Nonzero_digitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_nonzero_digit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc5424Parser.ONE) | (1 << Rfc5424Parser.TWO) | (1 << Rfc5424Parser.THREE) | (1 << Rfc5424Parser.FOUR) | (1 << Rfc5424Parser.FIVE) | (1 << Rfc5424Parser.SIX) | (1 << Rfc5424Parser.SEVEN) | (1 << Rfc5424Parser.EIGHT) | (1 << Rfc5424Parser.NINE))) != 0)):
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


    class DigitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Rfc5424Parser.RULE_digit

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ZeroDigitContext(DigitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.DigitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ZERO(self):
            return self.getToken(Rfc5424Parser.ZERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterZeroDigit" ):
                listener.enterZeroDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitZeroDigit" ):
                listener.exitZeroDigit(self)


    class NonZeroDigitContext(DigitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc5424Parser.DigitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nonzero_digit(self):
            return self.getTypedRuleContext(Rfc5424Parser.Nonzero_digitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonZeroDigit" ):
                listener.enterNonZeroDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonZeroDigit" ):
                listener.exitNonZeroDigit(self)



    def digit(self):

        localctx = Rfc5424Parser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_digit)
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Rfc5424Parser.ZERO]:
                localctx = Rfc5424Parser.ZeroDigitContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(Rfc5424Parser.ZERO)
                pass
            elif token in [Rfc5424Parser.ONE, Rfc5424Parser.TWO, Rfc5424Parser.THREE, Rfc5424Parser.FOUR, Rfc5424Parser.FIVE, Rfc5424Parser.SIX, Rfc5424Parser.SEVEN, Rfc5424Parser.EIGHT, Rfc5424Parser.NINE]:
                localctx = Rfc5424Parser.NonZeroDigitContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.nonzero_digit()
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


    class NilvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(Rfc5424Parser.DASH, 0)

        def getRuleIndex(self):
            return Rfc5424Parser.RULE_nilvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNilvalue" ):
                listener.enterNilvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNilvalue" ):
                listener.exitNilvalue(self)




    def nilvalue(self):

        localctx = Rfc5424Parser.NilvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_nilvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(Rfc5424Parser.DASH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





