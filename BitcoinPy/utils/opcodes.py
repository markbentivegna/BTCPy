"""Opcodes for Bitcoin Script language. For more details, see BitcoinGraph white paper"""

PUSH_DATA = {
    '00': 'OP_0',
    '01': 'OP_PUSHBYTES_1',
    '02': 'OP_PUSHBYTES_2',
    '03': 'OP_PUSHBYTES_3',
    '04': 'OP_PUSHBYTES_4',
    '05': 'OP_PUSHBYTES_5',
    '06': 'OP_PUSHBYTES_6',
    '07': 'OP_PUSHBYTES_7',
    '08': 'OP_PUSHBYTES_8',
    '09': 'OP_PUSHBYTES_9',
    '0a': 'OP_PUSHBYTES_10',
    '0b': 'OP_PUSHBYTES_11',
    '0c': 'OP_PUSHBYTES_12',
    '0d': 'OP_PUSHBYTES_13',
    '0e': 'OP_PUSHBYTES_14',
    '0f': 'OP_PUSHBYTES_15',
    '10': 'OP_PUSHBYTES_16',
    '11': 'OP_PUSHBYTES_17',
    '12': 'OP_PUSHBYTES_18',
    '13': 'OP_PUSHBYTES_19',
    '14': 'OP_PUSHBYTES_20',
    '15': 'OP_PUSHBYTES_21',
    '16': 'OP_PUSHBYTES_22',
    '17': 'OP_PUSHBYTES_23',
    '18': 'OP_PUSHBYTES_24',
    '19': 'OP_PUSHBYTES_25',
    '1a': 'OP_PUSHBYTES_26',
    '1b': 'OP_PUSHBYTES_27',
    '1c': 'OP_PUSHBYTES_28',
    '1d': 'OP_PUSHBYTES_29',
    '1e': 'OP_PUSHBYTES_30',
    '1f': 'OP_PUSHBYTES_31',
    '20': 'OP_PUSHBYTES_32',
    '21': 'OP_PUSHBYTES_33',
    '22': 'OP_PUSHBYTES_34',
    '23': 'OP_PUSHBYTES_35',
    '24': 'OP_PUSHBYTES_36',
    '25': 'OP_PUSHBYTES_37',
    '26': 'OP_PUSHBYTES_38',
    '27': 'OP_PUSHBYTES_39',
    '28': 'OP_PUSHBYTES_40',
    '29': 'OP_PUSHBYTES_41',
    '2a': 'OP_PUSHBYTES_42',
    '2b': 'OP_PUSHBYTES_43',
    '2c': 'OP_PUSHBYTES_44',
    '2d': 'OP_PUSHBYTES_45',
    '2e': 'OP_PUSHBYTES_46',
    '2f': 'OP_PUSHBYTES_47',
    '30': 'OP_PUSHBYTES_48',
    '31': 'OP_PUSHBYTES_49',
    '32': 'OP_PUSHBYTES_50',
    '33': 'OP_PUSHBYTES_51',
    '34': 'OP_PUSHBYTES_52',
    '35': 'OP_PUSHBYTES_53',
    '36': 'OP_PUSHBYTES_54',
    '37': 'OP_PUSHBYTES_55',
    '38': 'OP_PUSHBYTES_56',
    '39': 'OP_PUSHBYTES_57',
    '3a': 'OP_PUSHBYTES_58',
    '3b': 'OP_PUSHBYTES_59',
    '3c': 'OP_PUSHBYTES_60',
    '3d': 'OP_PUSHBYTES_61',
    '3e': 'OP_PUSHBYTES_62',
    '3f': 'OP_PUSHBYTES_63',
    '40': 'OP_PUSHBYTES_64',
    '41': 'OP_PUSHBYTES_65',
    '42': 'OP_PUSHBYTES_66',
    '43': 'OP_PUSHBYTES_67',
    '44': 'OP_PUSHBYTES_68',
    '45': 'OP_PUSHBYTES_69',
    '46': 'OP_PUSHBYTES_70',
    '47': 'OP_PUSHBYTES_71',
    '48': 'OP_PUSHBYTES_72',
    '49': 'OP_PUSHBYTES_73',
    '4a': 'OP_PUSHBYTES_74',
    '4b': 'OP_PUSHBYTES_75',
    '4c': 'OP_PUSHDATA1',
    '4d': 'OP_PUSHDATA2',
    '4e': 'OP_PUSHDATA4',
    '4f': 'OP_1NEGATE',
    '50': 'OP_RESERVED',
    '51': 'OP_1',
    '52': 'OP_2',
    '53': 'OP_3',
    '54': 'OP_4',
    '55': 'OP_5',
    '56': 'OP_6',
    '57': 'OP_7',
    '58': 'OP_8',
    '59': 'OP_9',
    '5a': 'OP_10',
    '5b': 'OP_11',
    '5c': 'OP_12',
    '5d': 'OP_13',
    '5e': 'OP_14',
    '5f': 'OP_15',
    '60': 'OP_16'
}

