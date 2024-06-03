# school_data.py
# Roxanne Mai
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here


# You may add your own additional classes, functions, variables, etc.

# School data in a dictionary
school_info = {
    1224: "Centennial High School",
    1679: "Robert Thirsk School",
    9626: "Louise Dean School",
    9806: "Queen Elizabeth High School",
    9813: "Forest Lawn High School",
    9815: "Crescent Heights High School",
    9816: "Western Canada High School",
    9823: "Central Memorial High School",
    9825: "James Fowler High School",
    9826: "Ernest Manning High School",
    9829: "William Aberhart High School",
    9830: "National Sport School",
    9836: "Henry Wise Wood High School",
    9847: "Bowness High School",
    9850: "Lord Beaverbrook High School",
    9856: "Jack James High School",
    9857: "Sir Winston Churchill High School",
    9858: "Dr. E. P. Scarlett High School",
    9860: "John G Diefenbaker High School",
    9865: "Lester B. Pearson High School"
}

# Load the data into a 3D NumPy array and reshape data into 10 years, 20 schools, 3 grades
data = np.array([
    year_2013, year_2014, year_2015, year_2016, year_2017,
    year_2018, year_2019, year_2020, year_2021, year_2022
]).reshape(10, 20, 3)

def get_school_code(name_or_code):
    '''
    get school code from the dictionary or return itself if it's a valid code.

    Parameters:
        name_or_code (str): The name or code of the school.

    Returns:
        int: The school code if found.

    Raises:
        ValueError: If the input is not a valid school name or code.
    '''
    try:
        # try to covert name_or_code to integer
        code = int(name_or_code)
        # if the conversion is successful and code exits in the dictionary, the function return the code
        if code in school_info:
            return code
    # if name_or_code is either the school name or invalid inputs, exception is caught and pass to continue further
    except ValueError:
        pass

    # if name_or_code has not yet returned as a valid code, check if name_or_code is school name in the dictionary    
    for code, name in school_info.items():
        if name.lower() == name_or_code.lower():
            return code
    # raise an exception when no match is found
    raise ValueError("You must enter a valid school name or code.")


def main():
    '''Main function to run the school enrollment statistics program.'''

    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    print(f"Shape of full data array: {data.shape}")
    print(f"Dimensions of full data array: {data.ndim}")

    # Prompt for user input
    user_input = input("Please enter the high school name or school code: ").strip()
    try:
        school_code = get_school_code(user_input)
        school_name = school_info[school_code]
    except ValueError as e:
        print(e)
        return
    
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print(f"School Name: {school_name}, School Code: {school_code}")
    
    # find the index of school code
    school_index = [code for code in school_info.keys()].index(school_code)
    # find 10 years 3 grades in specific school from the 3D array - data
    school_data = data[:, school_index, :]

    # get mean enrollment for Grade 10, 11, 12 across all years
    mean_grade_10 = np.floor(np.nanmean(school_data[:, 0]))
    mean_grade_11 = np.floor(np.nanmean(school_data[:, 1]))
    mean_grade_12 = np.floor(np.nanmean(school_data[:, 2]))
    
    # get highest and lowest enrollment for a single grade within 10 years
    highest_enrollment = np.nanmax(school_data)
    lowest_enrollment = np.nanmin(school_data)
    
    # get total enrollments per year
    total_enrollments_per_year = np.nansum(school_data, axis=1)
    # get total of 10 years enrollment 
    total_ten_year_enrollment = np.nansum(total_enrollments_per_year)
    # Mean total yearly enrollment over 10 years
    mean_yearly_enrollment = np.floor(np.nanmean(total_enrollments_per_year))
    
    # determine if any enrollment numbers were over 500. if there is, get the median value; if no, print message
    over_500_enrollments = school_data[school_data > 500]
    if over_500_enrollments.size > 0:
        median_over_500 = np.nanmedian(over_500_enrollments)
    else:
        median_over_500 = "No enrollments over 500."

    # print above calculation results for specific school
    print(f"Mean enrollment for Grade 10: {int(mean_grade_10)}")
    print(f"Mean enrollment for Grade 11: {int(mean_grade_11)}")
    print(f"Mean enrollment for Grade 12: {int(mean_grade_12)}")
    print(f"Highest enrollment for a single grade: {int(highest_enrollment)}")
    print(f"Lowest enrollment for a single grade: {int(lowest_enrollment)}")

    # print total enrollment each year from 2013 to 2023
    for i, year in enumerate(range(2013, 2023)):
        print(f"Total enrollment for {year}: {int(total_enrollments_per_year[i])}")
    
    # print more calculation results for specific school
    print(f"Total ten year enrollment: {int(total_ten_year_enrollment)}")
    print(f"Mean total enrollment over 10 years: {int(mean_yearly_enrollment)}")
    
    # check if median_over_500 it is String. If so pring
    if isinstance(median_over_500, str):
        print(median_over_500)
    else:
        print(f"For all enrollments over 500, the median value was: {int(median_over_500)}")
    
    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    # get mean enrollment in 2013
    mean_enrollment_2013 = np.floor(np.nanmean(data[0, :, :]))
    # get mean enrollment in 2022
    mean_enrollment_2022 = np.floor(np.nanmean(data[9, :, :]))
    # Total graduating class of 2022 across all schools
    total_graduating_2022 = np.nansum(data[9, :, 2])
    
    # get highest and lowest enrollment for a single grade within 10 years across all schools
    overall_highest_enrollment = np.nanmax(data)
    overall_lowest_enrollment = np.nanmin(data)
    
    # print calculations results for all school
    print(f"Mean enrollment in 2013: {int(mean_enrollment_2013)}")
    print(f"Mean enrollment in 2022: {int(mean_enrollment_2022)}")
    print(f"Total graduating class of 2022: {int(total_graduating_2022)}")
    print(f"Highest enrollment for a single grade: {int(overall_highest_enrollment)}")
    print(f"Lowest enrollment for a single grade: {int(overall_lowest_enrollment)}")

if __name__ == '__main__':
    main()

