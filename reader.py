import pandas as pd
from person import *

class Reader:
    def __init__(self):
        data = pd.ExcelFile('SpermPositive.xlsx')
        self.df = pd.read_excel(data, sheet_name='Sheet')
    
    def getDataFrame(self):
        return self.df

    def print_columns_and_a_value(self):
        for col in self.df.columns:
            value = self.df[col].iloc[1] if not self.df[col].empty else None
            print(f"Column: {col}, 2nd value: {value}")

    def get_participants(self):
        """
        This function reads the Excel file and returns a list of participants.
        It distinguishes between donors and recipients based on their responses.
        """
        participants = []
        for _, row in self.df.iterrows():
            if row['First of all, tell us which one applies to you'] == "I'm interested in donating":
                donor = Donor(
                    RID=row['Respondent ID'],
                    CID=row['Collector ID'],
                    Start_Date=row['Start Date'],
                    End_Date=row['End Date'],
                    IP_Address=row['IP Address'],
                    Email=row['Email Address'],
                    FirstName=row['First Name'],
                    LastName=row['Last Name'],
                    age=row['Demographics'],
                    City=row['Unnamed: 27'],
                    Country=row['Unnamed: 30'],
                    height=row['Unnamed: 34'],
                    weight=row['Unnamed: 35'],
                    nationality=row['Unnamed: 36'],
                    ethnicity=row['Unnamed: 37'],
                    )
                
                if row["After reading the description above, which option(s) appeal to you?"] == "Yes Yes Yes!":
                    donor.homeFertility = 3
                elif row["Unnamed: 12"] == "Perhaps":
                    donor.homeFertility = 2
                else:
                    donor.homeFertility = 1
                
                if row["Unnamed: 14"] == "Yes Yes Yes!":
                    donor.privateDonor = 3
                
                elif row["Unnamed: 15"] == "Perhaps":
                    donor.privateDonor = 2
                else:
                    donor.privateDonor = 1

                if row["What level of involvement would you want with any child born through this process?"] == "Full, shared parental responsibility and rights with the recipient and their partner":
                    donor.involvementLevel = 3
                elif row["Unnamed: 18"] == "Being a known figure in the child’s life without parental responsibilities and rights":
                    donor.involvementLevel = 2
                else:
                    donor.involvementLevel = 1

                donor.criteriaText = row["Sperm Positive is used by heterosexual and LGBTI+ singles and couples. Please specify any preferences or other criteria, such as cross-cultural or religious restrictions."]
                donor.awesomeText = row["What makes you awesome?"]
                donor.medicalText = row["Please give details of your medical history, or family medical history, that may be relevant."]
                donor.moreText = row["Anything else you'd like to share?"]
                
                participants.append(donor)
            else:
                recipient = Recipient(
                    RID=row['Respondent ID'],
                    CID=row['Collector ID'],
                    Start_Date=row['Start Date'],
                    End_Date=row['End Date'],
                    IP_Address=row['IP Address'],
                    Email=row['Email Address'],
                    FirstName=row['First Name'],
                    LastName=row['Last Name'],
                    age=row['Demographics'],
                    City=row['Unnamed: 27'],
                    Country=row['Unnamed: 30'],
                    height=row['Unnamed: 34'],
                    weight=row['Unnamed: 35'],
                    nationality=row['Unnamed: 36'],
                    ethnicity=row['Unnamed: 37'],
                    )
                
                if row["After reading the description above, which option(s) appeal to you?"] != None:
                    recipient.homeFertility = 3
                elif row["Unnamed: 12"] != None:
                    recipient.homeFertility = 2
                else:
                    recipient.homeFertility = 1

                if row["Unnamed: 14"] != None:
                    recipient.privateDonor = 3
                elif row["Unnamed: 15"] != None:
                    recipient.privateDonor = 2
                else:
                    recipient.privateDonor = 1

                if row["What level of involvement would you want with any child born through this process?"] != None:
                    recipient.involvementLevel = 3
                elif row["Unnamed: 18"] != None:
                    recipient.involvementLevel = 2
                else:
                    recipient.involvementLevel = 1

                recipient.criteriaText = row["Sperm Positive is used by heterosexual and LGBTI+ singles and couples. Please specify any preferences or other criteria, such as cross-cultural or religious restrictions."]
                recipient.awesomeText = row["What makes you awesome?"]
                recipient.medicalText = row["Please give details of your medical history, or family medical history, that may be relevant."]
                recipient.moreText = row["Anything else you'd like to share?"]
                participants.append(recipient)
        return participants