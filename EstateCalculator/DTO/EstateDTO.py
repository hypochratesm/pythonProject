import dataclasses as dc


#Custom class
#NamedTuple
#Dataclass
@dc.dataclass(unsafe_hash=True)
class EstateDTO:
    def __init__(self):
        self.dealAmount    = 0
        self.buildYear     =""
        self.dealYear      =""
        self.dong          =""
        self.apartmentName =""
        self.dealMonth     =""
        self.dealDay       =""
        self.areaExcl      = 0
        self.jibun         =""
        self.regionalCode  =""
        self.flor          =""
        self.reqGbn        =""
        self.contractMonth =""
        self.modifyDate    =""

    dealAmount    : float = float("inf")
    buildYear     : str =""
    dealYear      : str =""
    dong          : str =""
    apartmentName : str =""
    dealMonth     : str =""
    dealDay       : str =""
    areaExcl      : float = float("inf")
    jibun         : str =""
    regionalCode  : str =""
    flor          : str =""
    reqGbn        : str =""
    contractMonth : str =""
    modifyDate    : str =""