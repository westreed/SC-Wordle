from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x661390, Add, -330),# units:Construction Animation  index:184    from 330 To 0
        SetMemory(0x663770, Add, 37),# units:Ground Weapon  index:184    from 93 To 130
        SetMemory(0x664360, Add, -599783421),# units:Special Ability Flags  index:184    from 1140850689 To 541067268
        SetMemory(0x662E70, Add, -4),# units:Target Acquisition Range  index:184    from 4 To 0
        SetMemory(0x662B40, Add, -63),# units:StarEdit Placement Box Width  index:184    from 64 To 1
        SetMemory(0x662B40, Add, -4128768),# units:StarEdit Placement Box Height  index:184    from 64 To 1
        SetMemory(0x661D88, Add, -31),# units:Unit Size Left  index:184    from 32 To 1
        SetMemory(0x661D88, Add, -2031616),# units:Unit Size Up  index:184    from 32 To 1
        SetMemory(0x661D8C, Add, -30),# units:Unit Size Right  index:184    from 31 To 1
        SetMemory(0x661D8C, Add, -1966080),# units:Unit Size Down  index:184    from 31 To 1
        SetMemory(0x663858, Add, -72),# units:Staredit Group Flags  index:184    from 80 To 8
        SetMemory(0x661688, Add, 835),# units:Staredit Availability Flags  index:184    from 0 To 835
        SetMemory(0x666394, Add, -120),# sprites:Image File  index:282    from 353 To 233
        SetMemory(0x66EFEC, Add, 15),# images:Iscript ID  index:233    from 74 To 89
    ])

