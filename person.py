class Person:
    def __init__(self, RID, CID, Start_Date, End_Date, age, IP_Address=None, Email=None, FirstName=None, LastName=None, City=None, Country=None, height=None, weight=None, nationality=None, ethnicity=None):
        try:
            self.RID = int(RID)
            self.CID = int(CID)
        except: self.RID = self.CID = None
        self.Start_Date = Start_Date
        self.End_Date = End_Date
        self.IP_Address = IP_Address
        self.Email = Email
        self.FirstName = FirstName
        self.LastName = LastName
        self.age = age
        self.City = City
        self.Country = Country
        self.height = height
        self.weight = weight
        self.nationality = nationality
        self.ethnicity = ethnicity
        self.homeFertility = None
        self.privateDonor = None
        self.involvementLevel = None
        self.criteriaText = None # Survey gives raw text - maybe best to check it's safe to store
        self.awesomeText = None 
        self.medicalText = None
        self.moreText = None
    
    # Getters and Setters
    def getRID(self):
        return self.RID
    
    def getCID(self):
        return self.CID
    
    def getStartDate(self):
        return self.Start_Date
    
    def getEndDate(self):
        return self.End_Date
    
    def getIP(self):
        return self.IP_Address
    
    def getEmail(self):
        return self.Email
    
    def getFirstName(self):
        return self.FirstName
    
    def getLastName(self):
        return self.LastName
    
    def getAge(self):
        return self.age
    
    def getCity(self):
        return self.City
    
    def getCountry(self):
        return self.Country

    def getHeight(self):
        return self.height
    
    def getWeight(self):
        return self.weight
    
    def getNationality(self):
        return self.nationality
    
    def getEthnicity(self):
        return self.ethnicity
    
    def getHomeFertility(self):
        return self.homeFertility
    
    def getPrivateDonor(self):
        return self.privateDonor
    
    def getInvolvementLevel(self):
        return self.involvementLevel
    
    def getCriteriaText(self):
        return self.criteriaText

    def getAwesomeText(self):
        return self.awesomeText
    
    def getMedicalText(self):
        return self.medicalText
    
    def getMoreText(self):
        return self.moreText
    
    def setRID(self, RID):
        self.RID = RID

    def setCID(self, CID):
        self.CID = CID
    
    def setStartDate(self, Start_Date):
        self.Start_Date = Start_Date
    
    def setEndDate(self, End_Date):
        self.End_Date = End_Date
    
    def setIP(self, IP_Address):
        self.IP_Address = IP_Address
    
    def setEmail(self, Email):
        self.Email = Email
    
    def setFirstName(self, FirstName):
        self.FirstName = FirstName
    
    def setLastName(self, LastName):
        self.LastName = LastName
    
    def setAge(self, age):
        self.age = age
    
    def setCity(self, City):
        self.City = City
    
    def setCountry(self, Country):
        self.Country = Country
    
    def setHeight(self, height):
        self.height = height

    def setWeight(self, weight):
        self.weight = weight

    def setCriteriaText(self, criteriaText):
        self.criteriaText = criteriaText
    
    def setHomeFertility(self, homeFertility):
        self.homeFertility = homeFertility
    
    def setPrivateDonor(self, privateDonor):
        self.privateDonor = privateDonor

    def setInvolvementLevel(self, involvementLevel):
        self.involvementLevel = involvementLevel

    def setAwesomeText(self, awesomeText):
        self.awesomeText = awesomeText
    
    def setMedicalText(self, medicalText):
        self.medicalText = medicalText
    
    def setMoreText(self, moreText):
        self.moreText = moreText

    def __str__(self):
        return f"Person: RID={self.RID},\nCID={self.CID},\nStart Date={self.Start_Date},\nEnd Date={self.End_Date},\nIP Address={self.IP_Address},\nName={self.FirstName} {self.LastName},\nAge={self.age},\nCity={self.City},\nCountry={self.Country},\nHeight={self.height}, Weight={self.weight},\nNationality={self.nationality}, Ethnicity={self.ethnicity},\nHome Fertility={self.homeFertility}, Private Donor={self.privateDonor}, Involvement Level={self.involvementLevel},\nCriteria={self.criteriaText},\nAwesomeText={self.awesomeText},\nMedicalText={self.medicalText},\nMoreText={self.moreText}\n"

class Donor(Person):
    def __init__(self, RID, CID, Start_Date, End_Date, IP_Address=None, Email=None, FirstName=None, LastName=None, age=None, City=None, Country=None, height=None, weight=None, nationality=None, ethnicity=None):
        super().__init__(RID, CID, Start_Date, End_Date, age, IP_Address, Email, FirstName, LastName, City, Country, height, weight, nationality, ethnicity)
    
    def __str__(self):
        return f"Donor: RID={self.RID},\nCID={self.CID},\nStart Date={self.Start_Date},\nEnd Date={self.End_Date},\nIP Address={self.IP_Address},\nName={self.FirstName} {self.LastName},\nAge={self.age},\nCity={self.City},\nCountry={self.Country},\nHeight={self.height}, Weight={self.weight},\nNationality={self.nationality}, Ethnicity={self.ethnicity},\nHome Fertility={self.homeFertility}, Private Donor={self.privateDonor}, Involvement Level={self.involvementLevel},\nCriteria={self.criteriaText},\nAwesomeText={self.awesomeText},\nMedicalText={self.medicalText},\nMoreText={self.moreText}\n"

class Recipient(Person):
    def __init__(self, RID, CID, Start_Date, End_Date, IP_Address=None, Email=None, FirstName=None, LastName=None, age=None, City=None, Country=None, height=None, weight=None, nationality=None, ethnicity=None):
        super().__init__(RID, CID, Start_Date, End_Date, age, IP_Address, Email, FirstName, LastName, City, Country, height, weight, nationality, ethnicity)
    
    def __str__(self):
        return f"Recipient: RID={self.RID},\nCID={self.CID},\nStart Date={self.Start_Date},\nEnd Date={self.End_Date},\nIP Address={self.IP_Address},\nName={self.FirstName} {self.LastName},\nAge={self.age},\nCity={self.City},\nCountry={self.Country},\nHeight={self.height}, Weight={self.weight},\nNationality={self.nationality}, Ethnicity={self.ethnicity},\nHome Fertility={self.homeFertility}, Private Donor={self.privateDonor}, Involvement Level={self.involvementLevel},\nCriteria={self.criteriaText},\nAwesomeText={self.awesomeText},\nMedicalText={self.medicalText},\nMoreText={self.moreText}\n"
