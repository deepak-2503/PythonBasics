college_info = {
    "student1" : {
        "name" : "Deepak",
        "subject" : {
            "hindi" : 67,
            "phy" : 76,
            "chem" : 89,
        }
    } ,  # here , is important
    "student2" : {
        "name" : "Rahul",
        "subject" : {
            "hindi" : 86,
            "phy" : 96,
            "chem" : 54,
        }
        
    }
}

print(college_info)
print(college_info["student1"]["name"])
print(college_info["student1"]["subject"])
print(college_info["student2"]["subject"]["chem"])


