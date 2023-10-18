countries = ["Algeria","Angola","Benin","Botswana","Burkina Faso","Burundi","Cabo Verde","Cameroon","Central African Republic","Chad","Comoros","Ivory Coast","Djibouti",
"Democratic Republic of the Congo","Egypt","Equatorial Guinea","Eritrea","Eswatini",
"Ethiopia","Gabon","Gambia","Ghana","Guinea","Guinea-Bissau","Kenya","Lesotho",
"Liberia","Libya","Madagascar","Malawi","Mali","Mauritania","Mauritius","Morocco",
"Mozambique","Namibia","Niger","Nigeria","Republic of the Congo","Rwanda","Sao Tome & Principe","Senegal","Seychelles","Sierra Leone","Somalia","South Africa","South Sudan",
"Sudan","Tanzania","Togo","Tunisia","Uganda","Zambia","Zimbabwe" ]

print(countries)
score=0
score=int(score)
while len(countries) > 0:
    print("Number of countries to guess")
    
    print("There are 54 countries")
    print("Score")
    print(score)
    country= input("Enter the name of a country")
    if country in countries:
        print("Good guess")
        score=score+1
        countries.remove(country)
    else:
        print("Invalid guess")