CONTROL_FLOW = {
    '61': 'OP_NOP',
    '62': 'OP_VER',
    '63': 'OP_IF',
    '64': 'OP_NOTIF',
    '65': 'OP_VERIF',
    '66': 'OP_VERNOTIF',
    '67': 'OP_ELSE',
    '68': 'OP_ENDIF',
    '69': 'OP_VERIFY',
    '6a': 'OP_RETURN'
}

STACK_OPERATORS = {
    '6b': 'OP_TOALTSTACK',
    '6c': 'OP_FROMALTSTACK',
    '6d': 'OP_2DROP',
    '6e': 'OP_2DUP',
    '6f': 'OP_3DUP',
    '70': 'OP_2OVER',
    '71': 'OP_2ROT',
    '72': 'OP_2SWAP',
    '73': 'OP_IFDUP',
    '74': 'OP_DEPTH',
    '75': 'OP_DROP',
    '76': 'OP_DUP',
    '77': 'OP_NIP',
    '78': 'OP_OVER',
    '79': 'OP_PICK',
    '7a': 'OP_ROLL',
    '7b': 'OP_ROT',
    '7c': 'OP_SWAP',
    '7d': 'OP_TUCK',
}

STRINGS = {
    '7e': 'OP_CAT',
    '7f': 'OP_SUBSTR',
    '80': 'OP_LEFT',
    '81': 'OP_RIGHT',
    '82': 'OP_SIZE'
}

BITWISE_LOGIC = {
    '83': 'OP_INVERT',
    '84': 'OP_AND',
    '85': 'OP_OR',
    '86': 'OP_XOR',
    '87': 'OP_EQUAL',
    '88': 'OP_EQUALVERIFY',
    '89': 'OP_RESERVED1',
    '8a': 'OP_RESERVED2'
}

NUMERIC = {
    '8b': 'OP_1ADD',
    '8c': 'OP_1SUB',
    '8d': 'OP_2MUL',
    '8e': 'OP_2DIV',
    '8f': 'OP_NEGATE',
    '90': 'OP_ABS',
    '91': 'OP_NOT',
    '92': 'OP_0NOTEQUAL',
    '93': 'OP_ADD',
    '94': 'OP_SUB',
    '95': 'OP_MUL',
    '96': 'OP_DIV',
    '97': 'OP_MOD',
    '98': 'OP_LSHIFT',
    '99': 'OP_RSHIFT',
    '9a': 'OP_BOOLAND',
    '9b': 'OP_BOOLOR',
    '9c': 'OP_NUMEQUAL',
    '9d': 'OP_NUMEQUALVERIFY',
    '9e': 'OP_NUMNOTEQUAL',
    '9f': 'OP_LESSTHAN',
    'a0': 'OP_GREATERTHAN',
    'a1': 'OP_LESSTHANOREQUAL',
    'a2': 'OP_GREATERTHANOREQUAL',
    'a3': 'OP_MIN',
    'a4': 'OP_MAX',
    'a5': 'OP_WITHIN'
}

