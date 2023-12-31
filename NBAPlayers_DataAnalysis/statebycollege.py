def get_college_state(college):
    college_state_mapping = {
        # Mapping of college names to their respective states
        # Add more colleges and states as needed
        'Louisiana State': 'Louisiana',
        'Northwestern Oklahoma': 'Oklahoma',
        'North Carolina': 'North Carolina',
        'Florida State': 'Florida',
        'UCLA': 'California',
        'Tennessee-Chattanooga': 'Tennessee',
        'nan': 'Unknown',
        'Michigan': 'Michigan',
        'Purdue': 'Indiana',
        'Duke': 'North Carolina',
        'Ohio': 'Ohio',
        'Eastern Michigan': 'Michigan',
        'Nevada-Las Vegas': 'Nevada',
        'Kansas': 'Kansas',
        'Texas-El Paso': 'Texas',
        'Indiana': 'Indiana',
        'Louisville': 'Kentucky',
        'Houston': 'Texas',
        'Oklahoma': 'Oklahoma',
        'Oral Roberts': 'Oklahoma',
        'Oregon State': 'Oregon',
        'Brigham Young': 'Utah',
        'Washington': 'Washington',
        'Memphis': 'Tennessee',
        'Notre Dame': 'Indiana',
        'Delaware State': 'Delaware',
        'Alabama': 'Alabama',
        'Wyoming': 'Wyoming',
        'Pittsburgh': 'Pennsylvania',
        'Providence': 'Rhode Island',
        'Nebraska': 'Nebraska',
        'Michigan State': 'Michigan',
        'Mississippi State': 'Mississippi',
        'New Orleans': 'Louisiana',
        'Penn State': 'Pennsylvania',
        'Western Carolina': 'North Carolina',
        'Iowa State': 'Iowa',
        "St. Mary's (TX)": 'Texas',
        'Clemson': 'South Carolina',
        'Ohio State': 'Ohio',
        'Georgetown': 'Washington, D.C.',
        'Marquette': 'Wisconsin',
        'Virginia Tech': 'Virginia',
        'Southern Mississippi': 'Mississippi',
        'McNeese State': 'Louisiana',
        'Longwood': 'Virginia',
        'Arkansas': 'Arkansas',
        'Arkansas-Little Rock': 'Arkansas',
        'Virginia': 'Virginia',
        'Detroit Mercy': 'Michigan',
        'Oklahoma State': 'Oklahoma',
        'Gonzaga': 'Washington',
        'Syracuse': 'New York',
        'Richmond': 'Virginia',
        'Georgia Tech': 'Georgia',
        'Maryland': 'Maryland',
        'Pennsylvania': 'Pennsylvania',
        'Grand Canyon': 'Arizona',
        'Tulane': 'Louisiana',
        'Boston College': 'Massachusetts',
        'Arizona State': 'Arizona',
        'Kentucky': 'Kentucky',
        "St. John's (NY)": 'New York',
        'South Carolina': 'South Carolina',
        'California': 'California',
        'Texas Tech': 'Texas',
        'Bradley': 'Illinois',
        'Temple': 'Pennsylvania',
        'Illinois': 'Illinois',
        'Villanova': 'Pennsylvania',
        'Arizona': 'Arizona',
        'Auburn': 'Alabama',
        'Western Kentucky': 'Kentucky',
        'North Carolina State': 'North Carolina',
        'Old Dominion': 'Virginia',
        'Cincinnati': 'Ohio',
        'Washington State': 'Washington',
        'Tennessee': 'Tennessee',
        'Connecticut': 'Connecticut',
        'Yale': 'Connecticut',
        'Boise State': 'Idaho',
        'Southern Illinois': 'Illinois',
        'Xavier': 'Ohio',
        'California-Santa Barbara': 'California',
        'Cal State-Fullerton': 'California',
        'Long Beach State': 'California',
        'Tennessee State': 'Tennessee',
        'Albany State (GA)': 'Georgia',
        'Virginia Union': 'Virginia',
        'Central Michigan': 'Michigan',
        'Georgia': 'Georgia',
        'Northern Illinois': 'Illinois',
        'Colorado': 'Colorado',
        'Pepperdine': 'California',
        'La Salle': 'Pennsylvania',
        'Florida': 'Florida',
        'Fayetteville State': 'North Carolina',
        'Navy': 'Maryland',
        'Baylor': 'Texas',
        'Nevada-Reno': 'Nevada',
        'Jacksonville': 'Florida',
        'Pacific': 'California',
        'Southeastern Oklahoma State': 'Oklahoma',
        'Duquesne': 'Pennsylvania',
        'Augustana (SD)': 'South Dakota',
        'Central Arkansas': 'Arkansas',
        'West Virginia Tech': 'West Virginia',
        'California-Irvine': 'California',
        'Trinity Valley Community College': 'Texas',
        'DePaul': 'Illinois',
        'Hampton': 'Virginia',
        'Rice': 'Texas',
        'Marist': 'New York',
        'Southern California': 'California',
        'Centenary (LA)': 'Louisiana',
        'Wake Forest': 'North Carolina',
        'Miami (OH)': 'Ohio',
        'Weber State': 'Utah',
        'Mercer': 'Georgia',
        'Santa Clara': 'California',
        'Vanderbilt': 'Tennessee',
        'Minnesota': 'Minnesota',
        'Wright State': 'Ohio',
        'Hartford': 'Connecticut',
        'Tulsa': 'Oklahoma',
        'Wichita State': 'Kansas',
        'George Washington': 'Washington, D.C.',
        'Oregon': 'Oregon',
        'Seton Hall': 'New Jersey',
        'Wisconsin-Stevens Point': 'Wisconsin',
        'Utah': 'Utah',
        'Missouri-Kansas City': 'Missouri',
        'Jackson State': 'Mississippi',
        'Stetson': 'Florida',
        'Massachusetts': 'Massachusetts',
        'New Mexico': 'New Mexico',
        'Drexel': 'Pennsylvania',
        'Murray State': 'Kentucky',
        'American International': 'Massachusetts',
        'Coppin State': 'Maryland',
        'Eastern Illinois': 'Illinois',
        'Iowa': 'Iowa',
        'Texas Christian': 'Texas',
        'Texas': 'Texas',
        'Montana': 'Montana',
        'Louisiana Tech': 'Louisiana',
        'Central State (OH)': 'Ohio',
        'New Mexico State': 'New Mexico',
        'Montevallo': 'Alabama',
        'Seward County Community College': 'Kansas',
        'North Carolina-Wilmington': 'North Carolina',
        'Missouri': 'Missouri',
        'San Diego State': 'California',
        'Georgia Southern': 'Georgia',
        'Wisconsin': 'Wisconsin',
        'Kansas State': 'Kansas',
        'West Florida': 'Florida',
        'Mt. San Antonio': 'California',
        'Southern': 'Louisiana',
        'Creighton': 'Nebraska',
        'East Carolina': 'North Carolina',
        'Pfeiffer': 'North Carolina',
        'Stanford': 'California',
        'Lamar': 'Texas',
        'Central Connecticut State': 'Connecticut',
        'South Carolina State': 'South Carolina',
        'San Jose State': 'California',
        'Colgate': 'New York',
        'College of Charleston': 'South Carolina',
        'Bowling Green': 'Ohio',
        'Cal State-Bakersfield': 'California',
        'Austin Peay': 'Tennessee',
        'Morehead State': 'Kentucky',
        'Davidson': 'North Carolina',
        'Morehouse': 'Georgia',
        'Wisconsin-Green Bay': 'Wisconsin',
        'Auburn-Montgomery': 'Alabama',
        'Rhode Island': 'Rhode Island',
        'Nicholls State': 'Louisiana',
        'Ball State': 'Indiana',
        'Long Island-Brooklyn': 'New York',
        'Valparaiso': 'Indiana',
        'Toledo': 'Ohio',
        'Liberty': 'Virginia',
        'Florida A&M': 'Florida',
        'Saint Louis': 'Missouri',
        'Dayton': 'Ohio',
        'Colorado State': 'Colorado',
        'Miami (FL)': 'Florida',
        'Texas State': 'Texas',
        'Thomas More': 'Kentucky',
        'Fresno State': 'California',
        'George Mason': 'Virginia',
        'South Florida': 'Florida',
        'Hawaii': 'Hawaii',
        'Barton Community College': 'Kansas',
        'Northwestern': 'Illinois',
        'North Carolina-Charlotte': 'North Carolina',
        'Central Oklahoma': 'Oklahoma',
        'Augsburg': 'Minnesota',
        'Saint Rose': 'New York',
        'Louisiana-Monroe': 'Louisiana',
        "Master's": 'California',
        'Lebanon Valley': 'Pennsylvania',
        'Northern Arizona': 'Arizona',
        'Saint Vincent': 'Pennsylvania',
        "St. Bonaventure": 'New York',
        'Princeton': 'New Jersey',
        'Butler Community College': 'Kansas',
        'Florida International': 'Florida',
        'Venezuela': 'International',
        'Hofstra': 'New York',
        'Indian Hills Community College': 'Iowa',
        'Northwest Florida State': 'Florida',
        'Southern Methodist': 'Texas',
        'Blinn': 'Texas',
        'Mississippi': 'Mississippi',
        'Wingate': 'North Carolina',
        'Fordham': 'New York',
        'Northeast Mississippi Community College': 'Mississippi',
        'Marshall': 'West Virginia',
        'Texas-San Antonio': 'Texas',
        'Shaw': 'North Carolina',
        'Western Michigan': 'Michigan',
        'Portland State': 'Oregon',
        'Idaho': 'Idaho',
        'North Dakota': 'North Dakota',
        'Utah State': 'Utah',
        'Central Florida': 'Florida',
        'Nevada': 'Nevada',
        'Manhattan': 'New York',
        'Brigham Young-Hawaii': 'Hawaii',
        "Saint Joseph's": 'Pennsylvania',
        'Kent State': 'Ohio',
        'William Paterson': 'New Jersey',
        'Southeastern Illinois': 'Illinois',
        'Yonsei (KOR)': 'International',
        'Utah Valley': 'Utah',
        'Walsh': 'Ohio',
        'Oakland': 'Michigan',
        'Louisiana-Lafayette': 'Louisiana',
        'Texas A&M': 'Texas',
        'Alabama-Birmingham': 'Alabama',
        'Fairfield': 'Connecticut',
        'Rutgers': 'New Jersey',
        'Northeastern': 'Massachusetts',
        'Delta State': 'Mississippi',
        'Meridian Community College': 'Mississippi',
        'Missouri State': 'Missouri',
        'Eastern Washington': 'Washington',
        'West Virginia': 'West Virginia',
        'Rider': 'New Jersey',
        'Indiana Purdue-Indianapolis': 'Indiana',
        'Midland': 'Texas',
        "Saint Mary's (CA)": 'California',
        'Robert Morris (IL)': 'Illinois',
        'Virginia Military Institute': 'Virginia',
        'Northwestern State': 'Louisiana',
        'Virginia Commonwealth': 'Virginia',
        'Cleveland State': 'Ohio',
        'Tennessee-Martin': 'Tennessee',
        'Towson': 'Maryland',
        'Butler': 'Indiana',
        'Le Moyne': 'New York',
        'Harvard': 'Massachusetts',
        'Augusta State': 'Georgia',
        'Portland': 'Oregon',
        'Cornell': 'New York',
        'Cal State-San Bernardino': 'California',
        'Midwestern State': 'Texas',
        'Siena': 'New York',
        'Jacksonville State': 'Alabama',
        'Alabama A&M': 'Alabama',
        'Iona': 'New York',
        'Tennessee Tech': 'Tennessee',
        'Norfolk State': 'Virginia',
        'Belmont': 'Tennessee',
        'California-Berkeley': 'California',
        'Lehigh': 'Pennsylvania',
        'North Texas': 'Texas',
        'South Dakota State': 'South Dakota',
        'Bucknell': 'Pennsylvania',
        'USC': 'California',
        'UNLV': 'Nevada',
        'Georgia State': 'Georgia',
        'Westchester CC NY': 'New York',
        'Ohio U.': 'Ohio',
        'Miami (Fla.)': 'Florida',
        "St. Mary's (CA)": 'California',
        "St. John's, N.Y.": 'New York',
        'Holy Cross': 'Massachusetts',
        'Loyola (IL)': 'Illinois',
        'Alabama Huntsville': 'Alabama',
        'California-Los Angeles': 'California',
        'Va Commonwealth': 'Virginia',
        'South Carolina Upstate': 'South Carolina',
        ' ': 'Unknown',
        'St. Louis': 'Missouri',
        'Miami': 'Florida',
        'University of Dayton': 'Ohio',
        'American University': 'Washington, D.C.',
        'Cal-Santa Barbara': 'California',
        'S.E. Missouri': 'Missouri',
        'Molloy': 'New York',
        'Cal State-Long Beach': 'California',
        'Stony Brook, N.Y.': 'New York',
        'Boston U.': 'Massachusetts',
        'Louisana-Lafayette': 'Louisiana',
        'University of California, Berkeley': 'California',
        'University of Colorado Boulder': 'Colorado',
        'Illinois State': 'Illinois',
        'Georgia Institute of Technology': 'Georgia',
        'University of Texas at Austin': 'Texas',
        'California State-Long Beach': 'California',
        "St. John's": 'New York',
        'Texas-Austin': 'Texas',
        'Radford': 'Virginia',
        'Indiana-Purdue Indianapolis': 'Indiana',
        'Lipscomb': 'Tennessee',
        'Nebraska-Lincoln': 'Nebraska',
        'No College': 'Unknown',
        'Texas-Arlington': 'Texas',
        'TCU': 'Texas',
        "St. Joseph's (PA)": 'Pennsylvania',
        'Indiana-Purdue Fort Wayne': 'Indiana',
        'Virginia Tech ': 'Virginia',
        'Florida Gulf Coast': 'Florida',
        'Campbell University': 'North Carolina',
        'Cal Poly': 'California',
        "St.Mary's College of California": 'California',
        '                                   ': 'Unknown',
        'Truman State': 'Missouri',
        'Vermont': 'Vermont',
        'Montana State': 'Montana',
        'Delaware': 'Delaware',
        'William & Mary': 'Virginia',
        'Arizona St.': 'Arizona',
        'Lincoln Memorial': 'Tennessee',
        'Wheeling Jesuit': 'West Virginia',
        'Texas Legends': 'Texas',
        'Denver': 'Colorado',
        'Wisc.-Green Bay': 'Wisconsin',
        'UNC': 'North Carolina',
        'UCF': 'Florida',
        'Loyola-Maryland': 'Maryland',
        'LSU': 'Louisiana',
        'Chicago St.': 'Illinois',
        "St. Mary's": 'California',
        'Wisconsin-Milwaukee': 'Wisconsin',
        'Northwest Missouri State': 'Missouri',
        'Winthrop': 'South Carolina',
        'Northern Iowa': 'Iowa',
        'Cal-Davis': 'California',
        'Stephen F. Austin': 'Texas',
        'San Francisco': 'California',
        'John A. Logan': 'Illinois',
        'Buffalo': 'New York',
}
    # Get the state for the given college (or None if not found)
    college_state_mapping = college_state_mapping.get(college, None)
    
    # If you want to print a message when no state is found, uncomment the following lines
    # if college_state_mapping is None:
        # print(f"No predefined code found for {college}")
    
    return college_state_mapping


def get_state_code(state):
    state_codes = {
        # Mapping of state names to their two-letter codes (ISO 3166-2)
        # Add more states and codes as needed
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands': 'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Palau': 'PW',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
        'Atolón Palmyra': 'PW',
        'Isla Baker': 'IB',
        'Isla Howland': 'IH',
        'Isla Jarvis': 'IJ',
        'Isla Johnston': 'JT',
        'Kingman Reef': 'KR',
        'Midway Atoll': 'MA',
        'Samoa Americana': 'AS',
        'Isla Wake': 'WK',
    }
    # Get the state code for the given state (or None if not found)
    state_code = state_codes.get(state, None)
    
    # If you want to print a message when no state code is found, uncomment the following lines
    # if state_code is None:
    #     print(f"No predefined code found for {state}")
    
    return state_code