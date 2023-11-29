#------------------------------------------------------------------------------------------------------------------------------------#
# This get_predefined_code function maps certain country names to their ISO 3166-1 alpha-3 codes. If a country name is not found in 
# pycountry find in predefined list
#------------------------------------------------------------------------------------------------------------------------------------#

def get_predefined_code(country):
    # Dictionary mapping country names to ISO 3166-1 alpha-3 codes
    predefined_codes = {
        "Serbia and Montenegro": "SCG",
        "US Virgin Islands": "VIR",
        "St. Vincent & Grenadines": "VCT",
        "England": "GBR",
        "Yugoslavia": "YUG",
        "U.S. Virgin Islands": "VIR",
        "Russia": "RUS",
        "Sudan (UK)": "SDN",
        "Scotland": "GBR",
        "Iran": "IRN",
        "Tanzania": "TZA",
        "Bosnia": "BIH",
        "Macedonia": "MKD",
        "Bosnia & Herzegovina": "BIH",
        "DRC": "COD",
        "Republic of the Congo": "COG",
        "Democratic Republic of the Congo": "COD",
        "Great Britain": "GBR",
        "USSR": "SUN",
        "South Korea": "KOR",
        "Venezuela": "VEN",
        "Czech Republic": "CZE",
        # Add more names and codes as needed
    }
    # Get the predefined code for the given country (or None if not found)
    predefined_code = predefined_codes.get(country, None)
    # Print a message if no predefined code was found
    if predefined_code is None:
        print(f"No predefined code found for {country}")
    # Return the predefined code (or None if not found)
    return predefined_code