# Generated from grammars/Rfc3164.g4 by ANTLR 4.10.1
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
        4,1,257,246,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,1,0,1,0,5,0,71,8,0,10,0,12,0,74,9,0,1,0,1,0,1,0,1,1,1,1,
        1,1,3,1,82,8,1,1,2,3,2,85,8,2,1,2,3,2,88,8,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,4,1,4,3,4,100,8,4,1,4,1,4,1,4,3,4,105,8,4,1,5,5,5,
        108,8,5,10,5,12,5,111,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,122,8,6,1,7,1,7,1,7,1,7,1,8,1,8,3,8,130,8,8,1,8,1,8,3,8,134,8,
        8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,
        162,8,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,
        1,18,3,18,176,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,3,18,196,8,18,1,19,
        1,19,3,19,200,8,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,3,21,209,8,
        21,1,22,5,22,212,8,22,10,22,12,22,215,9,22,1,23,1,23,1,23,1,24,1,
        24,1,25,5,25,223,8,25,10,25,12,25,226,9,25,1,26,1,26,1,27,1,27,1,
        28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,3,31,240,8,31,1,32,1,32,1,
        33,1,33,1,33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,8,2,0,15,15,
        17,17,3,0,188,188,192,192,240,240,1,0,1,256,1,0,5,98,4,0,5,5,7,32,
        34,64,66,98,1,0,21,29,1,0,37,62,1,0,69,94,232,0,68,1,0,0,0,2,78,
        1,0,0,0,4,84,1,0,0,0,6,93,1,0,0,0,8,97,1,0,0,0,10,109,1,0,0,0,12,
        121,1,0,0,0,14,123,1,0,0,0,16,127,1,0,0,0,18,135,1,0,0,0,20,141,
        1,0,0,0,22,146,1,0,0,0,24,149,1,0,0,0,26,152,1,0,0,0,28,155,1,0,
        0,0,30,163,1,0,0,0,32,166,1,0,0,0,34,169,1,0,0,0,36,172,1,0,0,0,
        38,199,1,0,0,0,40,201,1,0,0,0,42,208,1,0,0,0,44,213,1,0,0,0,46,216,
        1,0,0,0,48,219,1,0,0,0,50,224,1,0,0,0,52,227,1,0,0,0,54,229,1,0,
        0,0,56,231,1,0,0,0,58,233,1,0,0,0,60,235,1,0,0,0,62,239,1,0,0,0,
        64,241,1,0,0,0,66,243,1,0,0,0,68,72,3,60,30,0,69,71,3,62,31,0,70,
        69,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,
        0,74,72,1,0,0,0,75,76,3,54,27,0,76,77,3,2,1,0,77,1,1,0,0,0,78,79,
        3,4,2,0,79,81,3,54,27,0,80,82,3,42,21,0,81,80,1,0,0,0,81,82,1,0,
        0,0,82,3,1,0,0,0,83,85,3,6,3,0,84,83,1,0,0,0,84,85,1,0,0,0,85,87,
        1,0,0,0,86,88,3,54,27,0,87,86,1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,
        0,89,90,3,12,6,0,90,91,3,54,27,0,91,92,3,10,5,0,92,5,1,0,0,0,93,
        94,5,32,0,0,94,95,3,8,4,0,95,96,5,34,0,0,96,7,1,0,0,0,97,104,3,62,
        31,0,98,100,3,62,31,0,99,98,1,0,0,0,99,100,1,0,0,0,100,105,1,0,0,
        0,101,102,3,62,31,0,102,103,3,62,31,0,103,105,1,0,0,0,104,99,1,0,
        0,0,104,101,1,0,0,0,105,9,1,0,0,0,106,108,3,56,28,0,107,106,1,0,
        0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,11,1,0,0,
        0,111,109,1,0,0,0,112,113,3,18,9,0,113,114,5,56,0,0,114,115,3,26,
        13,0,115,122,1,0,0,0,116,117,3,14,7,0,117,118,3,16,8,0,118,119,3,
        54,27,0,119,120,3,28,14,0,120,122,1,0,0,0,121,112,1,0,0,0,121,116,
        1,0,0,0,122,13,1,0,0,0,123,124,3,64,32,0,124,125,3,66,33,0,125,126,
        3,66,33,0,126,15,1,0,0,0,127,129,3,54,27,0,128,130,3,54,27,0,129,
        128,1,0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,133,3,62,31,0,132,
        134,3,62,31,0,133,132,1,0,0,0,133,134,1,0,0,0,134,17,1,0,0,0,135,
        136,3,20,10,0,136,137,5,17,0,0,137,138,3,22,11,0,138,139,5,17,0,
        0,139,140,3,24,12,0,140,19,1,0,0,0,141,142,3,62,31,0,142,143,3,62,
        31,0,143,144,3,62,31,0,144,145,3,62,31,0,145,21,1,0,0,0,146,147,
        3,62,31,0,147,148,3,62,31,0,148,23,1,0,0,0,149,150,3,62,31,0,150,
        151,3,62,31,0,151,25,1,0,0,0,152,153,3,28,14,0,153,154,3,38,19,0,
        154,27,1,0,0,0,155,156,3,30,15,0,156,157,5,30,0,0,157,158,3,32,16,
        0,158,159,5,30,0,0,159,161,3,34,17,0,160,162,3,36,18,0,161,160,1,
        0,0,0,161,162,1,0,0,0,162,29,1,0,0,0,163,164,3,62,31,0,164,165,3,
        62,31,0,165,31,1,0,0,0,166,167,3,62,31,0,167,168,3,62,31,0,168,33,
        1,0,0,0,169,170,3,62,31,0,170,171,3,62,31,0,171,35,1,0,0,0,172,173,
        5,18,0,0,173,195,3,62,31,0,174,176,3,62,31,0,175,174,1,0,0,0,175,
        176,1,0,0,0,176,196,1,0,0,0,177,178,3,62,31,0,178,179,3,62,31,0,
        179,196,1,0,0,0,180,181,3,62,31,0,181,182,3,62,31,0,182,183,3,62,
        31,0,183,196,1,0,0,0,184,185,3,62,31,0,185,186,3,62,31,0,186,187,
        3,62,31,0,187,188,3,62,31,0,188,196,1,0,0,0,189,190,3,62,31,0,190,
        191,3,62,31,0,191,192,3,62,31,0,192,193,3,62,31,0,193,194,3,62,31,
        0,194,196,1,0,0,0,195,175,1,0,0,0,195,177,1,0,0,0,195,180,1,0,0,
        0,195,184,1,0,0,0,195,189,1,0,0,0,196,37,1,0,0,0,197,200,5,62,0,
        0,198,200,3,40,20,0,199,197,1,0,0,0,199,198,1,0,0,0,200,39,1,0,0,
        0,201,202,7,0,0,0,202,203,3,30,15,0,203,204,5,30,0,0,204,205,3,32,
        16,0,205,41,1,0,0,0,206,209,3,44,22,0,207,209,3,46,23,0,208,206,
        1,0,0,0,208,207,1,0,0,0,209,43,1,0,0,0,210,212,3,52,26,0,211,210,
        1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,45,1,
        0,0,0,215,213,1,0,0,0,216,217,3,48,24,0,217,218,3,50,25,0,218,47,
        1,0,0,0,219,220,7,1,0,0,220,49,1,0,0,0,221,223,3,52,26,0,222,221,
        1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,51,1,
        0,0,0,226,224,1,0,0,0,227,228,7,2,0,0,228,53,1,0,0,0,229,230,5,4,
        0,0,230,55,1,0,0,0,231,232,7,3,0,0,232,57,1,0,0,0,233,234,7,4,0,
        0,234,59,1,0,0,0,235,236,7,5,0,0,236,61,1,0,0,0,237,240,5,20,0,0,
        238,240,3,60,30,0,239,237,1,0,0,0,239,238,1,0,0,0,240,63,1,0,0,0,
        241,242,7,6,0,0,242,65,1,0,0,0,243,244,7,7,0,0,244,67,1,0,0,0,18,
        72,81,84,87,99,104,109,121,129,133,161,175,195,199,208,213,224,239
    ]