CRYPTOGRAPHY = {
    'a6': 'OP_RIPEMD160',
    'a7': 'OP_SHA1',
    'a8': 'OP_SHA256',
    'a9': 'OP_HASH160',
    'aa': 'OP_HASH256',
    'ab': 'OP_CODESEPARATOR',
    'ac': 'OP_CHECKSIG',
    'ad': 'OP_CHECKSIGVERIFY',
    'ae': 'OP_CHECKMULTISIG',
    'af': 'OP_CHECKMULTISIGVERIFY'
}

OTHER = {
    'b0': 'OP_NOP1',
    'b1': 'OP_CHECKLOCKTIMEVERIFY',
    'b2': 'OP_CHECKSEQUENCEVERIFY',
    'b3': 'OP_NOP4',
    'b4': 'OP_NOP5',
    'b5': 'OP_NOP6',
    'b6': 'OP_NOP7',
    'b7': 'OP_NOP8',
    'b8': 'OP_NOP9',
    'b9': 'OP_NOP10',
    'ba': 'OP_CHECKSIGADD',
    'bb': 'OP_RETURN_187',
    'bc': 'OP_RETURN_188',
    'bd': 'OP_RETURN_189',
    'be': 'OP_RETURN_190',
    'bf': 'OP_RETURN_191',
    'c0': 'OP_RETURN_192',
    'c1': 'OP_RETURN_193',
    'c2': 'OP_RETURN_194',
    'c3': 'OP_RETURN_195',
    'c4': 'OP_RETURN_196',
    'c5': 'OP_RETURN_197',
    'c6': 'OP_RETURN_198',
    'c7': 'OP_RETURN_199',
    'c8': 'OP_RETURN_200',
    'c9': 'OP_RETURN_201',
    'ca': 'OP_RETURN_202',
    'cb': 'OP_RETURN_203',
    'cc': 'OP_RETURN_204',
    'cd': 'OP_RETURN_205',
    'ce': 'OP_RETURN_206',
    'cf': 'OP_RETURN_207',
    'd0': 'OP_RETURN_208',
    'd1': 'OP_RETURN_209',
    'd2': 'OP_RETURN_210',
    'd3': 'OP_RETURN_211',
    'd4': 'OP_RETURN_212',
    'd5': 'OP_RETURN_213',
    'd6': 'OP_RETURN_214',
    'd7': 'OP_RETURN_215',
    'd8': 'OP_RETURN_216',
    'd9': 'OP_RETURN_217',
    'da': 'OP_RETURN_218',
    'db': 'OP_RETURN_219',
    'dc': 'OP_RETURN_220',
    'dd': 'OP_RETURN_221',
    'de': 'OP_RETURN_222',
    'df': 'OP_RETURN_223',
    'e0': 'OP_RETURN_224',
    'e1': 'OP_RETURN_225',
    'e2': 'OP_RETURN_226',
    'e3': 'OP_RETURN_227',
    'e4': 'OP_RETURN_228',
    'e5': 'OP_RETURN_229',
    'e6': 'OP_RETURN_230',
    'e7': 'OP_RETURN_231',
    'e8': 'OP_RETURN_232',
    'e9': 'OP_RETURN_233',
    'ea': 'OP_RETURN_234',
    'eb': 'OP_RETURN_235',
    'ec': 'OP_RETURN_236',
    'ed': 'OP_RETURN_237',
    'ee': 'OP_RETURN_238',
    'ef': 'OP_RETURN_239',
    'f0': 'OP_RETURN_240',
    'f1': 'OP_RETURN_241',
    'f2': 'OP_RETURN_242',
    'f3': 'OP_RETURN_243',
    'f4': 'OP_RETURN_244',
    'f5': 'OP_RETURN_245',
    'f6': 'OP_RETURN_246',
    'f7': 'OP_RETURN_247',
    'f8': 'OP_RETURN_248',
    'f9': 'OP_RETURN_249',
    'fa': 'OP_RETURN_250',
    'fb': 'OP_RETURN_251',
    'fc': 'OP_RETURN_252',
    'fd': 'OP_RETURN_253',
    'fe': 'OP_RETURN_254',
    'ff': 'OP_INVALIDOPCODE'
}