class Rfc3164Parser ( Parser ):

    grammarFileName = "Rfc3164.g4"

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
                     "'\\u00FF'" ]

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
                      "U_00FD", "U_00FE", "U_00FF", "WS" ]

    RULE_octet_prefixed = 0
    RULE_syslog_msg = 1
    RULE_header = 2
    RULE_pri = 3
    RULE_prival = 4
    RULE_hostname = 5
    RULE_timestamp = 6
    RULE_date_month_short = 7
    RULE_date_day_short = 8
    RULE_full_date = 9
    RULE_date_fullyear = 10
    RULE_date_month = 11
    RULE_date_mday = 12
    RULE_full_time = 13
    RULE_partial_time = 14
    RULE_time_hour = 15
    RULE_time_minute = 16
    RULE_time_second = 17
    RULE_time_secfrac = 18
    RULE_time_offset = 19
    RULE_time_numoffset = 20
    RULE_msg = 21
    RULE_msg_any = 22
    RULE_msg_utf8 = 23
    RULE_bom = 24
    RULE_utf_8_string = 25
    RULE_octet = 26
    RULE_sp = 27
    RULE_printusascii = 28
    RULE_printusasciinospecials = 29
    RULE_nonzero_digit = 30
    RULE_digit = 31
    RULE_capital = 32
    RULE_lower = 33

    ruleNames =  [ "octet_prefixed", "syslog_msg", "header", "pri", "prival", 
                   "hostname", "timestamp", "date_month_short", "date_day_short", 
                   "full_date", "date_fullyear", "date_month", "date_mday", 
                   "full_time", "partial_time", "time_hour", "time_minute", 
                   "time_second", "time_secfrac", "time_offset", "time_numoffset", 
                   "msg", "msg_any", "msg_utf8", "bom", "utf_8_string", 
                   "octet", "sp", "printusascii", "printusasciinospecials", 
                   "nonzero_digit", "digit", "capital", "lower" ]

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
    WS=257

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Octet_prefixedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonzero_digit(self):
            return self.getTypedRuleContext(Rfc3164Parser.Nonzero_digitContext,0)


        def sp(self):
            return self.getTypedRuleContext(Rfc3164Parser.SpContext,0)


        def syslog_msg(self):
            return self.getTypedRuleContext(Rfc3164Parser.Syslog_msgContext,0)


        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_octet_prefixed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOctet_prefixed" ):
                listener.enterOctet_prefixed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOctet_prefixed" ):
                listener.exitOctet_prefixed(self)




    def octet_prefixed(self):

        localctx = Rfc3164Parser.Octet_prefixedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_octet_prefixed)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.nonzero_digit()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc3164Parser.ZERO) | (1 << Rfc3164Parser.ONE) | (1 << Rfc3164Parser.TWO) | (1 << Rfc3164Parser.THREE) | (1 << Rfc3164Parser.FOUR) | (1 << Rfc3164Parser.FIVE) | (1 << Rfc3164Parser.SIX) | (1 << Rfc3164Parser.SEVEN) | (1 << Rfc3164Parser.EIGHT) | (1 << Rfc3164Parser.NINE))) != 0):
                self.state = 69
                self.digit()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.sp()
            self.state = 76
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
            return Rfc3164Parser.RULE_syslog_msg

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SyslogMsgContext(Syslog_msgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.Syslog_msgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def header(self):
            return self.getTypedRuleContext(Rfc3164Parser.HeaderContext,0)

        def sp(self):
            return self.getTypedRuleContext(Rfc3164Parser.SpContext,0)

        def msg(self):
            return self.getTypedRuleContext(Rfc3164Parser.MsgContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSyslogMsg" ):
                listener.enterSyslogMsg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSyslogMsg" ):
                listener.exitSyslogMsg(self)



    def syslog_msg(self):

        localctx = Rfc3164Parser.Syslog_msgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_syslog_msg)
        try:
            localctx = Rfc3164Parser.SyslogMsgContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.header()
            self.state = 79
            self.sp()
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 80
                self.msg()


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
            return Rfc3164Parser.RULE_header

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SyslogHeaderContext(HeaderContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.HeaderContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def timestamp(self):
            return self.getTypedRuleContext(Rfc3164Parser.TimestampContext,0)

        def sp(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.SpContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.SpContext,i)

        def hostname(self):
            return self.getTypedRuleContext(Rfc3164Parser.HostnameContext,0)

        def pri(self):
            return self.getTypedRuleContext(Rfc3164Parser.PriContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSyslogHeader" ):
                listener.enterSyslogHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSyslogHeader" ):
                listener.exitSyslogHeader(self)



    def header(self):

        localctx = Rfc3164Parser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_header)
        self._la = 0 # Token type
        try:
            localctx = Rfc3164Parser.SyslogHeaderContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Rfc3164Parser.LESS_THAN:
                self.state = 83
                self.pri()


            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Rfc3164Parser.SPACE:
                self.state = 86
                self.sp()


            self.state = 89
            self.timestamp()
            self.state = 90
            self.sp()
            self.state = 91
            self.hostname()
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
            return Rfc3164Parser.RULE_pri

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderPriorityContext(PriContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.PriContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LESS_THAN(self):
            return self.getToken(Rfc3164Parser.LESS_THAN, 0)
        def prival(self):
            return self.getTypedRuleContext(Rfc3164Parser.PrivalContext,0)

        def GREATER_THAN(self):
            return self.getToken(Rfc3164Parser.GREATER_THAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderPriority" ):
                listener.enterHeaderPriority(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderPriority" ):
                listener.exitHeaderPriority(self)



    def pri(self):

        localctx = Rfc3164Parser.PriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pri)
        try:
            localctx = Rfc3164Parser.HeaderPriorityContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(Rfc3164Parser.LESS_THAN)
            self.state = 94
            self.prival()
            self.state = 95
            self.match(Rfc3164Parser.GREATER_THAN)
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
            return Rfc3164Parser.RULE_prival

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderPriorityValueContext(PrivalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.PrivalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderPriorityValue" ):
                listener.enterHeaderPriorityValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderPriorityValue" ):
                listener.exitHeaderPriorityValue(self)



    def prival(self):

        localctx = Rfc3164Parser.PrivalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_prival)
        self._la = 0 # Token type
        try:
            localctx = Rfc3164Parser.HeaderPriorityValueContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.digit()
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc3164Parser.ZERO) | (1 << Rfc3164Parser.ONE) | (1 << Rfc3164Parser.TWO) | (1 << Rfc3164Parser.THREE) | (1 << Rfc3164Parser.FOUR) | (1 << Rfc3164Parser.FIVE) | (1 << Rfc3164Parser.SIX) | (1 << Rfc3164Parser.SEVEN) | (1 << Rfc3164Parser.EIGHT) | (1 << Rfc3164Parser.NINE))) != 0):
                    self.state = 98
                    self.digit()


                pass

            elif la_ == 2:
                self.state = 101
                self.digit()
                self.state = 102
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
            return Rfc3164Parser.RULE_hostname

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderHostNameContext(HostnameContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.HostnameContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printusascii(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.PrintusasciiContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.PrintusasciiContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderHostName" ):
                listener.enterHeaderHostName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderHostName" ):
                listener.exitHeaderHostName(self)



    def hostname(self):

        localctx = Rfc3164Parser.HostnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hostname)
        self._la = 0 # Token type
        try:
            localctx = Rfc3164Parser.HeaderHostNameContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc3164Parser.EXCLAMATION) | (1 << Rfc3164Parser.QUOTE) | (1 << Rfc3164Parser.POUND) | (1 << Rfc3164Parser.DOLLAR) | (1 << Rfc3164Parser.PERCENT) | (1 << Rfc3164Parser.AMPERSAND) | (1 << Rfc3164Parser.APOSTROPHE) | (1 << Rfc3164Parser.LEFT_PAREN) | (1 << Rfc3164Parser.RIGHT_PAREN) | (1 << Rfc3164Parser.ASTERISK) | (1 << Rfc3164Parser.PLUS) | (1 << Rfc3164Parser.COMMA) | (1 << Rfc3164Parser.DASH) | (1 << Rfc3164Parser.PERIOD) | (1 << Rfc3164Parser.SLASH) | (1 << Rfc3164Parser.ZERO) | (1 << Rfc3164Parser.ONE) | (1 << Rfc3164Parser.TWO) | (1 << Rfc3164Parser.THREE) | (1 << Rfc3164Parser.FOUR) | (1 << Rfc3164Parser.FIVE) | (1 << Rfc3164Parser.SIX) | (1 << Rfc3164Parser.SEVEN) | (1 << Rfc3164Parser.EIGHT) | (1 << Rfc3164Parser.NINE) | (1 << Rfc3164Parser.COLON) | (1 << Rfc3164Parser.SEMICOLON) | (1 << Rfc3164Parser.LESS_THAN) | (1 << Rfc3164Parser.EQUALS) | (1 << Rfc3164Parser.GREATER_THAN) | (1 << Rfc3164Parser.QUESTION) | (1 << Rfc3164Parser.AT) | (1 << Rfc3164Parser.CAP_A) | (1 << Rfc3164Parser.CAP_B) | (1 << Rfc3164Parser.CAP_C) | (1 << Rfc3164Parser.CAP_D) | (1 << Rfc3164Parser.CAP_E) | (1 << Rfc3164Parser.CAP_F) | (1 << Rfc3164Parser.CAP_G) | (1 << Rfc3164Parser.CAP_H) | (1 << Rfc3164Parser.CAP_I) | (1 << Rfc3164Parser.CAP_J) | (1 << Rfc3164Parser.CAP_K) | (1 << Rfc3164Parser.CAP_L) | (1 << Rfc3164Parser.CAP_M) | (1 << Rfc3164Parser.CAP_N) | (1 << Rfc3164Parser.CAP_O) | (1 << Rfc3164Parser.CAP_P) | (1 << Rfc3164Parser.CAP_Q) | (1 << Rfc3164Parser.CAP_R) | (1 << Rfc3164Parser.CAP_S) | (1 << Rfc3164Parser.CAP_T) | (1 << Rfc3164Parser.CAP_U) | (1 << Rfc3164Parser.CAP_V) | (1 << Rfc3164Parser.CAP_W) | (1 << Rfc3164Parser.CAP_X) | (1 << Rfc3164Parser.CAP_Y) | (1 << Rfc3164Parser.CAP_Z) | (1 << Rfc3164Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc3164Parser.BACKSLASH - 64)) | (1 << (Rfc3164Parser.RIGHT_BRACE - 64)) | (1 << (Rfc3164Parser.CARAT - 64)) | (1 << (Rfc3164Parser.UNDERSCORE - 64)) | (1 << (Rfc3164Parser.ACCENT - 64)) | (1 << (Rfc3164Parser.A - 64)) | (1 << (Rfc3164Parser.B - 64)) | (1 << (Rfc3164Parser.C - 64)) | (1 << (Rfc3164Parser.D - 64)) | (1 << (Rfc3164Parser.E - 64)) | (1 << (Rfc3164Parser.F - 64)) | (1 << (Rfc3164Parser.G - 64)) | (1 << (Rfc3164Parser.H - 64)) | (1 << (Rfc3164Parser.I - 64)) | (1 << (Rfc3164Parser.J - 64)) | (1 << (Rfc3164Parser.K - 64)) | (1 << (Rfc3164Parser.L - 64)) | (1 << (Rfc3164Parser.M - 64)) | (1 << (Rfc3164Parser.N - 64)) | (1 << (Rfc3164Parser.O - 64)) | (1 << (Rfc3164Parser.P - 64)) | (1 << (Rfc3164Parser.Q - 64)) | (1 << (Rfc3164Parser.R - 64)) | (1 << (Rfc3164Parser.S - 64)) | (1 << (Rfc3164Parser.T - 64)) | (1 << (Rfc3164Parser.U - 64)) | (1 << (Rfc3164Parser.V - 64)) | (1 << (Rfc3164Parser.W - 64)) | (1 << (Rfc3164Parser.X - 64)) | (1 << (Rfc3164Parser.Y - 64)) | (1 << (Rfc3164Parser.Z - 64)) | (1 << (Rfc3164Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc3164Parser.PIPE - 64)) | (1 << (Rfc3164Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc3164Parser.TILDE - 64)))) != 0):
                self.state = 106
                self.printusascii()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return Rfc3164Parser.RULE_timestamp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HeaderTimeStamp3164Context(TimestampContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.TimestampContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def date_month_short(self):
            return self.getTypedRuleContext(Rfc3164Parser.Date_month_shortContext,0)

        def date_day_short(self):
            return self.getTypedRuleContext(Rfc3164Parser.Date_day_shortContext,0)

        def sp(self):
            return self.getTypedRuleContext(Rfc3164Parser.SpContext,0)

        def partial_time(self):
            return self.getTypedRuleContext(Rfc3164Parser.Partial_timeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderTimeStamp3164" ):
                listener.enterHeaderTimeStamp3164(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderTimeStamp3164" ):
                listener.exitHeaderTimeStamp3164(self)


    class HeaderTimeStampContext(TimestampContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.TimestampContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def full_date(self):
            return self.getTypedRuleContext(Rfc3164Parser.Full_dateContext,0)

        def CAP_T(self):
            return self.getToken(Rfc3164Parser.CAP_T, 0)
        def full_time(self):
            return self.getTypedRuleContext(Rfc3164Parser.Full_timeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderTimeStamp" ):
                listener.enterHeaderTimeStamp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderTimeStamp" ):
                listener.exitHeaderTimeStamp(self)



    def timestamp(self):

        localctx = Rfc3164Parser.TimestampContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_timestamp)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Rfc3164Parser.ZERO, Rfc3164Parser.ONE, Rfc3164Parser.TWO, Rfc3164Parser.THREE, Rfc3164Parser.FOUR, Rfc3164Parser.FIVE, Rfc3164Parser.SIX, Rfc3164Parser.SEVEN, Rfc3164Parser.EIGHT, Rfc3164Parser.NINE]:
                localctx = Rfc3164Parser.HeaderTimeStampContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.full_date()
                self.state = 113
                self.match(Rfc3164Parser.CAP_T)
                self.state = 114
                self.full_time()
                pass
            elif token in [Rfc3164Parser.CAP_A, Rfc3164Parser.CAP_B, Rfc3164Parser.CAP_C, Rfc3164Parser.CAP_D, Rfc3164Parser.CAP_E, Rfc3164Parser.CAP_F, Rfc3164Parser.CAP_G, Rfc3164Parser.CAP_H, Rfc3164Parser.CAP_I, Rfc3164Parser.CAP_J, Rfc3164Parser.CAP_K, Rfc3164Parser.CAP_L, Rfc3164Parser.CAP_M, Rfc3164Parser.CAP_N, Rfc3164Parser.CAP_O, Rfc3164Parser.CAP_P, Rfc3164Parser.CAP_Q, Rfc3164Parser.CAP_R, Rfc3164Parser.CAP_S, Rfc3164Parser.CAP_T, Rfc3164Parser.CAP_U, Rfc3164Parser.CAP_V, Rfc3164Parser.CAP_W, Rfc3164Parser.CAP_X, Rfc3164Parser.CAP_Y, Rfc3164Parser.CAP_Z]:
                localctx = Rfc3164Parser.HeaderTimeStamp3164Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.date_month_short()
                self.state = 117
                self.date_day_short()
                self.state = 118
                self.sp()
                self.state = 119
                self.partial_time()
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


    class Date_month_shortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def capital(self):
            return self.getTypedRuleContext(Rfc3164Parser.CapitalContext,0)


        def lower(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.LowerContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.LowerContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_date_month_short

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate_month_short" ):
                listener.enterDate_month_short(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate_month_short" ):
                listener.exitDate_month_short(self)




    def date_month_short(self):

        localctx = Rfc3164Parser.Date_month_shortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_date_month_short)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.capital()
            self.state = 124
            self.lower()
            self.state = 125
            self.lower()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Date_day_shortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sp(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.SpContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.SpContext,i)


        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_date_day_short

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate_day_short" ):
                listener.enterDate_day_short(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate_day_short" ):
                listener.exitDate_day_short(self)




    def date_day_short(self):

        localctx = Rfc3164Parser.Date_day_shortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_date_day_short)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.sp()

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Rfc3164Parser.SPACE:
                self.state = 128
                self.sp()


            self.state = 131
            self.digit()

            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc3164Parser.ZERO) | (1 << Rfc3164Parser.ONE) | (1 << Rfc3164Parser.TWO) | (1 << Rfc3164Parser.THREE) | (1 << Rfc3164Parser.FOUR) | (1 << Rfc3164Parser.FIVE) | (1 << Rfc3164Parser.SIX) | (1 << Rfc3164Parser.SEVEN) | (1 << Rfc3164Parser.EIGHT) | (1 << Rfc3164Parser.NINE))) != 0):
                self.state = 132
                self.digit()


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
            return self.getTypedRuleContext(Rfc3164Parser.Date_fullyearContext,0)


        def DASH(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc3164Parser.DASH)
            else:
                return self.getToken(Rfc3164Parser.DASH, i)

        def date_month(self):
            return self.getTypedRuleContext(Rfc3164Parser.Date_monthContext,0)


        def date_mday(self):
            return self.getTypedRuleContext(Rfc3164Parser.Date_mdayContext,0)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_full_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFull_date" ):
                listener.enterFull_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFull_date" ):
                listener.exitFull_date(self)




    def full_date(self):

        localctx = Rfc3164Parser.Full_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_full_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.date_fullyear()
            self.state = 136
            self.match(Rfc3164Parser.DASH)
            self.state = 137
            self.date_month()
            self.state = 138
            self.match(Rfc3164Parser.DASH)
            self.state = 139
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
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_date_fullyear

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate_fullyear" ):
                listener.enterDate_fullyear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate_fullyear" ):
                listener.exitDate_fullyear(self)




    def date_fullyear(self):

        localctx = Rfc3164Parser.Date_fullyearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_date_fullyear)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.digit()
            self.state = 142
            self.digit()
            self.state = 143
            self.digit()
            self.state = 144
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
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_date_month

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate_month" ):
                listener.enterDate_month(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate_month" ):
                listener.exitDate_month(self)




    def date_month(self):

        localctx = Rfc3164Parser.Date_monthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_date_month)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.digit()
            self.state = 147
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
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_date_mday

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate_mday" ):
                listener.enterDate_mday(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate_mday" ):
                listener.exitDate_mday(self)




    def date_mday(self):

        localctx = Rfc3164Parser.Date_mdayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_date_mday)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.digit()
            self.state = 150
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
            return self.getTypedRuleContext(Rfc3164Parser.Partial_timeContext,0)


        def time_offset(self):
            return self.getTypedRuleContext(Rfc3164Parser.Time_offsetContext,0)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_full_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFull_time" ):
                listener.enterFull_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFull_time" ):
                listener.exitFull_time(self)




    def full_time(self):

        localctx = Rfc3164Parser.Full_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_full_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.partial_time()
            self.state = 153
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
            return self.getTypedRuleContext(Rfc3164Parser.Time_hourContext,0)


        def COLON(self, i: Optional[int]=None):
            if i is None:
                return self.getTokens(Rfc3164Parser.COLON)
            else:
                return self.getToken(Rfc3164Parser.COLON, i)

        def time_minute(self):
            return self.getTypedRuleContext(Rfc3164Parser.Time_minuteContext,0)


        def time_second(self):
            return self.getTypedRuleContext(Rfc3164Parser.Time_secondContext,0)


        def time_secfrac(self):
            return self.getTypedRuleContext(Rfc3164Parser.Time_secfracContext,0)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_partial_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartial_time" ):
                listener.enterPartial_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartial_time" ):
                listener.exitPartial_time(self)




    def partial_time(self):

        localctx = Rfc3164Parser.Partial_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_partial_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.time_hour()
            self.state = 156
            self.match(Rfc3164Parser.COLON)
            self.state = 157
            self.time_minute()
            self.state = 158
            self.match(Rfc3164Parser.COLON)
            self.state = 159
            self.time_second()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Rfc3164Parser.PERIOD:
                self.state = 160
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
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_time_hour

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_hour" ):
                listener.enterTime_hour(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_hour" ):
                listener.exitTime_hour(self)




    def time_hour(self):

        localctx = Rfc3164Parser.Time_hourContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_time_hour)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.digit()
            self.state = 164
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
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_time_minute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_minute" ):
                listener.enterTime_minute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_minute" ):
                listener.exitTime_minute(self)




    def time_minute(self):

        localctx = Rfc3164Parser.Time_minuteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_time_minute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.digit()
            self.state = 167
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
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_time_second

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_second" ):
                listener.enterTime_second(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_second" ):
                listener.exitTime_second(self)




    def time_second(self):

        localctx = Rfc3164Parser.Time_secondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_time_second)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.digit()
            self.state = 170
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
            return self.getToken(Rfc3164Parser.PERIOD, 0)

        def digit(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.DigitContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.DigitContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_time_secfrac

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_secfrac" ):
                listener.enterTime_secfrac(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_secfrac" ):
                listener.exitTime_secfrac(self)




    def time_secfrac(self):

        localctx = Rfc3164Parser.Time_secfracContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_time_secfrac)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(Rfc3164Parser.PERIOD)
            self.state = 173
            self.digit()
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc3164Parser.ZERO) | (1 << Rfc3164Parser.ONE) | (1 << Rfc3164Parser.TWO) | (1 << Rfc3164Parser.THREE) | (1 << Rfc3164Parser.FOUR) | (1 << Rfc3164Parser.FIVE) | (1 << Rfc3164Parser.SIX) | (1 << Rfc3164Parser.SEVEN) | (1 << Rfc3164Parser.EIGHT) | (1 << Rfc3164Parser.NINE))) != 0):
                    self.state = 174
                    self.digit()


                pass

            elif la_ == 2:
                self.state = 177
                self.digit()
                self.state = 178
                self.digit()
                pass

            elif la_ == 3:
                self.state = 180
                self.digit()
                self.state = 181
                self.digit()
                self.state = 182
                self.digit()
                pass

            elif la_ == 4:
                self.state = 184
                self.digit()
                self.state = 185
                self.digit()
                self.state = 186
                self.digit()
                self.state = 187
                self.digit()
                pass

            elif la_ == 5:
                self.state = 189
                self.digit()
                self.state = 190
                self.digit()
                self.state = 191
                self.digit()
                self.state = 192
                self.digit()
                self.state = 193
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
            return self.getToken(Rfc3164Parser.CAP_Z, 0)

        def time_numoffset(self):
            return self.getTypedRuleContext(Rfc3164Parser.Time_numoffsetContext,0)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_time_offset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_offset" ):
                listener.enterTime_offset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_offset" ):
                listener.exitTime_offset(self)




    def time_offset(self):

        localctx = Rfc3164Parser.Time_offsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_time_offset)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Rfc3164Parser.CAP_Z]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(Rfc3164Parser.CAP_Z)
                pass
            elif token in [Rfc3164Parser.PLUS, Rfc3164Parser.DASH]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
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
            return self.getTypedRuleContext(Rfc3164Parser.Time_hourContext,0)


        def COLON(self):
            return self.getToken(Rfc3164Parser.COLON, 0)

        def time_minute(self):
            return self.getTypedRuleContext(Rfc3164Parser.Time_minuteContext,0)


        def PLUS(self):
            return self.getToken(Rfc3164Parser.PLUS, 0)

        def DASH(self):
            return self.getToken(Rfc3164Parser.DASH, 0)

        def getRuleIndex(self):
            return Rfc3164Parser.RULE_time_numoffset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_numoffset" ):
                listener.enterTime_numoffset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_numoffset" ):
                listener.exitTime_numoffset(self)




    def time_numoffset(self):

        localctx = Rfc3164Parser.Time_numoffsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_time_numoffset)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==Rfc3164Parser.PLUS or _la==Rfc3164Parser.DASH):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 202
            self.time_hour()
            self.state = 203
            self.match(Rfc3164Parser.COLON)
            self.state = 204
            self.time_minute()
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
            return Rfc3164Parser.RULE_msg

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MsgUTF8Context(MsgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.MsgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def msg_utf8(self):
            return self.getTypedRuleContext(Rfc3164Parser.Msg_utf8Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMsgUTF8" ):
                listener.enterMsgUTF8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMsgUTF8" ):
                listener.exitMsgUTF8(self)


    class MsgAnyContext(MsgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.MsgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def msg_any(self):
            return self.getTypedRuleContext(Rfc3164Parser.Msg_anyContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMsgAny" ):
                listener.enterMsgAny(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMsgAny" ):
                listener.exitMsgAny(self)



    def msg(self):

        localctx = Rfc3164Parser.MsgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_msg)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = Rfc3164Parser.MsgAnyContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.msg_any()
                pass

            elif la_ == 2:
                localctx = Rfc3164Parser.MsgUTF8Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.msg_utf8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Msg_anyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def octet(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.OctetContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.OctetContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_msg_any

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMsg_any" ):
                listener.enterMsg_any(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMsg_any" ):
                listener.exitMsg_any(self)




    def msg_any(self):

        localctx = Rfc3164Parser.Msg_anyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_msg_any)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (Rfc3164Parser.TAB - 1)) | (1 << (Rfc3164Parser.LF - 1)) | (1 << (Rfc3164Parser.CR - 1)) | (1 << (Rfc3164Parser.SPACE - 1)) | (1 << (Rfc3164Parser.EXCLAMATION - 1)) | (1 << (Rfc3164Parser.QUOTE - 1)) | (1 << (Rfc3164Parser.POUND - 1)) | (1 << (Rfc3164Parser.DOLLAR - 1)) | (1 << (Rfc3164Parser.PERCENT - 1)) | (1 << (Rfc3164Parser.AMPERSAND - 1)) | (1 << (Rfc3164Parser.APOSTROPHE - 1)) | (1 << (Rfc3164Parser.LEFT_PAREN - 1)) | (1 << (Rfc3164Parser.RIGHT_PAREN - 1)) | (1 << (Rfc3164Parser.ASTERISK - 1)) | (1 << (Rfc3164Parser.PLUS - 1)) | (1 << (Rfc3164Parser.COMMA - 1)) | (1 << (Rfc3164Parser.DASH - 1)) | (1 << (Rfc3164Parser.PERIOD - 1)) | (1 << (Rfc3164Parser.SLASH - 1)) | (1 << (Rfc3164Parser.ZERO - 1)) | (1 << (Rfc3164Parser.ONE - 1)) | (1 << (Rfc3164Parser.TWO - 1)) | (1 << (Rfc3164Parser.THREE - 1)) | (1 << (Rfc3164Parser.FOUR - 1)) | (1 << (Rfc3164Parser.FIVE - 1)) | (1 << (Rfc3164Parser.SIX - 1)) | (1 << (Rfc3164Parser.SEVEN - 1)) | (1 << (Rfc3164Parser.EIGHT - 1)) | (1 << (Rfc3164Parser.NINE - 1)) | (1 << (Rfc3164Parser.COLON - 1)) | (1 << (Rfc3164Parser.SEMICOLON - 1)) | (1 << (Rfc3164Parser.LESS_THAN - 1)) | (1 << (Rfc3164Parser.EQUALS - 1)) | (1 << (Rfc3164Parser.GREATER_THAN - 1)) | (1 << (Rfc3164Parser.QUESTION - 1)) | (1 << (Rfc3164Parser.AT - 1)) | (1 << (Rfc3164Parser.CAP_A - 1)) | (1 << (Rfc3164Parser.CAP_B - 1)) | (1 << (Rfc3164Parser.CAP_C - 1)) | (1 << (Rfc3164Parser.CAP_D - 1)) | (1 << (Rfc3164Parser.CAP_E - 1)) | (1 << (Rfc3164Parser.CAP_F - 1)) | (1 << (Rfc3164Parser.CAP_G - 1)) | (1 << (Rfc3164Parser.CAP_H - 1)) | (1 << (Rfc3164Parser.CAP_I - 1)) | (1 << (Rfc3164Parser.CAP_J - 1)) | (1 << (Rfc3164Parser.CAP_K - 1)) | (1 << (Rfc3164Parser.CAP_L - 1)) | (1 << (Rfc3164Parser.CAP_M - 1)) | (1 << (Rfc3164Parser.CAP_N - 1)) | (1 << (Rfc3164Parser.CAP_O - 1)) | (1 << (Rfc3164Parser.CAP_P - 1)) | (1 << (Rfc3164Parser.CAP_Q - 1)) | (1 << (Rfc3164Parser.CAP_R - 1)) | (1 << (Rfc3164Parser.CAP_S - 1)) | (1 << (Rfc3164Parser.CAP_T - 1)) | (1 << (Rfc3164Parser.CAP_U - 1)) | (1 << (Rfc3164Parser.CAP_V - 1)) | (1 << (Rfc3164Parser.CAP_W - 1)) | (1 << (Rfc3164Parser.CAP_X - 1)) | (1 << (Rfc3164Parser.CAP_Y - 1)) | (1 << (Rfc3164Parser.CAP_Z - 1)) | (1 << (Rfc3164Parser.LEFT_BRACE - 1)) | (1 << (Rfc3164Parser.BACKSLASH - 1)))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Rfc3164Parser.RIGHT_BRACE - 65)) | (1 << (Rfc3164Parser.CARAT - 65)) | (1 << (Rfc3164Parser.UNDERSCORE - 65)) | (1 << (Rfc3164Parser.ACCENT - 65)) | (1 << (Rfc3164Parser.A - 65)) | (1 << (Rfc3164Parser.B - 65)) | (1 << (Rfc3164Parser.C - 65)) | (1 << (Rfc3164Parser.D - 65)) | (1 << (Rfc3164Parser.E - 65)) | (1 << (Rfc3164Parser.F - 65)) | (1 << (Rfc3164Parser.G - 65)) | (1 << (Rfc3164Parser.H - 65)) | (1 << (Rfc3164Parser.I - 65)) | (1 << (Rfc3164Parser.J - 65)) | (1 << (Rfc3164Parser.K - 65)) | (1 << (Rfc3164Parser.L - 65)) | (1 << (Rfc3164Parser.M - 65)) | (1 << (Rfc3164Parser.N - 65)) | (1 << (Rfc3164Parser.O - 65)) | (1 << (Rfc3164Parser.P - 65)) | (1 << (Rfc3164Parser.Q - 65)) | (1 << (Rfc3164Parser.R - 65)) | (1 << (Rfc3164Parser.S - 65)) | (1 << (Rfc3164Parser.T - 65)) | (1 << (Rfc3164Parser.U - 65)) | (1 << (Rfc3164Parser.V - 65)) | (1 << (Rfc3164Parser.W - 65)) | (1 << (Rfc3164Parser.X - 65)) | (1 << (Rfc3164Parser.Y - 65)) | (1 << (Rfc3164Parser.Z - 65)) | (1 << (Rfc3164Parser.LEFT_CURLY_BRACE - 65)) | (1 << (Rfc3164Parser.PIPE - 65)) | (1 << (Rfc3164Parser.RIGHT_CURLY_BRACE - 65)) | (1 << (Rfc3164Parser.TILDE - 65)) | (1 << (Rfc3164Parser.U_0000 - 65)) | (1 << (Rfc3164Parser.U_0001 - 65)) | (1 << (Rfc3164Parser.U_0002 - 65)) | (1 << (Rfc3164Parser.U_0003 - 65)) | (1 << (Rfc3164Parser.U_0004 - 65)) | (1 << (Rfc3164Parser.U_0005 - 65)) | (1 << (Rfc3164Parser.U_0006 - 65)) | (1 << (Rfc3164Parser.U_0007 - 65)) | (1 << (Rfc3164Parser.U_0008 - 65)) | (1 << (Rfc3164Parser.U_000B - 65)) | (1 << (Rfc3164Parser.U_000C - 65)) | (1 << (Rfc3164Parser.U_000E - 65)) | (1 << (Rfc3164Parser.U_000F - 65)) | (1 << (Rfc3164Parser.U_0010 - 65)) | (1 << (Rfc3164Parser.U_0011 - 65)) | (1 << (Rfc3164Parser.U_0012 - 65)) | (1 << (Rfc3164Parser.U_0013 - 65)) | (1 << (Rfc3164Parser.U_0014 - 65)) | (1 << (Rfc3164Parser.U_0015 - 65)) | (1 << (Rfc3164Parser.U_0016 - 65)) | (1 << (Rfc3164Parser.U_0017 - 65)) | (1 << (Rfc3164Parser.U_0018 - 65)) | (1 << (Rfc3164Parser.U_0019 - 65)) | (1 << (Rfc3164Parser.U_001A - 65)) | (1 << (Rfc3164Parser.U_001B - 65)) | (1 << (Rfc3164Parser.U_001C - 65)) | (1 << (Rfc3164Parser.U_001D - 65)) | (1 << (Rfc3164Parser.U_001E - 65)) | (1 << (Rfc3164Parser.U_001F - 65)) | (1 << (Rfc3164Parser.U_007F - 65)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (Rfc3164Parser.U_0080 - 129)) | (1 << (Rfc3164Parser.U_0081 - 129)) | (1 << (Rfc3164Parser.U_0082 - 129)) | (1 << (Rfc3164Parser.U_0083 - 129)) | (1 << (Rfc3164Parser.U_0084 - 129)) | (1 << (Rfc3164Parser.U_0085 - 129)) | (1 << (Rfc3164Parser.U_0086 - 129)) | (1 << (Rfc3164Parser.U_0087 - 129)) | (1 << (Rfc3164Parser.U_0088 - 129)) | (1 << (Rfc3164Parser.U_0089 - 129)) | (1 << (Rfc3164Parser.U_008A - 129)) | (1 << (Rfc3164Parser.U_008B - 129)) | (1 << (Rfc3164Parser.U_008C - 129)) | (1 << (Rfc3164Parser.U_008D - 129)) | (1 << (Rfc3164Parser.U_008E - 129)) | (1 << (Rfc3164Parser.U_008F - 129)) | (1 << (Rfc3164Parser.U_0090 - 129)) | (1 << (Rfc3164Parser.U_0091 - 129)) | (1 << (Rfc3164Parser.U_0092 - 129)) | (1 << (Rfc3164Parser.U_0093 - 129)) | (1 << (Rfc3164Parser.U_0094 - 129)) | (1 << (Rfc3164Parser.U_0095 - 129)) | (1 << (Rfc3164Parser.U_0096 - 129)) | (1 << (Rfc3164Parser.U_0097 - 129)) | (1 << (Rfc3164Parser.U_0098 - 129)) | (1 << (Rfc3164Parser.U_0099 - 129)) | (1 << (Rfc3164Parser.U_009A - 129)) | (1 << (Rfc3164Parser.U_009B - 129)) | (1 << (Rfc3164Parser.U_009C - 129)) | (1 << (Rfc3164Parser.U_009D - 129)) | (1 << (Rfc3164Parser.U_009E - 129)) | (1 << (Rfc3164Parser.U_009F - 129)) | (1 << (Rfc3164Parser.U_00A0 - 129)) | (1 << (Rfc3164Parser.U_00A1 - 129)) | (1 << (Rfc3164Parser.U_00A2 - 129)) | (1 << (Rfc3164Parser.U_00A3 - 129)) | (1 << (Rfc3164Parser.U_00A4 - 129)) | (1 << (Rfc3164Parser.U_00A5 - 129)) | (1 << (Rfc3164Parser.U_00A6 - 129)) | (1 << (Rfc3164Parser.U_00A7 - 129)) | (1 << (Rfc3164Parser.U_00A8 - 129)) | (1 << (Rfc3164Parser.U_00A9 - 129)) | (1 << (Rfc3164Parser.U_00AA - 129)) | (1 << (Rfc3164Parser.U_00AB - 129)) | (1 << (Rfc3164Parser.U_00AC - 129)) | (1 << (Rfc3164Parser.U_00AD - 129)) | (1 << (Rfc3164Parser.U_00AE - 129)) | (1 << (Rfc3164Parser.U_00AF - 129)) | (1 << (Rfc3164Parser.U_00B0 - 129)) | (1 << (Rfc3164Parser.U_00B1 - 129)) | (1 << (Rfc3164Parser.U_00B2 - 129)) | (1 << (Rfc3164Parser.U_00B3 - 129)) | (1 << (Rfc3164Parser.U_00B4 - 129)) | (1 << (Rfc3164Parser.U_00B5 - 129)) | (1 << (Rfc3164Parser.U_00B6 - 129)) | (1 << (Rfc3164Parser.U_00B7 - 129)) | (1 << (Rfc3164Parser.U_00B8 - 129)) | (1 << (Rfc3164Parser.U_00B9 - 129)) | (1 << (Rfc3164Parser.U_00BA - 129)) | (1 << (Rfc3164Parser.U_00BB - 129)) | (1 << (Rfc3164Parser.U_00BC - 129)) | (1 << (Rfc3164Parser.U_00BD - 129)) | (1 << (Rfc3164Parser.U_00BE - 129)) | (1 << (Rfc3164Parser.U_00BF - 129)))) != 0) or ((((_la - 193)) & ~0x3f) == 0 and ((1 << (_la - 193)) & ((1 << (Rfc3164Parser.U_00C0 - 193)) | (1 << (Rfc3164Parser.U_00C1 - 193)) | (1 << (Rfc3164Parser.U_00C2 - 193)) | (1 << (Rfc3164Parser.U_00C3 - 193)) | (1 << (Rfc3164Parser.U_00C4 - 193)) | (1 << (Rfc3164Parser.U_00C5 - 193)) | (1 << (Rfc3164Parser.U_00C6 - 193)) | (1 << (Rfc3164Parser.U_00C7 - 193)) | (1 << (Rfc3164Parser.U_00C8 - 193)) | (1 << (Rfc3164Parser.U_00C9 - 193)) | (1 << (Rfc3164Parser.U_00CA - 193)) | (1 << (Rfc3164Parser.U_00CB - 193)) | (1 << (Rfc3164Parser.U_00CC - 193)) | (1 << (Rfc3164Parser.U_00CD - 193)) | (1 << (Rfc3164Parser.U_00CE - 193)) | (1 << (Rfc3164Parser.U_00CF - 193)) | (1 << (Rfc3164Parser.U_00D0 - 193)) | (1 << (Rfc3164Parser.U_00D1 - 193)) | (1 << (Rfc3164Parser.U_00D2 - 193)) | (1 << (Rfc3164Parser.U_00D3 - 193)) | (1 << (Rfc3164Parser.U_00D4 - 193)) | (1 << (Rfc3164Parser.U_00D5 - 193)) | (1 << (Rfc3164Parser.U_00D6 - 193)) | (1 << (Rfc3164Parser.U_00D7 - 193)) | (1 << (Rfc3164Parser.U_00D8 - 193)) | (1 << (Rfc3164Parser.U_00D9 - 193)) | (1 << (Rfc3164Parser.U_00DA - 193)) | (1 << (Rfc3164Parser.U_00DB - 193)) | (1 << (Rfc3164Parser.U_00DC - 193)) | (1 << (Rfc3164Parser.U_00DD - 193)) | (1 << (Rfc3164Parser.U_00DE - 193)) | (1 << (Rfc3164Parser.U_00DF - 193)) | (1 << (Rfc3164Parser.U_00E0 - 193)) | (1 << (Rfc3164Parser.U_00E1 - 193)) | (1 << (Rfc3164Parser.U_00E2 - 193)) | (1 << (Rfc3164Parser.U_00E3 - 193)) | (1 << (Rfc3164Parser.U_00E4 - 193)) | (1 << (Rfc3164Parser.U_00E5 - 193)) | (1 << (Rfc3164Parser.U_00E6 - 193)) | (1 << (Rfc3164Parser.U_00E7 - 193)) | (1 << (Rfc3164Parser.U_00E8 - 193)) | (1 << (Rfc3164Parser.U_00E9 - 193)) | (1 << (Rfc3164Parser.U_00EA - 193)) | (1 << (Rfc3164Parser.U_00EB - 193)) | (1 << (Rfc3164Parser.U_00EC - 193)) | (1 << (Rfc3164Parser.U_00ED - 193)) | (1 << (Rfc3164Parser.U_00EE - 193)) | (1 << (Rfc3164Parser.U_00EF - 193)) | (1 << (Rfc3164Parser.U_00F0 - 193)) | (1 << (Rfc3164Parser.U_00F1 - 193)) | (1 << (Rfc3164Parser.U_00F2 - 193)) | (1 << (Rfc3164Parser.U_00F3 - 193)) | (1 << (Rfc3164Parser.U_00F4 - 193)) | (1 << (Rfc3164Parser.U_00F5 - 193)) | (1 << (Rfc3164Parser.U_00F6 - 193)) | (1 << (Rfc3164Parser.U_00F7 - 193)) | (1 << (Rfc3164Parser.U_00F8 - 193)) | (1 << (Rfc3164Parser.U_00F9 - 193)) | (1 << (Rfc3164Parser.U_00FA - 193)) | (1 << (Rfc3164Parser.U_00FB - 193)) | (1 << (Rfc3164Parser.U_00FC - 193)) | (1 << (Rfc3164Parser.U_00FD - 193)) | (1 << (Rfc3164Parser.U_00FE - 193)) | (1 << (Rfc3164Parser.U_00FF - 193)))) != 0):
                self.state = 210
                self.octet()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def bom(self):
            return self.getTypedRuleContext(Rfc3164Parser.BomContext,0)


        def utf_8_string(self):
            return self.getTypedRuleContext(Rfc3164Parser.Utf_8_stringContext,0)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_msg_utf8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMsg_utf8" ):
                listener.enterMsg_utf8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMsg_utf8" ):
                listener.exitMsg_utf8(self)




    def msg_utf8(self):

        localctx = Rfc3164Parser.Msg_utf8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_msg_utf8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.bom()
            self.state = 217
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
            return self.getToken(Rfc3164Parser.U_00EF, 0)

        def U_00BB(self):
            return self.getToken(Rfc3164Parser.U_00BB, 0)

        def U_00BF(self):
            return self.getToken(Rfc3164Parser.U_00BF, 0)

        def getRuleIndex(self):
            return Rfc3164Parser.RULE_bom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBom" ):
                listener.enterBom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBom" ):
                listener.exitBom(self)




    def bom(self):

        localctx = Rfc3164Parser.BomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_bom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            _la = self._input.LA(1)
            if not(((((_la - 188)) & ~0x3f) == 0 and ((1 << (_la - 188)) & ((1 << (Rfc3164Parser.U_00BB - 188)) | (1 << (Rfc3164Parser.U_00BF - 188)) | (1 << (Rfc3164Parser.U_00EF - 188)))) != 0)):
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


    class Utf_8_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def octet(self, i: Optional[int]=None):
            if i is None:
                return self.getTypedRuleContexts(Rfc3164Parser.OctetContext)
            else:
                return self.getTypedRuleContext(Rfc3164Parser.OctetContext,i)


        def getRuleIndex(self):
            return Rfc3164Parser.RULE_utf_8_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUtf_8_string" ):
                listener.enterUtf_8_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUtf_8_string" ):
                listener.exitUtf_8_string(self)




    def utf_8_string(self):

        localctx = Rfc3164Parser.Utf_8_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_utf_8_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (Rfc3164Parser.TAB - 1)) | (1 << (Rfc3164Parser.LF - 1)) | (1 << (Rfc3164Parser.CR - 1)) | (1 << (Rfc3164Parser.SPACE - 1)) | (1 << (Rfc3164Parser.EXCLAMATION - 1)) | (1 << (Rfc3164Parser.QUOTE - 1)) | (1 << (Rfc3164Parser.POUND - 1)) | (1 << (Rfc3164Parser.DOLLAR - 1)) | (1 << (Rfc3164Parser.PERCENT - 1)) | (1 << (Rfc3164Parser.AMPERSAND - 1)) | (1 << (Rfc3164Parser.APOSTROPHE - 1)) | (1 << (Rfc3164Parser.LEFT_PAREN - 1)) | (1 << (Rfc3164Parser.RIGHT_PAREN - 1)) | (1 << (Rfc3164Parser.ASTERISK - 1)) | (1 << (Rfc3164Parser.PLUS - 1)) | (1 << (Rfc3164Parser.COMMA - 1)) | (1 << (Rfc3164Parser.DASH - 1)) | (1 << (Rfc3164Parser.PERIOD - 1)) | (1 << (Rfc3164Parser.SLASH - 1)) | (1 << (Rfc3164Parser.ZERO - 1)) | (1 << (Rfc3164Parser.ONE - 1)) | (1 << (Rfc3164Parser.TWO - 1)) | (1 << (Rfc3164Parser.THREE - 1)) | (1 << (Rfc3164Parser.FOUR - 1)) | (1 << (Rfc3164Parser.FIVE - 1)) | (1 << (Rfc3164Parser.SIX - 1)) | (1 << (Rfc3164Parser.SEVEN - 1)) | (1 << (Rfc3164Parser.EIGHT - 1)) | (1 << (Rfc3164Parser.NINE - 1)) | (1 << (Rfc3164Parser.COLON - 1)) | (1 << (Rfc3164Parser.SEMICOLON - 1)) | (1 << (Rfc3164Parser.LESS_THAN - 1)) | (1 << (Rfc3164Parser.EQUALS - 1)) | (1 << (Rfc3164Parser.GREATER_THAN - 1)) | (1 << (Rfc3164Parser.QUESTION - 1)) | (1 << (Rfc3164Parser.AT - 1)) | (1 << (Rfc3164Parser.CAP_A - 1)) | (1 << (Rfc3164Parser.CAP_B - 1)) | (1 << (Rfc3164Parser.CAP_C - 1)) | (1 << (Rfc3164Parser.CAP_D - 1)) | (1 << (Rfc3164Parser.CAP_E - 1)) | (1 << (Rfc3164Parser.CAP_F - 1)) | (1 << (Rfc3164Parser.CAP_G - 1)) | (1 << (Rfc3164Parser.CAP_H - 1)) | (1 << (Rfc3164Parser.CAP_I - 1)) | (1 << (Rfc3164Parser.CAP_J - 1)) | (1 << (Rfc3164Parser.CAP_K - 1)) | (1 << (Rfc3164Parser.CAP_L - 1)) | (1 << (Rfc3164Parser.CAP_M - 1)) | (1 << (Rfc3164Parser.CAP_N - 1)) | (1 << (Rfc3164Parser.CAP_O - 1)) | (1 << (Rfc3164Parser.CAP_P - 1)) | (1 << (Rfc3164Parser.CAP_Q - 1)) | (1 << (Rfc3164Parser.CAP_R - 1)) | (1 << (Rfc3164Parser.CAP_S - 1)) | (1 << (Rfc3164Parser.CAP_T - 1)) | (1 << (Rfc3164Parser.CAP_U - 1)) | (1 << (Rfc3164Parser.CAP_V - 1)) | (1 << (Rfc3164Parser.CAP_W - 1)) | (1 << (Rfc3164Parser.CAP_X - 1)) | (1 << (Rfc3164Parser.CAP_Y - 1)) | (1 << (Rfc3164Parser.CAP_Z - 1)) | (1 << (Rfc3164Parser.LEFT_BRACE - 1)) | (1 << (Rfc3164Parser.BACKSLASH - 1)))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Rfc3164Parser.RIGHT_BRACE - 65)) | (1 << (Rfc3164Parser.CARAT - 65)) | (1 << (Rfc3164Parser.UNDERSCORE - 65)) | (1 << (Rfc3164Parser.ACCENT - 65)) | (1 << (Rfc3164Parser.A - 65)) | (1 << (Rfc3164Parser.B - 65)) | (1 << (Rfc3164Parser.C - 65)) | (1 << (Rfc3164Parser.D - 65)) | (1 << (Rfc3164Parser.E - 65)) | (1 << (Rfc3164Parser.F - 65)) | (1 << (Rfc3164Parser.G - 65)) | (1 << (Rfc3164Parser.H - 65)) | (1 << (Rfc3164Parser.I - 65)) | (1 << (Rfc3164Parser.J - 65)) | (1 << (Rfc3164Parser.K - 65)) | (1 << (Rfc3164Parser.L - 65)) | (1 << (Rfc3164Parser.M - 65)) | (1 << (Rfc3164Parser.N - 65)) | (1 << (Rfc3164Parser.O - 65)) | (1 << (Rfc3164Parser.P - 65)) | (1 << (Rfc3164Parser.Q - 65)) | (1 << (Rfc3164Parser.R - 65)) | (1 << (Rfc3164Parser.S - 65)) | (1 << (Rfc3164Parser.T - 65)) | (1 << (Rfc3164Parser.U - 65)) | (1 << (Rfc3164Parser.V - 65)) | (1 << (Rfc3164Parser.W - 65)) | (1 << (Rfc3164Parser.X - 65)) | (1 << (Rfc3164Parser.Y - 65)) | (1 << (Rfc3164Parser.Z - 65)) | (1 << (Rfc3164Parser.LEFT_CURLY_BRACE - 65)) | (1 << (Rfc3164Parser.PIPE - 65)) | (1 << (Rfc3164Parser.RIGHT_CURLY_BRACE - 65)) | (1 << (Rfc3164Parser.TILDE - 65)) | (1 << (Rfc3164Parser.U_0000 - 65)) | (1 << (Rfc3164Parser.U_0001 - 65)) | (1 << (Rfc3164Parser.U_0002 - 65)) | (1 << (Rfc3164Parser.U_0003 - 65)) | (1 << (Rfc3164Parser.U_0004 - 65)) | (1 << (Rfc3164Parser.U_0005 - 65)) | (1 << (Rfc3164Parser.U_0006 - 65)) | (1 << (Rfc3164Parser.U_0007 - 65)) | (1 << (Rfc3164Parser.U_0008 - 65)) | (1 << (Rfc3164Parser.U_000B - 65)) | (1 << (Rfc3164Parser.U_000C - 65)) | (1 << (Rfc3164Parser.U_000E - 65)) | (1 << (Rfc3164Parser.U_000F - 65)) | (1 << (Rfc3164Parser.U_0010 - 65)) | (1 << (Rfc3164Parser.U_0011 - 65)) | (1 << (Rfc3164Parser.U_0012 - 65)) | (1 << (Rfc3164Parser.U_0013 - 65)) | (1 << (Rfc3164Parser.U_0014 - 65)) | (1 << (Rfc3164Parser.U_0015 - 65)) | (1 << (Rfc3164Parser.U_0016 - 65)) | (1 << (Rfc3164Parser.U_0017 - 65)) | (1 << (Rfc3164Parser.U_0018 - 65)) | (1 << (Rfc3164Parser.U_0019 - 65)) | (1 << (Rfc3164Parser.U_001A - 65)) | (1 << (Rfc3164Parser.U_001B - 65)) | (1 << (Rfc3164Parser.U_001C - 65)) | (1 << (Rfc3164Parser.U_001D - 65)) | (1 << (Rfc3164Parser.U_001E - 65)) | (1 << (Rfc3164Parser.U_001F - 65)) | (1 << (Rfc3164Parser.U_007F - 65)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (Rfc3164Parser.U_0080 - 129)) | (1 << (Rfc3164Parser.U_0081 - 129)) | (1 << (Rfc3164Parser.U_0082 - 129)) | (1 << (Rfc3164Parser.U_0083 - 129)) | (1 << (Rfc3164Parser.U_0084 - 129)) | (1 << (Rfc3164Parser.U_0085 - 129)) | (1 << (Rfc3164Parser.U_0086 - 129)) | (1 << (Rfc3164Parser.U_0087 - 129)) | (1 << (Rfc3164Parser.U_0088 - 129)) | (1 << (Rfc3164Parser.U_0089 - 129)) | (1 << (Rfc3164Parser.U_008A - 129)) | (1 << (Rfc3164Parser.U_008B - 129)) | (1 << (Rfc3164Parser.U_008C - 129)) | (1 << (Rfc3164Parser.U_008D - 129)) | (1 << (Rfc3164Parser.U_008E - 129)) | (1 << (Rfc3164Parser.U_008F - 129)) | (1 << (Rfc3164Parser.U_0090 - 129)) | (1 << (Rfc3164Parser.U_0091 - 129)) | (1 << (Rfc3164Parser.U_0092 - 129)) | (1 << (Rfc3164Parser.U_0093 - 129)) | (1 << (Rfc3164Parser.U_0094 - 129)) | (1 << (Rfc3164Parser.U_0095 - 129)) | (1 << (Rfc3164Parser.U_0096 - 129)) | (1 << (Rfc3164Parser.U_0097 - 129)) | (1 << (Rfc3164Parser.U_0098 - 129)) | (1 << (Rfc3164Parser.U_0099 - 129)) | (1 << (Rfc3164Parser.U_009A - 129)) | (1 << (Rfc3164Parser.U_009B - 129)) | (1 << (Rfc3164Parser.U_009C - 129)) | (1 << (Rfc3164Parser.U_009D - 129)) | (1 << (Rfc3164Parser.U_009E - 129)) | (1 << (Rfc3164Parser.U_009F - 129)) | (1 << (Rfc3164Parser.U_00A0 - 129)) | (1 << (Rfc3164Parser.U_00A1 - 129)) | (1 << (Rfc3164Parser.U_00A2 - 129)) | (1 << (Rfc3164Parser.U_00A3 - 129)) | (1 << (Rfc3164Parser.U_00A4 - 129)) | (1 << (Rfc3164Parser.U_00A5 - 129)) | (1 << (Rfc3164Parser.U_00A6 - 129)) | (1 << (Rfc3164Parser.U_00A7 - 129)) | (1 << (Rfc3164Parser.U_00A8 - 129)) | (1 << (Rfc3164Parser.U_00A9 - 129)) | (1 << (Rfc3164Parser.U_00AA - 129)) | (1 << (Rfc3164Parser.U_00AB - 129)) | (1 << (Rfc3164Parser.U_00AC - 129)) | (1 << (Rfc3164Parser.U_00AD - 129)) | (1 << (Rfc3164Parser.U_00AE - 129)) | (1 << (Rfc3164Parser.U_00AF - 129)) | (1 << (Rfc3164Parser.U_00B0 - 129)) | (1 << (Rfc3164Parser.U_00B1 - 129)) | (1 << (Rfc3164Parser.U_00B2 - 129)) | (1 << (Rfc3164Parser.U_00B3 - 129)) | (1 << (Rfc3164Parser.U_00B4 - 129)) | (1 << (Rfc3164Parser.U_00B5 - 129)) | (1 << (Rfc3164Parser.U_00B6 - 129)) | (1 << (Rfc3164Parser.U_00B7 - 129)) | (1 << (Rfc3164Parser.U_00B8 - 129)) | (1 << (Rfc3164Parser.U_00B9 - 129)) | (1 << (Rfc3164Parser.U_00BA - 129)) | (1 << (Rfc3164Parser.U_00BB - 129)) | (1 << (Rfc3164Parser.U_00BC - 129)) | (1 << (Rfc3164Parser.U_00BD - 129)) | (1 << (Rfc3164Parser.U_00BE - 129)) | (1 << (Rfc3164Parser.U_00BF - 129)))) != 0) or ((((_la - 193)) & ~0x3f) == 0 and ((1 << (_la - 193)) & ((1 << (Rfc3164Parser.U_00C0 - 193)) | (1 << (Rfc3164Parser.U_00C1 - 193)) | (1 << (Rfc3164Parser.U_00C2 - 193)) | (1 << (Rfc3164Parser.U_00C3 - 193)) | (1 << (Rfc3164Parser.U_00C4 - 193)) | (1 << (Rfc3164Parser.U_00C5 - 193)) | (1 << (Rfc3164Parser.U_00C6 - 193)) | (1 << (Rfc3164Parser.U_00C7 - 193)) | (1 << (Rfc3164Parser.U_00C8 - 193)) | (1 << (Rfc3164Parser.U_00C9 - 193)) | (1 << (Rfc3164Parser.U_00CA - 193)) | (1 << (Rfc3164Parser.U_00CB - 193)) | (1 << (Rfc3164Parser.U_00CC - 193)) | (1 << (Rfc3164Parser.U_00CD - 193)) | (1 << (Rfc3164Parser.U_00CE - 193)) | (1 << (Rfc3164Parser.U_00CF - 193)) | (1 << (Rfc3164Parser.U_00D0 - 193)) | (1 << (Rfc3164Parser.U_00D1 - 193)) | (1 << (Rfc3164Parser.U_00D2 - 193)) | (1 << (Rfc3164Parser.U_00D3 - 193)) | (1 << (Rfc3164Parser.U_00D4 - 193)) | (1 << (Rfc3164Parser.U_00D5 - 193)) | (1 << (Rfc3164Parser.U_00D6 - 193)) | (1 << (Rfc3164Parser.U_00D7 - 193)) | (1 << (Rfc3164Parser.U_00D8 - 193)) | (1 << (Rfc3164Parser.U_00D9 - 193)) | (1 << (Rfc3164Parser.U_00DA - 193)) | (1 << (Rfc3164Parser.U_00DB - 193)) | (1 << (Rfc3164Parser.U_00DC - 193)) | (1 << (Rfc3164Parser.U_00DD - 193)) | (1 << (Rfc3164Parser.U_00DE - 193)) | (1 << (Rfc3164Parser.U_00DF - 193)) | (1 << (Rfc3164Parser.U_00E0 - 193)) | (1 << (Rfc3164Parser.U_00E1 - 193)) | (1 << (Rfc3164Parser.U_00E2 - 193)) | (1 << (Rfc3164Parser.U_00E3 - 193)) | (1 << (Rfc3164Parser.U_00E4 - 193)) | (1 << (Rfc3164Parser.U_00E5 - 193)) | (1 << (Rfc3164Parser.U_00E6 - 193)) | (1 << (Rfc3164Parser.U_00E7 - 193)) | (1 << (Rfc3164Parser.U_00E8 - 193)) | (1 << (Rfc3164Parser.U_00E9 - 193)) | (1 << (Rfc3164Parser.U_00EA - 193)) | (1 << (Rfc3164Parser.U_00EB - 193)) | (1 << (Rfc3164Parser.U_00EC - 193)) | (1 << (Rfc3164Parser.U_00ED - 193)) | (1 << (Rfc3164Parser.U_00EE - 193)) | (1 << (Rfc3164Parser.U_00EF - 193)) | (1 << (Rfc3164Parser.U_00F0 - 193)) | (1 << (Rfc3164Parser.U_00F1 - 193)) | (1 << (Rfc3164Parser.U_00F2 - 193)) | (1 << (Rfc3164Parser.U_00F3 - 193)) | (1 << (Rfc3164Parser.U_00F4 - 193)) | (1 << (Rfc3164Parser.U_00F5 - 193)) | (1 << (Rfc3164Parser.U_00F6 - 193)) | (1 << (Rfc3164Parser.U_00F7 - 193)) | (1 << (Rfc3164Parser.U_00F8 - 193)) | (1 << (Rfc3164Parser.U_00F9 - 193)) | (1 << (Rfc3164Parser.U_00FA - 193)) | (1 << (Rfc3164Parser.U_00FB - 193)) | (1 << (Rfc3164Parser.U_00FC - 193)) | (1 << (Rfc3164Parser.U_00FD - 193)) | (1 << (Rfc3164Parser.U_00FE - 193)) | (1 << (Rfc3164Parser.U_00FF - 193)))) != 0):
                self.state = 221
                self.octet()
                self.state = 226
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
            return self.getToken(Rfc3164Parser.U_0000, 0)

        def U_0001(self):
            return self.getToken(Rfc3164Parser.U_0001, 0)

        def U_0002(self):
            return self.getToken(Rfc3164Parser.U_0002, 0)

        def U_0003(self):
            return self.getToken(Rfc3164Parser.U_0003, 0)

        def U_0004(self):
            return self.getToken(Rfc3164Parser.U_0004, 0)

        def U_0005(self):
            return self.getToken(Rfc3164Parser.U_0005, 0)

        def U_0006(self):
            return self.getToken(Rfc3164Parser.U_0006, 0)

        def U_0007(self):
            return self.getToken(Rfc3164Parser.U_0007, 0)

        def U_0008(self):
            return self.getToken(Rfc3164Parser.U_0008, 0)

        def TAB(self):
            return self.getToken(Rfc3164Parser.TAB, 0)

        def LF(self):
            return self.getToken(Rfc3164Parser.LF, 0)

        def U_000B(self):
            return self.getToken(Rfc3164Parser.U_000B, 0)

        def U_000C(self):
            return self.getToken(Rfc3164Parser.U_000C, 0)

        def CR(self):
            return self.getToken(Rfc3164Parser.CR, 0)

        def U_000E(self):
            return self.getToken(Rfc3164Parser.U_000E, 0)

        def U_000F(self):
            return self.getToken(Rfc3164Parser.U_000F, 0)

        def U_0010(self):
            return self.getToken(Rfc3164Parser.U_0010, 0)

        def U_0011(self):
            return self.getToken(Rfc3164Parser.U_0011, 0)

        def U_0012(self):
            return self.getToken(Rfc3164Parser.U_0012, 0)

        def U_0013(self):
            return self.getToken(Rfc3164Parser.U_0013, 0)

        def U_0014(self):
            return self.getToken(Rfc3164Parser.U_0014, 0)

        def U_0015(self):
            return self.getToken(Rfc3164Parser.U_0015, 0)

        def U_0016(self):
            return self.getToken(Rfc3164Parser.U_0016, 0)

        def U_0017(self):
            return self.getToken(Rfc3164Parser.U_0017, 0)

        def U_0018(self):
            return self.getToken(Rfc3164Parser.U_0018, 0)

        def U_0019(self):
            return self.getToken(Rfc3164Parser.U_0019, 0)

        def U_001A(self):
            return self.getToken(Rfc3164Parser.U_001A, 0)

        def U_001B(self):
            return self.getToken(Rfc3164Parser.U_001B, 0)

        def U_001C(self):
            return self.getToken(Rfc3164Parser.U_001C, 0)

        def U_001D(self):
            return self.getToken(Rfc3164Parser.U_001D, 0)

        def U_001E(self):
            return self.getToken(Rfc3164Parser.U_001E, 0)

        def U_001F(self):
            return self.getToken(Rfc3164Parser.U_001F, 0)

        def SPACE(self):
            return self.getToken(Rfc3164Parser.SPACE, 0)

        def EXCLAMATION(self):
            return self.getToken(Rfc3164Parser.EXCLAMATION, 0)

        def QUOTE(self):
            return self.getToken(Rfc3164Parser.QUOTE, 0)

        def POUND(self):
            return self.getToken(Rfc3164Parser.POUND, 0)

        def DOLLAR(self):
            return self.getToken(Rfc3164Parser.DOLLAR, 0)

        def PERCENT(self):
            return self.getToken(Rfc3164Parser.PERCENT, 0)

        def AMPERSAND(self):
            return self.getToken(Rfc3164Parser.AMPERSAND, 0)

        def APOSTROPHE(self):
            return self.getToken(Rfc3164Parser.APOSTROPHE, 0)

        def LEFT_PAREN(self):
            return self.getToken(Rfc3164Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(Rfc3164Parser.RIGHT_PAREN, 0)

        def ASTERISK(self):
            return self.getToken(Rfc3164Parser.ASTERISK, 0)

        def PLUS(self):
            return self.getToken(Rfc3164Parser.PLUS, 0)

        def COMMA(self):
            return self.getToken(Rfc3164Parser.COMMA, 0)

        def DASH(self):
            return self.getToken(Rfc3164Parser.DASH, 0)

        def PERIOD(self):
            return self.getToken(Rfc3164Parser.PERIOD, 0)

        def SLASH(self):
            return self.getToken(Rfc3164Parser.SLASH, 0)

        def ZERO(self):
            return self.getToken(Rfc3164Parser.ZERO, 0)

        def ONE(self):
            return self.getToken(Rfc3164Parser.ONE, 0)

        def TWO(self):
            return self.getToken(Rfc3164Parser.TWO, 0)

        def THREE(self):
            return self.getToken(Rfc3164Parser.THREE, 0)

        def FOUR(self):
            return self.getToken(Rfc3164Parser.FOUR, 0)

        def FIVE(self):
            return self.getToken(Rfc3164Parser.FIVE, 0)

        def SIX(self):
            return self.getToken(Rfc3164Parser.SIX, 0)

        def SEVEN(self):
            return self.getToken(Rfc3164Parser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(Rfc3164Parser.EIGHT, 0)

        def NINE(self):
            return self.getToken(Rfc3164Parser.NINE, 0)

        def COLON(self):
            return self.getToken(Rfc3164Parser.COLON, 0)

        def SEMICOLON(self):
            return self.getToken(Rfc3164Parser.SEMICOLON, 0)

        def LESS_THAN(self):
            return self.getToken(Rfc3164Parser.LESS_THAN, 0)

        def EQUALS(self):
            return self.getToken(Rfc3164Parser.EQUALS, 0)

        def GREATER_THAN(self):
            return self.getToken(Rfc3164Parser.GREATER_THAN, 0)

        def QUESTION(self):
            return self.getToken(Rfc3164Parser.QUESTION, 0)

        def AT(self):
            return self.getToken(Rfc3164Parser.AT, 0)

        def CAP_A(self):
            return self.getToken(Rfc3164Parser.CAP_A, 0)

        def CAP_B(self):
            return self.getToken(Rfc3164Parser.CAP_B, 0)

        def CAP_C(self):
            return self.getToken(Rfc3164Parser.CAP_C, 0)

        def CAP_D(self):
            return self.getToken(Rfc3164Parser.CAP_D, 0)

        def CAP_E(self):
            return self.getToken(Rfc3164Parser.CAP_E, 0)

        def CAP_F(self):
            return self.getToken(Rfc3164Parser.CAP_F, 0)

        def CAP_G(self):
            return self.getToken(Rfc3164Parser.CAP_G, 0)

        def CAP_H(self):
            return self.getToken(Rfc3164Parser.CAP_H, 0)

        def CAP_I(self):
            return self.getToken(Rfc3164Parser.CAP_I, 0)

        def CAP_J(self):
            return self.getToken(Rfc3164Parser.CAP_J, 0)

        def CAP_K(self):
            return self.getToken(Rfc3164Parser.CAP_K, 0)

        def CAP_L(self):
            return self.getToken(Rfc3164Parser.CAP_L, 0)

        def CAP_M(self):
            return self.getToken(Rfc3164Parser.CAP_M, 0)

        def CAP_N(self):
            return self.getToken(Rfc3164Parser.CAP_N, 0)

        def CAP_O(self):
            return self.getToken(Rfc3164Parser.CAP_O, 0)

        def CAP_P(self):
            return self.getToken(Rfc3164Parser.CAP_P, 0)

        def CAP_Q(self):
            return self.getToken(Rfc3164Parser.CAP_Q, 0)

        def CAP_R(self):
            return self.getToken(Rfc3164Parser.CAP_R, 0)

        def CAP_S(self):
            return self.getToken(Rfc3164Parser.CAP_S, 0)

        def CAP_T(self):
            return self.getToken(Rfc3164Parser.CAP_T, 0)

        def CAP_U(self):
            return self.getToken(Rfc3164Parser.CAP_U, 0)

        def CAP_V(self):
            return self.getToken(Rfc3164Parser.CAP_V, 0)

        def CAP_W(self):
            return self.getToken(Rfc3164Parser.CAP_W, 0)

        def CAP_X(self):
            return self.getToken(Rfc3164Parser.CAP_X, 0)

        def CAP_Y(self):
            return self.getToken(Rfc3164Parser.CAP_Y, 0)

        def CAP_Z(self):
            return self.getToken(Rfc3164Parser.CAP_Z, 0)

        def LEFT_BRACE(self):
            return self.getToken(Rfc3164Parser.LEFT_BRACE, 0)

        def BACKSLASH(self):
            return self.getToken(Rfc3164Parser.BACKSLASH, 0)

        def RIGHT_BRACE(self):
            return self.getToken(Rfc3164Parser.RIGHT_BRACE, 0)

        def CARAT(self):
            return self.getToken(Rfc3164Parser.CARAT, 0)

        def UNDERSCORE(self):
            return self.getToken(Rfc3164Parser.UNDERSCORE, 0)

        def ACCENT(self):
            return self.getToken(Rfc3164Parser.ACCENT, 0)

        def A(self):
            return self.getToken(Rfc3164Parser.A, 0)

        def B(self):
            return self.getToken(Rfc3164Parser.B, 0)

        def C(self):
            return self.getToken(Rfc3164Parser.C, 0)

        def D(self):
            return self.getToken(Rfc3164Parser.D, 0)

        def E(self):
            return self.getToken(Rfc3164Parser.E, 0)

        def F(self):
            return self.getToken(Rfc3164Parser.F, 0)

        def G(self):
            return self.getToken(Rfc3164Parser.G, 0)

        def H(self):
            return self.getToken(Rfc3164Parser.H, 0)

        def I(self):
            return self.getToken(Rfc3164Parser.I, 0)

        def J(self):
            return self.getToken(Rfc3164Parser.J, 0)

        def K(self):
            return self.getToken(Rfc3164Parser.K, 0)

        def L(self):
            return self.getToken(Rfc3164Parser.L, 0)

        def M(self):
            return self.getToken(Rfc3164Parser.M, 0)

        def N(self):
            return self.getToken(Rfc3164Parser.N, 0)

        def O(self):
            return self.getToken(Rfc3164Parser.O, 0)

        def P(self):
            return self.getToken(Rfc3164Parser.P, 0)

        def Q(self):
            return self.getToken(Rfc3164Parser.Q, 0)

        def R(self):
            return self.getToken(Rfc3164Parser.R, 0)

        def S(self):
            return self.getToken(Rfc3164Parser.S, 0)

        def T(self):
            return self.getToken(Rfc3164Parser.T, 0)

        def U(self):
            return self.getToken(Rfc3164Parser.U, 0)

        def V(self):
            return self.getToken(Rfc3164Parser.V, 0)

        def W(self):
            return self.getToken(Rfc3164Parser.W, 0)

        def X(self):
            return self.getToken(Rfc3164Parser.X, 0)

        def Y(self):
            return self.getToken(Rfc3164Parser.Y, 0)

        def Z(self):
            return self.getToken(Rfc3164Parser.Z, 0)

        def LEFT_CURLY_BRACE(self):
            return self.getToken(Rfc3164Parser.LEFT_CURLY_BRACE, 0)

        def PIPE(self):
            return self.getToken(Rfc3164Parser.PIPE, 0)

        def RIGHT_CURLY_BRACE(self):
            return self.getToken(Rfc3164Parser.RIGHT_CURLY_BRACE, 0)

        def TILDE(self):
            return self.getToken(Rfc3164Parser.TILDE, 0)

        def U_007F(self):
            return self.getToken(Rfc3164Parser.U_007F, 0)

        def U_0080(self):
            return self.getToken(Rfc3164Parser.U_0080, 0)

        def U_0081(self):
            return self.getToken(Rfc3164Parser.U_0081, 0)

        def U_0082(self):
            return self.getToken(Rfc3164Parser.U_0082, 0)

        def U_0083(self):
            return self.getToken(Rfc3164Parser.U_0083, 0)

        def U_0084(self):
            return self.getToken(Rfc3164Parser.U_0084, 0)

        def U_0085(self):
            return self.getToken(Rfc3164Parser.U_0085, 0)

        def U_0086(self):
            return self.getToken(Rfc3164Parser.U_0086, 0)

        def U_0087(self):
            return self.getToken(Rfc3164Parser.U_0087, 0)

        def U_0088(self):
            return self.getToken(Rfc3164Parser.U_0088, 0)

        def U_0089(self):
            return self.getToken(Rfc3164Parser.U_0089, 0)

        def U_008A(self):
            return self.getToken(Rfc3164Parser.U_008A, 0)

        def U_008B(self):
            return self.getToken(Rfc3164Parser.U_008B, 0)

        def U_008C(self):
            return self.getToken(Rfc3164Parser.U_008C, 0)

        def U_008D(self):
            return self.getToken(Rfc3164Parser.U_008D, 0)

        def U_008E(self):
            return self.getToken(Rfc3164Parser.U_008E, 0)

        def U_008F(self):
            return self.getToken(Rfc3164Parser.U_008F, 0)

        def U_0090(self):
            return self.getToken(Rfc3164Parser.U_0090, 0)

        def U_0091(self):
            return self.getToken(Rfc3164Parser.U_0091, 0)

        def U_0092(self):
            return self.getToken(Rfc3164Parser.U_0092, 0)

        def U_0093(self):
            return self.getToken(Rfc3164Parser.U_0093, 0)

        def U_0094(self):
            return self.getToken(Rfc3164Parser.U_0094, 0)

        def U_0095(self):
            return self.getToken(Rfc3164Parser.U_0095, 0)

        def U_0096(self):
            return self.getToken(Rfc3164Parser.U_0096, 0)

        def U_0097(self):
            return self.getToken(Rfc3164Parser.U_0097, 0)

        def U_0098(self):
            return self.getToken(Rfc3164Parser.U_0098, 0)

        def U_0099(self):
            return self.getToken(Rfc3164Parser.U_0099, 0)

        def U_009A(self):
            return self.getToken(Rfc3164Parser.U_009A, 0)

        def U_009B(self):
            return self.getToken(Rfc3164Parser.U_009B, 0)

        def U_009C(self):
            return self.getToken(Rfc3164Parser.U_009C, 0)

        def U_009D(self):
            return self.getToken(Rfc3164Parser.U_009D, 0)

        def U_009E(self):
            return self.getToken(Rfc3164Parser.U_009E, 0)

        def U_009F(self):
            return self.getToken(Rfc3164Parser.U_009F, 0)

        def U_00A0(self):
            return self.getToken(Rfc3164Parser.U_00A0, 0)

        def U_00A1(self):
            return self.getToken(Rfc3164Parser.U_00A1, 0)

        def U_00A2(self):
            return self.getToken(Rfc3164Parser.U_00A2, 0)

        def U_00A3(self):
            return self.getToken(Rfc3164Parser.U_00A3, 0)

        def U_00A4(self):
            return self.getToken(Rfc3164Parser.U_00A4, 0)

        def U_00A5(self):
            return self.getToken(Rfc3164Parser.U_00A5, 0)

        def U_00A6(self):
            return self.getToken(Rfc3164Parser.U_00A6, 0)

        def U_00A7(self):
            return self.getToken(Rfc3164Parser.U_00A7, 0)

        def U_00A8(self):
            return self.getToken(Rfc3164Parser.U_00A8, 0)

        def U_00A9(self):
            return self.getToken(Rfc3164Parser.U_00A9, 0)

        def U_00AA(self):
            return self.getToken(Rfc3164Parser.U_00AA, 0)

        def U_00AB(self):
            return self.getToken(Rfc3164Parser.U_00AB, 0)

        def U_00AC(self):
            return self.getToken(Rfc3164Parser.U_00AC, 0)

        def U_00AD(self):
            return self.getToken(Rfc3164Parser.U_00AD, 0)

        def U_00AE(self):
            return self.getToken(Rfc3164Parser.U_00AE, 0)

        def U_00AF(self):
            return self.getToken(Rfc3164Parser.U_00AF, 0)

        def U_00B0(self):
            return self.getToken(Rfc3164Parser.U_00B0, 0)

        def U_00B1(self):
            return self.getToken(Rfc3164Parser.U_00B1, 0)

        def U_00B2(self):
            return self.getToken(Rfc3164Parser.U_00B2, 0)

        def U_00B3(self):
            return self.getToken(Rfc3164Parser.U_00B3, 0)

        def U_00B4(self):
            return self.getToken(Rfc3164Parser.U_00B4, 0)

        def U_00B5(self):
            return self.getToken(Rfc3164Parser.U_00B5, 0)

        def U_00B6(self):
            return self.getToken(Rfc3164Parser.U_00B6, 0)

        def U_00B7(self):
            return self.getToken(Rfc3164Parser.U_00B7, 0)

        def U_00B8(self):
            return self.getToken(Rfc3164Parser.U_00B8, 0)

        def U_00B9(self):
            return self.getToken(Rfc3164Parser.U_00B9, 0)

        def U_00BA(self):
            return self.getToken(Rfc3164Parser.U_00BA, 0)

        def U_00BB(self):
            return self.getToken(Rfc3164Parser.U_00BB, 0)

        def U_00BC(self):
            return self.getToken(Rfc3164Parser.U_00BC, 0)

        def U_00BD(self):
            return self.getToken(Rfc3164Parser.U_00BD, 0)

        def U_00BE(self):
            return self.getToken(Rfc3164Parser.U_00BE, 0)

        def U_00BF(self):
            return self.getToken(Rfc3164Parser.U_00BF, 0)

        def U_00C0(self):
            return self.getToken(Rfc3164Parser.U_00C0, 0)

        def U_00C1(self):
            return self.getToken(Rfc3164Parser.U_00C1, 0)

        def U_00C2(self):
            return self.getToken(Rfc3164Parser.U_00C2, 0)

        def U_00C3(self):
            return self.getToken(Rfc3164Parser.U_00C3, 0)

        def U_00C4(self):
            return self.getToken(Rfc3164Parser.U_00C4, 0)

        def U_00C5(self):
            return self.getToken(Rfc3164Parser.U_00C5, 0)

        def U_00C6(self):
            return self.getToken(Rfc3164Parser.U_00C6, 0)

        def U_00C7(self):
            return self.getToken(Rfc3164Parser.U_00C7, 0)

        def U_00C8(self):
            return self.getToken(Rfc3164Parser.U_00C8, 0)

        def U_00C9(self):
            return self.getToken(Rfc3164Parser.U_00C9, 0)

        def U_00CA(self):
            return self.getToken(Rfc3164Parser.U_00CA, 0)

        def U_00CB(self):
            return self.getToken(Rfc3164Parser.U_00CB, 0)

        def U_00CC(self):
            return self.getToken(Rfc3164Parser.U_00CC, 0)

        def U_00CD(self):
            return self.getToken(Rfc3164Parser.U_00CD, 0)

        def U_00CE(self):
            return self.getToken(Rfc3164Parser.U_00CE, 0)

        def U_00CF(self):
            return self.getToken(Rfc3164Parser.U_00CF, 0)

        def U_00D0(self):
            return self.getToken(Rfc3164Parser.U_00D0, 0)

        def U_00D1(self):
            return self.getToken(Rfc3164Parser.U_00D1, 0)

        def U_00D2(self):
            return self.getToken(Rfc3164Parser.U_00D2, 0)

        def U_00D3(self):
            return self.getToken(Rfc3164Parser.U_00D3, 0)

        def U_00D4(self):
            return self.getToken(Rfc3164Parser.U_00D4, 0)

        def U_00D5(self):
            return self.getToken(Rfc3164Parser.U_00D5, 0)

        def U_00D6(self):
            return self.getToken(Rfc3164Parser.U_00D6, 0)

        def U_00D7(self):
            return self.getToken(Rfc3164Parser.U_00D7, 0)

        def U_00D8(self):
            return self.getToken(Rfc3164Parser.U_00D8, 0)

        def U_00D9(self):
            return self.getToken(Rfc3164Parser.U_00D9, 0)

        def U_00DA(self):
            return self.getToken(Rfc3164Parser.U_00DA, 0)

        def U_00DB(self):
            return self.getToken(Rfc3164Parser.U_00DB, 0)

        def U_00DC(self):
            return self.getToken(Rfc3164Parser.U_00DC, 0)

        def U_00DD(self):
            return self.getToken(Rfc3164Parser.U_00DD, 0)

        def U_00DE(self):
            return self.getToken(Rfc3164Parser.U_00DE, 0)

        def U_00DF(self):
            return self.getToken(Rfc3164Parser.U_00DF, 0)

        def U_00E0(self):
            return self.getToken(Rfc3164Parser.U_00E0, 0)

        def U_00E1(self):
            return self.getToken(Rfc3164Parser.U_00E1, 0)

        def U_00E2(self):
            return self.getToken(Rfc3164Parser.U_00E2, 0)

        def U_00E3(self):
            return self.getToken(Rfc3164Parser.U_00E3, 0)

        def U_00E4(self):
            return self.getToken(Rfc3164Parser.U_00E4, 0)

        def U_00E5(self):
            return self.getToken(Rfc3164Parser.U_00E5, 0)

        def U_00E6(self):
            return self.getToken(Rfc3164Parser.U_00E6, 0)

        def U_00E7(self):
            return self.getToken(Rfc3164Parser.U_00E7, 0)

        def U_00E8(self):
            return self.getToken(Rfc3164Parser.U_00E8, 0)

        def U_00E9(self):
            return self.getToken(Rfc3164Parser.U_00E9, 0)

        def U_00EA(self):
            return self.getToken(Rfc3164Parser.U_00EA, 0)

        def U_00EB(self):
            return self.getToken(Rfc3164Parser.U_00EB, 0)

        def U_00EC(self):
            return self.getToken(Rfc3164Parser.U_00EC, 0)

        def U_00ED(self):
            return self.getToken(Rfc3164Parser.U_00ED, 0)

        def U_00EE(self):
            return self.getToken(Rfc3164Parser.U_00EE, 0)

        def U_00EF(self):
            return self.getToken(Rfc3164Parser.U_00EF, 0)

        def U_00F0(self):
            return self.getToken(Rfc3164Parser.U_00F0, 0)

        def U_00F1(self):
            return self.getToken(Rfc3164Parser.U_00F1, 0)

        def U_00F2(self):
            return self.getToken(Rfc3164Parser.U_00F2, 0)

        def U_00F3(self):
            return self.getToken(Rfc3164Parser.U_00F3, 0)

        def U_00F4(self):
            return self.getToken(Rfc3164Parser.U_00F4, 0)

        def U_00F5(self):
            return self.getToken(Rfc3164Parser.U_00F5, 0)

        def U_00F6(self):
            return self.getToken(Rfc3164Parser.U_00F6, 0)

        def U_00F7(self):
            return self.getToken(Rfc3164Parser.U_00F7, 0)

        def U_00F8(self):
            return self.getToken(Rfc3164Parser.U_00F8, 0)

        def U_00F9(self):
            return self.getToken(Rfc3164Parser.U_00F9, 0)

        def U_00FA(self):
            return self.getToken(Rfc3164Parser.U_00FA, 0)

        def U_00FB(self):
            return self.getToken(Rfc3164Parser.U_00FB, 0)

        def U_00FC(self):
            return self.getToken(Rfc3164Parser.U_00FC, 0)

        def U_00FD(self):
            return self.getToken(Rfc3164Parser.U_00FD, 0)

        def U_00FE(self):
            return self.getToken(Rfc3164Parser.U_00FE, 0)

        def U_00FF(self):
            return self.getToken(Rfc3164Parser.U_00FF, 0)

        def getRuleIndex(self):
            return Rfc3164Parser.RULE_octet

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOctet" ):
                listener.enterOctet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOctet" ):
                listener.exitOctet(self)




    def octet(self):

        localctx = Rfc3164Parser.OctetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_octet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not(((((_la - 1)) & ~0x3f) == 0 and ((1 << (_la - 1)) & ((1 << (Rfc3164Parser.TAB - 1)) | (1 << (Rfc3164Parser.LF - 1)) | (1 << (Rfc3164Parser.CR - 1)) | (1 << (Rfc3164Parser.SPACE - 1)) | (1 << (Rfc3164Parser.EXCLAMATION - 1)) | (1 << (Rfc3164Parser.QUOTE - 1)) | (1 << (Rfc3164Parser.POUND - 1)) | (1 << (Rfc3164Parser.DOLLAR - 1)) | (1 << (Rfc3164Parser.PERCENT - 1)) | (1 << (Rfc3164Parser.AMPERSAND - 1)) | (1 << (Rfc3164Parser.APOSTROPHE - 1)) | (1 << (Rfc3164Parser.LEFT_PAREN - 1)) | (1 << (Rfc3164Parser.RIGHT_PAREN - 1)) | (1 << (Rfc3164Parser.ASTERISK - 1)) | (1 << (Rfc3164Parser.PLUS - 1)) | (1 << (Rfc3164Parser.COMMA - 1)) | (1 << (Rfc3164Parser.DASH - 1)) | (1 << (Rfc3164Parser.PERIOD - 1)) | (1 << (Rfc3164Parser.SLASH - 1)) | (1 << (Rfc3164Parser.ZERO - 1)) | (1 << (Rfc3164Parser.ONE - 1)) | (1 << (Rfc3164Parser.TWO - 1)) | (1 << (Rfc3164Parser.THREE - 1)) | (1 << (Rfc3164Parser.FOUR - 1)) | (1 << (Rfc3164Parser.FIVE - 1)) | (1 << (Rfc3164Parser.SIX - 1)) | (1 << (Rfc3164Parser.SEVEN - 1)) | (1 << (Rfc3164Parser.EIGHT - 1)) | (1 << (Rfc3164Parser.NINE - 1)) | (1 << (Rfc3164Parser.COLON - 1)) | (1 << (Rfc3164Parser.SEMICOLON - 1)) | (1 << (Rfc3164Parser.LESS_THAN - 1)) | (1 << (Rfc3164Parser.EQUALS - 1)) | (1 << (Rfc3164Parser.GREATER_THAN - 1)) | (1 << (Rfc3164Parser.QUESTION - 1)) | (1 << (Rfc3164Parser.AT - 1)) | (1 << (Rfc3164Parser.CAP_A - 1)) | (1 << (Rfc3164Parser.CAP_B - 1)) | (1 << (Rfc3164Parser.CAP_C - 1)) | (1 << (Rfc3164Parser.CAP_D - 1)) | (1 << (Rfc3164Parser.CAP_E - 1)) | (1 << (Rfc3164Parser.CAP_F - 1)) | (1 << (Rfc3164Parser.CAP_G - 1)) | (1 << (Rfc3164Parser.CAP_H - 1)) | (1 << (Rfc3164Parser.CAP_I - 1)) | (1 << (Rfc3164Parser.CAP_J - 1)) | (1 << (Rfc3164Parser.CAP_K - 1)) | (1 << (Rfc3164Parser.CAP_L - 1)) | (1 << (Rfc3164Parser.CAP_M - 1)) | (1 << (Rfc3164Parser.CAP_N - 1)) | (1 << (Rfc3164Parser.CAP_O - 1)) | (1 << (Rfc3164Parser.CAP_P - 1)) | (1 << (Rfc3164Parser.CAP_Q - 1)) | (1 << (Rfc3164Parser.CAP_R - 1)) | (1 << (Rfc3164Parser.CAP_S - 1)) | (1 << (Rfc3164Parser.CAP_T - 1)) | (1 << (Rfc3164Parser.CAP_U - 1)) | (1 << (Rfc3164Parser.CAP_V - 1)) | (1 << (Rfc3164Parser.CAP_W - 1)) | (1 << (Rfc3164Parser.CAP_X - 1)) | (1 << (Rfc3164Parser.CAP_Y - 1)) | (1 << (Rfc3164Parser.CAP_Z - 1)) | (1 << (Rfc3164Parser.LEFT_BRACE - 1)) | (1 << (Rfc3164Parser.BACKSLASH - 1)))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Rfc3164Parser.RIGHT_BRACE - 65)) | (1 << (Rfc3164Parser.CARAT - 65)) | (1 << (Rfc3164Parser.UNDERSCORE - 65)) | (1 << (Rfc3164Parser.ACCENT - 65)) | (1 << (Rfc3164Parser.A - 65)) | (1 << (Rfc3164Parser.B - 65)) | (1 << (Rfc3164Parser.C - 65)) | (1 << (Rfc3164Parser.D - 65)) | (1 << (Rfc3164Parser.E - 65)) | (1 << (Rfc3164Parser.F - 65)) | (1 << (Rfc3164Parser.G - 65)) | (1 << (Rfc3164Parser.H - 65)) | (1 << (Rfc3164Parser.I - 65)) | (1 << (Rfc3164Parser.J - 65)) | (1 << (Rfc3164Parser.K - 65)) | (1 << (Rfc3164Parser.L - 65)) | (1 << (Rfc3164Parser.M - 65)) | (1 << (Rfc3164Parser.N - 65)) | (1 << (Rfc3164Parser.O - 65)) | (1 << (Rfc3164Parser.P - 65)) | (1 << (Rfc3164Parser.Q - 65)) | (1 << (Rfc3164Parser.R - 65)) | (1 << (Rfc3164Parser.S - 65)) | (1 << (Rfc3164Parser.T - 65)) | (1 << (Rfc3164Parser.U - 65)) | (1 << (Rfc3164Parser.V - 65)) | (1 << (Rfc3164Parser.W - 65)) | (1 << (Rfc3164Parser.X - 65)) | (1 << (Rfc3164Parser.Y - 65)) | (1 << (Rfc3164Parser.Z - 65)) | (1 << (Rfc3164Parser.LEFT_CURLY_BRACE - 65)) | (1 << (Rfc3164Parser.PIPE - 65)) | (1 << (Rfc3164Parser.RIGHT_CURLY_BRACE - 65)) | (1 << (Rfc3164Parser.TILDE - 65)) | (1 << (Rfc3164Parser.U_0000 - 65)) | (1 << (Rfc3164Parser.U_0001 - 65)) | (1 << (Rfc3164Parser.U_0002 - 65)) | (1 << (Rfc3164Parser.U_0003 - 65)) | (1 << (Rfc3164Parser.U_0004 - 65)) | (1 << (Rfc3164Parser.U_0005 - 65)) | (1 << (Rfc3164Parser.U_0006 - 65)) | (1 << (Rfc3164Parser.U_0007 - 65)) | (1 << (Rfc3164Parser.U_0008 - 65)) | (1 << (Rfc3164Parser.U_000B - 65)) | (1 << (Rfc3164Parser.U_000C - 65)) | (1 << (Rfc3164Parser.U_000E - 65)) | (1 << (Rfc3164Parser.U_000F - 65)) | (1 << (Rfc3164Parser.U_0010 - 65)) | (1 << (Rfc3164Parser.U_0011 - 65)) | (1 << (Rfc3164Parser.U_0012 - 65)) | (1 << (Rfc3164Parser.U_0013 - 65)) | (1 << (Rfc3164Parser.U_0014 - 65)) | (1 << (Rfc3164Parser.U_0015 - 65)) | (1 << (Rfc3164Parser.U_0016 - 65)) | (1 << (Rfc3164Parser.U_0017 - 65)) | (1 << (Rfc3164Parser.U_0018 - 65)) | (1 << (Rfc3164Parser.U_0019 - 65)) | (1 << (Rfc3164Parser.U_001A - 65)) | (1 << (Rfc3164Parser.U_001B - 65)) | (1 << (Rfc3164Parser.U_001C - 65)) | (1 << (Rfc3164Parser.U_001D - 65)) | (1 << (Rfc3164Parser.U_001E - 65)) | (1 << (Rfc3164Parser.U_001F - 65)) | (1 << (Rfc3164Parser.U_007F - 65)))) != 0) or ((((_la - 129)) & ~0x3f) == 0 and ((1 << (_la - 129)) & ((1 << (Rfc3164Parser.U_0080 - 129)) | (1 << (Rfc3164Parser.U_0081 - 129)) | (1 << (Rfc3164Parser.U_0082 - 129)) | (1 << (Rfc3164Parser.U_0083 - 129)) | (1 << (Rfc3164Parser.U_0084 - 129)) | (1 << (Rfc3164Parser.U_0085 - 129)) | (1 << (Rfc3164Parser.U_0086 - 129)) | (1 << (Rfc3164Parser.U_0087 - 129)) | (1 << (Rfc3164Parser.U_0088 - 129)) | (1 << (Rfc3164Parser.U_0089 - 129)) | (1 << (Rfc3164Parser.U_008A - 129)) | (1 << (Rfc3164Parser.U_008B - 129)) | (1 << (Rfc3164Parser.U_008C - 129)) | (1 << (Rfc3164Parser.U_008D - 129)) | (1 << (Rfc3164Parser.U_008E - 129)) | (1 << (Rfc3164Parser.U_008F - 129)) | (1 << (Rfc3164Parser.U_0090 - 129)) | (1 << (Rfc3164Parser.U_0091 - 129)) | (1 << (Rfc3164Parser.U_0092 - 129)) | (1 << (Rfc3164Parser.U_0093 - 129)) | (1 << (Rfc3164Parser.U_0094 - 129)) | (1 << (Rfc3164Parser.U_0095 - 129)) | (1 << (Rfc3164Parser.U_0096 - 129)) | (1 << (Rfc3164Parser.U_0097 - 129)) | (1 << (Rfc3164Parser.U_0098 - 129)) | (1 << (Rfc3164Parser.U_0099 - 129)) | (1 << (Rfc3164Parser.U_009A - 129)) | (1 << (Rfc3164Parser.U_009B - 129)) | (1 << (Rfc3164Parser.U_009C - 129)) | (1 << (Rfc3164Parser.U_009D - 129)) | (1 << (Rfc3164Parser.U_009E - 129)) | (1 << (Rfc3164Parser.U_009F - 129)) | (1 << (Rfc3164Parser.U_00A0 - 129)) | (1 << (Rfc3164Parser.U_00A1 - 129)) | (1 << (Rfc3164Parser.U_00A2 - 129)) | (1 << (Rfc3164Parser.U_00A3 - 129)) | (1 << (Rfc3164Parser.U_00A4 - 129)) | (1 << (Rfc3164Parser.U_00A5 - 129)) | (1 << (Rfc3164Parser.U_00A6 - 129)) | (1 << (Rfc3164Parser.U_00A7 - 129)) | (1 << (Rfc3164Parser.U_00A8 - 129)) | (1 << (Rfc3164Parser.U_00A9 - 129)) | (1 << (Rfc3164Parser.U_00AA - 129)) | (1 << (Rfc3164Parser.U_00AB - 129)) | (1 << (Rfc3164Parser.U_00AC - 129)) | (1 << (Rfc3164Parser.U_00AD - 129)) | (1 << (Rfc3164Parser.U_00AE - 129)) | (1 << (Rfc3164Parser.U_00AF - 129)) | (1 << (Rfc3164Parser.U_00B0 - 129)) | (1 << (Rfc3164Parser.U_00B1 - 129)) | (1 << (Rfc3164Parser.U_00B2 - 129)) | (1 << (Rfc3164Parser.U_00B3 - 129)) | (1 << (Rfc3164Parser.U_00B4 - 129)) | (1 << (Rfc3164Parser.U_00B5 - 129)) | (1 << (Rfc3164Parser.U_00B6 - 129)) | (1 << (Rfc3164Parser.U_00B7 - 129)) | (1 << (Rfc3164Parser.U_00B8 - 129)) | (1 << (Rfc3164Parser.U_00B9 - 129)) | (1 << (Rfc3164Parser.U_00BA - 129)) | (1 << (Rfc3164Parser.U_00BB - 129)) | (1 << (Rfc3164Parser.U_00BC - 129)) | (1 << (Rfc3164Parser.U_00BD - 129)) | (1 << (Rfc3164Parser.U_00BE - 129)) | (1 << (Rfc3164Parser.U_00BF - 129)))) != 0) or ((((_la - 193)) & ~0x3f) == 0 and ((1 << (_la - 193)) & ((1 << (Rfc3164Parser.U_00C0 - 193)) | (1 << (Rfc3164Parser.U_00C1 - 193)) | (1 << (Rfc3164Parser.U_00C2 - 193)) | (1 << (Rfc3164Parser.U_00C3 - 193)) | (1 << (Rfc3164Parser.U_00C4 - 193)) | (1 << (Rfc3164Parser.U_00C5 - 193)) | (1 << (Rfc3164Parser.U_00C6 - 193)) | (1 << (Rfc3164Parser.U_00C7 - 193)) | (1 << (Rfc3164Parser.U_00C8 - 193)) | (1 << (Rfc3164Parser.U_00C9 - 193)) | (1 << (Rfc3164Parser.U_00CA - 193)) | (1 << (Rfc3164Parser.U_00CB - 193)) | (1 << (Rfc3164Parser.U_00CC - 193)) | (1 << (Rfc3164Parser.U_00CD - 193)) | (1 << (Rfc3164Parser.U_00CE - 193)) | (1 << (Rfc3164Parser.U_00CF - 193)) | (1 << (Rfc3164Parser.U_00D0 - 193)) | (1 << (Rfc3164Parser.U_00D1 - 193)) | (1 << (Rfc3164Parser.U_00D2 - 193)) | (1 << (Rfc3164Parser.U_00D3 - 193)) | (1 << (Rfc3164Parser.U_00D4 - 193)) | (1 << (Rfc3164Parser.U_00D5 - 193)) | (1 << (Rfc3164Parser.U_00D6 - 193)) | (1 << (Rfc3164Parser.U_00D7 - 193)) | (1 << (Rfc3164Parser.U_00D8 - 193)) | (1 << (Rfc3164Parser.U_00D9 - 193)) | (1 << (Rfc3164Parser.U_00DA - 193)) | (1 << (Rfc3164Parser.U_00DB - 193)) | (1 << (Rfc3164Parser.U_00DC - 193)) | (1 << (Rfc3164Parser.U_00DD - 193)) | (1 << (Rfc3164Parser.U_00DE - 193)) | (1 << (Rfc3164Parser.U_00DF - 193)) | (1 << (Rfc3164Parser.U_00E0 - 193)) | (1 << (Rfc3164Parser.U_00E1 - 193)) | (1 << (Rfc3164Parser.U_00E2 - 193)) | (1 << (Rfc3164Parser.U_00E3 - 193)) | (1 << (Rfc3164Parser.U_00E4 - 193)) | (1 << (Rfc3164Parser.U_00E5 - 193)) | (1 << (Rfc3164Parser.U_00E6 - 193)) | (1 << (Rfc3164Parser.U_00E7 - 193)) | (1 << (Rfc3164Parser.U_00E8 - 193)) | (1 << (Rfc3164Parser.U_00E9 - 193)) | (1 << (Rfc3164Parser.U_00EA - 193)) | (1 << (Rfc3164Parser.U_00EB - 193)) | (1 << (Rfc3164Parser.U_00EC - 193)) | (1 << (Rfc3164Parser.U_00ED - 193)) | (1 << (Rfc3164Parser.U_00EE - 193)) | (1 << (Rfc3164Parser.U_00EF - 193)) | (1 << (Rfc3164Parser.U_00F0 - 193)) | (1 << (Rfc3164Parser.U_00F1 - 193)) | (1 << (Rfc3164Parser.U_00F2 - 193)) | (1 << (Rfc3164Parser.U_00F3 - 193)) | (1 << (Rfc3164Parser.U_00F4 - 193)) | (1 << (Rfc3164Parser.U_00F5 - 193)) | (1 << (Rfc3164Parser.U_00F6 - 193)) | (1 << (Rfc3164Parser.U_00F7 - 193)) | (1 << (Rfc3164Parser.U_00F8 - 193)) | (1 << (Rfc3164Parser.U_00F9 - 193)) | (1 << (Rfc3164Parser.U_00FA - 193)) | (1 << (Rfc3164Parser.U_00FB - 193)) | (1 << (Rfc3164Parser.U_00FC - 193)) | (1 << (Rfc3164Parser.U_00FD - 193)) | (1 << (Rfc3164Parser.U_00FE - 193)) | (1 << (Rfc3164Parser.U_00FF - 193)))) != 0)):
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
            return self.getToken(Rfc3164Parser.SPACE, 0)

        def getRuleIndex(self):
            return Rfc3164Parser.RULE_sp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSp" ):
                listener.enterSp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSp" ):
                listener.exitSp(self)




    def sp(self):

        localctx = Rfc3164Parser.SpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_sp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(Rfc3164Parser.SPACE)
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
            return self.getToken(Rfc3164Parser.EXCLAMATION, 0)

        def QUOTE(self):
            return self.getToken(Rfc3164Parser.QUOTE, 0)

        def POUND(self):
            return self.getToken(Rfc3164Parser.POUND, 0)

        def DOLLAR(self):
            return self.getToken(Rfc3164Parser.DOLLAR, 0)

        def PERCENT(self):
            return self.getToken(Rfc3164Parser.PERCENT, 0)

        def AMPERSAND(self):
            return self.getToken(Rfc3164Parser.AMPERSAND, 0)

        def APOSTROPHE(self):
            return self.getToken(Rfc3164Parser.APOSTROPHE, 0)

        def LEFT_PAREN(self):
            return self.getToken(Rfc3164Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(Rfc3164Parser.RIGHT_PAREN, 0)

        def ASTERISK(self):
            return self.getToken(Rfc3164Parser.ASTERISK, 0)

        def PLUS(self):
            return self.getToken(Rfc3164Parser.PLUS, 0)

        def COMMA(self):
            return self.getToken(Rfc3164Parser.COMMA, 0)

        def DASH(self):
            return self.getToken(Rfc3164Parser.DASH, 0)

        def PERIOD(self):
            return self.getToken(Rfc3164Parser.PERIOD, 0)

        def SLASH(self):
            return self.getToken(Rfc3164Parser.SLASH, 0)

        def ZERO(self):
            return self.getToken(Rfc3164Parser.ZERO, 0)

        def ONE(self):
            return self.getToken(Rfc3164Parser.ONE, 0)

        def TWO(self):
            return self.getToken(Rfc3164Parser.TWO, 0)

        def THREE(self):
            return self.getToken(Rfc3164Parser.THREE, 0)

        def FOUR(self):
            return self.getToken(Rfc3164Parser.FOUR, 0)

        def FIVE(self):
            return self.getToken(Rfc3164Parser.FIVE, 0)

        def SIX(self):
            return self.getToken(Rfc3164Parser.SIX, 0)

        def SEVEN(self):
            return self.getToken(Rfc3164Parser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(Rfc3164Parser.EIGHT, 0)

        def NINE(self):
            return self.getToken(Rfc3164Parser.NINE, 0)

        def COLON(self):
            return self.getToken(Rfc3164Parser.COLON, 0)

        def SEMICOLON(self):
            return self.getToken(Rfc3164Parser.SEMICOLON, 0)

        def LESS_THAN(self):
            return self.getToken(Rfc3164Parser.LESS_THAN, 0)

        def EQUALS(self):
            return self.getToken(Rfc3164Parser.EQUALS, 0)

        def GREATER_THAN(self):
            return self.getToken(Rfc3164Parser.GREATER_THAN, 0)

        def QUESTION(self):
            return self.getToken(Rfc3164Parser.QUESTION, 0)

        def AT(self):
            return self.getToken(Rfc3164Parser.AT, 0)

        def CAP_A(self):
            return self.getToken(Rfc3164Parser.CAP_A, 0)

        def CAP_B(self):
            return self.getToken(Rfc3164Parser.CAP_B, 0)

        def CAP_C(self):
            return self.getToken(Rfc3164Parser.CAP_C, 0)

        def CAP_D(self):
            return self.getToken(Rfc3164Parser.CAP_D, 0)

        def CAP_E(self):
            return self.getToken(Rfc3164Parser.CAP_E, 0)

        def CAP_F(self):
            return self.getToken(Rfc3164Parser.CAP_F, 0)

        def CAP_G(self):
            return self.getToken(Rfc3164Parser.CAP_G, 0)

        def CAP_H(self):
            return self.getToken(Rfc3164Parser.CAP_H, 0)

        def CAP_I(self):
            return self.getToken(Rfc3164Parser.CAP_I, 0)

        def CAP_J(self):
            return self.getToken(Rfc3164Parser.CAP_J, 0)

        def CAP_K(self):
            return self.getToken(Rfc3164Parser.CAP_K, 0)

        def CAP_L(self):
            return self.getToken(Rfc3164Parser.CAP_L, 0)

        def CAP_M(self):
            return self.getToken(Rfc3164Parser.CAP_M, 0)

        def CAP_N(self):
            return self.getToken(Rfc3164Parser.CAP_N, 0)

        def CAP_O(self):
            return self.getToken(Rfc3164Parser.CAP_O, 0)

        def CAP_P(self):
            return self.getToken(Rfc3164Parser.CAP_P, 0)

        def CAP_Q(self):
            return self.getToken(Rfc3164Parser.CAP_Q, 0)

        def CAP_R(self):
            return self.getToken(Rfc3164Parser.CAP_R, 0)

        def CAP_S(self):
            return self.getToken(Rfc3164Parser.CAP_S, 0)

        def CAP_T(self):
            return self.getToken(Rfc3164Parser.CAP_T, 0)

        def CAP_U(self):
            return self.getToken(Rfc3164Parser.CAP_U, 0)

        def CAP_V(self):
            return self.getToken(Rfc3164Parser.CAP_V, 0)

        def CAP_W(self):
            return self.getToken(Rfc3164Parser.CAP_W, 0)

        def CAP_X(self):
            return self.getToken(Rfc3164Parser.CAP_X, 0)

        def CAP_Y(self):
            return self.getToken(Rfc3164Parser.CAP_Y, 0)

        def CAP_Z(self):
            return self.getToken(Rfc3164Parser.CAP_Z, 0)

        def LEFT_BRACE(self):
            return self.getToken(Rfc3164Parser.LEFT_BRACE, 0)

        def BACKSLASH(self):
            return self.getToken(Rfc3164Parser.BACKSLASH, 0)

        def RIGHT_BRACE(self):
            return self.getToken(Rfc3164Parser.RIGHT_BRACE, 0)

        def CARAT(self):
            return self.getToken(Rfc3164Parser.CARAT, 0)

        def UNDERSCORE(self):
            return self.getToken(Rfc3164Parser.UNDERSCORE, 0)

        def ACCENT(self):
            return self.getToken(Rfc3164Parser.ACCENT, 0)

        def A(self):
            return self.getToken(Rfc3164Parser.A, 0)

        def B(self):
            return self.getToken(Rfc3164Parser.B, 0)

        def C(self):
            return self.getToken(Rfc3164Parser.C, 0)

        def D(self):
            return self.getToken(Rfc3164Parser.D, 0)

        def E(self):
            return self.getToken(Rfc3164Parser.E, 0)

        def F(self):
            return self.getToken(Rfc3164Parser.F, 0)

        def G(self):
            return self.getToken(Rfc3164Parser.G, 0)

        def H(self):
            return self.getToken(Rfc3164Parser.H, 0)

        def I(self):
            return self.getToken(Rfc3164Parser.I, 0)

        def J(self):
            return self.getToken(Rfc3164Parser.J, 0)

        def K(self):
            return self.getToken(Rfc3164Parser.K, 0)

        def L(self):
            return self.getToken(Rfc3164Parser.L, 0)

        def M(self):
            return self.getToken(Rfc3164Parser.M, 0)

        def N(self):
            return self.getToken(Rfc3164Parser.N, 0)

        def O(self):
            return self.getToken(Rfc3164Parser.O, 0)

        def P(self):
            return self.getToken(Rfc3164Parser.P, 0)

        def Q(self):
            return self.getToken(Rfc3164Parser.Q, 0)

        def R(self):
            return self.getToken(Rfc3164Parser.R, 0)

        def S(self):
            return self.getToken(Rfc3164Parser.S, 0)

        def T(self):
            return self.getToken(Rfc3164Parser.T, 0)

        def U(self):
            return self.getToken(Rfc3164Parser.U, 0)

        def V(self):
            return self.getToken(Rfc3164Parser.V, 0)

        def W(self):
            return self.getToken(Rfc3164Parser.W, 0)

        def X(self):
            return self.getToken(Rfc3164Parser.X, 0)

        def Y(self):
            return self.getToken(Rfc3164Parser.Y, 0)

        def Z(self):
            return self.getToken(Rfc3164Parser.Z, 0)

        def LEFT_CURLY_BRACE(self):
            return self.getToken(Rfc3164Parser.LEFT_CURLY_BRACE, 0)

        def PIPE(self):
            return self.getToken(Rfc3164Parser.PIPE, 0)

        def RIGHT_CURLY_BRACE(self):
            return self.getToken(Rfc3164Parser.RIGHT_CURLY_BRACE, 0)

        def TILDE(self):
            return self.getToken(Rfc3164Parser.TILDE, 0)

        def getRuleIndex(self):
            return Rfc3164Parser.RULE_printusascii

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintusascii" ):
                listener.enterPrintusascii(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintusascii" ):
                listener.exitPrintusascii(self)




    def printusascii(self):

        localctx = Rfc3164Parser.PrintusasciiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_printusascii)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc3164Parser.EXCLAMATION) | (1 << Rfc3164Parser.QUOTE) | (1 << Rfc3164Parser.POUND) | (1 << Rfc3164Parser.DOLLAR) | (1 << Rfc3164Parser.PERCENT) | (1 << Rfc3164Parser.AMPERSAND) | (1 << Rfc3164Parser.APOSTROPHE) | (1 << Rfc3164Parser.LEFT_PAREN) | (1 << Rfc3164Parser.RIGHT_PAREN) | (1 << Rfc3164Parser.ASTERISK) | (1 << Rfc3164Parser.PLUS) | (1 << Rfc3164Parser.COMMA) | (1 << Rfc3164Parser.DASH) | (1 << Rfc3164Parser.PERIOD) | (1 << Rfc3164Parser.SLASH) | (1 << Rfc3164Parser.ZERO) | (1 << Rfc3164Parser.ONE) | (1 << Rfc3164Parser.TWO) | (1 << Rfc3164Parser.THREE) | (1 << Rfc3164Parser.FOUR) | (1 << Rfc3164Parser.FIVE) | (1 << Rfc3164Parser.SIX) | (1 << Rfc3164Parser.SEVEN) | (1 << Rfc3164Parser.EIGHT) | (1 << Rfc3164Parser.NINE) | (1 << Rfc3164Parser.COLON) | (1 << Rfc3164Parser.SEMICOLON) | (1 << Rfc3164Parser.LESS_THAN) | (1 << Rfc3164Parser.EQUALS) | (1 << Rfc3164Parser.GREATER_THAN) | (1 << Rfc3164Parser.QUESTION) | (1 << Rfc3164Parser.AT) | (1 << Rfc3164Parser.CAP_A) | (1 << Rfc3164Parser.CAP_B) | (1 << Rfc3164Parser.CAP_C) | (1 << Rfc3164Parser.CAP_D) | (1 << Rfc3164Parser.CAP_E) | (1 << Rfc3164Parser.CAP_F) | (1 << Rfc3164Parser.CAP_G) | (1 << Rfc3164Parser.CAP_H) | (1 << Rfc3164Parser.CAP_I) | (1 << Rfc3164Parser.CAP_J) | (1 << Rfc3164Parser.CAP_K) | (1 << Rfc3164Parser.CAP_L) | (1 << Rfc3164Parser.CAP_M) | (1 << Rfc3164Parser.CAP_N) | (1 << Rfc3164Parser.CAP_O) | (1 << Rfc3164Parser.CAP_P) | (1 << Rfc3164Parser.CAP_Q) | (1 << Rfc3164Parser.CAP_R) | (1 << Rfc3164Parser.CAP_S) | (1 << Rfc3164Parser.CAP_T) | (1 << Rfc3164Parser.CAP_U) | (1 << Rfc3164Parser.CAP_V) | (1 << Rfc3164Parser.CAP_W) | (1 << Rfc3164Parser.CAP_X) | (1 << Rfc3164Parser.CAP_Y) | (1 << Rfc3164Parser.CAP_Z) | (1 << Rfc3164Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc3164Parser.BACKSLASH - 64)) | (1 << (Rfc3164Parser.RIGHT_BRACE - 64)) | (1 << (Rfc3164Parser.CARAT - 64)) | (1 << (Rfc3164Parser.UNDERSCORE - 64)) | (1 << (Rfc3164Parser.ACCENT - 64)) | (1 << (Rfc3164Parser.A - 64)) | (1 << (Rfc3164Parser.B - 64)) | (1 << (Rfc3164Parser.C - 64)) | (1 << (Rfc3164Parser.D - 64)) | (1 << (Rfc3164Parser.E - 64)) | (1 << (Rfc3164Parser.F - 64)) | (1 << (Rfc3164Parser.G - 64)) | (1 << (Rfc3164Parser.H - 64)) | (1 << (Rfc3164Parser.I - 64)) | (1 << (Rfc3164Parser.J - 64)) | (1 << (Rfc3164Parser.K - 64)) | (1 << (Rfc3164Parser.L - 64)) | (1 << (Rfc3164Parser.M - 64)) | (1 << (Rfc3164Parser.N - 64)) | (1 << (Rfc3164Parser.O - 64)) | (1 << (Rfc3164Parser.P - 64)) | (1 << (Rfc3164Parser.Q - 64)) | (1 << (Rfc3164Parser.R - 64)) | (1 << (Rfc3164Parser.S - 64)) | (1 << (Rfc3164Parser.T - 64)) | (1 << (Rfc3164Parser.U - 64)) | (1 << (Rfc3164Parser.V - 64)) | (1 << (Rfc3164Parser.W - 64)) | (1 << (Rfc3164Parser.X - 64)) | (1 << (Rfc3164Parser.Y - 64)) | (1 << (Rfc3164Parser.Z - 64)) | (1 << (Rfc3164Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc3164Parser.PIPE - 64)) | (1 << (Rfc3164Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc3164Parser.TILDE - 64)))) != 0)):
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
            return self.getToken(Rfc3164Parser.EXCLAMATION, 0)

        def POUND(self):
            return self.getToken(Rfc3164Parser.POUND, 0)

        def DOLLAR(self):
            return self.getToken(Rfc3164Parser.DOLLAR, 0)

        def PERCENT(self):
            return self.getToken(Rfc3164Parser.PERCENT, 0)

        def AMPERSAND(self):
            return self.getToken(Rfc3164Parser.AMPERSAND, 0)

        def APOSTROPHE(self):
            return self.getToken(Rfc3164Parser.APOSTROPHE, 0)

        def LEFT_PAREN(self):
            return self.getToken(Rfc3164Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(Rfc3164Parser.RIGHT_PAREN, 0)

        def ASTERISK(self):
            return self.getToken(Rfc3164Parser.ASTERISK, 0)

        def PLUS(self):
            return self.getToken(Rfc3164Parser.PLUS, 0)

        def COMMA(self):
            return self.getToken(Rfc3164Parser.COMMA, 0)

        def DASH(self):
            return self.getToken(Rfc3164Parser.DASH, 0)

        def PERIOD(self):
            return self.getToken(Rfc3164Parser.PERIOD, 0)

        def SLASH(self):
            return self.getToken(Rfc3164Parser.SLASH, 0)

        def ZERO(self):
            return self.getToken(Rfc3164Parser.ZERO, 0)

        def ONE(self):
            return self.getToken(Rfc3164Parser.ONE, 0)

        def TWO(self):
            return self.getToken(Rfc3164Parser.TWO, 0)

        def THREE(self):
            return self.getToken(Rfc3164Parser.THREE, 0)

        def FOUR(self):
            return self.getToken(Rfc3164Parser.FOUR, 0)

        def FIVE(self):
            return self.getToken(Rfc3164Parser.FIVE, 0)

        def SIX(self):
            return self.getToken(Rfc3164Parser.SIX, 0)

        def SEVEN(self):
            return self.getToken(Rfc3164Parser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(Rfc3164Parser.EIGHT, 0)

        def NINE(self):
            return self.getToken(Rfc3164Parser.NINE, 0)

        def COLON(self):
            return self.getToken(Rfc3164Parser.COLON, 0)

        def SEMICOLON(self):
            return self.getToken(Rfc3164Parser.SEMICOLON, 0)

        def LESS_THAN(self):
            return self.getToken(Rfc3164Parser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(Rfc3164Parser.GREATER_THAN, 0)

        def QUESTION(self):
            return self.getToken(Rfc3164Parser.QUESTION, 0)

        def AT(self):
            return self.getToken(Rfc3164Parser.AT, 0)

        def CAP_A(self):
            return self.getToken(Rfc3164Parser.CAP_A, 0)

        def CAP_B(self):
            return self.getToken(Rfc3164Parser.CAP_B, 0)

        def CAP_C(self):
            return self.getToken(Rfc3164Parser.CAP_C, 0)

        def CAP_D(self):
            return self.getToken(Rfc3164Parser.CAP_D, 0)

        def CAP_E(self):
            return self.getToken(Rfc3164Parser.CAP_E, 0)

        def CAP_F(self):
            return self.getToken(Rfc3164Parser.CAP_F, 0)

        def CAP_G(self):
            return self.getToken(Rfc3164Parser.CAP_G, 0)

        def CAP_H(self):
            return self.getToken(Rfc3164Parser.CAP_H, 0)

        def CAP_I(self):
            return self.getToken(Rfc3164Parser.CAP_I, 0)

        def CAP_J(self):
            return self.getToken(Rfc3164Parser.CAP_J, 0)

        def CAP_K(self):
            return self.getToken(Rfc3164Parser.CAP_K, 0)

        def CAP_L(self):
            return self.getToken(Rfc3164Parser.CAP_L, 0)

        def CAP_M(self):
            return self.getToken(Rfc3164Parser.CAP_M, 0)

        def CAP_N(self):
            return self.getToken(Rfc3164Parser.CAP_N, 0)

        def CAP_O(self):
            return self.getToken(Rfc3164Parser.CAP_O, 0)

        def CAP_P(self):
            return self.getToken(Rfc3164Parser.CAP_P, 0)

        def CAP_Q(self):
            return self.getToken(Rfc3164Parser.CAP_Q, 0)

        def CAP_R(self):
            return self.getToken(Rfc3164Parser.CAP_R, 0)

        def CAP_S(self):
            return self.getToken(Rfc3164Parser.CAP_S, 0)

        def CAP_T(self):
            return self.getToken(Rfc3164Parser.CAP_T, 0)

        def CAP_U(self):
            return self.getToken(Rfc3164Parser.CAP_U, 0)

        def CAP_V(self):
            return self.getToken(Rfc3164Parser.CAP_V, 0)

        def CAP_W(self):
            return self.getToken(Rfc3164Parser.CAP_W, 0)

        def CAP_X(self):
            return self.getToken(Rfc3164Parser.CAP_X, 0)

        def CAP_Y(self):
            return self.getToken(Rfc3164Parser.CAP_Y, 0)

        def CAP_Z(self):
            return self.getToken(Rfc3164Parser.CAP_Z, 0)

        def LEFT_BRACE(self):
            return self.getToken(Rfc3164Parser.LEFT_BRACE, 0)

        def BACKSLASH(self):
            return self.getToken(Rfc3164Parser.BACKSLASH, 0)

        def CARAT(self):
            return self.getToken(Rfc3164Parser.CARAT, 0)

        def UNDERSCORE(self):
            return self.getToken(Rfc3164Parser.UNDERSCORE, 0)

        def ACCENT(self):
            return self.getToken(Rfc3164Parser.ACCENT, 0)

        def A(self):
            return self.getToken(Rfc3164Parser.A, 0)

        def B(self):
            return self.getToken(Rfc3164Parser.B, 0)

        def C(self):
            return self.getToken(Rfc3164Parser.C, 0)

        def D(self):
            return self.getToken(Rfc3164Parser.D, 0)

        def E(self):
            return self.getToken(Rfc3164Parser.E, 0)

        def F(self):
            return self.getToken(Rfc3164Parser.F, 0)

        def G(self):
            return self.getToken(Rfc3164Parser.G, 0)

        def H(self):
            return self.getToken(Rfc3164Parser.H, 0)

        def I(self):
            return self.getToken(Rfc3164Parser.I, 0)

        def J(self):
            return self.getToken(Rfc3164Parser.J, 0)

        def K(self):
            return self.getToken(Rfc3164Parser.K, 0)

        def L(self):
            return self.getToken(Rfc3164Parser.L, 0)

        def M(self):
            return self.getToken(Rfc3164Parser.M, 0)

        def N(self):
            return self.getToken(Rfc3164Parser.N, 0)

        def O(self):
            return self.getToken(Rfc3164Parser.O, 0)

        def P(self):
            return self.getToken(Rfc3164Parser.P, 0)

        def Q(self):
            return self.getToken(Rfc3164Parser.Q, 0)

        def R(self):
            return self.getToken(Rfc3164Parser.R, 0)

        def S(self):
            return self.getToken(Rfc3164Parser.S, 0)

        def T(self):
            return self.getToken(Rfc3164Parser.T, 0)

        def U(self):
            return self.getToken(Rfc3164Parser.U, 0)

        def V(self):
            return self.getToken(Rfc3164Parser.V, 0)

        def W(self):
            return self.getToken(Rfc3164Parser.W, 0)

        def X(self):
            return self.getToken(Rfc3164Parser.X, 0)

        def Y(self):
            return self.getToken(Rfc3164Parser.Y, 0)

        def Z(self):
            return self.getToken(Rfc3164Parser.Z, 0)

        def LEFT_CURLY_BRACE(self):
            return self.getToken(Rfc3164Parser.LEFT_CURLY_BRACE, 0)

        def PIPE(self):
            return self.getToken(Rfc3164Parser.PIPE, 0)

        def RIGHT_CURLY_BRACE(self):
            return self.getToken(Rfc3164Parser.RIGHT_CURLY_BRACE, 0)

        def TILDE(self):
            return self.getToken(Rfc3164Parser.TILDE, 0)

        def getRuleIndex(self):
            return Rfc3164Parser.RULE_printusasciinospecials

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintusasciinospecials" ):
                listener.enterPrintusasciinospecials(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintusasciinospecials" ):
                listener.exitPrintusasciinospecials(self)




    def printusasciinospecials(self):

        localctx = Rfc3164Parser.PrintusasciinospecialsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_printusasciinospecials)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc3164Parser.EXCLAMATION) | (1 << Rfc3164Parser.POUND) | (1 << Rfc3164Parser.DOLLAR) | (1 << Rfc3164Parser.PERCENT) | (1 << Rfc3164Parser.AMPERSAND) | (1 << Rfc3164Parser.APOSTROPHE) | (1 << Rfc3164Parser.LEFT_PAREN) | (1 << Rfc3164Parser.RIGHT_PAREN) | (1 << Rfc3164Parser.ASTERISK) | (1 << Rfc3164Parser.PLUS) | (1 << Rfc3164Parser.COMMA) | (1 << Rfc3164Parser.DASH) | (1 << Rfc3164Parser.PERIOD) | (1 << Rfc3164Parser.SLASH) | (1 << Rfc3164Parser.ZERO) | (1 << Rfc3164Parser.ONE) | (1 << Rfc3164Parser.TWO) | (1 << Rfc3164Parser.THREE) | (1 << Rfc3164Parser.FOUR) | (1 << Rfc3164Parser.FIVE) | (1 << Rfc3164Parser.SIX) | (1 << Rfc3164Parser.SEVEN) | (1 << Rfc3164Parser.EIGHT) | (1 << Rfc3164Parser.NINE) | (1 << Rfc3164Parser.COLON) | (1 << Rfc3164Parser.SEMICOLON) | (1 << Rfc3164Parser.LESS_THAN) | (1 << Rfc3164Parser.GREATER_THAN) | (1 << Rfc3164Parser.QUESTION) | (1 << Rfc3164Parser.AT) | (1 << Rfc3164Parser.CAP_A) | (1 << Rfc3164Parser.CAP_B) | (1 << Rfc3164Parser.CAP_C) | (1 << Rfc3164Parser.CAP_D) | (1 << Rfc3164Parser.CAP_E) | (1 << Rfc3164Parser.CAP_F) | (1 << Rfc3164Parser.CAP_G) | (1 << Rfc3164Parser.CAP_H) | (1 << Rfc3164Parser.CAP_I) | (1 << Rfc3164Parser.CAP_J) | (1 << Rfc3164Parser.CAP_K) | (1 << Rfc3164Parser.CAP_L) | (1 << Rfc3164Parser.CAP_M) | (1 << Rfc3164Parser.CAP_N) | (1 << Rfc3164Parser.CAP_O) | (1 << Rfc3164Parser.CAP_P) | (1 << Rfc3164Parser.CAP_Q) | (1 << Rfc3164Parser.CAP_R) | (1 << Rfc3164Parser.CAP_S) | (1 << Rfc3164Parser.CAP_T) | (1 << Rfc3164Parser.CAP_U) | (1 << Rfc3164Parser.CAP_V) | (1 << Rfc3164Parser.CAP_W) | (1 << Rfc3164Parser.CAP_X) | (1 << Rfc3164Parser.CAP_Y) | (1 << Rfc3164Parser.CAP_Z) | (1 << Rfc3164Parser.LEFT_BRACE))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Rfc3164Parser.BACKSLASH - 64)) | (1 << (Rfc3164Parser.CARAT - 64)) | (1 << (Rfc3164Parser.UNDERSCORE - 64)) | (1 << (Rfc3164Parser.ACCENT - 64)) | (1 << (Rfc3164Parser.A - 64)) | (1 << (Rfc3164Parser.B - 64)) | (1 << (Rfc3164Parser.C - 64)) | (1 << (Rfc3164Parser.D - 64)) | (1 << (Rfc3164Parser.E - 64)) | (1 << (Rfc3164Parser.F - 64)) | (1 << (Rfc3164Parser.G - 64)) | (1 << (Rfc3164Parser.H - 64)) | (1 << (Rfc3164Parser.I - 64)) | (1 << (Rfc3164Parser.J - 64)) | (1 << (Rfc3164Parser.K - 64)) | (1 << (Rfc3164Parser.L - 64)) | (1 << (Rfc3164Parser.M - 64)) | (1 << (Rfc3164Parser.N - 64)) | (1 << (Rfc3164Parser.O - 64)) | (1 << (Rfc3164Parser.P - 64)) | (1 << (Rfc3164Parser.Q - 64)) | (1 << (Rfc3164Parser.R - 64)) | (1 << (Rfc3164Parser.S - 64)) | (1 << (Rfc3164Parser.T - 64)) | (1 << (Rfc3164Parser.U - 64)) | (1 << (Rfc3164Parser.V - 64)) | (1 << (Rfc3164Parser.W - 64)) | (1 << (Rfc3164Parser.X - 64)) | (1 << (Rfc3164Parser.Y - 64)) | (1 << (Rfc3164Parser.Z - 64)) | (1 << (Rfc3164Parser.LEFT_CURLY_BRACE - 64)) | (1 << (Rfc3164Parser.PIPE - 64)) | (1 << (Rfc3164Parser.RIGHT_CURLY_BRACE - 64)) | (1 << (Rfc3164Parser.TILDE - 64)))) != 0)):
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
            return self.getToken(Rfc3164Parser.ONE, 0)

        def TWO(self):
            return self.getToken(Rfc3164Parser.TWO, 0)

        def THREE(self):
            return self.getToken(Rfc3164Parser.THREE, 0)

        def FOUR(self):
            return self.getToken(Rfc3164Parser.FOUR, 0)

        def FIVE(self):
            return self.getToken(Rfc3164Parser.FIVE, 0)

        def SIX(self):
            return self.getToken(Rfc3164Parser.SIX, 0)

        def SEVEN(self):
            return self.getToken(Rfc3164Parser.SEVEN, 0)

        def EIGHT(self):
            return self.getToken(Rfc3164Parser.EIGHT, 0)

        def NINE(self):
            return self.getToken(Rfc3164Parser.NINE, 0)

        def getRuleIndex(self):
            return Rfc3164Parser.RULE_nonzero_digit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonzero_digit" ):
                listener.enterNonzero_digit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonzero_digit" ):
                listener.exitNonzero_digit(self)




    def nonzero_digit(self):

        localctx = Rfc3164Parser.Nonzero_digitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_nonzero_digit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc3164Parser.ONE) | (1 << Rfc3164Parser.TWO) | (1 << Rfc3164Parser.THREE) | (1 << Rfc3164Parser.FOUR) | (1 << Rfc3164Parser.FIVE) | (1 << Rfc3164Parser.SIX) | (1 << Rfc3164Parser.SEVEN) | (1 << Rfc3164Parser.EIGHT) | (1 << Rfc3164Parser.NINE))) != 0)):
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
            return Rfc3164Parser.RULE_digit

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ZeroDigitContext(DigitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.DigitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ZERO(self):
            return self.getToken(Rfc3164Parser.ZERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterZeroDigit" ):
                listener.enterZeroDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitZeroDigit" ):
                listener.exitZeroDigit(self)


    class NonZeroDigitContext(DigitContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Rfc3164Parser.DigitContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def nonzero_digit(self):
            return self.getTypedRuleContext(Rfc3164Parser.Nonzero_digitContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonZeroDigit" ):
                listener.enterNonZeroDigit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonZeroDigit" ):
                listener.exitNonZeroDigit(self)



    def digit(self):

        localctx = Rfc3164Parser.DigitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_digit)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Rfc3164Parser.ZERO]:
                localctx = Rfc3164Parser.ZeroDigitContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(Rfc3164Parser.ZERO)
                pass
            elif token in [Rfc3164Parser.ONE, Rfc3164Parser.TWO, Rfc3164Parser.THREE, Rfc3164Parser.FOUR, Rfc3164Parser.FIVE, Rfc3164Parser.SIX, Rfc3164Parser.SEVEN, Rfc3164Parser.EIGHT, Rfc3164Parser.NINE]:
                localctx = Rfc3164Parser.NonZeroDigitContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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


    class CapitalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAP_A(self):
            return self.getToken(Rfc3164Parser.CAP_A, 0)

        def CAP_B(self):
            return self.getToken(Rfc3164Parser.CAP_B, 0)

        def CAP_C(self):
            return self.getToken(Rfc3164Parser.CAP_C, 0)

        def CAP_D(self):
            return self.getToken(Rfc3164Parser.CAP_D, 0)

        def CAP_E(self):
            return self.getToken(Rfc3164Parser.CAP_E, 0)

        def CAP_F(self):
            return self.getToken(Rfc3164Parser.CAP_F, 0)

        def CAP_G(self):
            return self.getToken(Rfc3164Parser.CAP_G, 0)

        def CAP_H(self):
            return self.getToken(Rfc3164Parser.CAP_H, 0)

        def CAP_I(self):
            return self.getToken(Rfc3164Parser.CAP_I, 0)

        def CAP_J(self):
            return self.getToken(Rfc3164Parser.CAP_J, 0)

        def CAP_K(self):
            return self.getToken(Rfc3164Parser.CAP_K, 0)

        def CAP_L(self):
            return self.getToken(Rfc3164Parser.CAP_L, 0)

        def CAP_M(self):
            return self.getToken(Rfc3164Parser.CAP_M, 0)

        def CAP_N(self):
            return self.getToken(Rfc3164Parser.CAP_N, 0)

        def CAP_O(self):
            return self.getToken(Rfc3164Parser.CAP_O, 0)

        def CAP_P(self):
            return self.getToken(Rfc3164Parser.CAP_P, 0)

        def CAP_Q(self):
            return self.getToken(Rfc3164Parser.CAP_Q, 0)

        def CAP_R(self):
            return self.getToken(Rfc3164Parser.CAP_R, 0)

        def CAP_S(self):
            return self.getToken(Rfc3164Parser.CAP_S, 0)

        def CAP_T(self):
            return self.getToken(Rfc3164Parser.CAP_T, 0)

        def CAP_U(self):
            return self.getToken(Rfc3164Parser.CAP_U, 0)

        def CAP_V(self):
            return self.getToken(Rfc3164Parser.CAP_V, 0)

        def CAP_W(self):
            return self.getToken(Rfc3164Parser.CAP_W, 0)

        def CAP_X(self):
            return self.getToken(Rfc3164Parser.CAP_X, 0)

        def CAP_Y(self):
            return self.getToken(Rfc3164Parser.CAP_Y, 0)

        def CAP_Z(self):
            return self.getToken(Rfc3164Parser.CAP_Z, 0)

        def getRuleIndex(self):
            return Rfc3164Parser.RULE_capital

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapital" ):
                listener.enterCapital(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapital" ):
                listener.exitCapital(self)




    def capital(self):

        localctx = Rfc3164Parser.CapitalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_capital)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Rfc3164Parser.CAP_A) | (1 << Rfc3164Parser.CAP_B) | (1 << Rfc3164Parser.CAP_C) | (1 << Rfc3164Parser.CAP_D) | (1 << Rfc3164Parser.CAP_E) | (1 << Rfc3164Parser.CAP_F) | (1 << Rfc3164Parser.CAP_G) | (1 << Rfc3164Parser.CAP_H) | (1 << Rfc3164Parser.CAP_I) | (1 << Rfc3164Parser.CAP_J) | (1 << Rfc3164Parser.CAP_K) | (1 << Rfc3164Parser.CAP_L) | (1 << Rfc3164Parser.CAP_M) | (1 << Rfc3164Parser.CAP_N) | (1 << Rfc3164Parser.CAP_O) | (1 << Rfc3164Parser.CAP_P) | (1 << Rfc3164Parser.CAP_Q) | (1 << Rfc3164Parser.CAP_R) | (1 << Rfc3164Parser.CAP_S) | (1 << Rfc3164Parser.CAP_T) | (1 << Rfc3164Parser.CAP_U) | (1 << Rfc3164Parser.CAP_V) | (1 << Rfc3164Parser.CAP_W) | (1 << Rfc3164Parser.CAP_X) | (1 << Rfc3164Parser.CAP_Y) | (1 << Rfc3164Parser.CAP_Z))) != 0)):
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


    class LowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: Optional[ParserRuleContext]=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A(self):
            return self.getToken(Rfc3164Parser.A, 0)

        def B(self):
            return self.getToken(Rfc3164Parser.B, 0)

        def C(self):
            return self.getToken(Rfc3164Parser.C, 0)

        def D(self):
            return self.getToken(Rfc3164Parser.D, 0)

        def E(self):
            return self.getToken(Rfc3164Parser.E, 0)

        def F(self):
            return self.getToken(Rfc3164Parser.F, 0)

        def G(self):
            return self.getToken(Rfc3164Parser.G, 0)

        def H(self):
            return self.getToken(Rfc3164Parser.H, 0)

        def I(self):
            return self.getToken(Rfc3164Parser.I, 0)

        def J(self):
            return self.getToken(Rfc3164Parser.J, 0)

        def K(self):
            return self.getToken(Rfc3164Parser.K, 0)

        def L(self):
            return self.getToken(Rfc3164Parser.L, 0)

        def M(self):
            return self.getToken(Rfc3164Parser.M, 0)

        def N(self):
            return self.getToken(Rfc3164Parser.N, 0)

        def O(self):
            return self.getToken(Rfc3164Parser.O, 0)

        def P(self):
            return self.getToken(Rfc3164Parser.P, 0)

        def Q(self):
            return self.getToken(Rfc3164Parser.Q, 0)

        def R(self):
            return self.getToken(Rfc3164Parser.R, 0)

        def S(self):
            return self.getToken(Rfc3164Parser.S, 0)

        def T(self):
            return self.getToken(Rfc3164Parser.T, 0)

        def U(self):
            return self.getToken(Rfc3164Parser.U, 0)

        def V(self):
            return self.getToken(Rfc3164Parser.V, 0)

        def W(self):
            return self.getToken(Rfc3164Parser.W, 0)

        def X(self):
            return self.getToken(Rfc3164Parser.X, 0)

        def Y(self):
            return self.getToken(Rfc3164Parser.Y, 0)

        def Z(self):
            return self.getToken(Rfc3164Parser.Z, 0)

        def getRuleIndex(self):
            return Rfc3164Parser.RULE_lower

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLower" ):
                listener.enterLower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLower" ):
                listener.exitLower(self)




    def lower(self):

        localctx = Rfc3164Parser.LowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_lower)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not(((((_la - 69)) & ~0x3f) == 0 and ((1 << (_la - 69)) & ((1 << (Rfc3164Parser.A - 69)) | (1 << (Rfc3164Parser.B - 69)) | (1 << (Rfc3164Parser.C - 69)) | (1 << (Rfc3164Parser.D - 69)) | (1 << (Rfc3164Parser.E - 69)) | (1 << (Rfc3164Parser.F - 69)) | (1 << (Rfc3164Parser.G - 69)) | (1 << (Rfc3164Parser.H - 69)) | (1 << (Rfc3164Parser.I - 69)) | (1 << (Rfc3164Parser.J - 69)) | (1 << (Rfc3164Parser.K - 69)) | (1 << (Rfc3164Parser.L - 69)) | (1 << (Rfc3164Parser.M - 69)) | (1 << (Rfc3164Parser.N - 69)) | (1 << (Rfc3164Parser.O - 69)) | (1 << (Rfc3164Parser.P - 69)) | (1 << (Rfc3164Parser.Q - 69)) | (1 << (Rfc3164Parser.R - 69)) | (1 << (Rfc3164Parser.S - 69)) | (1 << (Rfc3164Parser.T - 69)) | (1 << (Rfc3164Parser.U - 69)) | (1 << (Rfc3164Parser.V - 69)) | (1 << (Rfc3164Parser.W - 69)) | (1 << (Rfc3164Parser.X - 69)) | (1 << (Rfc3164Parser.Y - 69)) | (1 << (Rfc3164Parser.Z - 69)))) != 0)):
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





